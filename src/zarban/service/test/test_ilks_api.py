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
from openapi_client.api.ilks_api import IlksApi  # noqa: E501
from openapi_client.rest import ApiException


class TestIlksApi(unittest.TestCase):
    """IlksApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.ilks_api.IlksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ilks_get(self):
        """Test case for ilks_get

        Get all Ilks  # noqa: E501
        """
        pass

    def test_ilks_name_get(self):
        """Test case for ilks_name_get

        Get Ilk by name  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
