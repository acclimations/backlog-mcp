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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetSpaceDiskUsage200ResponseDetailsInner(BaseModel):
    """
    GetSpaceDiskUsage200ResponseDetailsInner
    """ # noqa: E501
    project_id: Optional[StrictInt] = Field(default=None, description="プロジェクトID", alias="projectId")
    issue: Optional[StrictInt] = Field(default=None, description="プロジェクトの課題使用容量")
    wiki: Optional[StrictInt] = Field(default=None, description="プロジェクトのWiki使用容量")
    file: Optional[StrictInt] = Field(default=None, description="プロジェクトのファイル使用容量")
    subversion: Optional[StrictInt] = Field(default=None, description="プロジェクトのSubversion使用容量")
    git: Optional[StrictInt] = Field(default=None, description="プロジェクトのGit使用容量")
    git_lfs: Optional[StrictInt] = Field(default=None, description="プロジェクトのGit LFS使用容量", alias="gitLFS")
    __properties: ClassVar[List[str]] = ["projectId", "issue", "wiki", "file", "subversion", "git", "gitLFS"]

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
        """Create an instance of GetSpaceDiskUsage200ResponseDetailsInner from a JSON string"""
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
        """Create an instance of GetSpaceDiskUsage200ResponseDetailsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "projectId": obj.get("projectId"),
            "issue": obj.get("issue"),
            "wiki": obj.get("wiki"),
            "file": obj.get("file"),
            "subversion": obj.get("subversion"),
            "git": obj.get("git"),
            "gitLFS": obj.get("gitLFS")
        })
        return _obj


