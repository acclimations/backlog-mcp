# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.get_custom_fields200_response_inner_items_inner import GetCustomFields200ResponseInnerItemsInner

class TestGetCustomFields200ResponseInnerItemsInner(unittest.TestCase):
    """GetCustomFields200ResponseInnerItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCustomFields200ResponseInnerItemsInner:
        """Test GetCustomFields200ResponseInnerItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCustomFields200ResponseInnerItemsInner`
        """
        model = GetCustomFields200ResponseInnerItemsInner()
        if include_optional:
            return GetCustomFields200ResponseInnerItemsInner(
                id = 56,
                name = '',
                display_order = 56
            )
        else:
            return GetCustomFields200ResponseInnerItemsInner(
        )
        """

    def testGetCustomFields200ResponseInnerItemsInner(self):
        """Test GetCustomFields200ResponseInnerItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
