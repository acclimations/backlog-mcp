# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.reset_notification_count200_response import ResetNotificationCount200Response

class TestResetNotificationCount200Response(unittest.TestCase):
    """ResetNotificationCount200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResetNotificationCount200Response:
        """Test ResetNotificationCount200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResetNotificationCount200Response`
        """
        model = ResetNotificationCount200Response()
        if include_optional:
            return ResetNotificationCount200Response(
                count = 4
            )
        else:
            return ResetNotificationCount200Response(
        )
        """

    def testResetNotificationCount200Response(self):
        """Test ResetNotificationCount200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
