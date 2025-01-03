# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_project_categories200_response_inner import GetProjectCategories200ResponseInner

class TestGetProjectCategories200ResponseInner(unittest.TestCase):
    """GetProjectCategories200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetProjectCategories200ResponseInner:
        """Test GetProjectCategories200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetProjectCategories200ResponseInner`
        """
        model = GetProjectCategories200ResponseInner()
        if include_optional:
            return GetProjectCategories200ResponseInner(
                id = 12,
                project_id = 5,
                name = '開発',
                display_order = 0
            )
        else:
            return GetProjectCategories200ResponseInner(
        )
        """

    def testGetProjectCategories200ResponseInner(self):
        """Test GetProjectCategories200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
