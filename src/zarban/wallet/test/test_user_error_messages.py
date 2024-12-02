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
from openapi_client.models.user_error_messages import UserErrorMessages  # noqa: E501
from openapi_client.rest import ApiException

class TestUserErrorMessages(unittest.TestCase):
    """UserErrorMessages unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserErrorMessages
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.user_error_messages.UserErrorMessages()  # noqa: E501
        if include_optional :
            return UserErrorMessages(
                user_message = 'Invalid request. Please check the provided address.', 
                solutions = [
                    'Ensure the address follows the correct format.'
                    ]
            )
        else :
            return UserErrorMessages(
                user_message = 'Invalid request. Please check the provided address.',
        )

    def testUserErrorMessages(self):
        """Test UserErrorMessages"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
