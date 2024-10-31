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

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from notehub_py.models.device_dfu_status import DeviceDfuStatus
from typing import Optional, Set
from typing_extensions import Self

class DeviceDfuStatusPage(BaseModel):
    """
    DeviceDfuStatusPage
    """ # noqa: E501
    devices: Optional[List[DeviceDfuStatus]] = None
    has_more: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["devices", "has_more"]

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
        """Create an instance of DeviceDfuStatusPage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in devices (list)
        _items = []
        if self.devices:
            for _item in self.devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['devices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceDfuStatusPage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "devices": [DeviceDfuStatus.from_dict(_item) for _item in obj["devices"]] if obj.get("devices") is not None else None,
            "has_more": obj.get("has_more") if obj.get("has_more") is not None else False
        })
        return _obj

