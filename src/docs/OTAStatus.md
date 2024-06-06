# OTAStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uid** | **str** | The device UID | [optional] 
**tags** | **str** | The tags associated with the device | [optional] 
**notecard_current_firmware** | [**FirmwareStatus**](FirmwareStatus.md) |  | [optional] 
**notecard_dfu_began_at** | **str** | The time the Notecard DFU began | [optional] 
**notecard_dfu_status** | **str** | The status of the Notecard DFU | [optional] 
**notecard_requested_firmware** | [**FirmwareStatus**](FirmwareStatus.md) |  | [optional] 
**notecard_requested_at** | **str** | The time the Notecard firmware was requested | [optional] 
**notecard_requested_scope** | **str** | The scope of the Notecard firmware request | [optional] 
**notecard_requested_show_details** | **bool** | Whether to show details of the Notecard firmware request | [optional] 
**notecard_requested_status** | **str** | The status of the Notecard firmware request | [optional] 
**host_current_firmware** | [**FirmwareStatus**](FirmwareStatus.md) |  | [optional] 
**host_dfu_began_at** | **str** | The time the host DFU began | [optional] 
**host_dfu_status** | **str** | The status of the host DFU | [optional] 
**host_requested_firmware** | [**FirmwareStatus**](FirmwareStatus.md) |  | [optional] 
**host_requested_at** | **str** | The time the host firmware was requested | [optional] 
**host_requested_scope** | **str** | The scope of the host firmware request | [optional] 
**host_requested_show_details** | **bool** | Whether to show details of the host firmware request | [optional] 
**host_requested_status** | **str** | The status of the host firmware request | [optional] 

## Example

```python
from notehub_py.models.ota_status import OTAStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OTAStatus from a JSON string
ota_status_instance = OTAStatus.from_json(json)
# print the JSON string representation of the object
print(OTAStatus.to_json())

# convert the object into a dict
ota_status_dict = ota_status_instance.to_dict()
# create an instance of OTAStatus from a dict
ota_status_from_dict = OTAStatus.from_dict(ota_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


