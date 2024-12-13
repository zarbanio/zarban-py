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
from zarban.service.openapi_client.models.vault_event_extension import VaultEventExtension  # noqa: E501
from zarban.service.openapi_client.rest import ApiException

class TestVaultEventExtension(unittest.TestCase):
    """VaultEventExtension unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VaultEventExtension
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.service.openapi_client.models.vault_event_extension.VaultEventExtension()  # noqa: E501
        if include_optional :
            return VaultEventExtension(
                payload = zarban.service.openapi_client.models.vault_event.VaultEvent(
                    delta_collateral = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    delta_debt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                    ilk = zarban.service.openapi_client.models.ilk.Ilk(
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
                        available_to_borrow = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, ), )
            )
        else :
            return VaultEventExtension(
        )

    def testVaultEventExtension(self):
        """Test VaultEventExtension"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()