# coding: utf-8

"""
    Zarban API

    API for Zarban services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.accounts_api import AccountsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accounts_address_get(self):
        """Test case for accounts_address_get

        Get account by address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
