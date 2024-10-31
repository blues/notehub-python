# Firmware


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**firmware** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**ver_major** | **int** |  | [optional] 
**ver_minor** | **int** |  | [optional] 
**ver_patch** | **int** |  | [optional] 
**ver_build** | **int** |  | [optional] 
**built** | **str** |  | [optional] 
**builder** | **str** |  | [optional] 

## Example

```python
from notehub_py.models.firmware import Firmware

# TODO update the JSON string below
json = "{}"
# create an instance of Firmware from a JSON string
firmware_instance = Firmware.from_json(json)
# print the JSON string representation of the object
print(Firmware.to_json())

# convert the object into a dict
firmware_dict = firmware_instance.to_dict()
# create an instance of Firmware from a dict
firmware_from_dict = Firmware.from_dict(firmware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


