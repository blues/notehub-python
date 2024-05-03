# Http

Route settings specific to HTTP routes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**filter** | [**HttpFilter**](HttpFilter.md) |  | [optional] 
**transform** | [**HttpTransform**](HttpTransform.md) |  | [optional] 
**throttle_ms** | **int** | Minimum time between requests in Miliseconds | [optional] 
**url** | **str** | Route URL | [optional] 
**http_headers** | **Dict[str, str]** |  | [optional] 
**disable_http_headers** | **bool** |  | [optional] [default to False]
**timeout** | **int** | Timeout in seconds for each request | [optional] [default to 15]

## Example

```python
from notehub_py.models.http import Http

# TODO update the JSON string below
json = "{}"
# create an instance of Http from a JSON string
http_instance = Http.from_json(json)
# print the JSON string representation of the object
print(Http.to_json())

# convert the object into a dict
http_dict = http_instance.to_dict()
# create an instance of Http from a dict
http_from_dict = Http.from_dict(http_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


