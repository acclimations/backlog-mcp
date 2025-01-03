# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_space_disk_usage200_response import GetSpaceDiskUsage200Response

class TestGetSpaceDiskUsage200Response(unittest.TestCase):
    """GetSpaceDiskUsage200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSpaceDiskUsage200Response:
        """Test GetSpaceDiskUsage200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSpaceDiskUsage200Response`
        """
        model = GetSpaceDiskUsage200Response()
        if include_optional:
            return GetSpaceDiskUsage200Response(
                capacity = 56,
                issue = 56,
                wiki = 56,
                file = 56,
                subversion = 56,
                git = 56,
                git_lfs = 56,
                details = [
                    backlog_client.models.get_space_disk_usage_200_response_details_inner.getSpaceDiskUsage_200_response_details_inner(
                        project_id = 56, 
                        issue = 56, 
                        wiki = 56, 
                        file = 56, 
                        subversion = 56, 
                        git = 56, 
                        git_lfs = 56, )
                    ]
            )
        else:
            return GetSpaceDiskUsage200Response(
        )
        """

    def testGetSpaceDiskUsage200Response(self):
        """Test GetSpaceDiskUsage200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
