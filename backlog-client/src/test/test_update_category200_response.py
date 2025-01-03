# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.update_category200_response import UpdateCategory200Response

class TestUpdateCategory200Response(unittest.TestCase):
    """UpdateCategory200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateCategory200Response:
        """Test UpdateCategory200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCategory200Response`
        """
        model = UpdateCategory200Response()
        if include_optional:
            return UpdateCategory200Response(
                id = 56,
                project_id = 56,
                name = '',
                display_order = 56
            )
        else:
            return UpdateCategory200Response(
        )
        """

    def testUpdateCategory200Response(self):
        """Test UpdateCategory200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
