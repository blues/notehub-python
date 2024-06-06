# OTAStatusList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[OTAStatus]**](OTAStatus.md) |  | [optional] 
**has_more** | **bool** | Indicates whether more items are available | [optional] 

## Example

```python
from notehub_py.models.ota_status_list import OTAStatusList

# TODO update the JSON string below
json = "{}"
# create an instance of OTAStatusList from a JSON string
ota_status_list_instance = OTAStatusList.from_json(json)
# print the JSON string representation of the object
print(OTAStatusList.to_json())

# convert the object into a dict
ota_status_list_dict = ota_status_list_instance.to_dict()
# create an instance of OTAStatusList from a dict
ota_status_list_from_dict = OTAStatusList.from_dict(ota_status_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


