# TowerLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** |  | [optional] 
**n** | **str** | Name of the location | [optional] 
**c** | **str** | Country code | [optional] 
**lat** | **float** |  | [optional] 
**lon** | **float** |  | [optional] 
**zone** | **str** |  | [optional] 
**mcc** | **float** |  | [optional] 
**mnc** | **float** |  | [optional] 
**lac** | **float** |  | [optional] 
**cid** | **float** |  | [optional] 
**l** | **str** | Open location code | [optional] 
**z** | **float** | Timezone ID | [optional] 
**count** | **float** | Number of times this location was recently used | [optional] 
**towers** | **float** | Number of triangulation points | [optional] 

## Example

```python
from notehub_py.models.tower_location import TowerLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TowerLocation from a JSON string
tower_location_instance = TowerLocation.from_json(json)
# print the JSON string representation of the object
print(TowerLocation.to_json())

# convert the object into a dict
tower_location_dict = tower_location_instance.to_dict()
# create an instance of TowerLocation from a dict
tower_location_from_dict = TowerLocation.from_dict(tower_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


