# GetProjectFleets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | [**List[Fleet]**](Fleet.md) |  | 

## Example

```python
from notehub_py.models.get_project_fleets200_response import GetProjectFleets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectFleets200Response from a JSON string
get_project_fleets200_response_instance = GetProjectFleets200Response.from_json(json)
# print the JSON string representation of the object
print(GetProjectFleets200Response.to_json())

# convert the object into a dict
get_project_fleets200_response_dict = get_project_fleets200_response_instance.to_dict()
# create an instance of GetProjectFleets200Response from a dict
get_project_fleets200_response_from_dict = GetProjectFleets200Response.from_dict(get_project_fleets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


