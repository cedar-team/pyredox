# -*- coding: utf-8 -*-
from importlib import import_module
from json import load
from pathlib import Path

import pytest

SAMPLES_DIR = (Path(__file__).parent / "fixtures").resolve()

PYREDOX_DIR = (Path(__file__).parent.parent / "pyredox").resolve()
SAMPLE_DATA_FILE_PATH = [
    (Path(f"{module.name}_{event.stem.lower()}.json"),)
    for module in PYREDOX_DIR.iterdir()
    if module.is_dir() and module.name != "generic"
    for event in module.iterdir()
    if not event.name.startswith("_")
]
SKIP_FILES = [
    str(SAMPLES_DIR / f)
    for f in [
        "clinicalsummary_patientpush.json",
        "clinicalsummary_visitpush.json",
        "clinicalsummary_visitqueryresponse.json",
        "clinicalsummary_patientqueryresponse.json",
        "clinicaldecisions_request.json",
    ]
]


@pytest.mark.parametrize(("json_file_path",), SAMPLE_DATA_FILE_PATH)
def test_json_pyredox_json(json_file_path: Path):
    current_sample_path = SAMPLES_DIR / json_file_path
    print(current_sample_path)
    assert current_sample_path.exists
    try:
        with open(current_sample_path) as sample_fd:
            sample = load(sample_fd)
    except FileNotFoundError as err:
        if err.filename in SKIP_FILES:
            return
        raise

    model: str = sample["Meta"]["DataModel"].lower().replace(" ", "")
    event: str = sample["Meta"]["EventType"]
    # This is to handle the weird naming in the SSO folder
    if "-" in event:
        event = event.replace("-", " ").title().replace(" ", "")

    module = import_module(f"pyredox.{model}")
    expected_type = getattr(module, event)

    obj = expected_type(**sample)
    assert isinstance(obj, expected_type)
    assert sample == obj.dict()
