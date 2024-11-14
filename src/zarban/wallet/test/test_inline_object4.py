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
from openapi_client.models.inline_object4 import InlineObject4  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineObject4(unittest.TestCase):
    """InlineObject4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject4
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_object4.InlineObject4()  # noqa: E501
        if include_optional :
            return InlineObject4(
                name = '0', 
                usage_limit = 56
            )
        else :
            return InlineObject4(
                usage_limit = 56,
        )

    def testInlineObject4(self):
        """Test InlineObject4"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
