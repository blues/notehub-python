# GetDeviceHealthLog200ResponseHealthLogInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when** | **datetime** |  | 
**alert** | **bool** |  | 
**text** | **str** |  | 

## Example

```python
from notehub_py.models.get_device_health_log200_response_health_log_inner import GetDeviceHealthLog200ResponseHealthLogInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceHealthLog200ResponseHealthLogInner from a JSON string
get_device_health_log200_response_health_log_inner_instance = GetDeviceHealthLog200ResponseHealthLogInner.from_json(json)
# print the JSON string representation of the object
print(GetDeviceHealthLog200ResponseHealthLogInner.to_json())

# convert the object into a dict
get_device_health_log200_response_health_log_inner_dict = get_device_health_log200_response_health_log_inner_instance.to_dict()
# create an instance of GetDeviceHealthLog200ResponseHealthLogInner from a dict
get_device_health_log200_response_health_log_inner_from_dict = GetDeviceHealthLog200ResponseHealthLogInner.from_dict(get_device_health_log200_response_health_log_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


