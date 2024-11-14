# coding: utf-8

"""
    Zarban Wallet API

    API for Zarban wallet services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.timestamp import Timestamp  # noqa: E501
from openapi_client.rest import ApiException

class TestTimestamp(unittest.TestCase):
    """Timestamp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Timestamp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.timestamp.Timestamp()  # noqa: E501
        if include_optional :
            return Timestamp(
                jalaali = '1399-01-01T00:00:00Z', 
                gregorian = '2020-01-01T00:00:00Z'
            )
        else :
            return Timestamp(
                jalaali = '1399-01-01T00:00:00Z',
                gregorian = '2020-01-01T00:00:00Z',
        )

    def testTimestamp(self):
        """Test Timestamp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
