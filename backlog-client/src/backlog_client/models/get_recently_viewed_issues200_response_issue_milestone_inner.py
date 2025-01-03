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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetRecentlyViewedIssues200ResponseIssueMilestoneInner(BaseModel):
    """
    GetRecentlyViewedIssues200ResponseIssueMilestoneInner
    """ # noqa: E501
    id: Optional[StrictInt] = None
    project_id: Optional[StrictInt] = Field(default=None, alias="projectId")
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    start_date: Optional[StrictStr] = Field(default=None, alias="startDate")
    release_due_date: Optional[StrictStr] = Field(default=None, alias="releaseDueDate")
    archived: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "projectId", "name", "description", "startDate", "releaseDueDate", "archived"]

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
        """Create an instance of GetRecentlyViewedIssues200ResponseIssueMilestoneInner from a JSON string"""
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
        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['startDate'] = None

        # set to None if release_due_date (nullable) is None
        # and model_fields_set contains the field
        if self.release_due_date is None and "release_due_date" in self.model_fields_set:
            _dict['releaseDueDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetRecentlyViewedIssues200ResponseIssueMilestoneInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "projectId": obj.get("projectId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "startDate": obj.get("startDate"),
            "releaseDueDate": obj.get("releaseDueDate"),
            "archived": obj.get("archived")
        })
        return _obj


