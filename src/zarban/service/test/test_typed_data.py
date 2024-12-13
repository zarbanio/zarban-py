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
from zarban.service.openapi_client.models.typed_data import TypedData  # noqa: E501
from zarban.service.openapi_client.rest import ApiException

class TestTypedData(unittest.TestCase):
    """TypedData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TypedData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = zarban.service.openapi_client.models.typed_data.TypedData()  # noqa: E501
        if include_optional :
            return TypedData(
                types = {
                    'key' : [
                        zarban.service.openapi_client.models.type.Type(
                            name = '0', 
                            type = '0', )
                        ]
                    }, 
                primary_type = '0', 
                domain = zarban.service.openapi_client.models.typed_data_domain.TypedDataDomain(
                    name = '0', 
                    version = '0', 
                    chain_id = '0', 
                    verifying_contract = '0', 
                    salt = '0', ), 
                message = { }
            )
        else :
            return TypedData(
                types = {
                    'key' : [
                        zarban.service.openapi_client.models.type.Type(
                            name = '0', 
                            type = '0', )
                        ]
                    },
                primary_type = '0',
                domain = zarban.service.openapi_client.models.typed_data_domain.TypedDataDomain(
                    name = '0', 
                    version = '0', 
                    chain_id = '0', 
                    verifying_contract = '0', 
                    salt = '0', ),
                message = { },
        )

    def testTypedData(self):
        """Test TypedData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
