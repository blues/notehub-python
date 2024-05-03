# GetRouteLogsByRoute200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | The date of the logs. | [optional] 
**route_uid** | **str** | The route UID. | [optional] 
**event_uid** | **str** | The event UID. | [optional] 
**attn** | **bool** | Whether the event was routed in error | [optional] 
**status** | **str** | The status of the event. | [optional] 
**text** | **str** | The response body of the route. | [optional] 
**url** | **str** | The URL of the route. | [optional] 

## Example

```python
from notehub_py.models.get_route_logs_by_route200_response_inner import GetRouteLogsByRoute200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRouteLogsByRoute200ResponseInner from a JSON string
get_route_logs_by_route200_response_inner_instance = GetRouteLogsByRoute200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetRouteLogsByRoute200ResponseInner.to_json())

# convert the object into a dict
get_route_logs_by_route200_response_inner_dict = get_route_logs_by_route200_response_inner_instance.to_dict()
# create an instance of GetRouteLogsByRoute200ResponseInner from a dict
get_route_logs_by_route200_response_inner_from_dict = GetRouteLogsByRoute200ResponseInner.from_dict(get_route_logs_by_route200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


