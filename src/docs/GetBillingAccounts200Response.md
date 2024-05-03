# GetBillingAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_accounts** | [**List[BillingAccount]**](BillingAccount.md) |  | [optional] 

## Example

```python
from notehub_py.models.get_billing_accounts200_response import GetBillingAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBillingAccounts200Response from a JSON string
get_billing_accounts200_response_instance = GetBillingAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetBillingAccounts200Response.to_json())

# convert the object into a dict
get_billing_accounts200_response_dict = get_billing_accounts200_response_instance.to_dict()
# create an instance of GetBillingAccounts200Response from a dict
get_billing_accounts200_response_from_dict = GetBillingAccounts200Response.from_dict(get_billing_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


