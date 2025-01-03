# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_project_activities200_response_inner import GetProjectActivities200ResponseInner

class TestGetProjectActivities200ResponseInner(unittest.TestCase):
    """GetProjectActivities200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetProjectActivities200ResponseInner:
        """Test GetProjectActivities200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetProjectActivities200ResponseInner`
        """
        model = GetProjectActivities200ResponseInner()
        if include_optional:
            return GetProjectActivities200ResponseInner(
                id = 56,
                project = backlog_client.models.delete_project_200_response.deleteProject_200_response(
                    id = 56, 
                    project_key = '', 
                    name = '', 
                    chart_enabled = True, 
                    use_resolved_for_chart = True, 
                    subtasking_enabled = True, 
                    project_leader_can_edit_project_leader = True, 
                    use_wiki = True, 
                    use_file_sharing = True, 
                    use_wiki_tree_view = True, 
                    use_original_image_size_at_wiki = True, 
                    text_formatting_rule = '', 
                    archived = True, 
                    display_order = 56, 
                    use_dev_attributes = True, ),
                type = 56,
                content = backlog_client.models.get_activity_200_response_content.getActivity_200_response_content(
                    id = 56, 
                    key_id = 56, 
                    summary = '', 
                    description = '', 
                    comment = backlog_client.models.get_activity_200_response_content_comment.getActivity_200_response_content_comment(
                        id = 56, 
                        content = '', ), 
                    changes = [
                        backlog_client.models.get_activity_200_response_content_changes_inner.getActivity_200_response_content_changes_inner(
                            field = '', 
                            new_value = '', 
                            old_value = '', 
                            type = '', )
                        ], ),
                notifications = [
                    None
                    ],
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
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetProjectActivities200ResponseInner(
        )
        """

    def testGetProjectActivities200ResponseInner(self):
        """Test GetProjectActivities200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
