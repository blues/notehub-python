# SlackBearerNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The bearer token for the Slack app. | [optional] 
**channel** | **str** | The channel to send the message to. | [optional] 
**message_type** | **str** | text or blocks | [optional] 
**text** | **str** | The text of the message, or the blocks definition | [optional] 

## Example

```python
from notehub_py.models.slack_bearer_notification import SlackBearerNotification

# TODO update the JSON string below
json = "{}"
# create an instance of SlackBearerNotification from a JSON string
slack_bearer_notification_instance = SlackBearerNotification.from_json(json)
# print the JSON string representation of the object
print(SlackBearerNotification.to_json())

# convert the object into a dict
slack_bearer_notification_dict = slack_bearer_notification_instance.to_dict()
# create an instance of SlackBearerNotification from a dict
slack_bearer_notification_from_dict = SlackBearerNotification.from_dict(slack_bearer_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


