# CloneProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label for the project. | 
**billing_account_uid** | **str** | The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned. | 
**disable_clone_routes** | **bool** | Whether to disallow the cloning of the routes from the parent project.  Default is false if not specified. | [optional] 
**disable_clone_fleets** | **bool** | Whether to disallow the cloning of the fleets from the parent project.  Default is false if not specified. | [optional] 

## Example

```python
from notehub_py.models.clone_project_request import CloneProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneProjectRequest from a JSON string
clone_project_request_instance = CloneProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CloneProjectRequest.to_json())

# convert the object into a dict
clone_project_request_dict = clone_project_request_instance.to_dict()
# create an instance of CloneProjectRequest from a dict
clone_project_request_from_dict = CloneProjectRequest.from_dict(clone_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


