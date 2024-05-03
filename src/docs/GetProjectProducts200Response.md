# GetProjectProducts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[Product]**](Product.md) |  | [optional] 

## Example

```python
from notehub_py.models.get_project_products200_response import GetProjectProducts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectProducts200Response from a JSON string
get_project_products200_response_instance = GetProjectProducts200Response.from_json(json)
# print the JSON string representation of the object
print(GetProjectProducts200Response.to_json())

# convert the object into a dict
get_project_products200_response_dict = get_project_products200_response_instance.to_dict()
# create an instance of GetProjectProducts200Response from a dict
get_project_products200_response_from_dict = GetProjectProducts200Response.from_dict(get_project_products200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


