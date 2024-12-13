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
from zarban.wallet.openapi_client.api.health_api import HealthApi  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = zarban.wallet.openapi_client.api.health_api.HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_api_health(self):
        """Test case for check_api_health

        Health check  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
