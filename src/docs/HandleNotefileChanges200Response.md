# HandleNotefileChanges200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of files. | [optional] 
**changes** | **int** | The number of pending changes in the Notefile. | [optional] 
**info** | **object** | An object with a key for each Notefile that matched the request parameters, and value object with the changes and total for each file. | [optional] 

## Example

```python
from notehub_py.models.handle_notefile_changes200_response import HandleNotefileChanges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HandleNotefileChanges200Response from a JSON string
handle_notefile_changes200_response_instance = HandleNotefileChanges200Response.from_json(json)
# print the JSON string representation of the object
print(HandleNotefileChanges200Response.to_json())

# convert the object into a dict
handle_notefile_changes200_response_dict = handle_notefile_changes200_response_instance.to_dict()
# create an instance of HandleNotefileChanges200Response from a dict
handle_notefile_changes200_response_from_dict = HandleNotefileChanges200Response.from_dict(handle_notefile_changes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


