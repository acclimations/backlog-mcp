# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from backlog_client.models.get_rate_limit200_response_rate_limit_icon import GetRateLimit200ResponseRateLimitIcon
from backlog_client.models.get_rate_limit200_response_rate_limit_read import GetRateLimit200ResponseRateLimitRead
from backlog_client.models.get_rate_limit200_response_rate_limit_update import GetRateLimit200ResponseRateLimitUpdate
from typing import Optional, Set
from typing_extensions import Self

class GetRateLimit200ResponseRateLimit(BaseModel):
    """
    GetRateLimit200ResponseRateLimit
    """ # noqa: E501
    read: Optional[GetRateLimit200ResponseRateLimitRead] = None
    update: Optional[GetRateLimit200ResponseRateLimitUpdate] = None
    search: Optional[GetRateLimit200ResponseRateLimitUpdate] = None
    icon: Optional[GetRateLimit200ResponseRateLimitIcon] = None
    __properties: ClassVar[List[str]] = ["read", "update", "search", "icon"]

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
        """Create an instance of GetRateLimit200ResponseRateLimit from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of read
        if self.read:
            _dict['read'] = self.read.to_dict()
        # override the default output from pydantic by calling `to_dict()` of update
        if self.update:
            _dict['update'] = self.update.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search
        if self.search:
            _dict['search'] = self.search.to_dict()
        # override the default output from pydantic by calling `to_dict()` of icon
        if self.icon:
            _dict['icon'] = self.icon.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetRateLimit200ResponseRateLimit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "read": GetRateLimit200ResponseRateLimitRead.from_dict(obj["read"]) if obj.get("read") is not None else None,
            "update": GetRateLimit200ResponseRateLimitUpdate.from_dict(obj["update"]) if obj.get("update") is not None else None,
            "search": GetRateLimit200ResponseRateLimitUpdate.from_dict(obj["search"]) if obj.get("search") is not None else None,
            "icon": GetRateLimit200ResponseRateLimitIcon.from_dict(obj["icon"]) if obj.get("icon") is not None else None
        })
        return _obj


