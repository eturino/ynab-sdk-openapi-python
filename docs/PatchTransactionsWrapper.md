# PatchTransactionsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[SaveTransactionWithIdOrImportId]**](SaveTransactionWithIdOrImportId.md) |  | 

## Example

```python
from ynab_sdk_openapi.models.patch_transactions_wrapper import PatchTransactionsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PatchTransactionsWrapper from a JSON string
patch_transactions_wrapper_instance = PatchTransactionsWrapper.from_json(json)
# print the JSON string representation of the object
print(PatchTransactionsWrapper.to_json())

# convert the object into a dict
patch_transactions_wrapper_dict = patch_transactions_wrapper_instance.to_dict()
# create an instance of PatchTransactionsWrapper from a dict
patch_transactions_wrapper_form_dict = patch_transactions_wrapper.from_dict(patch_transactions_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


