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
from zarban.service.openapi_client.models.formatted_reserve_data import FormattedReserveData  # noqa: E501
from zarban.service.openapi_client.rest import ApiException

class TestFormattedReserveData(unittest.TestCase):
    """FormattedReserveData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FormattedReserveData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.service.openapi_client.models.formatted_reserve_data.FormattedReserveData()  # noqa: E501
        if include_optional :
            return FormattedReserveData(
                id = '0x1234567890123456789012345678901234567890:0x1234567890123456789012345678901234567890', 
                underlying_asset = zarban.service.openapi_client.models.token.Token(
                    name = 'Zar Stablecoin', 
                    symbol = 'USD', 
                    decimals = 18, 
                    address = '0x1234567890123456789012345678901234567890', 
                    logo_uri = '/assets/logos/dai.svg', 
                    chain_id = 1, 
                    persian_name = 'زر', ), 
                z_token_address = '0x1234567890123456789012345678901234567890', 
                variable_debt_token_address = '0x1234567890123456789012345678901234567890', 
                borrowing_enabled = True, 
                is_active = True, 
                is_frozen = False, 
                usage_as_collateral_enabled = True, 
                reserve_factor = '0.1', 
                base_lt_vas_collateral = '0.5', 
                reserve_liquidation_threshold = '0.6', 
                reserve_liquidation_bonus = '0.1', 
                utilization_rate = '0.5', 
                total_debt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                total_liquidity = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                available_liquidity = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                supply_apy = '0.1', 
                supply_apr = '0.1', 
                variable_borrow_apy = '0.1', 
                variable_borrow_apr = '0.1', 
                price = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}
            )
        else :
            return FormattedReserveData(
                id = '0x1234567890123456789012345678901234567890:0x1234567890123456789012345678901234567890',
                underlying_asset = zarban.service.openapi_client.models.token.Token(
                    name = 'Zar Stablecoin', 
                    symbol = 'USD', 
                    decimals = 18, 
                    address = '0x1234567890123456789012345678901234567890', 
                    logo_uri = '/assets/logos/dai.svg', 
                    chain_id = 1, 
                    persian_name = 'زر', ),
                z_token_address = '0x1234567890123456789012345678901234567890',
                variable_debt_token_address = '0x1234567890123456789012345678901234567890',
                borrowing_enabled = True,
                is_active = True,
                is_frozen = False,
                usage_as_collateral_enabled = True,
                reserve_factor = '0.1',
                base_lt_vas_collateral = '0.5',
                reserve_liquidation_threshold = '0.6',
                reserve_liquidation_bonus = '0.1',
                utilization_rate = '0.5',
                total_debt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                total_liquidity = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                available_liquidity = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                supply_apy = '0.1',
                supply_apr = '0.1',
                variable_borrow_apy = '0.1',
                variable_borrow_apr = '0.1',
                price = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
        )

    def testFormattedReserveData(self):
        """Test FormattedReserveData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
