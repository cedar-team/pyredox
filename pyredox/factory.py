# -*- coding: utf-8 -*-
import importlib
from json import loads
from typing import Dict, List, Union

from .abstract_base import EventTypeAbstractModel

# Got inspiration from https://github.com/python/typing/issues/182
JSONValue = Union[None, bool, int, float, str]
JSONType = Union[List["JSONType"], Dict[str, Union[JSONValue, "JSONType"]]]
JsonPayload = Union[str, JSONType]


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

    meta: JSONType = json_payload.get("Meta")
    if not meta:
        raise ValueError("Unable to find Meta attribute of JSON payload.")

    data_model = meta["DataModel"]  # e.g., PatientAdmin, Scheduling, etc
    event_type = meta["EventType"]  # e.g., NewPatient, Reschedule, etc

    model_module_name = f"pyredox.{data_model.lower()}"
    model_module = None
    try:
        model_module = importlib.import_module(model_module_name)
    except ModuleNotFoundError:
        pass
    if not model_module:
        raise AttributeError(f"Couldn't find Redox model module for {data_model}")

    event_class = getattr(model_module, event_type)
    if not event_class:
        raise AttributeError(f"Couldn't find Redox event class for {event_type}")

    return event_class.parse_obj(json_payload)
