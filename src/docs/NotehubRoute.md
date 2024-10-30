# NotehubRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Route UID | [optional] 
**label** | **str** | Route Label | [optional] 
**route_type** | **str** | Type of route. | [optional] [default to 'http']
**modified** | **str** | Last Modified | [optional] 
**disabled** | **bool** | Is route disabled? | [optional] [default to False]
**var_schema** | [**NotehubRouteSchema**](NotehubRouteSchema.md) |  | [optional] 

## Example

```python
from notehub_py.models.notehub_route import NotehubRoute

# TODO update the JSON string below
json = "{}"
# create an instance of NotehubRoute from a JSON string
notehub_route_instance = NotehubRoute.from_json(json)
# print the JSON string representation of the object
print(NotehubRoute.to_json())

# convert the object into a dict
notehub_route_dict = notehub_route_instance.to_dict()
# create an instance of NotehubRoute from a dict
notehub_route_from_dict = NotehubRoute.from_dict(notehub_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


