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
from zarban.wallet.openapi_client.models.user_error import UserError  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException

class TestUserError(unittest.TestCase):
    """UserError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.wallet.openapi_client.models.user_error.UserError()  # noqa: E501
        if include_optional :
            return UserError(
                messages = {
                    'key' : zarban.wallet.openapi_client.models.error_detail.ErrorDetail(
                        user_message = 'Invalid request. Please check the provided address.', 
                        solutions = [
                            'Ensure the address follows the correct format.'
                            ], )
                    }
            )
        else :
            return UserError(
                messages = {
                    'key' : zarban.wallet.openapi_client.models.error_detail.ErrorDetail(
                        user_message = 'Invalid request. Please check the provided address.', 
                        solutions = [
                            'Ensure the address follows the correct format.'
                            ], )
                    },
        )

    def testUserError(self):
        """Test UserError"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
