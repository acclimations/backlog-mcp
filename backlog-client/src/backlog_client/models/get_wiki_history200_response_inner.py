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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backlog_client.models.get_groups200_response_inner_members_inner import GetGroups200ResponseInnerMembersInner
from typing import Optional, Set
from typing_extensions import Self

class GetWikiHistory200ResponseInner(BaseModel):
    """
    GetWikiHistory200ResponseInner
    """ # noqa: E501
    page_id: Optional[StrictInt] = Field(default=None, alias="pageId")
    version: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    content: Optional[StrictStr] = None
    created_user: Optional[GetGroups200ResponseInnerMembersInner] = Field(default=None, alias="createdUser")
    created: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["pageId", "version", "name", "content", "createdUser", "created"]

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
        """Create an instance of GetWikiHistory200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_user
        if self.created_user:
            _dict['createdUser'] = self.created_user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetWikiHistory200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pageId": obj.get("pageId"),
            "version": obj.get("version"),
            "name": obj.get("name"),
            "content": obj.get("content"),
            "createdUser": GetGroups200ResponseInnerMembersInner.from_dict(obj["createdUser"]) if obj.get("createdUser") is not None else None,
            "created": obj.get("created")
        })
        return _obj


