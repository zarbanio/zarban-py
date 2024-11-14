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
from openapi_client.models.swap_response import SwapResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestSwapResponse(unittest.TestCase):
    """SwapResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SwapResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.swap_response.SwapResponse()  # noqa: E501
        if include_optional :
            return SwapResponse(
                id = '0', 
                trade_type = 'ExactInput', 
                _in = 'USD', 
                out = 'USD', 
                amount = '0', 
                quote = '0', 
                rate = '0', 
                value = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                input_balance_after_swap = '0', 
                output_balance_after_swap = '0', 
                created_at = openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', ), 
                expires_at = openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', ), 
                executed_at = openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', )
            )
        else :
            return SwapResponse(
                id = '0',
                trade_type = 'ExactInput',
                _in = 'USD',
                out = 'USD',
                amount = '0',
                quote = '0',
                rate = '0',
                value = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                created_at = openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', ),
                expires_at = openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', ),
        )

    def testSwapResponse(self):
        """Test SwapResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
