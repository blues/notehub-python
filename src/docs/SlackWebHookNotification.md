# SlackWebHookNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the Slack webhook. | [optional] 
**message_type** | **str** | text or blocks | [optional] 
**text** | **str** | The text of the message, or the blocks definition | [optional] 

## Example

```python
from notehub_py.models.slack_web_hook_notification import SlackWebHookNotification

# TODO update the JSON string below
json = "{}"
# create an instance of SlackWebHookNotification from a JSON string
slack_web_hook_notification_instance = SlackWebHookNotification.from_json(json)
# print the JSON string representation of the object
print(SlackWebHookNotification.to_json())

# convert the object into a dict
slack_web_hook_notification_dict = slack_web_hook_notification_instance.to_dict()
# create an instance of SlackWebHookNotification from a dict
slack_web_hook_notification_from_dict = SlackWebHookNotification.from_dict(slack_web_hook_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


