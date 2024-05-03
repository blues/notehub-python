# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | 
**serial_number** | **str** |  | [optional] 
**provisioned** | **datetime** |  | 
**last_activity** | **datetime** |  | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**product_uid** | **str** |  | 
**fleet_uids** | **List[str]** |  | 
**tower_info** | [**DeviceTowerInfo**](DeviceTowerInfo.md) |  | [optional] 
**tower_location** | [**Location**](Location.md) |  | [optional] 
**gps_location** | [**Location**](Location.md) |  | [optional] 
**triangulated_location** | [**Location**](Location.md) |  | [optional] 
**voltage** | **float** |  | 
**temperature** | **float** |  | 
**dfu** | [**DFUEnv**](DFUEnv.md) |  | [optional] 
**sku** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from notehub_py.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


