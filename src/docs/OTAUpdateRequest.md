# OTAUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The name of the firmware file | [optional] 
**device_uids** | **List[str]** | The device UIDs to update | [optional] 
**fleet_uids** | **List[str]** | The fleet UIDs to update | [optional] 
**device_tags** | **List[str]** | The device tags to update | [optional] 
**version** | **str** | The version of the firmware | [optional] 
**md5** | **str** | The MD5 hash of the firmware file | [optional] 
**type** | **str** | The type of firmware | [optional] 
**product** | **str** | The product that the firmware is for | [optional] 
**target** | **str** | The target device for the firmware | [optional] 
**unpublished** | **bool** | If true, the firmware is unpublished | [optional] 
**cancel_dfu** | **bool** | If true, the DFU is canceled | [optional] 

## Example

```python
from notehub_py.models.ota_update_request import OTAUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OTAUpdateRequest from a JSON string
ota_update_request_instance = OTAUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OTAUpdateRequest.to_json())

# convert the object into a dict
ota_update_request_dict = ota_update_request_instance.to_dict()
# create an instance of OTAUpdateRequest from a dict
ota_update_request_from_dict = OTAUpdateRequest.from_dict(ota_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


