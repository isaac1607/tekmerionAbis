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
from pydantic import BaseModel, StrictBool, StrictInt
from pydantic import Field
from abis.rest.client.models.config_adjudicator_parameters import ConfigAdjudicatorParameters
from abis.rest.client.models.config_deduplication_parameters import ConfigDeduplicationParameters
from abis.rest.client.models.config_extraction_parameters import ConfigExtractionParameters
from abis.rest.client.models.config_icao_parameters import ConfigICAOParameters
from abis.rest.client.models.config_identification_parameters import ConfigIdentificationParameters
from abis.rest.client.models.config_mq_parameters import ConfigMQParameters
from abis.rest.client.models.config_trust_factor_parameters import ConfigTrustFactorParameters
from abis.rest.client.models.config_verification_parameters import ConfigVerificationParameters
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Configuration(BaseModel):
    """
    Configuration
    """ # noqa: E501
    adjudicator_parameters: Optional[ConfigAdjudicatorParameters] = Field(default=None, alias="adjudicatorParameters")
    deduplication_parameters: Optional[ConfigDeduplicationParameters] = Field(default=None, alias="deduplicationParameters")
    extraction_parameters: Optional[ConfigExtractionParameters] = Field(default=None, alias="extractionParameters")
    icao_parameters: Optional[ConfigICAOParameters] = Field(default=None, alias="icaoParameters")
    id: Optional[StrictInt] = None
    identification_parameters: Optional[ConfigIdentificationParameters] = Field(default=None, alias="identificationParameters")
    mq_parameters: Optional[ConfigMQParameters] = Field(default=None, alias="mqParameters")
    trust_factor_parameters: Optional[ConfigTrustFactorParameters] = Field(default=None, alias="trustFactorParameters")
    use_workflows: Optional[StrictBool] = Field(default=None, alias="useWorkflows")
    verification_parameters: Optional[ConfigVerificationParameters] = Field(default=None, alias="verificationParameters")
    __properties: ClassVar[List[str]] = ["adjudicatorParameters", "deduplicationParameters", "extractionParameters", "icaoParameters", "id", "identificationParameters", "mqParameters", "trustFactorParameters", "useWorkflows", "verificationParameters"]

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
        """Create an instance of Configuration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of adjudicator_parameters
        if self.adjudicator_parameters:
            _dict['adjudicatorParameters'] = self.adjudicator_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deduplication_parameters
        if self.deduplication_parameters:
            _dict['deduplicationParameters'] = self.deduplication_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extraction_parameters
        if self.extraction_parameters:
            _dict['extractionParameters'] = self.extraction_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of icao_parameters
        if self.icao_parameters:
            _dict['icaoParameters'] = self.icao_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identification_parameters
        if self.identification_parameters:
            _dict['identificationParameters'] = self.identification_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mq_parameters
        if self.mq_parameters:
            _dict['mqParameters'] = self.mq_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trust_factor_parameters
        if self.trust_factor_parameters:
            _dict['trustFactorParameters'] = self.trust_factor_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verification_parameters
        if self.verification_parameters:
            _dict['verificationParameters'] = self.verification_parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Configuration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adjudicatorParameters": ConfigAdjudicatorParameters.from_dict(obj.get("adjudicatorParameters")) if obj.get("adjudicatorParameters") is not None else None,
            "deduplicationParameters": ConfigDeduplicationParameters.from_dict(obj.get("deduplicationParameters")) if obj.get("deduplicationParameters") is not None else None,
            "extractionParameters": ConfigExtractionParameters.from_dict(obj.get("extractionParameters")) if obj.get("extractionParameters") is not None else None,
            "icaoParameters": ConfigICAOParameters.from_dict(obj.get("icaoParameters")) if obj.get("icaoParameters") is not None else None,
            "id": obj.get("id"),
            "identificationParameters": ConfigIdentificationParameters.from_dict(obj.get("identificationParameters")) if obj.get("identificationParameters") is not None else None,
            "mqParameters": ConfigMQParameters.from_dict(obj.get("mqParameters")) if obj.get("mqParameters") is not None else None,
            "trustFactorParameters": ConfigTrustFactorParameters.from_dict(obj.get("trustFactorParameters")) if obj.get("trustFactorParameters") is not None else None,
            "useWorkflows": obj.get("useWorkflows"),
            "verificationParameters": ConfigVerificationParameters.from_dict(obj.get("verificationParameters")) if obj.get("verificationParameters") is not None else None
        })
        return _obj


