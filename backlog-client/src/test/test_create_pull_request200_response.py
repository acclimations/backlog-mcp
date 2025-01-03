# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.create_pull_request200_response import CreatePullRequest200Response

class TestCreatePullRequest200Response(unittest.TestCase):
    """CreatePullRequest200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePullRequest200Response:
        """Test CreatePullRequest200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePullRequest200Response`
        """
        model = CreatePullRequest200Response()
        if include_optional:
            return CreatePullRequest200Response(
                id = 56,
                project_id = 56,
                repository_id = 56,
                number = 56,
                summary = '',
                description = '',
                base = '',
                branch = '',
                status = backlog_client.models.get_issue_200_response_priority.getIssue_200_response_priority(
                    id = 56, 
                    name = '', ),
                assignee = backlog_client.models.create_pull_request_200_response_assignee.createPullRequest_200_response_assignee(
                    id = 56, 
                    user_id = '', 
                    name = '', 
                    role_type = 56, 
                    lang = '', ),
                base_commit = '',
                branch_commit = '',
                close_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                merge_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CreatePullRequest200Response(
        )
        """

    def testCreatePullRequest200Response(self):
        """Test CreatePullRequest200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()