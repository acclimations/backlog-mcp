# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_project_versions200_response_inner import GetProjectVersions200ResponseInner

class TestGetProjectVersions200ResponseInner(unittest.TestCase):
    """GetProjectVersions200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetProjectVersions200ResponseInner:
        """Test GetProjectVersions200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetProjectVersions200ResponseInner`
        """
        model = GetProjectVersions200ResponseInner()
        if include_optional:
            return GetProjectVersions200ResponseInner(
                id = 56,
                project_id = 56,
                name = '',
                description = '',
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                release_due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                archived = True,
                display_order = 56
            )
        else:
            return GetProjectVersions200ResponseInner(
        )
        """

    def testGetProjectVersions200ResponseInner(self):
        """Test GetProjectVersions200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
