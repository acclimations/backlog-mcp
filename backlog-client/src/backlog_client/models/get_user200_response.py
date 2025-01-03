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
from backlog_client.models.get_groups200_response_inner_members_inner_nulab_account import GetGroups200ResponseInnerMembersInnerNulabAccount
from typing import Optional, Set
from typing_extensions import Self

class GetUser200Response(BaseModel):
    """
    GetUser200Response
    """ # noqa: E501
    id: Optional[StrictInt] = None
    user_id: Optional[StrictStr] = Field(default=None, alias="userId")
    name: Optional[StrictStr] = None
    role_type: Optional[StrictInt] = Field(default=None, description="クラシックプランの場合:1 管理者2 一般ユーザー3 レポーター4 ビューワー5 ゲストレポーター6 ゲストビューワー新プランの場合:1 管理者2 一般ユーザー、ゲスト（制限：制限なし）3 一般ユーザー、ゲスト（制限：課題の登録のみ）4 一般ユーザー、ゲスト（制限：課題の閲覧のみ）", alias="roleType")
    lang: Optional[StrictStr] = Field(default=None, description="\\\"en\\\" 英語\\\"ja\\\" 日本語null 未指定")
    nulab_account: Optional[GetGroups200ResponseInnerMembersInnerNulabAccount] = Field(default=None, alias="nulabAccount")
    mail_address: Optional[StrictStr] = Field(default=None, alias="mailAddress")
    last_login_time: Optional[datetime] = Field(default=None, alias="lastLoginTime")
    __properties: ClassVar[List[str]] = ["id", "userId", "name", "roleType", "lang", "nulabAccount", "mailAddress", "lastLoginTime"]

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
        """Create an instance of GetUser200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of nulab_account
        if self.nulab_account:
            _dict['nulabAccount'] = self.nulab_account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetUser200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "userId": obj.get("userId"),
            "name": obj.get("name"),
            "roleType": obj.get("roleType"),
            "lang": obj.get("lang"),
            "nulabAccount": GetGroups200ResponseInnerMembersInnerNulabAccount.from_dict(obj["nulabAccount"]) if obj.get("nulabAccount") is not None else None,
            "mailAddress": obj.get("mailAddress"),
            "lastLoginTime": obj.get("lastLoginTime")
        })
        return _obj


