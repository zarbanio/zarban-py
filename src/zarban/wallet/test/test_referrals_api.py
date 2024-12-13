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
from zarban.wallet.openapi_client.api.referrals_api import ReferralsApi  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException


class TestReferralsApi(unittest.TestCase):
    """ReferralsApi unit test stubs"""

    def setUp(self):
        self.api = zarban.wallet.openapi_client.api.referrals_api.ReferralsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_referral_by_id(self):
        """Test case for get_referral_by_id

        Get referral by ID  # noqa: E501
        """
        pass

    def test_get_referrals(self):
        """Test case for get_referrals

        Get referrals  # noqa: E501
        """
        pass

    def test_redeem_referral(self):
        """Test case for redeem_referral

        Redeem a referral  # noqa: E501
        """
        pass

    def test_validate_referral(self):
        """Test case for validate_referral

        Validate a referral  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
