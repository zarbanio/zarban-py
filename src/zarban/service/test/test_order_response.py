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
from zarban.service.openapi_client.models.order_response import OrderResponse  # noqa: E501
from zarban.service.openapi_client.rest import ApiException

class TestOrderResponse(unittest.TestCase):
    """OrderResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrderResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.service.openapi_client.models.order_response.OrderResponse()  # noqa: E501
        if include_optional :
            return OrderResponse(
                data = [
                    zarban.service.openapi_client.models.order.Order(
                        quote_id = 'a', 
                        outputs = [
                            zarban.service.openapi_client.models.raw_dutch_amount.RawDutchAmount(
                                token = 'a', 
                                start_amount = '0', 
                                end_amount = '0', 
                                recipient = 'a', )
                            ], 
                        encoded_order = 'a', 
                        signature = 'a', 
                        input = zarban.service.openapi_client.models.raw_dutch_amount.RawDutchAmount(
                            token = 'a', 
                            start_amount = '0', 
                            end_amount = '0', 
                            recipient = 'a', ), 
                        order_status = 'open', 
                        chain_id = 56, 
                        order_hash = 'a', 
                        order_type = 'dutch', )
                    ]
            )
        else :
            return OrderResponse(
                data = [
                    zarban.service.openapi_client.models.order.Order(
                        quote_id = 'a', 
                        outputs = [
                            zarban.service.openapi_client.models.raw_dutch_amount.RawDutchAmount(
                                token = 'a', 
                                start_amount = '0', 
                                end_amount = '0', 
                                recipient = 'a', )
                            ], 
                        encoded_order = 'a', 
                        signature = 'a', 
                        input = zarban.service.openapi_client.models.raw_dutch_amount.RawDutchAmount(
                            token = 'a', 
                            start_amount = '0', 
                            end_amount = '0', 
                            recipient = 'a', ), 
                        order_status = 'open', 
                        chain_id = 56, 
                        order_hash = 'a', 
                        order_type = 'dutch', )
                    ],
        )

    def testOrderResponse(self):
        """Test OrderResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()