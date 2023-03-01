# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Update(EventTypeAbstractModel):
    Items: List["UpdateItem"] = Field(...)
    Meta: "UpdateMeta" = Field(...)


class UpdateItem(RedoxAbstractModel):
    ContainsLatex: Union[bool, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Identifiers: List["UpdateItemIdentifier"] = Field(...)
    IsChargeable: Union[bool, None] = Field(None)
    Location: "UpdateItemLocation" = Field(None)
    Notes: Union[str, None] = Field(None)
    Price: Union[Number, None] = Field(None)
    Procedure: "UpdateItemProcedure" = Field(None)
    Quantity: Union[Number, None] = Field(None)
    Status: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)
    Units: Union[str, None] = Field(None)
    Vendor: "UpdateItemVendor" = Field(None)


class UpdateItemIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: str = Field(...)


class UpdateItemLocation(RedoxAbstractModel):
    Bin: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class UpdateItemProcedure(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Modifier: Union[str, None] = Field(None)


class UpdateItemVendor(RedoxAbstractModel):
    CatalogNumber: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdateMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["UpdateMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["UpdateMetaLog"] = Field(None)
    Message: "UpdateMetaMessage" = Field(None)
    Source: "UpdateMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "UpdateMetaTransmission" = Field(None)


class UpdateMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdateMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class UpdateMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class UpdateMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdateMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


Update.update_forward_refs()
UpdateItem.update_forward_refs()
UpdateMeta.update_forward_refs()
