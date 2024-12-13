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
from zarban.wallet.openapi_client.models.redemption_response import RedemptionResponse  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException

class TestRedemptionResponse(unittest.TestCase):
    """RedemptionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RedemptionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.wallet.openapi_client.models.redemption_response.RedemptionResponse()  # noqa: E501
        if include_optional :
            return RedemptionResponse(
                data = [
                    zarban.wallet.openapi_client.models.redemption.Redemption(
                        amount = {"values":{"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}}, 
                        destination_bank_info = zarban.wallet.openapi_client.models.bank_info.BankInfo(
                            bank_name = 'Bank Melli', 
                            card_number = '1234567890', 
                            iban = 'IR1234567890', ), 
                        status = {"en_US":"Zar Stablecoin","fa_IR":"استیبل کوین زر"}, 
                        id = '1234567890', 
                        created_at = zarban.wallet.openapi_client.models.timestamp.Timestamp(
                            jalaali = '1399-01-01T00:00:00Z', 
                            gregorian = '2020-01-01T00:00:00Z', ), 
                        updated_at = zarban.wallet.openapi_client.models.timestamp.Timestamp(
                            jalaali = '1399-01-01T00:00:00Z', 
                            gregorian = '2020-01-01T00:00:00Z', ), 
                        paya_tracking_code = '1234567890', )
                    ]
            )
        else :
            return RedemptionResponse(
                data = [
                    zarban.wallet.openapi_client.models.redemption.Redemption(
                        amount = {"values":{"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}}, 
                        destination_bank_info = zarban.wallet.openapi_client.models.bank_info.BankInfo(
                            bank_name = 'Bank Melli', 
                            card_number = '1234567890', 
                            iban = 'IR1234567890', ), 
                        status = {"en_US":"Zar Stablecoin","fa_IR":"استیبل کوین زر"}, 
                        id = '1234567890', 
                        created_at = zarban.wallet.openapi_client.models.timestamp.Timestamp(
                            jalaali = '1399-01-01T00:00:00Z', 
                            gregorian = '2020-01-01T00:00:00Z', ), 
                        updated_at = zarban.wallet.openapi_client.models.timestamp.Timestamp(
                            jalaali = '1399-01-01T00:00:00Z', 
                            gregorian = '2020-01-01T00:00:00Z', ), 
                        paya_tracking_code = '1234567890', )
                    ],
        )

    def testRedemptionResponse(self):
        """Test RedemptionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
