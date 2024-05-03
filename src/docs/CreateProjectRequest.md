# CreateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label for the project. | 
**billing_account_uid** | **str** | The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.  | 

## Example

```python
from notehub_py.models.create_project_request import CreateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectRequest from a JSON string
create_project_request_instance = CreateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectRequest.to_json())

# convert the object into a dict
create_project_request_dict = create_project_request_instance.to_dict()
# create an instance of CreateProjectRequest from a dict
create_project_request_from_dict = CreateProjectRequest.from_dict(create_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


