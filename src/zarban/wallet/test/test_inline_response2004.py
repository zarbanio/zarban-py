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
from openapi_client.models.inline_response2004 import InlineResponse2004  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse2004(unittest.TestCase):
    """InlineResponse2004 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2004
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response2004.InlineResponse2004()  # noqa: E501
        if include_optional :
            return InlineResponse2004(
                id = 1234567890
            )
        else :
            return InlineResponse2004(
                id = 1234567890,
        )

    def testInlineResponse2004(self):
        """Test InlineResponse2004"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
