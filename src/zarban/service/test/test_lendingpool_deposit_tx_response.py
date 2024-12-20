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
from zarban.service.openapi_client.models.lendingpool_deposit_tx_response import LendingpoolDepositTxResponse  # noqa: E501
from zarban.service.openapi_client.rest import ApiException

class TestLendingpoolDepositTxResponse(unittest.TestCase):
    """LendingpoolDepositTxResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LendingpoolDepositTxResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.service.openapi_client.models.lendingpool_deposit_tx_response.LendingpoolDepositTxResponse()  # noqa: E501
        if include_optional :
            return LendingpoolDepositTxResponse(
                chain_activity = zarban.service.openapi_client.models.chain_activity.ChainActivity(
                    step_number = 56, 
                    number_of_steps = 56, 
                    steps = [
                        zarban.service.openapi_client.models.chain_activity_step.ChainActivityStep(
                            type = 'PreparedTx', 
                            data = null, )
                        ], ), 
                response = zarban.service.openapi_client.models.lendingpool_tx_response.LendingpoolTxResponse(
                    next_health_factor = '1.2', )
            )
        else :
            return LendingpoolDepositTxResponse(
        )

    def testLendingpoolDepositTxResponse(self):
        """Test LendingpoolDepositTxResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
