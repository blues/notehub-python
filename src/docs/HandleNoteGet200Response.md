# HandleNoteGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **object** | The note body | [optional] 
**payload** | **str** | The note payload | [optional] 
**time** | **int** | The time the Note was added to the Notecard or Notehub | [optional] 

## Example

```python
from notehub_py.models.handle_note_get200_response import HandleNoteGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HandleNoteGet200Response from a JSON string
handle_note_get200_response_instance = HandleNoteGet200Response.from_json(json)
# print the JSON string representation of the object
print(HandleNoteGet200Response.to_json())

# convert the object into a dict
handle_note_get200_response_dict = handle_note_get200_response_instance.to_dict()
# create an instance of HandleNoteGet200Response from a dict
handle_note_get200_response_from_dict = HandleNoteGet200Response.from_dict(handle_note_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


