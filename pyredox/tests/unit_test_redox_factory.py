# -*- coding: utf-8 -*-
from copy import deepcopy
from unittest import TestCase

from pydantic import ValidationError
from pydantic.typing import NoneType

try:
    from pyredox.factory import redox_object_factory
    from pyredox.patientadmin import PatientUpdate
except ImportError:
    # This is a little messy, but would be very easy to clean up if we made pyredox an
    # open-source library by using Poetry and the right directory structure.
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).parent.parent.parent.resolve()))
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


class TestRedoxFactory(TestCase):
    def test_redox_factory_singles(self):
        for model_type, payload in singles:
            redox_object = redox_object_factory(payload)
            self.assertIsInstance(redox_object, model_type)
            if redox_object is None:
                continue
            # Test a few representative fields exist in created object
            self.assertTrue(hasattr(redox_object, "Meta"))
            # Meta is always required to have DataModel and EventType
            self.assertTrue(hasattr(redox_object.Meta, "DataModel"))
            self.assertTrue(hasattr(redox_object.Meta, "EventType"))

    def test_redox_factory_list(self):
        for model_types, payload in lists:
            returned_objects = redox_object_factory(payload)
            self.assertIsInstance(returned_objects, list)
            self.assertEqual(len(model_types), len(returned_objects))

            for obj_type, obj in zip(model_types, returned_objects):
                self.assertIsInstance(obj, obj_type)

    def test_invalid_payload(self):
        """Ensure a missing required field raises a ValidationError."""
        patient_missing = deepcopy(dict_patient_update)
        patient_missing["Patient"] = {}

        with self.assertRaises(ValidationError):
            redox_object_factory(patient_missing)

    def test_extra_field_doesnt_break_anything(self):
        """Ensure adding extra fields still yields a valid model instance."""
        patient_extra = deepcopy(dict_patient_update)
        patient_extra["Blobby"] = {"Bloop": []}

        redox_object = redox_object_factory(patient_extra)
        self.assertIsInstance(redox_object, PatientUpdate)
