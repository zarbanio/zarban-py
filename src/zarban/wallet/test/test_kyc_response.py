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
from zarban.wallet.openapi_client.models.kyc_response import KycResponse  # noqa: E501
from zarban.wallet.openapi_client.rest import ApiException

class TestKycResponse(unittest.TestCase):
    """KycResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KycResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.wallet.openapi_client.models.kyc_response.KycResponse()  # noqa: E501
        if include_optional :
            return KycResponse(
                id = '1234567890', 
                first_name = 'John', 
                last_name = 'Doe', 
                national_id = '1234567890', 
                date_of_birth = '1360/01/01', 
                bank_info = zarban.wallet.openapi_client.models.bank_info.BankInfo(
                    bank_name = 'Bank Melli', 
                    card_number = '1234567890', 
                    iban = 'IR1234567890', )
            )
        else :
            return KycResponse(
                id = '1234567890',
                first_name = 'John',
                last_name = 'Doe',
                national_id = '1234567890',
                date_of_birth = '1360/01/01',
                bank_info = zarban.wallet.openapi_client.models.bank_info.BankInfo(
                    bank_name = 'Bank Melli', 
                    card_number = '1234567890', 
                    iban = 'IR1234567890', ),
        )

    def testKycResponse(self):
        """Test KycResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
