# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.update_space_notification200_response import UpdateSpaceNotification200Response

class TestUpdateSpaceNotification200Response(unittest.TestCase):
    """UpdateSpaceNotification200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSpaceNotification200Response:
        """Test UpdateSpaceNotification200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSpaceNotification200Response`
        """
        model = UpdateSpaceNotification200Response()
        if include_optional:
            return UpdateSpaceNotification200Response(
                content = 'Notification',
                updated = '2013-06-18T07:55:37Z'
            )
        else:
            return UpdateSpaceNotification200Response(
        )
        """

    def testUpdateSpaceNotification200Response(self):
        """Test UpdateSpaceNotification200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
