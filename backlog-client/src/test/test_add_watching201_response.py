# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.add_watching201_response import AddWatching201Response

class TestAddWatching201Response(unittest.TestCase):
    """AddWatching201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddWatching201Response:
        """Test AddWatching201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddWatching201Response`
        """
        model = AddWatching201Response()
        if include_optional:
            return AddWatching201Response(
                id = 56,
                note = '',
                type = '',
                issue = backlog_client.models.add_watching_201_response_issue.addWatching_201_response_issue(
                    id = 56, 
                    project_id = 56, 
                    issue_key = '', 
                    key_id = 56, 
                    issue_type = backlog_client.models.get_issues_200_response_inner_issue_type.getIssues_200_response_inner_issueType(
                        id = 56, 
                        project_id = 56, 
                        name = '', 
                        color = '', 
                        display_order = 56, ), 
                    summary = '', 
                    description = '', 
                    resolution = '', 
                    priority = backlog_client.models.get_issues_200_response_inner_priority.getIssues_200_response_inner_priority(
                        id = 56, 
                        name = '', ), 
                    status = backlog_client.models.get_issues_200_response_inner_issue_type.getIssues_200_response_inner_issueType(
                        id = 56, 
                        project_id = 56, 
                        name = '', 
                        color = '', 
                        display_order = 56, ), 
                    assignee = backlog_client.models.get_groups_200_response_inner_members_inner.getGroups_200_response_inner_members_inner(
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
                    category = [
                        None
                        ], 
                    versions = [
                        None
                        ], 
                    milestone = [
                        None
                        ], 
                    start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    estimated_hours = 1.337, 
                    actual_hours = 1.337, 
                    parent_issue_id = 56, 
                    created_user = backlog_client.models.get_issue_comment_notifications_200_response_inner_user.getIssueCommentNotifications_200_response_inner_user(
                        id = 56, 
                        user_id = '', 
                        name = '', 
                        role_type = 56, 
                        lang = '', 
                        mail_address = '', 
                        last_login_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_user = backlog_client.models.get_issue_comment_notifications_200_response_inner_user.getIssueCommentNotifications_200_response_inner_user(
                        id = 56, 
                        user_id = '', 
                        name = '', 
                        role_type = 56, 
                        lang = '', 
                        mail_address = '', 
                        last_login_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    custom_fields = [
                        None
                        ], 
                    attachments = [
                        None
                        ], 
                    shared_files = [
                        None
                        ], 
                    stars = [
                        None
                        ], ),
                last_content_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return AddWatching201Response(
        )
        """

    def testAddWatching201Response(self):
        """Test AddWatching201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()