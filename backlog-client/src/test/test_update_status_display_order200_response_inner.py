# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.update_status_display_order200_response_inner import UpdateStatusDisplayOrder200ResponseInner

class TestUpdateStatusDisplayOrder200ResponseInner(unittest.TestCase):
    """UpdateStatusDisplayOrder200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateStatusDisplayOrder200ResponseInner:
        """Test UpdateStatusDisplayOrder200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateStatusDisplayOrder200ResponseInner`
        """
        model = UpdateStatusDisplayOrder200ResponseInner()
        if include_optional:
            return UpdateStatusDisplayOrder200ResponseInner(
                id = 56,
                project_id = 56,
                name = '',
                color = '',
                display_order = 56
            )
        else:
            return UpdateStatusDisplayOrder200ResponseInner(
        )
        """

    def testUpdateStatusDisplayOrder200ResponseInner(self):
        """Test UpdateStatusDisplayOrder200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
