# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.add_recently_viewed_wiki200_response import AddRecentlyViewedWiki200Response

class TestAddRecentlyViewedWiki200Response(unittest.TestCase):
    """AddRecentlyViewedWiki200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddRecentlyViewedWiki200Response:
        """Test AddRecentlyViewedWiki200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddRecentlyViewedWiki200Response`
        """
        model = AddRecentlyViewedWiki200Response()
        if include_optional:
            return AddRecentlyViewedWiki200Response(
                id = 56,
                project_id = 56,
                name = '',
                content = '',
                tags = [
                    backlog_client.models.get_issue_200_response_priority.getIssue_200_response_priority(
                        id = 56, 
                        name = '', )
                    ],
                attachments = [
                    backlog_client.models.delete_pull_request_attachment_200_response.deletePullRequestAttachment_200_response(
                        id = 56, 
                        name = '', 
                        size = 56, 
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
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                shared_files = [
                    backlog_client.models.get_issue_shared_files_200_response_inner.getIssueSharedFiles_200_response_inner(
                        id = 56, 
                        project_id = 56, 
                        type = '', 
                        dir = '', 
                        name = '', 
                        size = 56, 
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
                            mail_address = '', 
                            last_login_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                stars = [
                    None
                    ],
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
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return AddRecentlyViewedWiki200Response(
        )
        """

    def testAddRecentlyViewedWiki200Response(self):
        """Test AddRecentlyViewedWiki200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
