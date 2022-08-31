# -*- coding: utf-8 -*-
from copy import deepcopy
from datetime import date, datetime, timezone
from typing import List, Type

import pytest
from pydantic import ValidationError
from pydantic.typing import NoneType

from pyredox.abstract_base import EventTypeAbstractModel
from pyredox.claim import Submission
from pyredox.factory import redox_object_factory
from pyredox.generic import Claim as GenericClaim, types
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


def test_casting():
    meta = types.Meta(
        DataModel="Scheduling",
        EventType="Modification",
        EventDateTime=datetime.now().isoformat(),
        Test=True,
        Source=types.Source(ID="SecretSourceID", Name="Cedar"),
        Destinations=[types.Destination(ID="SecretDestinationID")],
    )

    address = types.Address(
        StreetAddress="123 Sesame Street",
        City="New York",
        State="NY",
        ZIP="10123",
        Country="USA",
    )

    patient = types.Patient(
        Demographics=types.Demographics(
            FirstName="Olivia",
            MiddleName="Test",
            LastName="Patient",
            Address=address,
            Citizenship=["United States of America", "Canada", "Mexico"],
            DeathDateTime=datetime(2050, 2, 14, 9, 15, tzinfo=timezone.utc).isoformat(),
            DOB=date(1970, 2, 15).isoformat(),
            SSN="123-43-2123",
            IsHispanic=False,
            Sex="Female",
            PhoneNumber=types.PhoneNumber(Mobile="123-456-7890"),
        )
    )
    subscriber = types.Subscriber.cast_from(
        patient.Demographics,
        dict(
            ResponsibilityLevel="High",
            Insurance=dict(
                Company=dict(Address=dict(StreetAddress="123 Nowhere", Blahblah="Nope"))
            ),
            FirstName="Emma",
        ),
    )

    generic_submission = GenericClaim.Submission(
        Meta=meta,
        Patient=patient,
        Subscriber=subscriber,
    )

    # Calling to_redox() forces validation of all the values by the stricter models
    modification = generic_submission.to_redox()

    assert isinstance(modification, Submission)

    # This verifies that setting fields by dictionary works as expected
    assert modification.Subscriber.ResponsibilityLevel == "High"
    assert (
        modification.Subscriber.Insurance.Company.Address.StreetAddress == "123 Nowhere"
    )
    assert not hasattr(modification.Subscriber.Insurance.Company.Address, "Blahblah")

    # This shows that the value from the patient.Demographics object took precedence
    assert modification.Subscriber.FirstName == "Olivia"
