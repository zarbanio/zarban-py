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
from zarban.wallet.openapi_client.models.transaction_response import TransactionResponse  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException

class TestTransactionResponse(unittest.TestCase):
    """TransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransactionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.wallet.openapi_client.models.transaction_response.TransactionResponse()  # noqa: E501
        if include_optional :
            return TransactionResponse(
                data = [
                    zarban.wallet.openapi_client.models.transaction.Transaction(
                        id = 56, 
                        time = zarban.wallet.openapi_client.models.timestamp.Timestamp(
                            jalaali = '1399-01-01T00:00:00Z', 
                            gregorian = '2020-01-01T00:00:00Z', ), 
                        type = 'Credit', 
                        from = '0', 
                        to = '0', 
                        symbol = 'USD', 
                        amount = {"values":{"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}}, 
                        direction = 'Inbound', 
                        external_transaction = zarban.wallet.openapi_client.models.external_transaction.ExternalTransaction(
                            id = 56, 
                            time = zarban.wallet.openapi_client.models.timestamp.Timestamp(
                                jalaali = '1399-01-01T00:00:00Z', 
                                gregorian = '2020-01-01T00:00:00Z', ), 
                            type = 'Credit', 
                            hash = '0', 
                            from = '0', 
                            to = '0', 
                            comment = '0', 
                            amount = {"values":{"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}}, 
                            symbol = 'USD', 
                            network = zarban.wallet.openapi_client.models.network.Network(
                                name = {"en_US":"Zar Stablecoin","fa_IR":"استیبل کوین زر"}, 
                                logo_uri = '0', ), 
                            status = 'Sent', ), )
                    ]
            )
        else :
            return TransactionResponse(
                data = [
                    zarban.wallet.openapi_client.models.transaction.Transaction(
                        id = 56, 
                        time = zarban.wallet.openapi_client.models.timestamp.Timestamp(
                            jalaali = '1399-01-01T00:00:00Z', 
                            gregorian = '2020-01-01T00:00:00Z', ), 
                        type = 'Credit', 
                        from = '0', 
                        to = '0', 
                        symbol = 'USD', 
                        amount = {"values":{"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}}, 
                        direction = 'Inbound', 
                        external_transaction = zarban.wallet.openapi_client.models.external_transaction.ExternalTransaction(
                            id = 56, 
                            time = zarban.wallet.openapi_client.models.timestamp.Timestamp(
                                jalaali = '1399-01-01T00:00:00Z', 
                                gregorian = '2020-01-01T00:00:00Z', ), 
                            type = 'Credit', 
                            hash = '0', 
                            from = '0', 
                            to = '0', 
                            comment = '0', 
                            amount = {"values":{"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}}, 
                            symbol = 'USD', 
                            network = zarban.wallet.openapi_client.models.network.Network(
                                name = {"en_US":"Zar Stablecoin","fa_IR":"استیبل کوین زر"}, 
                                logo_uri = '0', ), 
                            status = 'Sent', ), )
                    ],
        )

    def testTransactionResponse(self):
        """Test TransactionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
