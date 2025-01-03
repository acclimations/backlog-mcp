# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.models.update_issue200_response_stars_inner import UpdateIssue200ResponseStarsInner

class TestUpdateIssue200ResponseStarsInner(unittest.TestCase):
    """UpdateIssue200ResponseStarsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateIssue200ResponseStarsInner:
        """Test UpdateIssue200ResponseStarsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateIssue200ResponseStarsInner`
        """
        model = UpdateIssue200ResponseStarsInner()
        if include_optional:
            return UpdateIssue200ResponseStarsInner(
                id = 56,
                comment = '',
                url = '',
                title = '',
                presenter = None,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return UpdateIssue200ResponseStarsInner(
        )
        """

    def testUpdateIssue200ResponseStarsInner(self):
        """Test UpdateIssue200ResponseStarsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
