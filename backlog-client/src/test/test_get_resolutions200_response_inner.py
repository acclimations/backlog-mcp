# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_resolutions200_response_inner import GetResolutions200ResponseInner

class TestGetResolutions200ResponseInner(unittest.TestCase):
    """GetResolutions200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetResolutions200ResponseInner:
        """Test GetResolutions200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetResolutions200ResponseInner`
        """
        model = GetResolutions200ResponseInner()
        if include_optional:
            return GetResolutions200ResponseInner(
                id = 0,
                name = '対応済み'
            )
        else:
            return GetResolutions200ResponseInner(
        )
        """

    def testGetResolutions200ResponseInner(self):
        """Test GetResolutions200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
