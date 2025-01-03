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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backlog_client.models.get_git_repository200_response_created_user import GetGitRepository200ResponseCreatedUser
from typing import Optional, Set
from typing_extensions import Self

class GetGitRepository200Response(BaseModel):
    """
    GetGitRepository200Response
    """ # noqa: E501
    id: Optional[StrictInt] = None
    project_id: Optional[StrictInt] = Field(default=None, alias="projectId")
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    hook_url: Optional[StrictStr] = Field(default=None, alias="hookUrl")
    http_url: Optional[StrictStr] = Field(default=None, alias="httpUrl")
    ssh_url: Optional[StrictStr] = Field(default=None, alias="sshUrl")
    display_order: Optional[StrictInt] = Field(default=None, alias="displayOrder")
    pushed_at: Optional[StrictStr] = Field(default=None, alias="pushedAt")
    created_user: Optional[GetGitRepository200ResponseCreatedUser] = Field(default=None, alias="createdUser")
    created: Optional[StrictStr] = None
    updated_user: Optional[GetGitRepository200ResponseCreatedUser] = Field(default=None, alias="updatedUser")
    updated: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "projectId", "name", "description", "hookUrl", "httpUrl", "sshUrl", "displayOrder", "pushedAt", "createdUser", "created", "updatedUser", "updated"]

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
        """Create an instance of GetGitRepository200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of updated_user
        if self.updated_user:
            _dict['updatedUser'] = self.updated_user.to_dict()
        # set to None if hook_url (nullable) is None
        # and model_fields_set contains the field
        if self.hook_url is None and "hook_url" in self.model_fields_set:
            _dict['hookUrl'] = None

        # set to None if pushed_at (nullable) is None
        # and model_fields_set contains the field
        if self.pushed_at is None and "pushed_at" in self.model_fields_set:
            _dict['pushedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetGitRepository200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "projectId": obj.get("projectId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "hookUrl": obj.get("hookUrl"),
            "httpUrl": obj.get("httpUrl"),
            "sshUrl": obj.get("sshUrl"),
            "displayOrder": obj.get("displayOrder"),
            "pushedAt": obj.get("pushedAt"),
            "createdUser": GetGitRepository200ResponseCreatedUser.from_dict(obj["createdUser"]) if obj.get("createdUser") is not None else None,
            "created": obj.get("created"),
            "updatedUser": GetGitRepository200ResponseCreatedUser.from_dict(obj["updatedUser"]) if obj.get("updatedUser") is not None else None,
            "updated": obj.get("updated")
        })
        return _obj

