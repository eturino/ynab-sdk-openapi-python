# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_sdk_openapi.models.month_summary import MonthSummary

class TestMonthSummary(unittest.TestCase):
    """MonthSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MonthSummary:
        """Test MonthSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MonthSummary`
        """
        model = MonthSummary()
        if include_optional:
            return MonthSummary(
                month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                note = '',
                income = 56,
                budgeted = 56,
                activity = 56,
                to_be_budgeted = 56,
                age_of_money = 56,
                deleted = True
            )
        else:
            return MonthSummary(
                month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                income = 56,
                budgeted = 56,
                activity = 56,
                to_be_budgeted = 56,
                deleted = True,
        )
        """

    def testMonthSummary(self):
        """Test MonthSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
