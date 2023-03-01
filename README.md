# Pyredox - A Pydantic-Based Library for Redox Data

[![PyPI Info](https://img.shields.io/pypi/v/pyredox.svg)](https://pypi.python.org/pypi/pyredox)
[![Python Version](https://img.shields.io/pypi/pyversions/pyredox)](https://pypi.python.org/pypi/pyredox)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/cedar-team/pyredox/test_and_coverage.yml?branch=main)](https://github.com/cedar-team/pyredox/actions)
[![Coverage Info](https://coveralls.io/repos/github/cedar-team/pyredox/badge.svg?branch=main)](https://coveralls.io/github/cedar-team/pyredox?branch=main)
[![Black Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyredox)](https://pypi.python.org/pypi/pyredox)
[![PyPI - License](https://img.shields.io/pypi/l/pyredox?color=blue)](https://pypi.python.org/pypi/pyredox)

Pyredox is library for producing, ingesting, and validating data from [Redox], a "data platform designed to connect
providers, payers and products."

Pyredox is a set of [Pydantic] models that conforms to the [Redox data model] specification for the purpose of making it
easy to convert Redox-formatted JSON to Python objects and vice versa. Because pyredox inherits the functionality of
Pydantic, it validates that the JSON data conforms to the spec automatically upon object creation.

For example, if you tried to create a [`NewPatient`
model](https://developer.redoxengine.com/data-models/PatientAdmin.html#NewPatient) with insufficient data, you would get
an error like this:

```
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

[Redox]: https://www.redoxengine.com/

[Redox data model]: https://developer.redoxengine.com/data-models/index.html

[Pydantic]: https://pydantic-docs.helpmanual.io/

## Usage

There are two primary methods to create a `pyredox` object:

1. [JSON Dict Expansion](#json-dict-expansion):
    - Benefits:
        - Simple to use if you already have a JSON string or dictionary (or list of dictionaries) and want to get the
          `pyredox` object that corresponds to that payload.
        - Options for if you already know the Redox type of the JSON payload and options for if you don't.
    - Shortcomings:
        - Writing out or creating a full JSON payload can be quite verbose if you're crafting it yourself (vs processing
          a received payload).

2. [Generic Objects](#using-generics):
    - Benefits:
        - Very composable; objects for sub-objects can be created separately from the Event Type model you're building.
    - Shortcomings:
        - Validation of the field values against the original Redox schema isn't fully performed until you call one of
          the `to_redox()`, `dict()`, or `json()` methods.

For instructions on how to serialize an object, see the [Serialize to JSON or `dict`](#serialize-to-json-or-dict)
section down below.

### JSON Dict Expansion

The simplest way to create a `pyredox` model from a JSON payload is to pass an unpacked `dict` as the parameter when
initializing the object, like this:

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

If you have a payload and don't know which object type it is, you can use the factory helper, which can take a JSON
string or the loaded JSON dict/list:

```python
from pyredox.factory import redox_object_factory

redox_object1 = redox_object_factory(payload_str)  # str input
redox_object2 = redox_object_factory(data)  # dict input
```

To create a JSON payload to send to Redox from an existing `pyredox` object, just call the `json()` method of the
object:

```python
new_patient.json()
```

When working with the individual fields of a model object, you can traverse the element properties like so:

```python
new_patient.patient.identifiers[0].id  # "e167267c-16c9-4fe3-96ae-9cff5703e90a"
```

### Using Generics

The Redox schema redefines every property of the Event Types in every location they're used. This is the case whether
the property definitions are exactly the same or have slight differences. In order to make sure that every Event Type
class in the library would perform structure validation exactly as defined in the schema, the "proper Redox" classes (my
term for all Redox objects *not* residing in the `generic` folder) all have their own property class definitions that
match the schema. This means that there are classes that have the exact same fields that exist in the same Python file
and fall under the same Event Type.

For example, in `pyredox/provider/new.py`, the `NewProviderRoleLocationAddress` and `NewProviderRoleOrganizationAddress`
classes have the exact same definition because they're both Addresses. However, because one represents the address of
the location for a provider's role and the other represents the address of the organization for the provider's role,
Redox treats them differently. In contrast, most Event Types' `Meta` properties have similar but different fields,
although all of them have the required `DataModel` and `EventType` fields.

Because of all this, it becomes quite difficult to write a program that can build up a Redox message from multiple data
sources without coupling with it a knowledge of the exact message you're creating. And even then the code can become
very unwieldy with sprawling Python dictionaries.

The solution is to use the Event Type classes and property classes defined in the `generic` directory. So, instead of
creating a new provider like this:

```python
# THIS IS THE HARDER WAY TO DO THINGS!
from pyredox.provider import New
from pyredox.provider.new import (
    NewMeta,
    NewProvider,
    NewProviderIdentifier,
    NewProviderRole,
    NewProviderRoleLocation,
    NewProviderRoleLocationAddress,
    NewProviderRoleOrganization,
    NewProviderRoleOrganizationAddress,
)

provider_org = NewProviderRoleOrganization(
    Address=NewProviderRoleOrganizationAddress(
        StreetAddress="123 Cherry St",
        City="Green Bay",
        State="Wisconsin",
        ZIP="54321",
        Country="USA",
    )
)
provider_loc1 = NewProviderRoleLocation(
    Address=NewProviderRoleLocationAddress(
        StreetAddress="123 Cherry St",
        City="Green Bay",
        State="Wisconsin",
        ZIP="54321",
        Country="USA",
    ),
)
provider_loc2 = NewProviderRoleLocation(
    Address=NewProviderRoleLocationAddress(
        StreetAddress="567 Splenda Way",
        City="Green Bay",
        State="Wisconsin",
        ZIP="54321",
        Country="USA",
    )
)
provider = NewProvider(
    Identifiers=[NewProviderIdentifier(ID="FakeProviderID")],
    IsActive=True,
    Roles=[
        NewProviderRole(
            Organization=provider_org,
            Locations=[provider_loc1, provider_loc2],
        )
    ],
)

new_provider_msg = New(
    Meta=NewMeta(DataModel="Provider", EventType="New", Test=True),
    Providers=[provider],
)
```

The following is more composable and somewhat simpler:

```python
# Simpler way to create a new Provider
from pyredox.generic import types as pyredox_types
from pyredox.generic.Provider import New as NewProvider

# Because office_address is a generic Address type, we can reuse it for both
# the Organization and the Location for this Provider.
office_address = pyredox_types.Address(
    StreetAddress="123 Cherry St",
    City="Green Bay",
    State="Wisconsin",
    ZIP="54321",
    Country="USA",
)
clinic_address = pyredox_types.Address(
    StreetAddress="567 Splenda Way",
    City="Green Bay",
    State="Wisconsin",
    ZIP="54321",
    Country="USA",
)
provider_org = pyredox_types.Organization(Address=office_address)
provider_loc1 = pyredox_types.Location(Address=office_address)
provider_loc2 = pyredox_types.Location(Address=clinic_address)
provider = pyredox_types.Provider(
    Identifiers=[pyredox_types.Identifier(ID="FakeProviderID")],
    IsActive=True,
    Roles=[
        pyredox_types.Role(
            Organization=provider_org,
            Locations=[provider_loc1, provider_loc2],
        )
    ],
)

new_provider_msg = NewProvider(
    Meta=pyredox_types.Meta(DataModel="Provider", EventType="New", Test=True),
    Providers=[provider],
).to_redox()  # This converts the object to a "proper Redox" model
```

It's important to note here that both the `.dict()` and `.json()` methods of the generic Event Type classes
automatically convert the data to the "proper Redox" form first, so that last statement could also be written like this:

```python
new_provider_json = NewProvider(
    Meta=pyredox_types.Meta(DataModel="Provider", EventType="New", Test=True),
    Providers=[provider],
).json()  # This converts the object to a "proper Redox" model, then gets the JSON string
```

There is a chance that, by using the generic types to build up the Redox message in a composable way, you may introduce
fields that are available in the generic version of the object that are not defined in the "proper Redox" model. The
library's default behavior is to silently drop those fields with no current plans to make this configurable.

There's also a possibility that the "proper Redox" object you're building specifies a data type for a field that differs
from other models that use that data type, which is a result of how the schema is specified. For example, the
[generic `Demographics` class has the following field definition]([https://github.com/cedar-team/pyredox/blob/341407063f27d3b82000bcb86362ec00ce48dec2/pyredox/generic/types.py#L644]):

```python
EmailAddresses: Union[List["EmailAddress"], List[str]]
```

Some Event Type models specify a list of strings and others require an `EmailAddress` object. Currently, the only way to
detect when such a type mismatch occurs is to catch the `pydantic.ValidationError` exception, like this:

```python
from pydantic import ValidationError

try:
    new_provider_json = NewProvider(
        Meta=pyredox_types.Meta(DataModel="Provider", EventType="New", Test=True),
        Providers=[provider],
    ).json()  # This converts the object to a "proper Redox" model
except ValidationError:
    # TODO: Handle the validation error here
    pass
```

### Serialize to JSON or `dict`

All `pyredox` objects have methods that allow for easy serialization:
- For the `dict` version of an object, call the `dict()` method.
- For the JSON `str` version of an object, call the `json()` method.

To customize how `pyredox` exports the data from your model, you can use any of the [parameters available from the
underlying Pydantic models](https://pydantic-docs.helpmanual.io/usage/exporting_models/). Note that when calling the
`json()` method, you can also include keyword arguments to be passed to the `json.dumps()`.

When serializing generic types, be aware that `pyredox` will convert the object to the corresponding "proper Redox"
before returning the serialized data. See above for more information.

### Casting between types

Every `pyredox` object has a `cast_from()` method that is intended for use when you need to assign the same values to
multiple objects while avoiding any type-checking errors. For example, on a generic `Visit` object, there are multiple
provider fields that only differ in which role that provider filled for the visit. If the same provider filled multiple
roles, it is redundant to specify the same provider information in multiple object instances.

Using this `cast_from()` class method, you only need to create a generic object with all the provider information and
then cast it to the different types:

```python
provider = AdmittingProvider(...)
visit = Visit(
    AdmittingProvider=provider,
    AttendingProvider=AttendingProvider.cast_from(provider),
    VisitProvider=VisitProvider.cast_from(provider),
)
```

If multiple objects are passed to `cast_from`, the first object's fields will be given preference, then the second
object's fields, and so on. This mimics the MRO for multiple inheritance (see
https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
for more info).
