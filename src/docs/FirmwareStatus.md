# FirmwareStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the firmware | [optional] 
**organization** | **str** | The organization that owns the firmware | [optional] 
**description** | **str** | A description of the firmware | [optional] 
**product** | **str** | The product that the firmware is for | [optional] 
**built** | **str** | The date the firmware was built | [optional] 

## Example

```python
from notehub_py.models.firmware_status import FirmwareStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FirmwareStatus from a JSON string
firmware_status_instance = FirmwareStatus.from_json(json)
# print the JSON string representation of the object
print(FirmwareStatus.to_json())

# convert the object into a dict
firmware_status_dict = firmware_status_instance.to_dict()
# create an instance of FirmwareStatus from a dict
firmware_status_from_dict = FirmwareStatus.from_dict(firmware_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


