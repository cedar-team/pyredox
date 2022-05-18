# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class PushSlots(EventTypeAbstractModel):

    Meta: "PushSlotsMeta" = Field(...)
    Slots: List["PushSlotsSlot"] = Field(...)


class PushSlotsMeta(RedoxAbstractModel):

    BatchID: Union[str, None] = Field(None)
    CurrentBatch: Union[str, None] = Field(None)
    DataModel: str = Field(...)
    Destinations: List["PushSlotsMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["PushSlotsMetaLog"] = Field(None)
    Message: "PushSlotsMetaMessage" = Field(None)
    Source: "PushSlotsMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    TotalBatches: Union[str, None] = Field(None)
    Transmission: "PushSlotsMetaTransmission" = Field(None)


class PushSlotsMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PushSlotsMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class PushSlotsMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class PushSlotsMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PushSlotsMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class PushSlotsSlot(RedoxAbstractModel):

    DateTime: str = Field(...)
    Duration: Number = Field(...)
    ID: Union[str, None] = Field(None)
    Location: "PushSlotsSlotLocation" = Field(None)
    Provider: "PushSlotsSlotProvider" = Field(None)
    Reason: Union[str, None] = Field(None)


class PushSlotsSlotLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PushSlotsSlotProvider(RedoxAbstractModel):

    Address: "PushSlotsSlotProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    PhoneNumber: "PushSlotsSlotProviderPhoneNumber" = Field(None)


class PushSlotsSlotProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PushSlotsSlotProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


PushSlots.update_forward_refs()
PushSlotsMeta.update_forward_refs()
PushSlotsSlot.update_forward_refs()
PushSlotsSlotProvider.update_forward_refs()
