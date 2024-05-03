# GetDeviceEnvironmentVariables200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_variables** | **Dict[str, str]** | The environment variables for this device that have been set using host firmware or the Notehub API or UI. | 
**environment_variables_env_default** | **Dict[str, str]** | The environment variables that have been set using the env.default request through the Notecard API. | 

## Example

```python
from notehub_py.models.get_device_environment_variables200_response import GetDeviceEnvironmentVariables200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceEnvironmentVariables200Response from a JSON string
get_device_environment_variables200_response_instance = GetDeviceEnvironmentVariables200Response.from_json(json)
# print the JSON string representation of the object
print(GetDeviceEnvironmentVariables200Response.to_json())

# convert the object into a dict
get_device_environment_variables200_response_dict = get_device_environment_variables200_response_instance.to_dict()
# create an instance of GetDeviceEnvironmentVariables200Response from a dict
get_device_environment_variables200_response_from_dict = GetDeviceEnvironmentVariables200Response.from_dict(get_device_environment_variables200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


