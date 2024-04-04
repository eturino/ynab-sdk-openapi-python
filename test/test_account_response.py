# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_sdk_openapi.models.account_response import AccountResponse

class TestAccountResponse(unittest.TestCase):
    """AccountResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountResponse:
        """Test AccountResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountResponse`
        """
        model = AccountResponse()
        if include_optional:
            return AccountResponse(
                data = ynab_sdk_openapi.models.account_response_data.AccountResponse_data(
                    account = ynab_sdk_openapi.models.account.Account(
                        id = '', 
                        name = '', 
                        type = 'checking', 
                        on_budget = True, 
                        closed = True, 
                        note = '', 
                        balance = 56, 
                        cleared_balance = 56, 
                        uncleared_balance = 56, 
                        transfer_payee_id = '', 
                        direct_import_linked = True, 
                        direct_import_in_error = True, 
                        last_reconciled_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        debt_original_balance = 56, 
                        debt_interest_rates = {
                            'key' : 56
                            }, 
                        debt_minimum_payments = {
                            'key' : 56
                            }, 
                        debt_escrow_amounts = , 
                        deleted = True, ), )
            )
        else:
            return AccountResponse(
                data = ynab_sdk_openapi.models.account_response_data.AccountResponse_data(
                    account = ynab_sdk_openapi.models.account.Account(
                        id = '', 
                        name = '', 
                        type = 'checking', 
                        on_budget = True, 
                        closed = True, 
                        note = '', 
                        balance = 56, 
                        cleared_balance = 56, 
                        uncleared_balance = 56, 
                        transfer_payee_id = '', 
                        direct_import_linked = True, 
                        direct_import_in_error = True, 
                        last_reconciled_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        debt_original_balance = 56, 
                        debt_interest_rates = {
                            'key' : 56
                            }, 
                        debt_minimum_payments = {
                            'key' : 56
                            }, 
                        debt_escrow_amounts = , 
                        deleted = True, ), ),
        )
        """

    def testAccountResponse(self):
        """Test AccountResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
