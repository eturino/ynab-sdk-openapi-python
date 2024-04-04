# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_sdk_openapi.models.budget_detail import BudgetDetail

class TestBudgetDetail(unittest.TestCase):
    """BudgetDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetDetail:
        """Test BudgetDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetDetail`
        """
        model = BudgetDetail()
        if include_optional:
            return BudgetDetail(
                id = '',
                name = '',
                last_modified_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                first_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                last_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                date_format = ynab_sdk_openapi.models.date_format.DateFormat(
                    format = '', ),
                currency_format = ynab_sdk_openapi.models.currency_format.CurrencyFormat(
                    iso_code = '', 
                    example_format = '', 
                    decimal_digits = 56, 
                    decimal_separator = '', 
                    symbol_first = True, 
                    group_separator = '', 
                    currency_symbol = '', 
                    display_symbol = True, ),
                accounts = [
                    ynab_sdk_openapi.models.account.Account(
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
                        deleted = True, )
                    ],
                payees = [
                    ynab_sdk_openapi.models.payee.Payee(
                        id = '', 
                        name = '', 
                        transfer_account_id = '', 
                        deleted = True, )
                    ],
                payee_locations = [
                    ynab_sdk_openapi.models.payee_location.PayeeLocation(
                        id = '', 
                        payee_id = '', 
                        latitude = '', 
                        longitude = '', 
                        deleted = True, )
                    ],
                category_groups = [
                    ynab_sdk_openapi.models.category_group.CategoryGroup(
                        id = '', 
                        name = '', 
                        hidden = True, 
                        deleted = True, )
                    ],
                categories = [
                    ynab_sdk_openapi.models.category.Category(
                        id = '', 
                        category_group_id = '', 
                        category_group_name = '', 
                        name = '', 
                        hidden = True, 
                        original_category_group_id = '', 
                        note = '', 
                        budgeted = 56, 
                        activity = 56, 
                        balance = 56, 
                        goal_type = 'TB', 
                        goal_day = 56, 
                        goal_cadence = 56, 
                        goal_cadence_frequency = 56, 
                        goal_creation_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_target = 56, 
                        goal_target_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_percentage_complete = 56, 
                        goal_months_to_budget = 56, 
                        goal_under_funded = 56, 
                        goal_overall_funded = 56, 
                        goal_overall_left = 56, 
                        deleted = True, )
                    ],
                months = [
                    null
                    ],
                transactions = [
                    ynab_sdk_openapi.models.transaction_summary.TransactionSummary(
                        id = '', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
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
                        deleted = True, )
                    ],
                subtransactions = [
                    ynab_sdk_openapi.models.sub_transaction.SubTransaction(
                        id = '', 
                        transaction_id = '', 
                        amount = 56, 
                        memo = '', 
                        payee_id = '', 
                        payee_name = '', 
                        category_id = '', 
                        category_name = '', 
                        transfer_account_id = '', 
                        transfer_transaction_id = '', 
                        deleted = True, )
                    ],
                scheduled_transactions = [
                    ynab_sdk_openapi.models.scheduled_transaction_summary.ScheduledTransactionSummary(
                        id = '', 
                        date_first = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        date_next = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        frequency = 'never', 
                        amount = 56, 
                        memo = '', 
                        flag_color = 'red', 
                        flag_name = '', 
                        account_id = '', 
                        payee_id = '', 
                        category_id = '', 
                        transfer_account_id = '', 
                        deleted = True, )
                    ],
                scheduled_subtransactions = [
                    ynab_sdk_openapi.models.scheduled_sub_transaction.ScheduledSubTransaction(
                        id = '', 
                        scheduled_transaction_id = '', 
                        amount = 56, 
                        memo = '', 
                        payee_id = '', 
                        category_id = '', 
                        transfer_account_id = '', 
                        deleted = True, )
                    ]
            )
        else:
            return BudgetDetail(
                id = '',
                name = '',
        )
        """

    def testBudgetDetail(self):
        """Test BudgetDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()