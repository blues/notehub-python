# Fleet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | 
**label** | **str** |  | 
**created** | **datetime** |  | 

## Example

```python
from notehub_py.models.fleet import Fleet

# TODO update the JSON string below
json = "{}"
# create an instance of Fleet from a JSON string
fleet_instance = Fleet.from_json(json)
# print the JSON string representation of the object
print(Fleet.to_json())

# convert the object into a dict
fleet_dict = fleet_instance.to_dict()
# create an instance of Fleet from a dict
fleet_from_dict = Fleet.from_dict(fleet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


