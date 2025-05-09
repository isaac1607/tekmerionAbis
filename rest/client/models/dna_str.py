# coding: utf-8

"""
    ABIS REST API

    Innovatrics ABIS proprietary REST API

    The version of the OpenAPI document: 6.62.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DnaStr(BaseModel):
    """
    DnaStr
    """ # noqa: E501
    allele_call1: Optional[StrictStr] = Field(default=None, alias="alleleCall1")
    allele_call2: Optional[StrictStr] = Field(default=None, alias="alleleCall2")
    allele_call3: Optional[StrictStr] = Field(default=None, alias="alleleCall3")
    allele_indicator: Optional[StrictStr] = Field(default=None, description="AlleleIndicator", alias="alleleIndicator")
    dna_locus_reference: Optional[StrictInt] = Field(default=None, alias="dnaLocusReference")
    kit_description: Optional[StrictStr] = Field(default=None, alias="kitDescription")
    kit_id: Optional[StrictInt] = Field(default=None, alias="kitId")
    kit_manufacturer: Optional[StrictStr] = Field(default=None, alias="kitManufacturer")
    kit_name: Optional[StrictStr] = Field(default=None, alias="kitName")
    locus_analysis_indicator: Optional[StrictStr] = Field(default=None, description="Locus analysis indicator", alias="locusAnalysisIndicator")
    precise_call_determination: Optional[StrictStr] = Field(default=None, description="Precise call determination", alias="preciseCallDetermination")
    str_type: Optional[StrictStr] = Field(default=None, description="STR type", alias="strType")
    __properties: ClassVar[List[str]] = ["alleleCall1", "alleleCall2", "alleleCall3", "alleleIndicator", "dnaLocusReference", "kitDescription", "kitId", "kitManufacturer", "kitName", "locusAnalysisIndicator", "preciseCallDetermination", "strType"]

    @field_validator('allele_indicator')
    def allele_indicator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NoAlleleFound', 'Other'):
            raise ValueError("must be one of enum values ('NoAlleleFound', 'Other')")
        return value

    @field_validator('locus_analysis_indicator')
    def locus_analysis_indicator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NotAnalyzed', 'Other'):
            raise ValueError("must be one of enum values ('NotAnalyzed', 'Other')")
        return value

    @field_validator('precise_call_determination')
    def precise_call_determination_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Precise', 'Other'):
            raise ValueError("must be one of enum values ('Precise', 'Other')")
        return value

    @field_validator('str_type')
    def str_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AutosomalStrProfile', 'XStrProfile', 'YStrProfile'):
            raise ValueError("must be one of enum values ('AutosomalStrProfile', 'XStrProfile', 'YStrProfile')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DnaStr from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DnaStr from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alleleCall1": obj.get("alleleCall1"),
            "alleleCall2": obj.get("alleleCall2"),
            "alleleCall3": obj.get("alleleCall3"),
            "alleleIndicator": obj.get("alleleIndicator"),
            "dnaLocusReference": obj.get("dnaLocusReference"),
            "kitDescription": obj.get("kitDescription"),
            "kitId": obj.get("kitId"),
            "kitManufacturer": obj.get("kitManufacturer"),
            "kitName": obj.get("kitName"),
            "locusAnalysisIndicator": obj.get("locusAnalysisIndicator"),
            "preciseCallDetermination": obj.get("preciseCallDetermination"),
            "strType": obj.get("strType")
        })
        return _obj


