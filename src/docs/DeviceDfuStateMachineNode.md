# DeviceDfuStateMachineNode

Represents a single request to update the host or Notecard firmware

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status for this step in the firmware update process | [optional] 
**phase** | **str** | Phase for this step in the firmware update process | [optional] 
**datetime** | **str** | RFC3339 compatible datetime of when this status update happened | [optional] 
**description** | **str** | Additional information | [optional] 

## Example

```python
from notehub_py.models.device_dfu_state_machine_node import DeviceDfuStateMachineNode

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDfuStateMachineNode from a JSON string
device_dfu_state_machine_node_instance = DeviceDfuStateMachineNode.from_json(json)
# print the JSON string representation of the object
print(DeviceDfuStateMachineNode.to_json())

# convert the object into a dict
device_dfu_state_machine_node_dict = device_dfu_state_machine_node_instance.to_dict()
# create an instance of DeviceDfuStateMachineNode from a dict
device_dfu_state_machine_node_from_dict = DeviceDfuStateMachineNode.from_dict(device_dfu_state_machine_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


