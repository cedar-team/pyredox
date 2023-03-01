# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Study(EventTypeAbstractModel):
    Meta: "StudyMeta" = Field(...)
    Protocols: List["StudyProtocol"] = Field(None)
    Study: "StudyStudy" = Field(None)


class StudyMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["StudyMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["StudyMetaLog"] = Field(None)
    Message: "StudyMetaMessage" = Field(None)
    Source: "StudyMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "StudyMetaTransmission" = Field(None)


class StudyMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class StudyMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class StudyMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class StudyMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class StudyMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class StudyProtocol(RedoxAbstractModel):
    Cycles: List["StudyProtocolCycle"] = Field(None)
    Description: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class StudyProtocolCycle(RedoxAbstractModel):
    Days: List["StudyProtocolCycleDay"] = Field(None)
    Description: Union[str, None] = Field(None)
    EndDate: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    StartDate: Union[str, None] = Field(None)


class StudyProtocolCycleDay(RedoxAbstractModel):
    ActivityDateTime: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    EarliestDateTime: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LatestDateTime: Union[str, None] = Field(None)
    Procedures: List["StudyProtocolCycleDayProcedure"] = Field(None)


class StudyProtocolCycleDayProcedure(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSet: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Modifiers: List[str] = Field(None)


class StudyStudy(RedoxAbstractModel):
    Conditions: List["StudyStudyCondition"] = Field(None)
    Coordinators: List["StudyStudyCoordinator"] = Field(None)
    Description: Union[str, None] = Field(None)
    Design: "StudyStudyDesign" = Field(None)
    Eligibility: "StudyStudyEligibility" = Field(None)
    Identifiers: List["StudyStudyIdentifier"] = Field(None)
    Location: "StudyStudyLocation" = Field(None)
    PrincipalInvestigator: "StudyStudyPrincipalInvestigator" = Field(None)
    Sponsor: "StudyStudySponsor" = Field(None)
    StartDateTime: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    Title: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class StudyStudyCondition(RedoxAbstractModel):
    AltCodes: List["StudyStudyConditionAltCode"] = Field(None)
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class StudyStudyConditionAltCode(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class StudyStudyCoordinator(RedoxAbstractModel):
    Address: "StudyStudyCoordinatorAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "StudyStudyCoordinatorLocation" = Field(None)
    PhoneNumber: "StudyStudyCoordinatorPhoneNumber" = Field(None)


class StudyStudyCoordinatorAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class StudyStudyCoordinatorLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "StudyStudyCoordinatorLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "StudyStudyCoordinatorLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class StudyStudyCoordinatorLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class StudyStudyCoordinatorLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class StudyStudyCoordinatorPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class StudyStudyDesign(RedoxAbstractModel):
    Phase: Union[str, None] = Field(None)
    Purpose: Union[str, None] = Field(None)


class StudyStudyEligibility(RedoxAbstractModel):
    Gender: Union[str, None] = Field(None)
    MaximumAge: Union[Number, None] = Field(None)
    MinimumAge: Union[Number, None] = Field(None)


class StudyStudyIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class StudyStudyLocation(RedoxAbstractModel):
    Address: "StudyStudyLocationAddress" = Field(None)
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List["StudyStudyLocationDepartmentIdentifier"] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["StudyStudyLocationFacilityIdentifier"] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class StudyStudyLocationAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class StudyStudyLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class StudyStudyLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class StudyStudyPrincipalInvestigator(RedoxAbstractModel):
    Address: "StudyStudyPrincipalInvestigatorAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "StudyStudyPrincipalInvestigatorLocation" = Field(None)
    PhoneNumber: "StudyStudyPrincipalInvestigatorPhoneNumber" = Field(None)


class StudyStudyPrincipalInvestigatorAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class StudyStudyPrincipalInvestigatorLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "StudyStudyPrincipalInvestigatorLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "StudyStudyPrincipalInvestigatorLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class StudyStudyPrincipalInvestigatorLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class StudyStudyPrincipalInvestigatorLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class StudyStudyPrincipalInvestigatorPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class StudyStudySponsor(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


Study.update_forward_refs()
StudyMeta.update_forward_refs()
StudyProtocol.update_forward_refs()
StudyProtocolCycle.update_forward_refs()
StudyProtocolCycleDay.update_forward_refs()
StudyStudy.update_forward_refs()
StudyStudyCondition.update_forward_refs()
StudyStudyCoordinator.update_forward_refs()
StudyStudyCoordinatorLocation.update_forward_refs()
StudyStudyLocation.update_forward_refs()
StudyStudyPrincipalInvestigator.update_forward_refs()
StudyStudyPrincipalInvestigatorLocation.update_forward_refs()
