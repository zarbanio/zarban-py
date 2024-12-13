# coding: utf-8

"""
    Zarban Wallet API

    API for Zarban wallet services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: info@zarban.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import zarban.wallet.openapi_client
from zarban.wallet.openapi_client.models.withdraw_request_response import WithdrawRequestResponse  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException

class TestWithdrawRequestResponse(unittest.TestCase):
    """WithdrawRequestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WithdrawRequestResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.wallet.openapi_client.models.withdraw_request_response.WithdrawRequestResponse()  # noqa: E501
        if include_optional :
            return WithdrawRequestResponse(
                data = [
                    zarban.wallet.openapi_client.models.withdraw_request.WithdrawRequest(
                        id = 56, 
                        time_created = zarban.wallet.openapi_client.models.timestamp.Timestamp(
                            jalaali = '1399-01-01T00:00:00Z', 
                            gregorian = '2020-01-01T00:00:00Z', ), 
                        network = zarban.wallet.openapi_client.models.network.Network(
                            name = {"en_US":"Zar Stablecoin","fa_IR":"استیبل کوین زر"}, 
                            logo_uri = '0', ), 
                        symbol = 'USD', 
                        amount = '0', 
                        to = '0', 
                        comment = '0', 
                        status = 'Pending', 
                        block_explorer_url = 'https://etherscan.io/tx/0x1234567890abcdef', )
                    ]
            )
        else :
            return WithdrawRequestResponse(
                data = [
                    zarban.wallet.openapi_client.models.withdraw_request.WithdrawRequest(
                        id = 56, 
                        time_created = zarban.wallet.openapi_client.models.timestamp.Timestamp(
                            jalaali = '1399-01-01T00:00:00Z', 
                            gregorian = '2020-01-01T00:00:00Z', ), 
                        network = zarban.wallet.openapi_client.models.network.Network(
                            name = {"en_US":"Zar Stablecoin","fa_IR":"استیبل کوین زر"}, 
                            logo_uri = '0', ), 
                        symbol = 'USD', 
                        amount = '0', 
                        to = '0', 
                        comment = '0', 
                        status = 'Pending', 
                        block_explorer_url = 'https://etherscan.io/tx/0x1234567890abcdef', )
                    ],
        )

    def testWithdrawRequestResponse(self):
        """Test WithdrawRequestResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
