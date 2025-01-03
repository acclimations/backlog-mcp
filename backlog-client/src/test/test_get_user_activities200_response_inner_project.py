# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_user_activities200_response_inner_project import GetUserActivities200ResponseInnerProject

class TestGetUserActivities200ResponseInnerProject(unittest.TestCase):
    """GetUserActivities200ResponseInnerProject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUserActivities200ResponseInnerProject:
        """Test GetUserActivities200ResponseInnerProject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUserActivities200ResponseInnerProject`
        """
        model = GetUserActivities200ResponseInnerProject()
        if include_optional:
            return GetUserActivities200ResponseInnerProject(
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
                use_dev_attributes = True
            )
        else:
            return GetUserActivities200ResponseInnerProject(
        )
        """

    def testGetUserActivities200ResponseInnerProject(self):
        """Test GetUserActivities200ResponseInnerProject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
