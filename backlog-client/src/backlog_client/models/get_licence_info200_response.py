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
from typing import Optional, Set
from typing_extensions import Self

class GetLicenceInfo200Response(BaseModel):
    """
    GetLicenceInfo200Response
    """ # noqa: E501
    active: Optional[StrictBool] = None
    attachment_limit: Optional[StrictInt] = Field(default=None, alias="attachmentLimit")
    attachment_limit_per_file: Optional[StrictInt] = Field(default=None, alias="attachmentLimitPerFile")
    attachment_num_limit: Optional[StrictInt] = Field(default=None, alias="attachmentNumLimit")
    attribute: Optional[StrictBool] = None
    attribute_limit: Optional[StrictInt] = Field(default=None, alias="attributeLimit")
    burndown: Optional[StrictBool] = None
    comment_limit: Optional[StrictInt] = Field(default=None, alias="commentLimit")
    component_limit: Optional[StrictInt] = Field(default=None, alias="componentLimit")
    file_sharing: Optional[StrictBool] = Field(default=None, alias="fileSharing")
    gantt: Optional[StrictBool] = None
    git: Optional[StrictBool] = None
    issue_limit: Optional[StrictInt] = Field(default=None, alias="issueLimit")
    licence_type_id: Optional[StrictInt] = Field(default=None, alias="licenceTypeId")
    limit_date: Optional[datetime] = Field(default=None, alias="limitDate")
    nulab_account: Optional[StrictBool] = Field(default=None, alias="nulabAccount")
    parent_child_issue: Optional[StrictBool] = Field(default=None, alias="parentChildIssue")
    post_issue_by_mail: Optional[StrictBool] = Field(default=None, alias="postIssueByMail")
    project_limit: Optional[StrictInt] = Field(default=None, alias="projectLimit")
    pull_request_attachment_limit_per_file: Optional[StrictInt] = Field(default=None, alias="pullRequestAttachmentLimitPerFile")
    pull_request_attachment_num_limit: Optional[StrictInt] = Field(default=None, alias="pullRequestAttachmentNumLimit")
    remote_address: Optional[StrictBool] = Field(default=None, alias="remoteAddress")
    remote_address_limit: Optional[StrictInt] = Field(default=None, alias="remoteAddressLimit")
    started_on: Optional[datetime] = Field(default=None, alias="startedOn")
    storage_limit: Optional[StrictInt] = Field(default=None, alias="storageLimit")
    subversion: Optional[StrictBool] = None
    subversion_external: Optional[StrictBool] = Field(default=None, alias="subversionExternal")
    user_limit: Optional[StrictInt] = Field(default=None, alias="userLimit")
    version_limit: Optional[StrictInt] = Field(default=None, alias="versionLimit")
    wiki_attachment: Optional[StrictBool] = Field(default=None, alias="wikiAttachment")
    wiki_attachment_limit_per_file: Optional[StrictInt] = Field(default=None, alias="wikiAttachmentLimitPerFile")
    wiki_attachment_num_limit: Optional[StrictInt] = Field(default=None, alias="wikiAttachmentNumLimit")
    __properties: ClassVar[List[str]] = ["active", "attachmentLimit", "attachmentLimitPerFile", "attachmentNumLimit", "attribute", "attributeLimit", "burndown", "commentLimit", "componentLimit", "fileSharing", "gantt", "git", "issueLimit", "licenceTypeId", "limitDate", "nulabAccount", "parentChildIssue", "postIssueByMail", "projectLimit", "pullRequestAttachmentLimitPerFile", "pullRequestAttachmentNumLimit", "remoteAddress", "remoteAddressLimit", "startedOn", "storageLimit", "subversion", "subversionExternal", "userLimit", "versionLimit", "wikiAttachment", "wikiAttachmentLimitPerFile", "wikiAttachmentNumLimit"]

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
        """Create an instance of GetLicenceInfo200Response from a JSON string"""
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
        """Create an instance of GetLicenceInfo200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "attachmentLimit": obj.get("attachmentLimit"),
            "attachmentLimitPerFile": obj.get("attachmentLimitPerFile"),
            "attachmentNumLimit": obj.get("attachmentNumLimit"),
            "attribute": obj.get("attribute"),
            "attributeLimit": obj.get("attributeLimit"),
            "burndown": obj.get("burndown"),
            "commentLimit": obj.get("commentLimit"),
            "componentLimit": obj.get("componentLimit"),
            "fileSharing": obj.get("fileSharing"),
            "gantt": obj.get("gantt"),
            "git": obj.get("git"),
            "issueLimit": obj.get("issueLimit"),
            "licenceTypeId": obj.get("licenceTypeId"),
            "limitDate": obj.get("limitDate"),
            "nulabAccount": obj.get("nulabAccount"),
            "parentChildIssue": obj.get("parentChildIssue"),
            "postIssueByMail": obj.get("postIssueByMail"),
            "projectLimit": obj.get("projectLimit"),
            "pullRequestAttachmentLimitPerFile": obj.get("pullRequestAttachmentLimitPerFile"),
            "pullRequestAttachmentNumLimit": obj.get("pullRequestAttachmentNumLimit"),
            "remoteAddress": obj.get("remoteAddress"),
            "remoteAddressLimit": obj.get("remoteAddressLimit"),
            "startedOn": obj.get("startedOn"),
            "storageLimit": obj.get("storageLimit"),
            "subversion": obj.get("subversion"),
            "subversionExternal": obj.get("subversionExternal"),
            "userLimit": obj.get("userLimit"),
            "versionLimit": obj.get("versionLimit"),
            "wikiAttachment": obj.get("wikiAttachment"),
            "wikiAttachmentLimitPerFile": obj.get("wikiAttachmentLimitPerFile"),
            "wikiAttachmentNumLimit": obj.get("wikiAttachmentNumLimit")
        })
        return _obj


