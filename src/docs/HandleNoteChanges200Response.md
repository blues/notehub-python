# HandleNoteChanges200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of notes. | [optional] 
**changes** | **int** | The number of pending changes in the Notefile. | [optional] 
**notes** | **object** | An object with a key for each note and a value object with the body of each Note and the time the Note was added. | [optional] 

## Example

```python
from notehub_py.models.handle_note_changes200_response import HandleNoteChanges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HandleNoteChanges200Response from a JSON string
handle_note_changes200_response_instance = HandleNoteChanges200Response.from_json(json)
# print the JSON string representation of the object
print(HandleNoteChanges200Response.to_json())

# convert the object into a dict
handle_note_changes200_response_dict = handle_note_changes200_response_instance.to_dict()
# create an instance of HandleNoteChanges200Response from a dict
handle_note_changes200_response_from_dict = HandleNoteChanges200Response.from_dict(handle_note_changes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


