# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import List, Type

import pytest
from pydantic import ValidationError
from pydantic.typing import NoneType

from pyredox.abstract_base import EventTypeAbstractModel
from pyredox.factory import redox_object_factory
from pyredox.patientadmin import PatientUpdate

str_patient_update = """
{
   "Meta": {
      "DataModel": "PatientAdmin",
      "EventType": "PatientUpdate",
      "EventDateTime": "2022-03-16T16:16:26.695Z",
      "Test": true,
      "Source": {
         "ID": "7ce6f387-c33c-417d-8682-81e83628cbd9",
         "Name": "Redox Dev Tools"
      }
   },
   "Patient": {
      "Identifiers": []
   }
}"""
dict_patient_update = {
    "Meta": {
        "DataModel": "PatientAdmin",
        "EventType": "PatientUpdate",
        "EventDateTime": "2022-03-16T16:16:26.695Z",
        "Test": True,
        "Source": {
            "ID": "7ce6f387-c33c-417d-8682-81e83628cbd9",
            "Name": "Redox Dev Tools",
        },
    },
    "Patient": {"Identifiers": []},
}
singles = [
    (PatientUpdate, str_patient_update),
    (PatientUpdate, dict_patient_update),
    (NoneType, None),
]

lists = [
    ((PatientUpdate, PatientUpdate), f"[{str_patient_update}, {str_patient_update}]"),
    ((PatientUpdate, PatientUpdate), [str_patient_update, str_patient_update]),
]


@pytest.mark.parametrize(("model_type", "payload"), singles)
def test_redox_factory_singles(model_type: Type[EventTypeAbstractModel], payload):
    redox_object = redox_object_factory(payload)
    assert isinstance(redox_object, model_type)
    if redox_object is None:
        return

    # Test a few representative fields exist in created object
    assert hasattr(redox_object, "Meta")
    # Meta is always required to have DataModel and EventType
    assert hasattr(redox_object.Meta, "DataModel")
    assert hasattr(redox_object.Meta, "EventType")


@pytest.mark.parametrize(("model_types", "payload"), lists)
def test_redox_factory_list(model_types: List[Type[EventTypeAbstractModel]], payload):
    returned_objects = redox_object_factory(payload)
    assert isinstance(returned_objects, list)
    assert len(model_types) == len(returned_objects)

    for obj_type, obj in zip(model_types, returned_objects):
        assert isinstance(obj, obj_type)


def test_invalid_payload():
    """Ensure a missing required field raises a ValidationError."""
    patient_missing = deepcopy(dict_patient_update)
    # noinspection PyTypedDict
    patient_missing["Patient"] = {}

    with pytest.raises(ValidationError):
        redox_object_factory(patient_missing)


def test_extra_field_doesnt_break_anything():
    """Ensure adding extra fields still yields a valid model instance."""
    patient_extra = deepcopy(dict_patient_update)
    patient_extra["Blobby"] = {"Bloop": []}

    redox_object = redox_object_factory(patient_extra)
    assert isinstance(redox_object, PatientUpdate)
