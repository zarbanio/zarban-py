# coding: utf-8

"""
    Zarban API

    API for Zarban services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.log import Log  # noqa: E501
from openapi_client.rest import ApiException

class TestLog(unittest.TestCase):
    """Log unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Log
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.log.Log()  # noqa: E501
        if include_optional :
            return Log(
                id = 1, 
                timestamp = openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', ), 
                address = '0', 
                block_number = '0', 
                tx_hash = '0', 
                block_hash = '0', 
                index = 56, 
                topics = [
                    '0x1234567890abcdef1234567abcdef'
                    ], 
                data = '0x1234567890abcdef1234567abcdef'
            )
        else :
            return Log(
                id = 1,
                timestamp = openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', ),
                address = '0',
                block_number = '0',
                tx_hash = '0',
                block_hash = '0',
                index = 56,
                topics = [
                    '0x1234567890abcdef1234567abcdef'
                    ],
                data = '0x1234567890abcdef1234567abcdef',
        )

    def testLog(self):
        """Test Log"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
