# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_priorities200_response_inner import GetPriorities200ResponseInner

class TestGetPriorities200ResponseInner(unittest.TestCase):
    """GetPriorities200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPriorities200ResponseInner:
        """Test GetPriorities200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPriorities200ResponseInner`
        """
        model = GetPriorities200ResponseInner()
        if include_optional:
            return GetPriorities200ResponseInner(
                id = 2,
                name = '高'
            )
        else:
            return GetPriorities200ResponseInner(
        )
        """

    def testGetPriorities200ResponseInner(self):
        """Test GetPriorities200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()