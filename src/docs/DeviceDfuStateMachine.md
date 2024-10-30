# DeviceDfuStateMachine

Represents a single request to update the host or Notecard firmware

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_version** | **str** | Version of the firmware that was requested to be installed | [optional] 
**current_version** | **str** | Version of the firmware that was installed prior to this request | [optional] 
**initiated** | **str** | RFC3339 datetime of when this update was requested | [optional] 
**updates** | [**List[DeviceDfuStateMachineNode]**](DeviceDfuStateMachineNode.md) |  | [optional] 

## Example

```python
from notehub_py.models.device_dfu_state_machine import DeviceDfuStateMachine

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDfuStateMachine from a JSON string
device_dfu_state_machine_instance = DeviceDfuStateMachine.from_json(json)
# print the JSON string representation of the object
print(DeviceDfuStateMachine.to_json())

# convert the object into a dict
device_dfu_state_machine_dict = device_dfu_state_machine_instance.to_dict()
# create an instance of DeviceDfuStateMachine from a dict
device_dfu_state_machine_from_dict = DeviceDfuStateMachine.from_dict(device_dfu_state_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


