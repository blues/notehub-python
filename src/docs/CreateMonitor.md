# CreateMonitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | 
**source_type** | **str** | The type of source to monitor. Currently only \&quot;event\&quot; is supported. | [optional] 
**disabled** | **bool** | If true, the monitor will not be evaluated. | [optional] 
**alert** | **bool** | If true, the monitor is in alert state. | [optional] 
**notefile_filter** | **List[str]** |  | 
**fleet_filter** | **List[str]** |  | [optional] 
**source_selector** | **str** | A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value. | [optional] 
**condition_type** | **str** | A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to] | [optional] 
**threshold** | **int** | The type of condition to apply to the value selected by the source_selector | [optional] 
**alert_routes** | [**List[MonitorAlertRoutesInner]**](MonitorAlertRoutesInner.md) |  | 
**last_routed_at** | **str** | The last time the monitor was evaluated and routed. | [optional] 
**silenced** | **bool** | If true, alerts will be created, but no notifications will be sent. | [optional] 
**routing_cooldown_period** | **str** | The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit. | [optional] 
**aggregate_function** | **str** | Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min] | [optional] 
**aggregate_window** | **str** | The time window to aggregate the selected values. It follows the format of a number followed by a time unit | [optional] 
**per_device** | **bool** | Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices. | [optional] 

## Example

```python
from notehub_py.models.create_monitor import CreateMonitor

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMonitor from a JSON string
create_monitor_instance = CreateMonitor.from_json(json)
# print the JSON string representation of the object
print(CreateMonitor.to_json())

# convert the object into a dict
create_monitor_dict = create_monitor_instance.to_dict()
# create an instance of CreateMonitor from a dict
create_monitor_from_dict = CreateMonitor.from_dict(create_monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


