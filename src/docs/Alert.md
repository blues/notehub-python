# Alert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Alert UID | [optional] 
**monitor_uid** | **str** | Monitor UID | [optional] 
**device_uid** | **str** | Device UID | [optional] 
**created_at** | **int** | The time the alert was created | [optional] 
**value** | **float** | The value that triggered the alert | [optional] 
**resolved** | **bool** | If true, the alert has been resolved | [optional] 
**version** | **int** | The version of the alert | [optional] 
**alert_source** | **str** | The source of the alert | [optional] 
**source** | **str** | The UID of the source of the alert | [optional] 
**data** | [**List[AlertDataInner]**](AlertDataInner.md) |  | [optional] 
**notifications** | [**List[AlertNotificationsInner]**](AlertNotificationsInner.md) |  | [optional] 

## Example

```python
from notehub_py.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print(Alert.to_json())

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_from_dict = Alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


