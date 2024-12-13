# coding: utf-8

"""
    Zarban API

    API for Zarban services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: info@zarban.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import zarban.service.openapi_client
from zarban.service.openapi_client.models.stablecoin_system_redo_tx_request import StablecoinSystemRedoTxRequest  # noqa: E501
from zarban.service.openapi_client.rest import ApiException

class TestStablecoinSystemRedoTxRequest(unittest.TestCase):
    """StablecoinSystemRedoTxRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StablecoinSystemRedoTxRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.service.openapi_client.models.stablecoin_system_redo_tx_request.StablecoinSystemRedoTxRequest()  # noqa: E501
        if include_optional :
            return StablecoinSystemRedoTxRequest(
                user = '0x1234567890123456789012345678901234567890', 
                auction_id = 1, 
                ilk = 'ETHA'
            )
        else :
            return StablecoinSystemRedoTxRequest(
                user = '0x1234567890123456789012345678901234567890',
                auction_id = 1,
                ilk = 'ETHA',
        )

    def testStablecoinSystemRedoTxRequest(self):
        """Test StablecoinSystemRedoTxRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
