# Monitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source_type** | **str** | The type of source to monitor. Currently only \&quot;event\&quot; is supported. | [optional] 
**disabled** | **bool** | If true, the monitor will not be evaluated. | [optional] 
**alert** | **bool** | If true, the monitor is in alert state. | [optional] 
**notefile_filter** | **List[str]** |  | [optional] 
**fleet_filter** | **List[str]** |  | [optional] 
**source_selector** | **str** | A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value. | [optional] 
**condition_type** | **str** | The type of condition to apply to the value selected by the source_selector | [optional] 
**thresholds** | [**MonitorThresholds**](MonitorThresholds.md) |  | [optional] 
**alert_routes** | [**List[MonitorAlertRoutesInner]**](MonitorAlertRoutesInner.md) |  | [optional] 
**last_routed_at** | **str** | The last time the monitor was evaluated and routed. | [optional] 
**silenced** | **bool** | If true, alerts will be created, but no notifications will be sent. | [optional] 
**routing_cooldown_period** | **str** | The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit. | [optional] 

## Example

```python
from notehub_py.models.monitor import Monitor

# TODO update the JSON string below
json = "{}"
# create an instance of Monitor from a JSON string
monitor_instance = Monitor.from_json(json)
# print the JSON string representation of the object
print(Monitor.to_json())

# convert the object into a dict
monitor_dict = monitor_instance.to_dict()
# create an instance of Monitor from a dict
monitor_from_dict = Monitor.from_dict(monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


