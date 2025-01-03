# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.delete_issue_comment200_response import DeleteIssueComment200Response

class TestDeleteIssueComment200Response(unittest.TestCase):
    """DeleteIssueComment200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteIssueComment200Response:
        """Test DeleteIssueComment200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteIssueComment200Response`
        """
        model = DeleteIssueComment200Response()
        if include_optional:
            return DeleteIssueComment200Response(
                id = 56,
                project_id = 56,
                issue_id = 56,
                content = '',
                change_log = None,
                created_user = backlog_client.models.get_issue_comment_notifications_200_response_inner_user.getIssueCommentNotifications_200_response_inner_user(
                    id = 56, 
                    user_id = '', 
                    name = '', 
                    role_type = 56, 
                    lang = '', 
                    nulab_account = backlog_client.models.get_issue_comment_notifications_200_response_inner_user_nulab_account.getIssueCommentNotifications_200_response_inner_user_nulabAccount(
                        nulab_id = '', 
                        name = '', 
                        unique_id = '', ), 
                    mail_address = '', 
                    last_login_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                stars = [
                    None
                    ],
                notifications = [
                    None
                    ]
            )
        else:
            return DeleteIssueComment200Response(
        )
        """

    def testDeleteIssueComment200Response(self):
        """Test DeleteIssueComment200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
