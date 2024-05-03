# UserDbRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] [default to 'route:8d65a087d5d290ce5bdf03aeff2becc0']
**label** | **str** |  | [optional] [default to 'success route']
**type** | **str** |  | [optional] [default to 'http']
**modified** | **str** |  | [optional] [default to '2020-03-09T17:58:37Z']
**disabled** | **bool** |  | [optional] [default to False]

## Example

```python
from notehub_py.models.user_db_route import UserDbRoute

# TODO update the JSON string below
json = "{}"
# create an instance of UserDbRoute from a JSON string
user_db_route_instance = UserDbRoute.from_json(json)
# print the JSON string representation of the object
print(UserDbRoute.to_json())

# convert the object into a dict
user_db_route_dict = user_db_route_instance.to_dict()
# create an instance of UserDbRoute from a dict
user_db_route_from_dict = UserDbRoute.from_dict(user_db_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


