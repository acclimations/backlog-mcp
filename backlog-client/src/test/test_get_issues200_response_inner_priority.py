# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_issues200_response_inner_priority import GetIssues200ResponseInnerPriority

class TestGetIssues200ResponseInnerPriority(unittest.TestCase):
    """GetIssues200ResponseInnerPriority unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetIssues200ResponseInnerPriority:
        """Test GetIssues200ResponseInnerPriority
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetIssues200ResponseInnerPriority`
        """
        model = GetIssues200ResponseInnerPriority()
        if include_optional:
            return GetIssues200ResponseInnerPriority(
                id = 56,
                name = ''
            )
        else:
            return GetIssues200ResponseInnerPriority(
        )
        """

    def testGetIssues200ResponseInnerPriority(self):
        """Test GetIssues200ResponseInnerPriority"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
