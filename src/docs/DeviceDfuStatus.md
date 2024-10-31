# DeviceDfuStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uid** | **str** | Device UID | [optional] 
**dfu_in_progress** | **bool** | true if there is a DFU currently in progress | [optional] 
**current** | [**DeviceDfuStatusCurrent**](DeviceDfuStatusCurrent.md) |  | [optional] 
**status** | [**DeviceDfuStateMachine**](DeviceDfuStateMachine.md) |  | [optional] 

## Example

```python
from notehub_py.models.device_dfu_status import DeviceDfuStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDfuStatus from a JSON string
device_dfu_status_instance = DeviceDfuStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceDfuStatus.to_json())

# convert the object into a dict
device_dfu_status_dict = device_dfu_status_instance.to_dict()
# create an instance of DeviceDfuStatus from a dict
device_dfu_status_from_dict = DeviceDfuStatus.from_dict(device_dfu_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


