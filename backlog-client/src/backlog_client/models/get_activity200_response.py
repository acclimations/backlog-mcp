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
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from backlog_client.models.delete_project200_response import DeleteProject200Response
from backlog_client.models.get_activity200_response_content import GetActivity200ResponseContent
from backlog_client.models.get_activity200_response_notifications_inner import GetActivity200ResponseNotificationsInner
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from typing import Optional, Set
from typing_extensions import Self

class GetActivity200Response(BaseModel):
    """
    GetActivity200Response
    """ # noqa: E501
    id: Optional[StrictInt] = None
    project: Optional[DeleteProject200Response] = None
    type: Optional[StrictInt] = Field(default=None, description="最近の更新の種別：1:課題の追加2:課題の更新3:課題にコメント4:課題の削除5:Wikiを追加6:Wikiを更新7:Wikiを削除8:共有ファイルを追加9:共有ファイルを更新10:共有ファイルを削除11:Subversionコミット12:GITプッシュ13:GITリポジトリ作成14:課題をまとめて更新15:ユーザーがプロジェクトに参加16:ユーザーがプロジェクトから脱退17:コメントにお知らせを追加18:プルリクエストの追加19:プルリクエストの更新20:プルリクエストにコメント21:プルリクエストの削除22:マイルストーンの追加23:マイルストーンの更新24:マイルストーンの削除25:グループがプロジェクトに参加26:グループがプロジェクトから脱退")
    content: Optional[GetActivity200ResponseContent] = None
    notifications: Optional[List[GetActivity200ResponseNotificationsInner]] = None
    created_user: Optional[GetIssueCommentNotifications200ResponseInnerUser] = Field(default=None, alias="createdUser")
    created: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "project", "type", "content", "notifications", "createdUser", "created"]

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
        """Create an instance of GetActivity200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict['content'] = self.content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item_notifications in self.notifications:
                if _item_notifications:
                    _items.append(_item_notifications.to_dict())
            _dict['notifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_user
        if self.created_user:
            _dict['createdUser'] = self.created_user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetActivity200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "project": DeleteProject200Response.from_dict(obj["project"]) if obj.get("project") is not None else None,
            "type": obj.get("type"),
            "content": GetActivity200ResponseContent.from_dict(obj["content"]) if obj.get("content") is not None else None,
            "notifications": [GetActivity200ResponseNotificationsInner.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None,
            "createdUser": GetIssueCommentNotifications200ResponseInnerUser.from_dict(obj["createdUser"]) if obj.get("createdUser") is not None else None,
            "created": obj.get("created")
        })
        return _obj


