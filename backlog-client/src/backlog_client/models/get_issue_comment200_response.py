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
from backlog_client.models.get_groups200_response_inner_created_user import GetGroups200ResponseInnerCreatedUser
from typing import Optional, Set
from typing_extensions import Self

class GetIssueComment200Response(BaseModel):
    """
    GetIssueComment200Response
    """ # noqa: E501
    id: Optional[StrictInt] = None
    project_id: Optional[StrictInt] = Field(default=None, alias="projectId")
    issue_id: Optional[StrictInt] = Field(default=None, alias="issueId")
    content: Optional[StrictStr] = None
    change_log: Optional[Any] = Field(default=None, alias="changeLog")
    created_user: Optional[GetGroups200ResponseInnerCreatedUser] = Field(default=None, alias="createdUser")
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    stars: Optional[List[Any]] = None
    notifications: Optional[List[Any]] = None
    __properties: ClassVar[List[str]] = ["id", "projectId", "issueId", "content", "changeLog", "createdUser", "created", "updated", "stars", "notifications"]

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
        """Create an instance of GetIssueComment200Response from a JSON string"""
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
        # set to None if change_log (nullable) is None
        # and model_fields_set contains the field
        if self.change_log is None and "change_log" in self.model_fields_set:
            _dict['changeLog'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetIssueComment200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "projectId": obj.get("projectId"),
            "issueId": obj.get("issueId"),
            "content": obj.get("content"),
            "changeLog": obj.get("changeLog"),
            "createdUser": GetGroups200ResponseInnerCreatedUser.from_dict(obj["createdUser"]) if obj.get("createdUser") is not None else None,
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "stars": obj.get("stars"),
            "notifications": obj.get("notifications")
        })
        return _obj


