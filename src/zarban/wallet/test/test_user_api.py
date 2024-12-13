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

import zarban.wallet.openapi_client
from zarban.wallet.openapi_client.api.user_api import UserApi  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = zarban.wallet.openapi_client.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_confirm_kyc(self):
        """Test case for confirm_kyc

        Confirm KYC  # noqa: E501
        """
        pass

    def test_confirm_phone_number(self):
        """Test case for confirm_phone_number

        Confirm phone number  # noqa: E501
        """
        pass

    def test_create_child_user(self):
        """Test case for create_child_user

        create a child user  # noqa: E501
        """
        pass

    def test_get_user_profile(self):
        """Test case for get_user_profile

        Get profile  # noqa: E501
        """
        pass

    def test_submit_email_confirmation_otp(self):
        """Test case for submit_email_confirmation_otp

        Submit email confirmation OTP  # noqa: E501
        """
        pass

    def test_submit_kyc(self):
        """Test case for submit_kyc

        Submit KYC  # noqa: E501
        """
        pass

    def test_verify_phone_number(self):
        """Test case for verify_phone_number

        Verify phone number  # noqa: E501
        """
        pass

    def test_verify_user_email_address(self):
        """Test case for verify_user_email_address

        Verify email  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
