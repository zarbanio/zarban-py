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
from openapi_client.api.addresses_api import AddressesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestAddressesApi(unittest.TestCase):
    """AddressesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.addresses_api.AddressesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_addresses_get(self):
        """Test case for addresses_get

        Get all addresses  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
