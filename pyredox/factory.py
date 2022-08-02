# -*- coding: utf-8 -*-
import contextlib
from importlib import import_module
from json import loads

from typing import Dict, List, Optional, Tuple, Type, Union
from warnings import warn

from . import generic
from .abstract_base import (
    EventTypeAbstractModel,
    GenericRedoxAbstractModel,
    RedoxAbstractModel,
)

# Got inspiration from https://github.com/python/typing/issues/182
JSONValue = Union[None, bool, int, float, str]
JSONType = Union[List["JSONType"], Dict[str, Union[JSONValue, "JSONType"]]]
JsonPayload = Union[str, JSONType]


def get_model_and_event(redox_dict: dict) -> Tuple[str, str]:
    meta: JSONType = redox_dict.get("Meta")
    if not meta:
        raise ValueError("Unable to find Meta attribute of JSON payload.")

    model: str = meta["DataModel"].replace(" ", "")  # PatientAdmin, Scheduling, etc
    event: str = meta["EventType"]  # NewPatient, Reschedule, etc

    # This is to handle the weird naming in the SSO folder
    if "-" in event:
        event = event.replace("-", " ").title().replace(" ", "")

    return model, event


def get_class_type(redox_dict: dict) -> Type[EventTypeAbstractModel]:
    data_model, event_type = get_model_and_event(redox_dict)

    with contextlib.suppress(ModuleNotFoundError):
        model_module = import_module(f"pyredox.{data_model.lower()}")
    if not model_module:
        raise AttributeError(f"Couldn't find Redox model module for {data_model}")

    event_class = getattr(model_module, event_type)
    if event_class:
        return event_class
    raise AttributeError(f"Couldn't find Redox event class for {event_type}")


def redox_object_factory(
    json_payload: JsonPayload,
) -> Union[EventTypeAbstractModel, List[EventTypeAbstractModel], None]:
    """Return a Redox model instance of the JSON payload.

    The type of Redox model returned is determined by inspecting the contents
    of the JSON payload. The Redox spec requires all payloads to have a
    ``Meta`` object with the fields ``EventType`` and ``DataModel``, which
    can lead us to the specific class that corresponds to the message type.
    """
    if json_payload is None:
        return None

    elif isinstance(json_payload, str):
        json_payload = loads(json_payload)

    if isinstance(json_payload, list):
        return [redox_object_factory(j) for j in json_payload]

    elif not isinstance(json_payload, dict):
        raise TypeError(
            f"Can only create Redox objects from a valid JSON payload, got "
            f"{type(json_payload)}"
        )

    event_class = get_class_type(json_payload)
    return event_class.parse_obj(json_payload)


def from_redox_to_generic(
    redox_instance: RedoxAbstractModel,
) -> Optional[GenericRedoxAbstractModel]:
    redox_dict = redox_instance.dict()
    # We don't have to do as much validation as the pyredox factory because we're
    # working with a validated Redox obj
    data_model = redox_dict["Meta"]["DataModel"]  # e.g., PatientAdmin, Scheduling, etc
    event_type = redox_dict["Meta"]["EventType"]  # e.g., NewPatient, Reschedule, etc

    model_module = getattr(generic, data_model)
    if not model_module:
        warn(f"Couldn't find the CedarRedox model module for {data_model}")
        return None

    event_class = getattr(model_module, event_type)
    if not event_class:
        warn(f"Couldn't find CedarRedox event class for {event_type}")
        return None

    return event_class(**redox_dict)
