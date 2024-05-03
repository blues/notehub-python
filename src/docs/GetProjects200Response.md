# GetProjects200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[Project]**](Project.md) |  | [optional] 

## Example

```python
from notehub_py.models.get_projects200_response import GetProjects200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjects200Response from a JSON string
get_projects200_response_instance = GetProjects200Response.from_json(json)
# print the JSON string representation of the object
print(GetProjects200Response.to_json())

# convert the object into a dict
get_projects200_response_dict = get_projects200_response_instance.to_dict()
# create an instance of GetProjects200Response from a dict
get_projects200_response_from_dict = GetProjects200Response.from_dict(get_projects200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


