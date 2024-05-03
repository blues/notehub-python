# DeviceTowerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mcc** | **int** |  | [optional] 
**mnc** | **int** |  | [optional] 
**lac** | **int** |  | [optional] 
**cell_id** | **int** |  | [optional] 

## Example

```python
from notehub_py.models.device_tower_info import DeviceTowerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceTowerInfo from a JSON string
device_tower_info_instance = DeviceTowerInfo.from_json(json)
# print the JSON string representation of the object
print(DeviceTowerInfo.to_json())

# convert the object into a dict
device_tower_info_dict = device_tower_info_instance.to_dict()
# create an instance of DeviceTowerInfo from a dict
device_tower_info_from_dict = DeviceTowerInfo.from_dict(device_tower_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


