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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from notehub_py.models.http_filter import HttpFilter
from notehub_py.models.http_transform import HttpTransform
from typing import Optional, Set
from typing_extensions import Self

class Aws(BaseModel):
    """
    Route settings specific to AWS routes.
    """ # noqa: E501
    fleets: Optional[Annotated[List[StrictStr], Field(min_length=0)]] = Field(default=None, description="list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets")
    filter: Optional[HttpFilter] = None
    transform: Optional[HttpTransform] = None
    throttle_ms: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
    http_headers: Optional[Dict[str, StrictStr]] = None
    disable_http_headers: Optional[StrictBool] = False
    timeout: Optional[StrictInt] = Field(default=15, description="Timeout in seconds for each request")
    region: Optional[StrictStr] = None
    access_key_id: Optional[StrictStr] = None
    access_key_secret: Optional[StrictStr] = Field(default=None, description="This value is input-only and will be omitted from the response and replaced with a placeholder")
    message_group_id: Optional[StrictStr] = None
    message_deduplication_id: Optional[StrictStr] = None
    channel: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["fleets", "filter", "transform", "throttle_ms", "url", "http_headers", "disable_http_headers", "timeout", "region", "access_key_id", "access_key_secret", "message_group_id", "message_deduplication_id", "channel"]

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
        """Create an instance of Aws from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transform
        if self.transform:
            _dict['transform'] = self.transform.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Aws from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fleets": obj.get("fleets"),
            "filter": HttpFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "transform": HttpTransform.from_dict(obj["transform"]) if obj.get("transform") is not None else None,
            "throttle_ms": obj.get("throttle_ms"),
            "url": obj.get("url"),
            "http_headers": obj.get("http_headers"),
            "disable_http_headers": obj.get("disable_http_headers") if obj.get("disable_http_headers") is not None else False,
            "timeout": obj.get("timeout") if obj.get("timeout") is not None else 15,
            "region": obj.get("region"),
            "access_key_id": obj.get("access_key_id"),
            "access_key_secret": obj.get("access_key_secret"),
            "message_group_id": obj.get("message_group_id"),
            "message_deduplication_id": obj.get("message_deduplication_id"),
            "channel": obj.get("channel")
        })
        return _obj


