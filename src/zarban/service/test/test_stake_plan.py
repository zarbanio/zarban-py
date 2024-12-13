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
from zarban.service.openapi_client.models.stake_plan import StakePlan  # noqa: E501
from zarban.service.openapi_client.rest import ApiException

class TestStakePlan(unittest.TestCase):
    """StakePlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StakePlan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.service.openapi_client.models.stake_plan.StakePlan()  # noqa: E501
        if include_optional :
            return StakePlan(
                plan_name = 'Zar Staking', 
                contract_address = '0x1234567890123456789012345678901234567890', 
                apy = '0.12', 
                stake_token = zarban.service.openapi_client.models.token.Token(
                    name = 'Zar Stablecoin', 
                    symbol = 'USD', 
                    decimals = 18, 
                    address = '0x1234567890123456789012345678901234567890', 
                    logo_uri = '/assets/logos/dai.svg', 
                    chain_id = 1, 
                    persian_name = 'زر', ), 
                reward_token = zarban.service.openapi_client.models.token.Token(
                    name = 'Zar Stablecoin', 
                    symbol = 'USD', 
                    decimals = 18, 
                    address = '0x1234567890123456789012345678901234567890', 
                    logo_uri = '/assets/logos/dai.svg', 
                    chain_id = 1, 
                    persian_name = 'زر', ), 
                finish_at = zarban.service.openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', )
            )
        else :
            return StakePlan(
                plan_name = 'Zar Staking',
                contract_address = '0x1234567890123456789012345678901234567890',
                apy = '0.12',
                stake_token = zarban.service.openapi_client.models.token.Token(
                    name = 'Zar Stablecoin', 
                    symbol = 'USD', 
                    decimals = 18, 
                    address = '0x1234567890123456789012345678901234567890', 
                    logo_uri = '/assets/logos/dai.svg', 
                    chain_id = 1, 
                    persian_name = 'زر', ),
                reward_token = zarban.service.openapi_client.models.token.Token(
                    name = 'Zar Stablecoin', 
                    symbol = 'USD', 
                    decimals = 18, 
                    address = '0x1234567890123456789012345678901234567890', 
                    logo_uri = '/assets/logos/dai.svg', 
                    chain_id = 1, 
                    persian_name = 'زر', ),
                finish_at = zarban.service.openapi_client.models.timestamp.Timestamp(
                    jalaali = '1399-01-01T00:00:00Z', 
                    gregorian = '2020-01-01T00:00:00Z', ),
        )

    def testStakePlan(self):
        """Test StakePlan"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()