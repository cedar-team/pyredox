# Pyredox - A Pydantic-Based Library for Redox Data

[![PyPI Info](https://img.shields.io/pypi/v/pyredox.svg)](https://pypi.python.org/pypi/pyredox)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cedar-team/pyredox/main)](https://github.com/cedar-team/pyredox/actions)
[![Coverage Info](https://coveralls.io/repos/github/cedar-team/pyredox/badge.svg?branch=main)](https://coveralls.io/github/cedar-team/pyredox?branch=main)
[![Black Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Pyredox is library for producing, ingesting, and validating data from [Redox], a
"data platform designed to connect providers, payers and products."

Pyredox is a set of [Pydantic] models that conforms to the [Redox data model]
specification for the purpose of making it easy to convert Redox-formatted JSON to
Python objects and vice versa. Because pyredox inherits the functionality of
Pydantic, it validates that the JSON data conforms to the spec automatically upon
object creation.

For example, if you tried to create a [`NewPatient`
model](https://developer.redoxengine.com/data-models/PatientAdmin.html#NewPatient) with
insufficient data, you would get an error like this:

```python
>>> from pyredox.patientadmin.newpatient import NewPatient
>>> NewPatient(Meta={})

ValidationError: 3 validation errors for NewPatient
Meta -> DataModel
  field required (type=value_error.missing)
Meta -> EventType
  field required (type=value_error.missing)
Patient
  field required (type=value_error.missing)
```


## Usage

The simplest way to create a `pyredox` model from a JSON payload is to pass an
unpacked `dict` as the parameter when initializing the object, like this:

```python
payload_str = """
{
   "Meta": {
      "DataModel": "PatientAdmin",
      "EventType": "NewPatient"
   },
   "Patient": {
      "Identifiers": [
         {
            "ID": "e167267c-16c9-4fe3-96ae-9cff5703e90a",
            "IDType": "EHRID"
         }
      ]
   }
}
"""
data = json.loads(payload_str)
new_patient = NewPatient(**data)
```

If you have a payload and don't know which object type it is, you can use the
factory helper, which can take a JSON string or the loaded JSON dict/list:

```python
from pyredox.factory import redox_object_factory

redox_object1 = redox_object_factory(payload_str)  # str input
redox_object2 = redox_object_factory(data)  # dict input
```

To create a JSON payload to send to Redox from an existing `pyredox` object, just
call the `json()` method of the object:

```python
new_patient.json()
```

When working with the individual fields of a model object, you can traverse the
element properties like so:

```python
new_patient.patient.identifiers[0].id  # "e167267c-16c9-4fe3-96ae-9cff5703e90a"
```


[Redox]: https://www.redoxengine.com/
[Redox data model]: https://developer.redoxengine.com/data-models/index.html
[Pydantic]: https://pydantic-docs.helpmanual.io/
