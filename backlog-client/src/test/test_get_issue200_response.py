# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_issue200_response import GetIssue200Response

class TestGetIssue200Response(unittest.TestCase):
    """GetIssue200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetIssue200Response:
        """Test GetIssue200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetIssue200Response`
        """
        model = GetIssue200Response()
        if include_optional:
            return GetIssue200Response(
                id = 56,
                project_id = 56,
                issue_key = '',
                key_id = 56,
                issue_type = backlog_client.models.get_issue_200_response_issue_type.getIssue_200_response_issueType(
                    id = 56, 
                    project_id = 56, 
                    name = '', 
                    color = '', 
                    display_order = 56, ),
                summary = '',
                description = '',
                resolution = '',
                priority = backlog_client.models.get_issue_200_response_priority.getIssue_200_response_priority(
                    id = 56, 
                    name = '', ),
                status = backlog_client.models.get_issue_200_response_issue_type.getIssue_200_response_issueType(
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
                    nulab_account = backlog_client.models.get_groups_200_response_inner_members_inner_nulab_account.getGroups_200_response_inner_members_inner_nulabAccount(
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
                    backlog_client.models.get_issue_200_response_milestone_inner.getIssue_200_response_milestone_inner(
                        id = 56, 
                        project_id = 56, 
                        name = '', 
                        description = '', 
                        start_date = '', 
                        release_due_date = '', 
                        archived = True, 
                        display_order = 56, )
                    ],
                start_date = '',
                due_date = '',
                estimated_hours = 1.337,
                actual_hours = 1.337,
                parent_issue_id = 56,
                created_user = backlog_client.models.get_groups_200_response_inner_created_user.getGroups_200_response_inner_createdUser(
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
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_user = backlog_client.models.get_groups_200_response_inner_created_user.getGroups_200_response_inner_createdUser(
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
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                custom_fields = [
                    None
                    ],
                attachments = [
                    backlog_client.models.get_issue_200_response_attachments_inner.getIssue_200_response_attachments_inner(
                        id = 56, 
                        name = '', 
                        size = 56, )
                    ],
                shared_files = [
                    None
                    ],
                stars = [
                    backlog_client.models.get_issue_200_response_stars_inner.getIssue_200_response_stars_inner(
                        id = 56, 
                        comment = '', 
                        url = '', 
                        title = '', 
                        presenter = backlog_client.models.get_groups_200_response_inner_created_user.getGroups_200_response_inner_createdUser(
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
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return GetIssue200Response(
        )
        """

    def testGetIssue200Response(self):
        """Test GetIssue200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
