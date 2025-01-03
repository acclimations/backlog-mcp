# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.delete_issue_type200_response import DeleteIssueType200Response

class TestDeleteIssueType200Response(unittest.TestCase):
    """DeleteIssueType200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteIssueType200Response:
        """Test DeleteIssueType200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteIssueType200Response`
        """
        model = DeleteIssueType200Response()
        if include_optional:
            return DeleteIssueType200Response(
                id = 56,
                project_id = 56,
                name = '',
                color = '',
                display_order = 56,
                template_summary = '',
                template_description = ''
            )
        else:
            return DeleteIssueType200Response(
        )
        """

    def testDeleteIssueType200Response(self):
        """Test DeleteIssueType200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
