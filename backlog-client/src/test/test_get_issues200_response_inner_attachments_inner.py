# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_issues200_response_inner_attachments_inner import GetIssues200ResponseInnerAttachmentsInner

class TestGetIssues200ResponseInnerAttachmentsInner(unittest.TestCase):
    """GetIssues200ResponseInnerAttachmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetIssues200ResponseInnerAttachmentsInner:
        """Test GetIssues200ResponseInnerAttachmentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetIssues200ResponseInnerAttachmentsInner`
        """
        model = GetIssues200ResponseInnerAttachmentsInner()
        if include_optional:
            return GetIssues200ResponseInnerAttachmentsInner(
                id = 56,
                name = '',
                size = 56
            )
        else:
            return GetIssues200ResponseInnerAttachmentsInner(
        )
        """

    def testGetIssues200ResponseInnerAttachmentsInner(self):
        """Test GetIssues200ResponseInnerAttachmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
