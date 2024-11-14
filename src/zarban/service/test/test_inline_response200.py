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
from openapi_client.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse200(unittest.TestCase):
    """InlineResponse200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse200
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response200.InlineResponse200()  # noqa: E501
        if include_optional :
            return InlineResponse200(
                chain_activity = openapi_client.models.chain_activity.ChainActivity(
                    step_number = 56, 
                    number_of_steps = 56, 
                    steps = [
                        openapi_client.models.chain_activity_step.ChainActivityStep(
                            type = 'PreparedTx', 
                            data = null, )
                        ], ), 
                response = openapi_client.models.lendingpool_tx_response.LendingpoolTxResponse(
                    next_health_factor = '1.2', )
            )
        else :
            return InlineResponse200(
        )

    def testInlineResponse200(self):
        """Test InlineResponse200"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
