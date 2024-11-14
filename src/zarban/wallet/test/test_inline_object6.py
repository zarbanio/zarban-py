# coding: utf-8

"""
    Zarban Wallet API

    API for Zarban wallet services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.inline_object6 import InlineObject6  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineObject6(unittest.TestCase):
    """InlineObject6 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject6
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_object6.InlineObject6()  # noqa: E501
        if include_optional :
            return InlineObject6(
                intent = 'Swap', 
                quote_id = '1234567890', 
                trade_type = 'ExactInput', 
                _in = 'ZAR', 
                out = 'ETH', 
                amount = '100.00'
            )
        else :
            return InlineObject6(
                intent = 'Swap',
        )

    def testInlineObject6(self):
        """Test InlineObject6"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
