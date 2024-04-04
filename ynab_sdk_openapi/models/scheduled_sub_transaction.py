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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ScheduledSubTransaction(BaseModel):
    """
    ScheduledSubTransaction
    """ # noqa: E501
    id: StrictStr
    scheduled_transaction_id: StrictStr
    amount: StrictInt = Field(description="The scheduled subtransaction amount in milliunits format")
    memo: Optional[StrictStr] = None
    payee_id: Optional[StrictStr] = None
    category_id: Optional[StrictStr] = None
    transfer_account_id: Optional[StrictStr] = Field(default=None, description="If a transfer, the account_id which the scheduled subtransaction transfers to")
    deleted: StrictBool = Field(description="Whether or not the scheduled subtransaction has been deleted. Deleted scheduled subtransactions will only be included in delta requests.")
    __properties: ClassVar[List[str]] = ["id", "scheduled_transaction_id", "amount", "memo", "payee_id", "category_id", "transfer_account_id", "deleted"]

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
        """Create an instance of ScheduledSubTransaction from a JSON string"""
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
        # set to None if memo (nullable) is None
        # and model_fields_set contains the field
        if self.memo is None and "memo" in self.model_fields_set:
            _dict['memo'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScheduledSubTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "scheduled_transaction_id": obj.get("scheduled_transaction_id"),
            "amount": obj.get("amount"),
            "memo": obj.get("memo"),
            "payee_id": obj.get("payee_id"),
            "category_id": obj.get("category_id"),
            "transfer_account_id": obj.get("transfer_account_id"),
            "deleted": obj.get("deleted")
        })
        return _obj


