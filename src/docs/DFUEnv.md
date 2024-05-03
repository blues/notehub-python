# DFUEnv


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**DFUState**](DFUState.md) |  | [optional] 
**user** | [**DFUState**](DFUState.md) |  | [optional] 

## Example

```python
from notehub_py.models.dfu_env import DFUEnv

# TODO update the JSON string below
json = "{}"
# create an instance of DFUEnv from a JSON string
dfu_env_instance = DFUEnv.from_json(json)
# print the JSON string representation of the object
print(DFUEnv.to_json())

# convert the object into a dict
dfu_env_dict = dfu_env_instance.to_dict()
# create an instance of DFUEnv from a dict
dfu_env_from_dict = DFUEnv.from_dict(dfu_env_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


