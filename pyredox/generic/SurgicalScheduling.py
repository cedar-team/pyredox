# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from pyredox import surgicalscheduling
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _SurgicalScheduling(GenericEventTypeAbstractModel):
    _redox_module = surgicalscheduling


class Cancel(_SurgicalScheduling):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Procedures: List[generic.Procedure] = Field(...)
    SurgeryStaff: List[generic.SurgeryStaff] = Field(None)
    SurgicalCase: generic.SurgicalCase = Field(None)
    SurgicalInfo: List[generic.SurgicalInfo] = Field(None)
    Visit: generic.Visit = Field(...)


class Modification(_SurgicalScheduling):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Procedures: List[generic.Procedure] = Field(...)
    SurgeryStaff: List[generic.SurgeryStaff] = Field(None)
    SurgicalCase: generic.SurgicalCase = Field(None)
    SurgicalInfo: List[generic.SurgicalInfo] = Field(None)
    Visit: generic.Visit = Field(...)


class New(_SurgicalScheduling):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Procedures: List[generic.Procedure] = Field(...)
    SurgeryStaff: List[generic.SurgeryStaff] = Field(None)
    SurgicalCase: generic.SurgicalCase = Field(None)
    SurgicalInfo: List[generic.SurgicalInfo] = Field(None)
    Visit: generic.Visit = Field(...)


class NoShow(_SurgicalScheduling):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Procedures: List[generic.Procedure] = Field(...)
    SurgeryStaff: List[generic.SurgeryStaff] = Field(None)
    SurgicalCase: generic.SurgicalCase = Field(None)
    SurgicalInfo: List[generic.SurgicalInfo] = Field(None)
    Visit: generic.Visit = Field(...)


class Reschedule(_SurgicalScheduling):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Procedures: List[generic.Procedure] = Field(...)
    SurgeryStaff: List[generic.SurgeryStaff] = Field(None)
    SurgicalCase: generic.SurgicalCase = Field(None)
    SurgicalInfo: List[generic.SurgicalInfo] = Field(None)
    Visit: generic.Visit = Field(...)
