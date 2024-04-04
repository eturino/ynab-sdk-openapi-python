# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TransactionClearedStatus(str, Enum):
    """
    The cleared status of the transaction
    """

    """
    allowed enum values
    """
    CLEARED = 'cleared'
    UNCLEARED = 'uncleared'
    RECONCILED = 'reconciled'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionClearedStatus from a JSON string"""
        return cls(json.loads(json_str))


