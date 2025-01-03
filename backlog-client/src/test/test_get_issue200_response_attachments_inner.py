# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_issue200_response_attachments_inner import GetIssue200ResponseAttachmentsInner

class TestGetIssue200ResponseAttachmentsInner(unittest.TestCase):
    """GetIssue200ResponseAttachmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetIssue200ResponseAttachmentsInner:
        """Test GetIssue200ResponseAttachmentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetIssue200ResponseAttachmentsInner`
        """
        model = GetIssue200ResponseAttachmentsInner()
        if include_optional:
            return GetIssue200ResponseAttachmentsInner(
                id = 56,
                name = '',
                size = 56
            )
        else:
            return GetIssue200ResponseAttachmentsInner(
        )
        """

    def testGetIssue200ResponseAttachmentsInner(self):
        """Test GetIssue200ResponseAttachmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
