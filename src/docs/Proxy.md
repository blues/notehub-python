# Proxy

Route settings specific to Proxy routes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**url** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**http_headers** | **Dict[str, str]** |  | [optional] 
**timeout** | **int** | Timeout in seconds for each request | [optional] [default to 15]

## Example

```python
from notehub_py.models.proxy import Proxy

# TODO update the JSON string below
json = "{}"
# create an instance of Proxy from a JSON string
proxy_instance = Proxy.from_json(json)
# print the JSON string representation of the object
print(Proxy.to_json())

# convert the object into a dict
proxy_dict = proxy_instance.to_dict()
# create an instance of Proxy from a dict
proxy_from_dict = Proxy.from_dict(proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


