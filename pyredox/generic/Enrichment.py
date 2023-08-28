# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from redox_parser import enrichment
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _Enrichment(GenericEventTypeAbstractModel):
    _redox_module = enrichment


class NaturalLanguageProcessingQuery(_Enrichment):
    Meta: generic.Meta = Field(...)
    Task: generic.Task = Field(None)
    Text: generic.Text = Field(None)


class NaturalLanguageProcessingQueryResponse(_Enrichment):
    Entries: List[generic.Entry] = Field(...)
    Meta: generic.Meta = Field(...)
    Transaction: generic.Transaction = Field(...)


class NormalizationQuery(_Enrichment):
    Entries: List[generic.Entry] = Field(...)
    Meta: generic.Meta = Field(...)


class NormalizationQueryResponse(_Enrichment):
    Entries: List[generic.Entry] = Field(...)
    Meta: generic.Meta = Field(...)
