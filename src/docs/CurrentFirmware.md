# CurrentFirmware


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**metadata** | [**Firmware**](Firmware.md) |  | [optional] 

## Example

```python
from notehub_py.models.current_firmware import CurrentFirmware

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentFirmware from a JSON string
current_firmware_instance = CurrentFirmware.from_json(json)
# print the JSON string representation of the object
print(CurrentFirmware.to_json())

# convert the object into a dict
current_firmware_dict = current_firmware_instance.to_dict()
# create an instance of CurrentFirmware from a dict
current_firmware_from_dict = CurrentFirmware.from_dict(current_firmware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


