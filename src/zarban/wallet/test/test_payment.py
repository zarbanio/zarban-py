# coding: utf-8

"""
    Zarban Wallet API

    API for Zarban wallet services.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: info@zarban.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import zarban.wallet.openapi_client
from zarban.wallet.openapi_client.models.payment import Payment  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException

class TestPayment(unittest.TestCase):
    """Payment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Payment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.wallet.openapi_client.models.payment.Payment()  # noqa: E501
        if include_optional :
            return Payment(
                amount = '100.00', 
                hash = '0x1234567890abcdef', 
                url = 'https://t.me/catizenbot/gameapp?startapp=rp_1365932', 
                sender_first_name = 'John', 
                text = 'Payment for the game', 
                share_url = 'https://t.me/share/url?url=https://t.me/catizenbot/gameapp?startapp=rp_1365932&text=%F0%9F%92%B0Catizen%3A%20Unleash%2C%20Play%2C%20Earn%20-%20Where%20Every%20Game%20Leads%20to%20an%20Airdrop%20Adventure!%0A%F0%9F%8E%81Let%27s%20play-to-earn%20airdrop%20right%20now!'
            )
        else :
            return Payment(
                amount = '100.00',
                hash = '0x1234567890abcdef',
                url = 'https://t.me/catizenbot/gameapp?startapp=rp_1365932',
                sender_first_name = 'John',
                text = 'Payment for the game',
                share_url = 'https://t.me/share/url?url=https://t.me/catizenbot/gameapp?startapp=rp_1365932&text=%F0%9F%92%B0Catizen%3A%20Unleash%2C%20Play%2C%20Earn%20-%20Where%20Every%20Game%20Leads%20to%20an%20Airdrop%20Adventure!%0A%F0%9F%8E%81Let%27s%20play-to-earn%20airdrop%20right%20now!',
        )

    def testPayment(self):
        """Test Payment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
