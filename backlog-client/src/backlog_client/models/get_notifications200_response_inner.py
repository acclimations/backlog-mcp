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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from backlog_client.models.delete_project200_response import DeleteProject200Response
from backlog_client.models.get_notifications200_response_inner_comment import GetNotifications200ResponseInnerComment
from backlog_client.models.get_notifications200_response_inner_issue import GetNotifications200ResponseInnerIssue
from backlog_client.models.get_notifications200_response_inner_sender import GetNotifications200ResponseInnerSender
from typing import Optional, Set
from typing_extensions import Self

class GetNotifications200ResponseInner(BaseModel):
    """
    GetNotifications200ResponseInner
    """ # noqa: E501
    id: Optional[StrictInt] = None
    already_read: Optional[StrictBool] = Field(default=None, alias="alreadyRead")
    reason: Optional[StrictInt] = Field(default=None, description="通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新")
    resource_already_read: Optional[StrictBool] = Field(default=None, alias="resourceAlreadyRead")
    project: Optional[DeleteProject200Response] = None
    issue: Optional[GetNotifications200ResponseInnerIssue] = None
    comment: Optional[GetNotifications200ResponseInnerComment] = None
    sender: Optional[GetNotifications200ResponseInnerSender] = None
    created: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "alreadyRead", "reason", "resourceAlreadyRead", "project", "issue", "comment", "sender", "created"]

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
        """Create an instance of GetNotifications200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issue
        if self.issue:
            _dict['issue'] = self.issue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict['comment'] = self.comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sender
        if self.sender:
            _dict['sender'] = self.sender.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetNotifications200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "alreadyRead": obj.get("alreadyRead"),
            "reason": obj.get("reason"),
            "resourceAlreadyRead": obj.get("resourceAlreadyRead"),
            "project": DeleteProject200Response.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "issue": GetNotifications200ResponseInnerIssue.from_dict(obj["issue"]) if obj.get("issue") is not None else None,
            "comment": GetNotifications200ResponseInnerComment.from_dict(obj["comment"]) if obj.get("comment") is not None else None,
            "sender": GetNotifications200ResponseInnerSender.from_dict(obj["sender"]) if obj.get("sender") is not None else None,
            "created": obj.get("created")
        })
        return _obj


