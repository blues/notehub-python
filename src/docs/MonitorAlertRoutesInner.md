# MonitorAlertRoutesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the Slack webhook. | [optional] 
**message_type** | **str** | text or blocks | [optional] 
**text** | **str** | The text of the message, or the blocks definition | [optional] 
**token** | **str** | The bearer token for the Slack app. | [optional] 
**channel** | **str** | The channel to send the message to. | [optional] 
**email** | **str** | Email Address | [optional] 

## Example

```python
from notehub_py.models.monitor_alert_routes_inner import MonitorAlertRoutesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorAlertRoutesInner from a JSON string
monitor_alert_routes_inner_instance = MonitorAlertRoutesInner.from_json(json)
# print the JSON string representation of the object
print(MonitorAlertRoutesInner.to_json())

# convert the object into a dict
monitor_alert_routes_inner_dict = monitor_alert_routes_inner_instance.to_dict()
# create an instance of MonitorAlertRoutesInner from a dict
monitor_alert_routes_inner_from_dict = MonitorAlertRoutesInner.from_dict(monitor_alert_routes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


