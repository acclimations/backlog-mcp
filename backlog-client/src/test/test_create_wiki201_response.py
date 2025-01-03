# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.create_wiki201_response import CreateWiki201Response

class TestCreateWiki201Response(unittest.TestCase):
    """CreateWiki201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateWiki201Response:
        """Test CreateWiki201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateWiki201Response`
        """
        model = CreateWiki201Response()
        if include_optional:
            return CreateWiki201Response(
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
                    None
                    ],
                shared_files = [
                    None
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
            return CreateWiki201Response(
        )
        """

    def testCreateWiki201Response(self):
        """Test CreateWiki201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
