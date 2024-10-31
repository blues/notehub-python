# DeviceDfuStatusCurrent

Description of the current firmware

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Firmware version | [optional] 
**organization** | **str** | Firmware organization | [optional] 
**description** | **str** | Firmware description | [optional] 
**product** | **str** | Firmware product | [optional] 
**built** | **str** | Firmware build date | [optional] 
**builder** | **str** | Firmware author | [optional] 

## Example

```python
from notehub_py.models.device_dfu_status_current import DeviceDfuStatusCurrent

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDfuStatusCurrent from a JSON string
device_dfu_status_current_instance = DeviceDfuStatusCurrent.from_json(json)
# print the JSON string representation of the object
print(DeviceDfuStatusCurrent.to_json())

# convert the object into a dict
device_dfu_status_current_dict = device_dfu_status_current_instance.to_dict()
# create an instance of DeviceDfuStatusCurrent from a dict
device_dfu_status_current_from_dict = DeviceDfuStatusCurrent.from_dict(device_dfu_status_current_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


