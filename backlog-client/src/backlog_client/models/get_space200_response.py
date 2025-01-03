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
from typing import Optional, Set
from typing_extensions import Self

class GetSpace200Response(BaseModel):
    """
    GetSpace200Response
    """ # noqa: E501
    space_key: Optional[StrictStr] = Field(default=None, alias="spaceKey")
    name: Optional[StrictStr] = None
    owner_id: Optional[StrictInt] = Field(default=None, alias="ownerId")
    lang: Optional[StrictStr] = None
    timezone: Optional[StrictStr] = None
    report_send_time: Optional[StrictStr] = Field(default=None, alias="reportSendTime")
    text_formatting_rule: Optional[StrictStr] = Field(default=None, alias="textFormattingRule")
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["spaceKey", "name", "ownerId", "lang", "timezone", "reportSendTime", "textFormattingRule", "created", "updated"]

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
        """Create an instance of GetSpace200Response from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetSpace200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "spaceKey": obj.get("spaceKey"),
            "name": obj.get("name"),
            "ownerId": obj.get("ownerId"),
            "lang": obj.get("lang"),
            "timezone": obj.get("timezone"),
            "reportSendTime": obj.get("reportSendTime"),
            "textFormattingRule": obj.get("textFormattingRule"),
            "created": obj.get("created"),
            "updated": obj.get("updated")
        })
        return _obj


