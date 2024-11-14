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
from openapi_client.models.lendingpool_stats import LendingpoolStats  # noqa: E501
from openapi_client.rest import ApiException

class TestLendingpoolStats(unittest.TestCase):
    """LendingpoolStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LendingpoolStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.lendingpool_stats.LendingpoolStats()  # noqa: E501
        if include_optional :
            return LendingpoolStats(
                total_available = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                total_borrows = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}, 
                total_market_size = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"}
            )
        else :
            return LendingpoolStats(
                total_available = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                total_borrows = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
                total_market_size = {"USD":"1.23","TMN":"45.67","ZAR":"89.01","ETH":"0.02"},
        )

    def testLendingpoolStats(self):
        """Test LendingpoolStats"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
