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
from zarban.wallet.openapi_client.models.coin_config import CoinConfig  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException

class TestCoinConfig(unittest.TestCase):
    """CoinConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CoinConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.wallet.openapi_client.models.coin_config.CoinConfig()  # noqa: E501
        if include_optional :
            return CoinConfig(
                is_tradeable = True, 
                withdraw_fees = {"tron":"10"}, 
                min_withdrawal = {"tron":"10"}, 
                needs_memo = True
            )
        else :
            return CoinConfig(
                is_tradeable = True,
                withdraw_fees = {"tron":"10"},
                min_withdrawal = {"tron":"10"},
                needs_memo = True,
        )

    def testCoinConfig(self):
        """Test CoinConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
