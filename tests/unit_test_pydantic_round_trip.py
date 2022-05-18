# -*- coding: utf-8 -*-
from json import load
from pathlib import Path
from unittest import TestCase

from .. import patientadmin, scheduling

SAMPLES_DIR = (Path(__file__).parent / "sample_data").resolve()

SAMPLE_DATA_TYPE_AND_FILE_PATH = [
    (patientadmin.Arrival, Path("patientadmin_arrival.json")),
    (patientadmin.Cancel, Path("patientadmin_cancel.json")),
    (patientadmin.CensusQuery, Path("patientadmin_censusquery.json")),
    (patientadmin.CensusQueryResponse, Path("patientadmin_censusqueryresponse.json")),
    (patientadmin.Discharge, Path("patientadmin_discharge.json")),
    (patientadmin.NewPatient, Path("patientadmin_newpatient.json")),
    (patientadmin.PatientMerge, Path("patientadmin_patientmerge.json")),
    (patientadmin.PatientUpdate, Path("patientadmin_patientupdate.json")),
    (patientadmin.PreAdmit, Path("patientadmin_preadmit.json")),
    (patientadmin.Registration, Path("patientadmin_registration.json")),
    (patientadmin.Transfer, Path("patientadmin_transfer.json")),
    (patientadmin.VisitMerge, Path("patientadmin_visitmerge.json")),
    (patientadmin.VisitQuery, Path("patientadmin_visitquery.json")),
    (patientadmin.VisitQueryResponse, Path("patientadmin_visitqueryresponse.json")),
    (patientadmin.VisitUpdate, Path("patientadmin_visitupdate.json")),
    (scheduling.AvailableSlots, Path("scheduling_availableslots.json")),
    (scheduling.AvailableSlotsResponse, Path("scheduling_availableslotsresponse.json")),
    (scheduling.Booked, Path("scheduling_booked.json")),
    (scheduling.BookedResponse, Path("scheduling_bookedresponse.json")),
    (scheduling.Cancel, Path("scheduling_cancel.json")),
    (scheduling.Modification, Path("scheduling_modification.json")),
    (scheduling.New, Path("scheduling_new.json")),
    (scheduling.NoShow, Path("scheduling_noshow.json")),
    (scheduling.PushSlots, Path("scheduling_pushslots.json")),
    (scheduling.Reschedule, Path("scheduling_reschedule.json")),
]


class TestPydanticRoundTrip(TestCase):
    def test_json_pyredox_json(self):
        for expected_type, json_file_path in SAMPLE_DATA_TYPE_AND_FILE_PATH:
            with self.subTest(
                expected_type=expected_type, json_file_path=json_file_path
            ):
                current_sample_path = SAMPLES_DIR / json_file_path
                self.assertTrue(current_sample_path.exists)
                with open(current_sample_path) as sample_fd:
                    sample = load(sample_fd)

                obj = expected_type(**sample)
                self.assertIsInstance(obj, expected_type)
                self.assertEqual(sample, obj.dict())
