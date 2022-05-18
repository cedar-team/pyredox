# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Discharge(EventTypeAbstractModel):

    Meta: "DischargeMeta" = Field(...)
    Patient: "DischargePatient" = Field(...)
    Visit: "DischargeVisit" = Field(None)


class DischargeMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["DischargeMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["DischargeMetaLog"] = Field(None)
    Message: "DischargeMetaMessage" = Field(None)
    Source: "DischargeMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "DischargeMetaTransmission" = Field(None)


class DischargeMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DischargeMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class DischargeMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class DischargeMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DischargeMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class DischargePatient(RedoxAbstractModel):

    Allergies: List["DischargePatientAllergy"] = Field(None)
    Contacts: List["DischargePatientContact"] = Field(None)
    Demographics: "DischargePatientDemographics" = Field(None)
    Diagnoses: List["DischargePatientDiagnosis"] = Field(None)
    Identifiers: List["DischargePatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)
    PCP: "DischargePatientPCP" = Field(None)


class DischargePatientAllergy(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    OnsetDateTime: Union[str, None] = Field(None)
    Reaction: List["DischargePatientAllergyReaction"] = Field(None)
    Severity: "DischargePatientAllergySeverity" = Field(None)
    Status: Union[str, None] = Field(None)
    Type: "DischargePatientAllergyType" = Field(None)


class DischargePatientAllergyReaction(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DischargePatientAllergySeverity(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DischargePatientAllergyType(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DischargePatientContact(RedoxAbstractModel):

    Address: "DischargePatientContactAddress" = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "DischargePatientContactPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Roles: List[str] = Field(None)


class DischargePatientContactAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargePatientContactPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class DischargePatientDemographics(RedoxAbstractModel):

    Address: "DischargePatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "DischargePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)


class DischargePatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargePatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class DischargePatientDiagnosis(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargePatientIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


class DischargePatientPCP(RedoxAbstractModel):

    Address: "DischargePatientPCPAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DischargePatientPCPLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "DischargePatientPCPPhoneNumber" = Field(None)


class DischargePatientPCPAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargePatientPCPLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargePatientPCPPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class DischargeVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    AdditionalStaff: List["DischargeVisitAdditionalStaff"] = Field(None)
    AdmittingProvider: "DischargeVisitAdmittingProvider" = Field(None)
    AttendingProvider: "DischargeVisitAttendingProvider" = Field(None)
    Balance: Union[Number, None] = Field(None)
    ConsultingProvider: "DischargeVisitConsultingProvider" = Field(None)
    DiagnosisRelatedGroup: Union[Number, None] = Field(None)
    DiagnosisRelatedGroupType: Union[Number, None] = Field(None)
    DischargeDateTime: Union[str, None] = Field(None)
    DischargeLocation: "DischargeVisitDischargeLocation" = Field(None)
    DischargeStatus: "DischargeVisitDischargeStatus" = Field(None)
    Duration: Union[Number, None] = Field(None)
    Guarantor: "DischargeVisitGuarantor" = Field(None)
    Instructions: List[str] = Field(None)
    Insurances: List["DischargeVisitInsurance"] = Field(None)
    Location: "DischargeVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    Reason: Union[str, None] = Field(None)
    ReferringProvider: "DischargeVisitReferringProvider" = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class DischargeVisitAdditionalStaff(RedoxAbstractModel):

    Address: "DischargeVisitAdditionalStaffAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DischargeVisitAdditionalStaffLocation" = Field(None)
    PhoneNumber: "DischargeVisitAdditionalStaffPhoneNumber" = Field(None)
    Role: "DischargeVisitAdditionalStaffRole" = Field(None)


class DischargeVisitAdditionalStaffAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargeVisitAdditionalStaffLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargeVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class DischargeVisitAdditionalStaffRole(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class DischargeVisitAdmittingProvider(RedoxAbstractModel):

    Address: "DischargeVisitAdmittingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DischargeVisitAdmittingProviderLocation" = Field(None)
    PhoneNumber: "DischargeVisitAdmittingProviderPhoneNumber" = Field(None)


class DischargeVisitAdmittingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargeVisitAdmittingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargeVisitAdmittingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class DischargeVisitAttendingProvider(RedoxAbstractModel):

    Address: "DischargeVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DischargeVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "DischargeVisitAttendingProviderPhoneNumber" = Field(None)


class DischargeVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargeVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargeVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class DischargeVisitConsultingProvider(RedoxAbstractModel):

    Address: "DischargeVisitConsultingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DischargeVisitConsultingProviderLocation" = Field(None)
    PhoneNumber: "DischargeVisitConsultingProviderPhoneNumber" = Field(None)


class DischargeVisitConsultingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargeVisitConsultingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargeVisitConsultingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class DischargeVisitDischargeLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargeVisitDischargeStatus(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class DischargeVisitGuarantor(RedoxAbstractModel):

    Address: "DischargeVisitGuarantorAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    Employer: "DischargeVisitGuarantorEmployer" = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Number: Union[str, None] = Field(None)
    PhoneNumber: "DischargeVisitGuarantorPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    Spouse: "DischargeVisitGuarantorSpouse" = Field(None)
    SSN: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargeVisitGuarantorAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargeVisitGuarantorEmployer(RedoxAbstractModel):

    Address: "DischargeVisitGuarantorEmployerAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class DischargeVisitGuarantorEmployerAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargeVisitGuarantorPhoneNumber(RedoxAbstractModel):

    Business: Union[str, None] = Field(None)
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)


class DischargeVisitGuarantorSpouse(RedoxAbstractModel):

    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)


class DischargeVisitInsurance(RedoxAbstractModel):

    AgreementType: Union[str, None] = Field(None)
    Company: "DischargeVisitInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "DischargeVisitInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "DischargeVisitInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class DischargeVisitInsuranceCompany(RedoxAbstractModel):

    Address: "DischargeVisitInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class DischargeVisitInsuranceCompanyAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargeVisitInsuranceInsured(RedoxAbstractModel):

    Address: "DischargeVisitInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["DischargeVisitInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)


class DischargeVisitInsuranceInsuredAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargeVisitInsuranceInsuredIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DischargeVisitInsurancePlan(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargeVisitLocation(RedoxAbstractModel):

    Address: "DischargeVisitLocationAddress" = Field(None)
    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargeVisitLocationAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargeVisitReferringProvider(RedoxAbstractModel):

    Address: "DischargeVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DischargeVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "DischargeVisitReferringProviderPhoneNumber" = Field(None)


class DischargeVisitReferringProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DischargeVisitReferringProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DischargeVisitReferringProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


Discharge.update_forward_refs()
DischargeMeta.update_forward_refs()
DischargePatient.update_forward_refs()
DischargePatientAllergy.update_forward_refs()
DischargePatientContact.update_forward_refs()
DischargePatientDemographics.update_forward_refs()
DischargePatientPCP.update_forward_refs()
DischargeVisit.update_forward_refs()
DischargeVisitAdditionalStaff.update_forward_refs()
DischargeVisitAdmittingProvider.update_forward_refs()
DischargeVisitAttendingProvider.update_forward_refs()
DischargeVisitConsultingProvider.update_forward_refs()
DischargeVisitGuarantor.update_forward_refs()
DischargeVisitGuarantorEmployer.update_forward_refs()
DischargeVisitInsurance.update_forward_refs()
DischargeVisitInsuranceCompany.update_forward_refs()
DischargeVisitInsuranceInsured.update_forward_refs()
DischargeVisitLocation.update_forward_refs()
DischargeVisitReferringProvider.update_forward_refs()
