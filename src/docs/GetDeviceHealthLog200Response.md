# GetDeviceHealthLog200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_log** | [**List[GetDeviceHealthLog200ResponseHealthLogInner]**](GetDeviceHealthLog200ResponseHealthLogInner.md) |  | 

## Example

```python
from notehub_py.models.get_device_health_log200_response import GetDeviceHealthLog200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceHealthLog200Response from a JSON string
get_device_health_log200_response_instance = GetDeviceHealthLog200Response.from_json(json)
# print the JSON string representation of the object
print(GetDeviceHealthLog200Response.to_json())

# convert the object into a dict
get_device_health_log200_response_dict = get_device_health_log200_response_instance.to_dict()
# create an instance of GetDeviceHealthLog200Response from a dict
get_device_health_log200_response_from_dict = GetDeviceHealthLog200Response.from_dict(get_device_health_log200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


