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
from pydantic import BaseModel, StrictInt
from pydantic import Field
from abis.rest.client.models.latent_gallery_configuration import LatentGalleryConfiguration

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LatentIdentificationParameters(BaseModel):
    """
    LatentIdentificationParameters
    """ # noqa: E501
    candidates_count: Optional[StrictInt] = Field(default=None, alias="candidatesCount")
    galleries: Optional[List[str]] = None
    gallery_configurations: Optional[List[LatentGalleryConfiguration]] = Field(default=None, alias="galleryConfigurations")
    threshold: Optional[StrictInt] = None
    verify_count: Optional[StrictInt] = Field(default=None, alias="verifyCount")
    __properties: ClassVar[List[str]] = ["candidatesCount", "galleries", "galleryConfigurations", "threshold", "verifyCount"]

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
        """Create an instance of LatentIdentificationParameters from a JSON string"""
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
        """Create an instance of LatentIdentificationParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "candidatesCount": obj.get("candidatesCount"),
            "threshold": obj.get("threshold"),
            "verifyCount": obj.get("verifyCount")
        })
        return _obj


