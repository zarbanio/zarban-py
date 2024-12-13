# coding: utf-8

"""
    Zarban API

    API for Zarban services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: info@zarban.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import zarban.service.openapi_client
from zarban.service.openapi_client.models.vault_events_response import VaultEventsResponse  # noqa: E501
from zarban.service.openapi_client.rest import ApiException

class TestVaultEventsResponse(unittest.TestCase):
    """VaultEventsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VaultEventsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.service.openapi_client.models.vault_events_response.VaultEventsResponse()  # noqa: E501
        if include_optional :
            return VaultEventsResponse(
                data = [
                    zarban.service.openapi_client.models.extended_event.ExtendedEvent(
                        domain = 'stableCoinSystem', 
                        id = 56, 
                        name = 'VaultRepay', 
                        raw = zarban.service.openapi_client.models.log.Log(
                            name = '0', 
                            contract = '0', 
                            timestamp = zarban.service.openapi_client.models.timestamp.Timestamp(
                                jalaali = '1399-01-01T00:00:00Z', 
                                gregorian = '2020-01-01T00:00:00Z', ), 
                            address = '0', 
                            block_number = 56, 
                            tx_hash = '0', 
                            block_hash = '0', 
                            index = 56, 
                            topics = [
                                '0x1234567890abcdef1234567abcdef'
                                ], 
                            data = '0x1234567890abcdef1234567abcdef', 
                            decoded = {
                                'key' : '0x1234567890abcdef1234567abcdef'
                                }, ), 
                        type = 'executive', 
                        payload = { }, )
                    ]
            )
        else :
            return VaultEventsResponse(
                data = [
                    zarban.service.openapi_client.models.extended_event.ExtendedEvent(
                        domain = 'stableCoinSystem', 
                        id = 56, 
                        name = 'VaultRepay', 
                        raw = zarban.service.openapi_client.models.log.Log(
                            name = '0', 
                            contract = '0', 
                            timestamp = zarban.service.openapi_client.models.timestamp.Timestamp(
                                jalaali = '1399-01-01T00:00:00Z', 
                                gregorian = '2020-01-01T00:00:00Z', ), 
                            address = '0', 
                            block_number = 56, 
                            tx_hash = '0', 
                            block_hash = '0', 
                            index = 56, 
                            topics = [
                                '0x1234567890abcdef1234567abcdef'
                                ], 
                            data = '0x1234567890abcdef1234567abcdef', 
                            decoded = {
                                'key' : '0x1234567890abcdef1234567abcdef'
                                }, ), 
                        type = 'executive', 
                        payload = { }, )
                    ],
        )

    def testVaultEventsResponse(self):
        """Test VaultEventsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
