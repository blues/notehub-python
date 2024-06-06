# EmailNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email Address | [optional] 

## Example

```python
from notehub_py.models.email_notification import EmailNotification

# TODO update the JSON string below
json = "{}"
# create an instance of EmailNotification from a JSON string
email_notification_instance = EmailNotification.from_json(json)
# print the JSON string representation of the object
print(EmailNotification.to_json())

# convert the object into a dict
email_notification_dict = email_notification_instance.to_dict()
# create an instance of EmailNotification from a dict
email_notification_from_dict = EmailNotification.from_dict(email_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


