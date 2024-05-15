# AlertDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_source** | **str** | The source of the alert | [optional] 
**source** | **str** | The UID of the source of the alert | [optional] 
**source_type** | **str** | The type of source. | [optional] 
**value** | **float** | The value that triggered the alert | [optional] 
**source_uid** | **str** | The UID of the source of the alert | [optional] 
**when** | **str** | The time the alert was created | [optional] 

## Example

```python
from notehub_py.models.alert_data_inner import AlertDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlertDataInner from a JSON string
alert_data_inner_instance = AlertDataInner.from_json(json)
# print the JSON string representation of the object
print(AlertDataInner.to_json())

# convert the object into a dict
alert_data_inner_dict = alert_data_inner_instance.to_dict()
# create an instance of AlertDataInner from a dict
alert_data_inner_from_dict = AlertDataInner.from_dict(alert_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


