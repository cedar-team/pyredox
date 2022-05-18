# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class CensusQuery(EventTypeAbstractModel):

    Departments: List[str] = Field(None)
    Facilities: List[str] = Field(None)
    Meta: "CensusQueryMeta" = Field(...)
    PatientClasses: List[str] = Field(None)


class CensusQueryMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["CensusQueryMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["CensusQueryMetaLog"] = Field(None)
    Message: "CensusQueryMetaMessage" = Field(None)
    Source: "CensusQueryMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "CensusQueryMetaTransmission" = Field(None)


class CensusQueryMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CensusQueryMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class CensusQueryMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class CensusQueryMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CensusQueryMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


CensusQuery.update_forward_refs()
CensusQueryMeta.update_forward_refs()
