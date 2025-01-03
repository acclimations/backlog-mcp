# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_rate_limit200_response_rate_limit import GetRateLimit200ResponseRateLimit

class TestGetRateLimit200ResponseRateLimit(unittest.TestCase):
    """GetRateLimit200ResponseRateLimit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetRateLimit200ResponseRateLimit:
        """Test GetRateLimit200ResponseRateLimit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRateLimit200ResponseRateLimit`
        """
        model = GetRateLimit200ResponseRateLimit()
        if include_optional:
            return GetRateLimit200ResponseRateLimit(
                read = backlog_client.models.get_rate_limit_200_response_rate_limit_read.getRateLimit_200_response_rateLimit_read(
                    limit = 600, 
                    remaining = 600, 
                    reset = 1603881873, ),
                update = backlog_client.models.get_rate_limit_200_response_rate_limit_update.getRateLimit_200_response_rateLimit_update(
                    limit = 150, 
                    remaining = 150, 
                    reset = 1603881873, ),
                search = backlog_client.models.get_rate_limit_200_response_rate_limit_update.getRateLimit_200_response_rateLimit_update(
                    limit = 150, 
                    remaining = 150, 
                    reset = 1603881873, ),
                icon = backlog_client.models.get_rate_limit_200_response_rate_limit_icon.getRateLimit_200_response_rateLimit_icon(
                    limit = 60, 
                    remaining = 60, 
                    reset = 1603881873, )
            )
        else:
            return GetRateLimit200ResponseRateLimit(
        )
        """

    def testGetRateLimit200ResponseRateLimit(self):
        """Test GetRateLimit200ResponseRateLimit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
