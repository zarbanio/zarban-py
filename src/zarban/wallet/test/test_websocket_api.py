# coding: utf-8

"""
    Zarban Wallet API

    API for Zarban wallet services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.websocket_api import WebsocketApi  # noqa: E501
from openapi_client.rest import ApiException


class TestWebsocketApi(unittest.TestCase):
    """WebsocketApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.websocket_api.WebsocketApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ws_get(self):
        """Test case for ws_get

        Websocket Upgrade  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
