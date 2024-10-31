# UserDfuStateMachineStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** |  | [optional] 
**phase_description** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from notehub_py.models.user_dfu_state_machine_status import UserDfuStateMachineStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UserDfuStateMachineStatus from a JSON string
user_dfu_state_machine_status_instance = UserDfuStateMachineStatus.from_json(json)
# print the JSON string representation of the object
print(UserDfuStateMachineStatus.to_json())

# convert the object into a dict
user_dfu_state_machine_status_dict = user_dfu_state_machine_status_instance.to_dict()
# create an instance of UserDfuStateMachineStatus from a dict
user_dfu_state_machine_status_from_dict = UserDfuStateMachineStatus.from_dict(user_dfu_state_machine_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


