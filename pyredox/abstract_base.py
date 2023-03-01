# -*- coding: utf-8 -*-
"""Base class for all Redox elements."""
import abc
from typing import Any, Mapping, Union

from pydantic import BaseModel, ExtraError, Field, ValidationError
from pydantic.error_wrappers import ErrorWrapper

__all__ = [
    "CannotRectifyValidationError",
    "EventTypeAbstractModel",
    "GenericEventTypeAbstractModel",
    "RedoxAbstractModel",
]


class CannotRectifyValidationError(Exception):
    """Raised when cast_from can't autocorrect a ValidationError."""


def _pop_offending_field_values(
    args_for_new_object: dict, validation_err: ValidationError
):
    err: ErrorWrapper
    for err in validation_err.raw_errors:
        if isinstance(err.exc, ValidationError):
            # The location should only have one key in it
            if len(err.loc_tuple()) != 1:
                raise CannotRectifyValidationError(
                    "Don't know what to do with a ValidationError that has a "
                    "loc_tuple w/len > 1"
                )
            sub_args = args_for_new_object[err.loc_tuple()[0]]
            _pop_offending_field_values(sub_args, err.exc)
            continue

        elif not isinstance(err.exc, ExtraError):
            raise CannotRectifyValidationError(
                f"Unknown validation error type: {err.exc.__class__.__name__}"
            )
        parent_of_offending_field = args_for_new_object
        # noinspection PyProtectedMember
        locations = list(err.loc_tuple())
        offending_field = locations.pop()
        traversed = []
        for field in locations:
            # Note: It's currently unclear if this loop will ever be used. It wasn't in
            # tests, but since loc_tuple() is always a tuple, we're erring on the side
            # of caution by leaving this here. But it's also unclear how to test the
            # loop operations properly.
            next_in_loc = parent_of_offending_field.get(field, None)
            if not next_in_loc:
                raise CannotRectifyValidationError(
                    f"Cannot traverse path to offending field: "
                    f"{'->'.join(traversed) if traversed else 'Object'} doesn't have "
                    f'a field called "{field}".'
                )
            traversed.append(field)
            parent_of_offending_field = next_in_loc

        try:
            parent_of_offending_field.pop(offending_field)
        except KeyError as err:
            raise CannotRectifyValidationError(
                f"Cannot traverse path to offending field: "
                f"{'->'.join(traversed) if traversed else 'Object'} doesn't have "
                f'a field called "{offending_field}".'
            ) from err


class RedoxAbstractModel(BaseModel, abc.ABC):
    Extensions: Any = Field(None)

    def __str__(self):
        return self.json()

    @classmethod
    def cast_from(
        cls, *others: Union["RedoxAbstractModel", Mapping]
    ) -> "RedoxAbstractModel":
        """Create a new pyredox object from the passed object(s).

        Intended for use when you need to assign the same values to multiple
        objects while avoiding any type-checking errors. For example, on a
        generic ``Visit`` object, there are multiple provider fields that only
        differ in which role that provider filled for the visit. If the same
        provider filled multiple roles, it is redundant to specify the same
        provider information in multiple object instances.

        Using this ``cast_from`` class method, you only need to create a
        generic object with all the provider information and then cast it to
        the different types::

            provider = AdmittingProvider(...)
            visit = Visit(
                AdmittingProvider=provider,
                AttendingProvider=AttendingProvider.cast_from(provider),
                VisitProvider=VisitProvider.cast_from(provider),
            )

        If multiple objects are passed to ``cast_from``, the first object's
        fields will be given preference, then the second object's fields, and
        so on. This mimics the MRO for multiple inheritance (see
        https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
        for more info).
        """

        # Gather all arguments for creating the new object into a single dictionary by
        # starting with an empty dict then `update()`ing it using the dict version of
        # each object in ``others``.
        others = [
            other.dict() if hasattr(other, "dict") else dict(other)
            for other in reversed(others)
        ]
        args = {}
        for other in others:
            args.update(other)

        new_object = None
        while new_object is None:
            try:
                new_object = cls(**args)
            except ValidationError as err:
                _pop_offending_field_values(args, err)

        return new_object

    def dict(
        self,
        *,
        include=None,
        exclude=None,
        by_alias: bool = False,
        skip_defaults: bool = None,
        exclude_unset: bool = True,  # Differs from default
        exclude_defaults: bool = False,
        exclude_none: bool = True,  # Differs from default
    ):
        return super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )


class _Meta(RedoxAbstractModel, abc.ABC):
    """Bare minimum fields for all ``Meta`` types.

    This is defined strictly for type hinting purposes. No ``Meta`` field class
    should inherit from this or reference this class for simplicity's sake.
    """

    DataModel: str = Field(...)
    EventType: str = Field(...)


class EventTypeAbstractModel(RedoxAbstractModel, abc.ABC):
    """Event types should inherit from this instead of RedoxAbstractModel."""

    Meta: _Meta = Field(...)


class GenericEventTypeAbstractModel(RedoxAbstractModel):
    _redox_module = ...  # e.g. patientadmin
    Meta: _Meta = Field(...)

    def to_redox(self) -> RedoxAbstractModel:
        """Figure out the correct pyredox model, instantiate, and return."""

        class_name = type(self).__name__

        event_module = getattr(self._redox_module, class_name.lower())
        if not event_module:
            raise AttributeError(
                f"Couldn't find Redox event module for {class_name.lower()}"
            )

        event_class = getattr(event_module, class_name)
        if not event_class:
            raise AttributeError(f"Couldn't find Redox event class for {class_name}")

        return event_class(**super().dict())

    def dict(self, *args, **kwargs):
        return self.to_redox().dict(*args, **kwargs)

    def json(self, *args, **kwargs):
        return self.to_redox().json(*args, **kwargs)
