# UserFirmwareInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_firmware** | [**CurrentFirmware**](CurrentFirmware.md) |  | [optional] 
**firmware_update** | [**UserDfuStateMachine**](UserDfuStateMachine.md) |  | [optional] 

## Example

```python
from notehub_py.models.user_firmware_info import UserFirmwareInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserFirmwareInfo from a JSON string
user_firmware_info_instance = UserFirmwareInfo.from_json(json)
# print the JSON string representation of the object
print(UserFirmwareInfo.to_json())

# convert the object into a dict
user_firmware_info_dict = user_firmware_info_instance.to_dict()
# create an instance of UserFirmwareInfo from a dict
user_firmware_info_from_dict = UserFirmwareInfo.from_dict(user_firmware_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


