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
from openapi_client.models.stablecoin_system_mint_zar_tx_request import StablecoinSystemMintZarTxRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestStablecoinSystemMintZarTxRequest(unittest.TestCase):
    """StablecoinSystemMintZarTxRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StablecoinSystemMintZarTxRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.stablecoin_system_mint_zar_tx_request.StablecoinSystemMintZarTxRequest()  # noqa: E501
        if include_optional :
            return StablecoinSystemMintZarTxRequest(
                user = '0x1234567890123456789012345678901234567890', 
                vault_id = 1, 
                amount = '10000000000000000000'
            )
        else :
            return StablecoinSystemMintZarTxRequest(
                user = '0x1234567890123456789012345678901234567890',
                vault_id = 1,
        )

    def testStablecoinSystemMintZarTxRequest(self):
        """Test StablecoinSystemMintZarTxRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
