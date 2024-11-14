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
from openapi_client.api.vaults_api import VaultsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestVaultsApi(unittest.TestCase):
    """VaultsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.vaults_api.VaultsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_vaults_get(self):
        """Test case for vaults_get

        Get vaults by owner query  # noqa: E501
        """
        pass

    def test_vaults_id_events_get(self):
        """Test case for vaults_id_events_get

        Get vault events by ID  # noqa: E501
        """
        pass

    def test_vaults_id_get(self):
        """Test case for vaults_id_get

        Get a vault by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
