# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from ynab_sdk_openapi.models.scheduled_sub_transaction import ScheduledSubTransaction
from ynab_sdk_openapi.models.transaction_flag_color import TransactionFlagColor
from typing import Optional, Set
from typing_extensions import Self

class ScheduledTransactionDetail(BaseModel):
    """
    ScheduledTransactionDetail
    """ # noqa: E501
    id: StrictStr
    date_first: date = Field(description="The first date for which the Scheduled Transaction was scheduled.")
    date_next: date = Field(description="The next date for which the Scheduled Transaction is scheduled.")
    frequency: StrictStr
    amount: StrictInt = Field(description="The scheduled transaction amount in milliunits format")
    memo: Optional[StrictStr] = None
    flag_color: Optional[TransactionFlagColor] = None
    flag_name: Optional[StrictStr] = Field(default=None, description="The customized name of a transaction flag")
    account_id: StrictStr
    payee_id: Optional[StrictStr] = None
    category_id: Optional[StrictStr] = None
    transfer_account_id: Optional[StrictStr] = Field(default=None, description="If a transfer, the account_id which the scheduled transaction transfers to")
    deleted: StrictBool = Field(description="Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests.")
    account_name: StrictStr
    payee_name: Optional[StrictStr] = None
    category_name: Optional[StrictStr] = Field(default=None, description="The name of the category.  If a split scheduled transaction, this will be 'Split'.")
    subtransactions: List[ScheduledSubTransaction] = Field(description="If a split scheduled transaction, the subtransactions.")
    __properties: ClassVar[List[str]] = ["id", "date_first", "date_next", "frequency", "amount", "memo", "flag_color", "flag_name", "account_id", "payee_id", "category_id", "transfer_account_id", "deleted", "account_name", "payee_name", "category_name", "subtransactions"]

    @field_validator('frequency')
    def frequency_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['never', 'daily', 'weekly', 'everyOtherWeek', 'twiceAMonth', 'every4Weeks', 'monthly', 'everyOtherMonth', 'every3Months', 'every4Months', 'twiceAYear', 'yearly', 'everyOtherYear']):
            raise ValueError("must be one of enum values ('never', 'daily', 'weekly', 'everyOtherWeek', 'twiceAMonth', 'every4Weeks', 'monthly', 'everyOtherMonth', 'every3Months', 'every4Months', 'twiceAYear', 'yearly', 'everyOtherYear')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ScheduledTransactionDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in subtransactions (list)
        _items = []
        if self.subtransactions:
            for _item in self.subtransactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subtransactions'] = _items
        # set to None if memo (nullable) is None
        # and model_fields_set contains the field
        if self.memo is None and "memo" in self.model_fields_set:
            _dict['memo'] = None

        # set to None if flag_color (nullable) is None
        # and model_fields_set contains the field
        if self.flag_color is None and "flag_color" in self.model_fields_set:
            _dict['flag_color'] = None

        # set to None if flag_name (nullable) is None
        # and model_fields_set contains the field
        if self.flag_name is None and "flag_name" in self.model_fields_set:
            _dict['flag_name'] = None

        # set to None if payee_id (nullable) is None
        # and model_fields_set contains the field
        if self.payee_id is None and "payee_id" in self.model_fields_set:
            _dict['payee_id'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if transfer_account_id (nullable) is None
        # and model_fields_set contains the field
        if self.transfer_account_id is None and "transfer_account_id" in self.model_fields_set:
            _dict['transfer_account_id'] = None

        # set to None if payee_name (nullable) is None
        # and model_fields_set contains the field
        if self.payee_name is None and "payee_name" in self.model_fields_set:
            _dict['payee_name'] = None

        # set to None if category_name (nullable) is None
        # and model_fields_set contains the field
        if self.category_name is None and "category_name" in self.model_fields_set:
            _dict['category_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScheduledTransactionDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "date_first": obj.get("date_first"),
            "date_next": obj.get("date_next"),
            "frequency": obj.get("frequency"),
            "amount": obj.get("amount"),
            "memo": obj.get("memo"),
            "flag_color": obj.get("flag_color"),
            "flag_name": obj.get("flag_name"),
            "account_id": obj.get("account_id"),
            "payee_id": obj.get("payee_id"),
            "category_id": obj.get("category_id"),
            "transfer_account_id": obj.get("transfer_account_id"),
            "deleted": obj.get("deleted"),
            "account_name": obj.get("account_name"),
            "payee_name": obj.get("payee_name"),
            "category_name": obj.get("category_name"),
            "subtransactions": [ScheduledSubTransaction.from_dict(_item) for _item in obj["subtransactions"]] if obj.get("subtransactions") is not None else None
        })
        return _obj

