# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_space_notification200_response import GetSpaceNotification200Response

class TestGetSpaceNotification200Response(unittest.TestCase):
    """GetSpaceNotification200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSpaceNotification200Response:
        """Test GetSpaceNotification200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSpaceNotification200Response`
        """
        model = GetSpaceNotification200Response()
        if include_optional:
            return GetSpaceNotification200Response(
                content = 'Notification',
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetSpaceNotification200Response(
        )
        """

    def testGetSpaceNotification200Response(self):
        """Test GetSpaceNotification200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
