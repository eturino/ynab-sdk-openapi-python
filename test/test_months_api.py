# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab_sdk_openapi.api.months_api import MonthsApi


class TestMonthsApi(unittest.TestCase):
    """MonthsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MonthsApi()

    def tearDown(self) -> None:
        pass

    def test_get_budget_month(self) -> None:
        """Test case for get_budget_month

        Single budget month
        """
        pass

    def test_get_budget_months(self) -> None:
        """Test case for get_budget_months

        List budget months
        """
        pass


if __name__ == '__main__':
    unittest.main()
