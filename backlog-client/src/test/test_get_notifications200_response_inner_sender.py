# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_notifications200_response_inner_sender import GetNotifications200ResponseInnerSender

class TestGetNotifications200ResponseInnerSender(unittest.TestCase):
    """GetNotifications200ResponseInnerSender unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetNotifications200ResponseInnerSender:
        """Test GetNotifications200ResponseInnerSender
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetNotifications200ResponseInnerSender`
        """
        model = GetNotifications200ResponseInnerSender()
        if include_optional:
            return GetNotifications200ResponseInnerSender(
                id = 56,
                user_id = '',
                name = '',
                role_type = 56,
                lang = '',
                mail_address = '',
                last_login_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetNotifications200ResponseInnerSender(
        )
        """

    def testGetNotifications200ResponseInnerSender(self):
        """Test GetNotifications200ResponseInnerSender"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
