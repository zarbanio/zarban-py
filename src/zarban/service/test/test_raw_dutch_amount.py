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
from openapi_client.models.raw_dutch_amount import RawDutchAmount  # noqa: E501
from openapi_client.rest import ApiException

class TestRawDutchAmount(unittest.TestCase):
    """RawDutchAmount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RawDutchAmount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.raw_dutch_amount.RawDutchAmount()  # noqa: E501
        if include_optional :
            return RawDutchAmount(
                token = 'a', 
                start_amount = '0', 
                end_amount = '0', 
                recipient = 'a'
            )
        else :
            return RawDutchAmount(
                token = 'a',
                start_amount = '0',
                end_amount = '0',
        )

    def testRawDutchAmount(self):
        """Test RawDutchAmount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
