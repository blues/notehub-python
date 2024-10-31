# coding: utf-8

"""
    Notehub API

    The OpenAPI definition for the Notehub.io API. 

    The version of the OpenAPI document: 1.2.0
    Contact: engineering@blues.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from notehub_py.models.current_firmware import CurrentFirmware
from notehub_py.models.user_dfu_state_machine import UserDfuStateMachine
from typing import Optional, Set
from typing_extensions import Self

class UserFirmwareInfo(BaseModel):
    """
    UserFirmwareInfo
    """ # noqa: E501
    current_firmware: Optional[CurrentFirmware] = None
    firmware_update: Optional[UserDfuStateMachine] = None
    __properties: ClassVar[List[str]] = ["current_firmware", "firmware_update"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserFirmwareInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of current_firmware
        if self.current_firmware:
            _dict['current_firmware'] = self.current_firmware.to_dict()
        # override the default output from pydantic by calling `to_dict()` of firmware_update
        if self.firmware_update:
            _dict['firmware_update'] = self.firmware_update.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserFirmwareInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current_firmware": CurrentFirmware.from_dict(obj["current_firmware"]) if obj.get("current_firmware") is not None else None,
            "firmware_update": UserDfuStateMachine.from_dict(obj["firmware_update"]) if obj.get("firmware_update") is not None else None
        })
        return _obj


