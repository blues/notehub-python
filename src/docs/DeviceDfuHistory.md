# DeviceDfuHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uid** | **str** | Device UID | [optional] 
**current** | [**DeviceDfuStatusCurrent**](DeviceDfuStatusCurrent.md) |  | [optional] 
**history** | [**List[DeviceDfuStateMachine]**](DeviceDfuStateMachine.md) |  | [optional] 

## Example

```python
from notehub_py.models.device_dfu_history import DeviceDfuHistory

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDfuHistory from a JSON string
device_dfu_history_instance = DeviceDfuHistory.from_json(json)
# print the JSON string representation of the object
print(DeviceDfuHistory.to_json())

# convert the object into a dict
device_dfu_history_dict = device_dfu_history_instance.to_dict()
# create an instance of DeviceDfuHistory from a dict
device_dfu_history_from_dict = DeviceDfuHistory.from_dict(device_dfu_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


