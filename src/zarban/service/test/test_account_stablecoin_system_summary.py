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
from zarban.service.openapi_client.models.account_stablecoin_system_summary import AccountStablecoinSystemSummary  # noqa: E501
from zarban.service.openapi_client.rest import ApiException

class TestAccountStablecoinSystemSummary(unittest.TestCase):
    """AccountStablecoinSystemSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountStablecoinSystemSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.service.openapi_client.models.account_stablecoin_system_summary.AccountStablecoinSystemSummary()  # noqa: E501
        if include_optional :
            return AccountStablecoinSystemSummary(
                total_debt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                total_deposits = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                net_apy = '0.30'
            )
        else :
            return AccountStablecoinSystemSummary(
                total_debt = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                total_deposits = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                net_apy = '0.30',
        )

    def testAccountStablecoinSystemSummary(self):
        """Test AccountStablecoinSystemSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
