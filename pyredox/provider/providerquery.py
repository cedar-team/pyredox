# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class ProviderQuery(EventTypeAbstractModel):
    Meta: "ProviderQueryMeta" = Field(...)
    Provider: "ProviderQueryProvider" = Field(None)


class ProviderQueryMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["ProviderQueryMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["ProviderQueryMetaLog"] = Field(None)
    Message: "ProviderQueryMetaMessage" = Field(None)
    Source: "ProviderQueryMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "ProviderQueryMetaTransmission" = Field(None)


class ProviderQueryMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class ProviderQueryMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class ProviderQueryMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class ProviderQueryMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class ProviderQueryMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class ProviderQueryProvider(RedoxAbstractModel):
    Demographics: "ProviderQueryProviderDemographics" = Field(None)
    Identifiers: List["ProviderQueryProviderIdentifier"] = Field(None)


class ProviderQueryProviderDemographics(RedoxAbstractModel):
    Address: "ProviderQueryProviderDemographicsAddress" = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)


class ProviderQueryProviderDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class ProviderQueryProviderIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


ProviderQuery.update_forward_refs()
ProviderQueryMeta.update_forward_refs()
ProviderQueryProvider.update_forward_refs()
ProviderQueryProviderDemographics.update_forward_refs()
