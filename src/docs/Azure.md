# Azure

Route settings specific to Azure routes.  Only used for Azure route types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**filter** | [**HttpFilter**](HttpFilter.md) |  | [optional] 
**transform** | [**HttpTransform**](HttpTransform.md) |  | [optional] 
**throttle_ms** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**timeout** | **int** | Timeout in seconds for each request | [optional] [default to 15]
**functions_key_secret** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**sas_policy_name** | **str** |  | [optional] 
**sas_policy_key** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 

## Example

```python
from notehub_py.models.azure import Azure

# TODO update the JSON string below
json = "{}"
# create an instance of Azure from a JSON string
azure_instance = Azure.from_json(json)
# print the JSON string representation of the object
print(Azure.to_json())

# convert the object into a dict
azure_dict = azure_instance.to_dict()
# create an instance of Azure from a dict
azure_from_dict = Azure.from_dict(azure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


