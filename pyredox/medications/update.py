# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Update(EventTypeAbstractModel):

    Meta: "UpdateMeta" = Field(...)
    Order: "UpdateOrder" = Field(...)
    Patient: "UpdatePatient" = Field(...)
    Visit: "UpdateVisit" = Field(None)


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


class UpdateOrder(RedoxAbstractModel):

    EnteredBy: "UpdateOrderEnteredBy" = Field(None)
    ID: str = Field(...)
    Indications: List["UpdateOrderIndication"] = Field(None)
    Medication: "UpdateOrderMedication" = Field(...)
    Notes: List[str] = Field(None)
    Pharmacy: "UpdateOrderPharmacy" = Field(None)
    Priority: Union[str, None] = Field(None)
    Provider: "UpdateOrderProvider" = Field(None)
    VerifiedBy: "UpdateOrderVerifiedBy" = Field(None)


class UpdateOrderEnteredBy(RedoxAbstractModel):

    Address: "UpdateOrderEnteredByAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "UpdateOrderEnteredByLocation" = Field(None)
    PhoneNumber: "UpdateOrderEnteredByPhoneNumber" = Field(None)


class UpdateOrderEnteredByAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateOrderEnteredByLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateOrderEnteredByPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class UpdateOrderIndication(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class UpdateOrderMedication(RedoxAbstractModel):

    Components: List["UpdateOrderMedicationComponent"] = Field(None)
    Dispense: "UpdateOrderMedicationDispense" = Field(None)
    Dose: "UpdateOrderMedicationDose" = Field(None)
    EndDate: Union[str, None] = Field(None)
    FreeTextSig: Union[str, None] = Field(None)
    Frequency: "UpdateOrderMedicationFrequency" = Field(None)
    IsPRN: Union[bool, None] = Field(None)
    NumberOfRefillsRemaining: Union[Number, None] = Field(None)
    Product: "UpdateOrderMedicationProduct" = Field(...)
    Rate: "UpdateOrderMedicationRate" = Field(None)
    Route: "UpdateOrderMedicationRoute" = Field(None)
    StartDate: Union[str, None] = Field(None)


class UpdateOrderMedicationComponent(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Dose: "UpdateOrderMedicationComponentDose" = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateOrderMedicationComponentDose(RedoxAbstractModel):

    Quantity: Union[Number, None] = Field(None)
    Units: Union[str, None] = Field(None)


class UpdateOrderMedicationDispense(RedoxAbstractModel):

    Amount: Union[Number, None] = Field(None)
    Units: Union[str, None] = Field(None)


class UpdateOrderMedicationDose(RedoxAbstractModel):

    Quantity: Union[Number, None] = Field(None)
    Units: Union[str, None] = Field(None)


class UpdateOrderMedicationFrequency(RedoxAbstractModel):

    Period: Union[Number, None] = Field(None)
    Unit: Union[str, None] = Field(None)


class UpdateOrderMedicationProduct(RedoxAbstractModel):

    AltCodes: List["UpdateOrderMedicationProductAltCode"] = Field(None)
    Code: str = Field(...)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdateOrderMedicationProductAltCode(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdateOrderMedicationRate(RedoxAbstractModel):

    Quantity: Union[Number, None] = Field(None)
    Units: Union[str, None] = Field(None)


class UpdateOrderMedicationRoute(RedoxAbstractModel):

    AltCodes: List["UpdateOrderMedicationRouteAltCode"] = Field(None)
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdateOrderMedicationRouteAltCode(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdateOrderPharmacy(RedoxAbstractModel):

    Address: "UpdateOrderPharmacyAddress" = Field(None)
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    PhoneNumber: "UpdateOrderPharmacyPhoneNumber" = Field(None)


class UpdateOrderPharmacyAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateOrderPharmacyPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class UpdateOrderProvider(RedoxAbstractModel):

    Address: "UpdateOrderProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "UpdateOrderProviderLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "UpdateOrderProviderPhoneNumber" = Field(None)


class UpdateOrderProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateOrderProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateOrderProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class UpdateOrderVerifiedBy(RedoxAbstractModel):

    Address: "UpdateOrderVerifiedByAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "UpdateOrderVerifiedByLocation" = Field(None)
    PhoneNumber: "UpdateOrderVerifiedByPhoneNumber" = Field(None)


class UpdateOrderVerifiedByAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateOrderVerifiedByLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateOrderVerifiedByPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class UpdatePatient(RedoxAbstractModel):

    Allergies: List["UpdatePatientAllergy"] = Field(None)
    Demographics: "UpdatePatientDemographics" = Field(None)
    Identifiers: List["UpdatePatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class UpdatePatientAllergy(RedoxAbstractModel):

    AltCodes: List["UpdatePatientAllergyAltCode"] = Field(None)
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Comment: Union[str, None] = Field(None)
    Criticality: "UpdatePatientAllergyCriticality" = Field(None)
    EndDate: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Reaction: List["UpdatePatientAllergyReaction"] = Field(None)
    Severity: "UpdatePatientAllergySeverity" = Field(None)
    StartDate: Union[str, None] = Field(None)
    Status: "UpdatePatientAllergyStatus" = Field(None)
    Substance: "UpdatePatientAllergySubstance" = Field(None)


class UpdatePatientAllergyAltCode(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdatePatientAllergyCriticality(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdatePatientAllergyReaction(RedoxAbstractModel):

    AltCodes: List["UpdatePatientAllergyReactionAltCode"] = Field(None)
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Severity: "UpdatePatientAllergyReactionSeverity" = Field(None)
    Text: Union[str, None] = Field(None)


class UpdatePatientAllergyReactionAltCode(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdatePatientAllergyReactionSeverity(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdatePatientAllergySeverity(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdatePatientAllergyStatus(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdatePatientAllergySubstance(RedoxAbstractModel):

    AltCodes: List["UpdatePatientAllergySubstanceAltCode"] = Field(None)
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdatePatientAllergySubstanceAltCode(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdatePatientDemographics(RedoxAbstractModel):

    Address: "UpdatePatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DOB: Union[str, None] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "UpdatePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class UpdatePatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdatePatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class UpdatePatientIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


class UpdateVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    AttendingProvider: "UpdateVisitAttendingProvider" = Field(None)
    Insurances: List["UpdateVisitInsurance"] = Field(None)
    Location: "UpdateVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    ReferringProvider: "UpdateVisitReferringProvider" = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class UpdateVisitAttendingProvider(RedoxAbstractModel):

    Address: "UpdateVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "UpdateVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "UpdateVisitAttendingProviderPhoneNumber" = Field(None)


class UpdateVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class UpdateVisitInsurance(RedoxAbstractModel):

    AgreementType: Union[str, None] = Field(None)
    Company: "UpdateVisitInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "UpdateVisitInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "UpdateVisitInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class UpdateVisitInsuranceCompany(RedoxAbstractModel):

    Address: "UpdateVisitInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class UpdateVisitInsuranceCompanyAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitInsuranceInsured(RedoxAbstractModel):

    Address: "UpdateVisitInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["UpdateVisitInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class UpdateVisitInsuranceInsuredAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitInsuranceInsuredIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateVisitInsurancePlan(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateVisitLocation(RedoxAbstractModel):

    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateVisitReferringProvider(RedoxAbstractModel):

    Address: "UpdateVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "UpdateVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "UpdateVisitReferringProviderPhoneNumber" = Field(None)


class UpdateVisitReferringProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitReferringProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateVisitReferringProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


Update.update_forward_refs()
UpdateMeta.update_forward_refs()
UpdateOrder.update_forward_refs()
UpdateOrderEnteredBy.update_forward_refs()
UpdateOrderMedication.update_forward_refs()
UpdateOrderMedicationComponent.update_forward_refs()
UpdateOrderMedicationProduct.update_forward_refs()
UpdateOrderMedicationRoute.update_forward_refs()
UpdateOrderPharmacy.update_forward_refs()
UpdateOrderProvider.update_forward_refs()
UpdateOrderVerifiedBy.update_forward_refs()
UpdatePatient.update_forward_refs()
UpdatePatientAllergy.update_forward_refs()
UpdatePatientAllergyReaction.update_forward_refs()
UpdatePatientAllergySubstance.update_forward_refs()
UpdatePatientDemographics.update_forward_refs()
UpdateVisit.update_forward_refs()
UpdateVisitAttendingProvider.update_forward_refs()
UpdateVisitInsurance.update_forward_refs()
UpdateVisitInsuranceCompany.update_forward_refs()
UpdateVisitInsuranceInsured.update_forward_refs()
UpdateVisitReferringProvider.update_forward_refs()
