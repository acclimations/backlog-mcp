# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_issue_comment_notifications200_response_inner import GetIssueCommentNotifications200ResponseInner

class TestGetIssueCommentNotifications200ResponseInner(unittest.TestCase):
    """GetIssueCommentNotifications200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetIssueCommentNotifications200ResponseInner:
        """Test GetIssueCommentNotifications200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetIssueCommentNotifications200ResponseInner`
        """
        model = GetIssueCommentNotifications200ResponseInner()
        if include_optional:
            return GetIssueCommentNotifications200ResponseInner(
                id = 56,
                already_read = True,
                reason = 56,
                user = backlog_client.models.get_groups_200_response_inner_created_user.getGroups_200_response_inner_createdUser(
                    id = 56, 
                    user_id = '', 
                    name = '', 
                    role_type = 56, 
                    lang = '', 
                    nulab_account = backlog_client.models.get_groups_200_response_inner_members_inner_nulab_account.getGroups_200_response_inner_members_inner_nulabAccount(
                        nulab_id = '', 
                        name = '', 
                        unique_id = '', ), 
                    mail_address = '', 
                    last_login_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                resource_already_read = True
            )
        else:
            return GetIssueCommentNotifications200ResponseInner(
        )
        """

    def testGetIssueCommentNotifications200ResponseInner(self):
        """Test GetIssueCommentNotifications200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
