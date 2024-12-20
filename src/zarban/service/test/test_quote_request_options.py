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
from zarban.service.openapi_client.models.quote_request_options import QuoteRequestOptions  # noqa: E501
from zarban.service.openapi_client.rest import ApiException

class TestQuoteRequestOptions(unittest.TestCase):
    """QuoteRequestOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test QuoteRequestOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.service.openapi_client.models.quote_request_options.QuoteRequestOptions()  # noqa: E501
        if include_optional :
            return QuoteRequestOptions(
                dry_run = True, 
                slippage_tolerance = '0.005', 
                use_synthetic_quotes = True, 
                permit_signature = 'a', 
                permit_nonce = '0', 
                permit_expiration = 56, 
                permit_amount = '0', 
                permit_sig_deadline = 56, 
                quote_id = 'a', 
                encoded_order = 'a'
            )
        else :
            return QuoteRequestOptions(
        )

    def testQuoteRequestOptions(self):
        """Test QuoteRequestOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
