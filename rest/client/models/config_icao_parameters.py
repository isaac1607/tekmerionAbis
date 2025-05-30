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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigICAOParameters(BaseModel):
    """
    ConfigICAOParameters
    """ # noqa: E501
    background_elimination: Optional[StrictBool] = Field(default=None, alias="backgroundElimination")
    bg_uniformity_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="bgUniformityMax")
    bg_uniformity_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="bgUniformityMin")
    brightness_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="brightnessMax")
    brightness_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="brightnessMin")
    color_profile_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="colorProfileMax")
    color_profile_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="colorProfileMin")
    contrast_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="contrastMax")
    contrast_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="contrastMin")
    eye_distance_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="eyeDistanceMax")
    eye_distance_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="eyeDistanceMin")
    eye_gaze_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="eyeGazeMax")
    eye_gaze_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="eyeGazeMin")
    eye_status_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="eyeStatusMax")
    eye_status_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="eyeStatusMin")
    face_detection_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="faceDetectionMax")
    face_detection_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="faceDetectionMin")
    glasses_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="glassesMax")
    glasses_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="glassesMin")
    glasses_status_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="glassesStatusMax")
    glasses_status_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="glassesStatusMin")
    heavy_frame_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="heavyFrameMax")
    heavy_frame_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="heavyFrameMin")
    horiz_nose_root_pos_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="horizNoseRootPosMax")
    horiz_nose_root_pos_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="horizNoseRootPosMin")
    image_ratio: Optional[StrictStr] = Field(default=None, alias="imageRatio")
    mouth_status_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="mouthStatusMax")
    mouth_status_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="mouthStatusMin")
    nose_shadow_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="noseShadowMax")
    nose_shadow_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="noseShadowMin")
    pitch_angle_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pitchAngleMax")
    pitch_angle_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pitchAngleMin")
    rect_width_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="rectWidthMax")
    rect_width_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="rectWidthMin")
    red_eyes_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="redEyesMax")
    red_eyes_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="redEyesMin")
    roll_angle_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="rollAngleMax")
    shadow_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="shadowMax")
    shadow_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="shadowMin")
    sharpness_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sharpnessMax")
    sharpness_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sharpnessMin")
    specularity_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="specularityMax")
    specularity_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="specularityMin")
    vertical_eye_position_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="verticalEyePositionMax")
    vertical_eye_position_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="verticalEyePositionMin")
    yaw_angle_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="yawAngleMax")
    yaw_angle_min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="yawAngleMin")
    __properties: ClassVar[List[str]] = ["backgroundElimination", "bgUniformityMax", "bgUniformityMin", "brightnessMax", "brightnessMin", "colorProfileMax", "colorProfileMin", "contrastMax", "contrastMin", "eyeDistanceMax", "eyeDistanceMin", "eyeGazeMax", "eyeGazeMin", "eyeStatusMax", "eyeStatusMin", "faceDetectionMax", "faceDetectionMin", "glassesMax", "glassesMin", "glassesStatusMax", "glassesStatusMin", "heavyFrameMax", "heavyFrameMin", "horizNoseRootPosMax", "horizNoseRootPosMin", "imageRatio", "mouthStatusMax", "mouthStatusMin", "noseShadowMax", "noseShadowMin", "pitchAngleMax", "pitchAngleMin", "rectWidthMax", "rectWidthMin", "redEyesMax", "redEyesMin", "rollAngleMax", "shadowMax", "shadowMin", "sharpnessMax", "sharpnessMin", "specularityMax", "specularityMin", "verticalEyePositionMax", "verticalEyePositionMin", "yawAngleMax", "yawAngleMin"]

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
        """Create an instance of ConfigICAOParameters from a JSON string"""
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
        """Create an instance of ConfigICAOParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backgroundElimination": obj.get("backgroundElimination"),
            "bgUniformityMax": obj.get("bgUniformityMax"),
            "bgUniformityMin": obj.get("bgUniformityMin"),
            "brightnessMax": obj.get("brightnessMax"),
            "brightnessMin": obj.get("brightnessMin"),
            "colorProfileMax": obj.get("colorProfileMax"),
            "colorProfileMin": obj.get("colorProfileMin"),
            "contrastMax": obj.get("contrastMax"),
            "contrastMin": obj.get("contrastMin"),
            "eyeDistanceMax": obj.get("eyeDistanceMax"),
            "eyeDistanceMin": obj.get("eyeDistanceMin"),
            "eyeGazeMax": obj.get("eyeGazeMax"),
            "eyeGazeMin": obj.get("eyeGazeMin"),
            "eyeStatusMax": obj.get("eyeStatusMax"),
            "eyeStatusMin": obj.get("eyeStatusMin"),
            "faceDetectionMax": obj.get("faceDetectionMax"),
            "faceDetectionMin": obj.get("faceDetectionMin"),
            "glassesMax": obj.get("glassesMax"),
            "glassesMin": obj.get("glassesMin"),
            "glassesStatusMax": obj.get("glassesStatusMax"),
            "glassesStatusMin": obj.get("glassesStatusMin"),
            "heavyFrameMax": obj.get("heavyFrameMax"),
            "heavyFrameMin": obj.get("heavyFrameMin"),
            "horizNoseRootPosMax": obj.get("horizNoseRootPosMax"),
            "horizNoseRootPosMin": obj.get("horizNoseRootPosMin"),
            "imageRatio": obj.get("imageRatio"),
            "mouthStatusMax": obj.get("mouthStatusMax"),
            "mouthStatusMin": obj.get("mouthStatusMin"),
            "noseShadowMax": obj.get("noseShadowMax"),
            "noseShadowMin": obj.get("noseShadowMin"),
            "pitchAngleMax": obj.get("pitchAngleMax"),
            "pitchAngleMin": obj.get("pitchAngleMin"),
            "rectWidthMax": obj.get("rectWidthMax"),
            "rectWidthMin": obj.get("rectWidthMin"),
            "redEyesMax": obj.get("redEyesMax"),
            "redEyesMin": obj.get("redEyesMin"),
            "rollAngleMax": obj.get("rollAngleMax"),
            "shadowMax": obj.get("shadowMax"),
            "shadowMin": obj.get("shadowMin"),
            "sharpnessMax": obj.get("sharpnessMax"),
            "sharpnessMin": obj.get("sharpnessMin"),
            "specularityMax": obj.get("specularityMax"),
            "specularityMin": obj.get("specularityMin"),
            "verticalEyePositionMax": obj.get("verticalEyePositionMax"),
            "verticalEyePositionMin": obj.get("verticalEyePositionMin"),
            "yawAngleMax": obj.get("yawAngleMax"),
            "yawAngleMin": obj.get("yawAngleMin")
        })
        return _obj


