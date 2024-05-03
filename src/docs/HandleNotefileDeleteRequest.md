# HandleNotefileDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[str]** | One or more files to obtain change information from. | [optional] 

## Example

```python
from notehub_py.models.handle_notefile_delete_request import HandleNotefileDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HandleNotefileDeleteRequest from a JSON string
handle_notefile_delete_request_instance = HandleNotefileDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(HandleNotefileDeleteRequest.to_json())

# convert the object into a dict
handle_notefile_delete_request_dict = handle_notefile_delete_request_instance.to_dict()
# create an instance of HandleNotefileDeleteRequest from a dict
handle_notefile_delete_request_from_dict = HandleNotefileDeleteRequest.from_dict(handle_notefile_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


