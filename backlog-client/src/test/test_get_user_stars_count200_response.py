# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_user_stars_count200_response import GetUserStarsCount200Response

class TestGetUserStarsCount200Response(unittest.TestCase):
    """GetUserStarsCount200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUserStarsCount200Response:
        """Test GetUserStarsCount200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUserStarsCount200Response`
        """
        model = GetUserStarsCount200Response()
        if include_optional:
            return GetUserStarsCount200Response(
                count = 54
            )
        else:
            return GetUserStarsCount200Response(
        )
        """

    def testGetUserStarsCount200Response(self):
        """Test GetUserStarsCount200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()