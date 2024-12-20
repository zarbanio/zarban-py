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

import zarban.wallet.openapi_client
from zarban.wallet.openapi_client.api.balance_api import BalanceApi  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException


class TestBalanceApi(unittest.TestCase):
    """BalanceApi unit test stubs"""

    def setUp(self):
        self.api = zarban.wallet.openapi_client.api.balance_api.BalanceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_balance_by_symbol(self):
        """Test case for get_balance_by_symbol

        Get balance  # noqa: E501
        """
        pass

    def test_get_wallet_balance(self):
        """Test case for get_wallet_balance

        Get wallet balance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
