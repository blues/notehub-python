# OTAUpdateStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the OTA request | [optional] 
**successful** | **List[str]** | The successful device UIDs | [optional] 
**failed** | **List[str]** | The failed device UIDs | [optional] 

## Example

```python
from notehub_py.models.ota_update_status import OTAUpdateStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OTAUpdateStatus from a JSON string
ota_update_status_instance = OTAUpdateStatus.from_json(json)
# print the JSON string representation of the object
print(OTAUpdateStatus.to_json())

# convert the object into a dict
ota_update_status_dict = ota_update_status_instance.to_dict()
# create an instance of OTAUpdateStatus from a dict
ota_update_status_from_dict = OTAUpdateStatus.from_dict(ota_update_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


