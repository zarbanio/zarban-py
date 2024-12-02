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
from openapi_client.api.orders_api import OrdersApi  # noqa: E501
from openapi_client.rest import ApiException


class TestOrdersApi(unittest.TestCase):
    """OrdersApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.orders_api.OrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_orders_get(self):
        """Test case for orders_get

        Fetch Unfilled Orders  # noqa: E501
        """
        pass

    def test_orders_sync_post(self):
        """Test case for orders_sync_post

        Updates Order Entity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
