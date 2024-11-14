# coding: utf-8

"""
    Zarban API

    API for Zarban services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.vault import Vault  # noqa: E501
from openapi_client.rest import ApiException

class TestVault(unittest.TestCase):
    """Vault unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Vault
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.vault.Vault()  # noqa: E501
        if include_optional :
            return Vault(
                id = 1, 
                owner = '0x1234567890123456789012345678901234567890', 
                urn = '0x1234567890123456789012345678901234567890', 
                liquidation_price = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                collateral_locked = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                collateralization_ratio = '1.5', 
                loan_to_value = '0.5', 
                debt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                available_to_withdraw = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                available_to_mint = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                ilk = openapi_client.models.ilk.Ilk(
                    name = '0', 
                    symbol = 'USD', 
                    minimum_collateralization_ratio = '0', 
                    maximum_loan_to_value = '0', 
                    liquidation_penalty = '0', 
                    debt_ceiling = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    debt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    annual_stability_fee = '0', 
                    dust_limit = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    price = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    next_price = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    join = '0', 
                    median = '0', 
                    gem = '0', 
                    clipper = '0', 
                    pip = '0', 
                    hole = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    dirt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    available_to_borrow = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, )
            )
        else :
            return Vault(
                id = 1,
                owner = '0x1234567890123456789012345678901234567890',
                urn = '0x1234567890123456789012345678901234567890',
                liquidation_price = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                collateral_locked = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                collateralization_ratio = '1.5',
                loan_to_value = '0.5',
                debt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                available_to_withdraw = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                available_to_mint = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                ilk = openapi_client.models.ilk.Ilk(
                    name = '0', 
                    symbol = 'USD', 
                    minimum_collateralization_ratio = '0', 
                    maximum_loan_to_value = '0', 
                    liquidation_penalty = '0', 
                    debt_ceiling = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    debt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    annual_stability_fee = '0', 
                    dust_limit = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    price = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    next_price = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    join = '0', 
                    median = '0', 
                    gem = '0', 
                    clipper = '0', 
                    pip = '0', 
                    hole = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    dirt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    available_to_borrow = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, ),
        )

    def testVault(self):
        """Test Vault"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
