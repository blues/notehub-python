# DeviceUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**since** | **float** |  | [optional] 
**duration** | **float** |  | [optional] 
**bytes_rcvd** | **float** |  | [optional] 
**bytes_sent** | **float** |  | [optional] 
**bytes_rcvd_secondary** | **float** |  | [optional] 
**bytes_sent_secondary** | **float** |  | [optional] 
**sessions_tcp** | **float** |  | [optional] 
**sessions_tls** | **float** |  | [optional] 
**notes_rcvd** | **float** |  | [optional] 
**note_sent** | **float** |  | [optional] 

## Example

```python
from notehub_py.models.device_usage import DeviceUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsage from a JSON string
device_usage_instance = DeviceUsage.from_json(json)
# print the JSON string representation of the object
print(DeviceUsage.to_json())

# convert the object into a dict
device_usage_dict = device_usage_instance.to_dict()
# create an instance of DeviceUsage from a dict
device_usage_from_dict = DeviceUsage.from_dict(device_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


