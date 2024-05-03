# Google

Route settings specific to Google routes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**filter** | [**HttpFilter**](HttpFilter.md) |  | [optional] 
**transform** | [**HttpTransform**](HttpTransform.md) |  | [optional] 
**throttle_ms** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**timeout** | **int** | Timeout in seconds for each request | [optional] [default to 15]
**token** | **str** | Optional authentication token | [optional] 

## Example

```python
from notehub_py.models.google import Google

# TODO update the JSON string below
json = "{}"
# create an instance of Google from a JSON string
google_instance = Google.from_json(json)
# print the JSON string representation of the object
print(Google.to_json())

# convert the object into a dict
google_dict = google_instance.to_dict()
# create an instance of Google from a dict
google_from_dict = Google.from_dict(google_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


