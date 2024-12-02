# coding: utf-8

"""
    Zarban Wallet API

    API for Zarban wallet services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.saving_offer import SavingOffer  # noqa: E501
from openapi_client.rest import ApiException

class TestSavingOffer(unittest.TestCase):
    """SavingOffer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SavingOffer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.saving_offer.SavingOffer()  # noqa: E501
        if include_optional :
            return SavingOffer(
                id = '0', 
                name = 'Zarban ZAR 10% APY', 
                description = 'Earn 10% APY on your ZAR savings', 
                apy = '0.20', 
                min_amount = '100.00', 
                symbol = 'USD'
            )
        else :
            return SavingOffer(
                id = '0',
                name = 'Zarban ZAR 10% APY',
                description = 'Earn 10% APY on your ZAR savings',
                apy = '0.20',
                min_amount = '100.00',
                symbol = 'USD',
        )

    def testSavingOffer(self):
        """Test SavingOffer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
