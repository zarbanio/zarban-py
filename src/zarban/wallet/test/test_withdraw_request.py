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
from openapi_client.models.withdraw_request import WithdrawRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestWithdrawRequest(unittest.TestCase):
    """WithdrawRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WithdrawRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.withdraw_request.WithdrawRequest()  # noqa: E501
        if include_optional :
            return WithdrawRequest(
                id = 56, 
                time_created = openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', ), 
                network = openapi_client.models.network.Network(
                    name = {"en_US":"Zar Stablecoin","fa_IR":"استیبل کوین زر"}, 
                    logo_uri = '0', ), 
                symbol = 'USD', 
                amount = '0', 
                to = '0', 
                comment = '0', 
                status = 'Pending', 
                block_explorer_url = 'https://etherscan.io/tx/0x1234567890abcdef'
            )
        else :
            return WithdrawRequest(
                id = 56,
                time_created = openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', ),
                network = openapi_client.models.network.Network(
                    name = {"en_US":"Zar Stablecoin","fa_IR":"استیبل کوین زر"}, 
                    logo_uri = '0', ),
                symbol = 'USD',
                amount = '0',
                to = '0',
                status = 'Pending',
        )

    def testWithdrawRequest(self):
        """Test WithdrawRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
