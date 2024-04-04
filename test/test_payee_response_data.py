# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_sdk_openapi.models.payee_response_data import PayeeResponseData

class TestPayeeResponseData(unittest.TestCase):
    """PayeeResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayeeResponseData:
        """Test PayeeResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayeeResponseData`
        """
        model = PayeeResponseData()
        if include_optional:
            return PayeeResponseData(
                payee = ynab_sdk_openapi.models.payee.Payee(
                    id = '', 
                    name = '', 
                    transfer_account_id = '', 
                    deleted = True, )
            )
        else:
            return PayeeResponseData(
                payee = ynab_sdk_openapi.models.payee.Payee(
                    id = '', 
                    name = '', 
                    transfer_account_id = '', 
                    deleted = True, ),
        )
        """

    def testPayeeResponseData(self):
        """Test PayeeResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
