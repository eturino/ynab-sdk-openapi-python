# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_sdk_openapi.models.transaction_summary import TransactionSummary

class TestTransactionSummary(unittest.TestCase):
    """TransactionSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionSummary:
        """Test TransactionSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionSummary`
        """
        model = TransactionSummary()
        if include_optional:
            return TransactionSummary(
                id = '',
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                amount = 56,
                memo = '',
                cleared = 'cleared',
                approved = True,
                flag_color = 'red',
                flag_name = '',
                account_id = '',
                payee_id = '',
                category_id = '',
                transfer_account_id = '',
                transfer_transaction_id = '',
                matched_transaction_id = '',
                import_id = '',
                import_payee_name = '',
                import_payee_name_original = '',
                debt_transaction_type = 'payment',
                deleted = True
            )
        else:
            return TransactionSummary(
                id = '',
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                amount = 56,
                cleared = 'cleared',
                approved = True,
                account_id = '',
                deleted = True,
        )
        """

    def testTransactionSummary(self):
        """Test TransactionSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
