# AlertNotificationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_type** | **str** | The type of notification | [optional] 
**status** | **float** | The status of the notification | [optional] 
**recipients** | **str** | The recipients of the notification | [optional] 

## Example

```python
from notehub_py.models.alert_notifications_inner import AlertNotificationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlertNotificationsInner from a JSON string
alert_notifications_inner_instance = AlertNotificationsInner.from_json(json)
# print the JSON string representation of the object
print(AlertNotificationsInner.to_json())

# convert the object into a dict
alert_notifications_inner_dict = alert_notifications_inner_instance.to_dict()
# create an instance of AlertNotificationsInner from a dict
alert_notifications_inner_from_dict = AlertNotificationsInner.from_dict(alert_notifications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


