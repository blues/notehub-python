# UserDfuStateMachine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**UserDfuStateMachineStatus**](UserDfuStateMachineStatus.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**from_version** | **str** |  | [optional] 
**metadata** | [**UploadMetadata**](UploadMetadata.md) |  | [optional] 

## Example

```python
from notehub_py.models.user_dfu_state_machine import UserDfuStateMachine

# TODO update the JSON string below
json = "{}"
# create an instance of UserDfuStateMachine from a JSON string
user_dfu_state_machine_instance = UserDfuStateMachine.from_json(json)
# print the JSON string representation of the object
print(UserDfuStateMachine.to_json())

# convert the object into a dict
user_dfu_state_machine_dict = user_dfu_state_machine_instance.to_dict()
# create an instance of UserDfuStateMachine from a dict
user_dfu_state_machine_from_dict = UserDfuStateMachine.from_dict(user_dfu_state_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


