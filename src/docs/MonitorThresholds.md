# MonitorThresholds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarm** | **float** | The value that triggers the monitor at an alarm level | [optional] 

## Example

```python
from notehub_py.models.monitor_thresholds import MonitorThresholds

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorThresholds from a JSON string
monitor_thresholds_instance = MonitorThresholds.from_json(json)
# print the JSON string representation of the object
print(MonitorThresholds.to_json())

# convert the object into a dict
monitor_thresholds_dict = monitor_thresholds_instance.to_dict()
# create an instance of MonitorThresholds from a dict
monitor_thresholds_from_dict = MonitorThresholds.from_dict(monitor_thresholds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


