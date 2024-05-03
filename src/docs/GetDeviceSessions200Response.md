# GetDeviceSessions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions** | [**List[DeviceSession]**](DeviceSession.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from notehub_py.models.get_device_sessions200_response import GetDeviceSessions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceSessions200Response from a JSON string
get_device_sessions200_response_instance = GetDeviceSessions200Response.from_json(json)
# print the JSON string representation of the object
print(GetDeviceSessions200Response.to_json())

# convert the object into a dict
get_device_sessions200_response_dict = get_device_sessions200_response_instance.to_dict()
# create an instance of GetDeviceSessions200Response from a dict
get_device_sessions200_response_from_dict = GetDeviceSessions200Response.from_dict(get_device_sessions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


