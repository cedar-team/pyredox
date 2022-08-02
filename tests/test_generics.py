# -*- coding: utf-8 -*-
from datetime import datetime, timezone

from typing import Type

import pytest

from pyredox.abstract_base import GenericRedoxAbstractModel
from pyredox.generic import PatientAdmin


round_trip_cases = (
    (
        PatientAdmin.Arrival,
        {
            "Meta": {"DataModel": "PatientAdmin", "EventType": "Arrival"},
            "Patient": {
                "Identifiers": [
                    {
                        "ID": "MySeCrEtId",
                        "IDType": "SECRET",
                    }
                ],
            },
            "Visit": {"VisitDateTime": datetime.now(tz=timezone.utc).isoformat()},
        },
    ),
)


@pytest.mark.parametrize(("model", "dict_input"), round_trip_cases)
def test_dict_to_generic_to_redox_to_dict(
    model: Type[GenericRedoxAbstractModel], dict_input: dict
):
    generic_object = model(**dict_input)
    assert isinstance(generic_object, model)
    assert dict_input == generic_object.dict()
