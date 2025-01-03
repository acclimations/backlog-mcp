# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.create_pull_request200_response_assignee import CreatePullRequest200ResponseAssignee

class TestCreatePullRequest200ResponseAssignee(unittest.TestCase):
    """CreatePullRequest200ResponseAssignee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePullRequest200ResponseAssignee:
        """Test CreatePullRequest200ResponseAssignee
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePullRequest200ResponseAssignee`
        """
        model = CreatePullRequest200ResponseAssignee()
        if include_optional:
            return CreatePullRequest200ResponseAssignee(
                id = 56,
                user_id = '',
                name = '',
                role_type = 56,
                lang = ''
            )
        else:
            return CreatePullRequest200ResponseAssignee(
        )
        """

    def testCreatePullRequest200ResponseAssignee(self):
        """Test CreatePullRequest200ResponseAssignee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()