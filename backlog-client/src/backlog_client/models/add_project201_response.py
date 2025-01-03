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

class AddProject201Response(BaseModel):
    """
    AddProject201Response
    """ # noqa: E501
    id: Optional[StrictInt] = None
    project_key: Optional[StrictStr] = Field(default=None, alias="projectKey")
    name: Optional[StrictStr] = None
    chart_enabled: Optional[StrictBool] = Field(default=None, alias="chartEnabled")
    use_resolved_for_chart: Optional[StrictBool] = Field(default=None, alias="useResolvedForChart")
    subtasking_enabled: Optional[StrictBool] = Field(default=None, alias="subtaskingEnabled")
    project_leader_can_edit_project_leader: Optional[StrictBool] = Field(default=None, alias="projectLeaderCanEditProjectLeader")
    use_wiki: Optional[StrictBool] = Field(default=None, alias="useWiki")
    use_file_sharing: Optional[StrictBool] = Field(default=None, alias="useFileSharing")
    use_wiki_tree_view: Optional[StrictBool] = Field(default=None, alias="useWikiTreeView")
    use_original_image_size_at_wiki: Optional[StrictBool] = Field(default=None, alias="useOriginalImageSizeAtWiki")
    use_subversion: Optional[StrictBool] = Field(default=None, alias="useSubversion")
    use_git: Optional[StrictBool] = Field(default=None, alias="useGit")
    text_formatting_rule: Optional[StrictStr] = Field(default=None, alias="textFormattingRule")
    archived: Optional[StrictBool] = None
    display_order: Optional[StrictInt] = Field(default=None, alias="displayOrder")
    use_dev_attributes: Optional[StrictBool] = Field(default=None, alias="useDevAttributes")
    __properties: ClassVar[List[str]] = ["id", "projectKey", "name", "chartEnabled", "useResolvedForChart", "subtaskingEnabled", "projectLeaderCanEditProjectLeader", "useWiki", "useFileSharing", "useWikiTreeView", "useOriginalImageSizeAtWiki", "useSubversion", "useGit", "textFormattingRule", "archived", "displayOrder", "useDevAttributes"]

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
        """Create an instance of AddProject201Response from a JSON string"""
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
        """Create an instance of AddProject201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "projectKey": obj.get("projectKey"),
            "name": obj.get("name"),
            "chartEnabled": obj.get("chartEnabled"),
            "useResolvedForChart": obj.get("useResolvedForChart"),
            "subtaskingEnabled": obj.get("subtaskingEnabled"),
            "projectLeaderCanEditProjectLeader": obj.get("projectLeaderCanEditProjectLeader"),
            "useWiki": obj.get("useWiki"),
            "useFileSharing": obj.get("useFileSharing"),
            "useWikiTreeView": obj.get("useWikiTreeView"),
            "useOriginalImageSizeAtWiki": obj.get("useOriginalImageSizeAtWiki"),
            "useSubversion": obj.get("useSubversion"),
            "useGit": obj.get("useGit"),
            "textFormattingRule": obj.get("textFormattingRule"),
            "archived": obj.get("archived"),
            "displayOrder": obj.get("displayOrder"),
            "useDevAttributes": obj.get("useDevAttributes")
        })
        return _obj


