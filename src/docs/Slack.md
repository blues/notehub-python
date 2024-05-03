# Slack

Route settings specific to Slack routes.  Only used for Slack route types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**filter** | [**HttpFilter**](HttpFilter.md) |  | [optional] 
**transform** | [**SnowflakeTransform**](SnowflakeTransform.md) |  | [optional] 
**throttle_ms** | **int** | Minimum time between requests in Miliseconds | [optional] 
**timeout** | **int** | Timeout in seconds for each request | [optional] [default to 15]
**slack_type** | **str** | The type of Slack message.  Must be one of \&quot;slack-bearer\&quot; for Bearer Token or \&quot;slack-webhook\&quot; for Webhook messages | [optional] 
**bearer** | **str** | The Bearer Token for Slack messaging, if the \&quot;slack-bearer\&quot; type is selected | [optional] 
**channel** | **str** | The Channel ID for Bearer Token method, if the \&quot;slack-bearer\&quot; type is selected | [optional] 
**webhook_url** | **str** | The Webhook URL for Slack Messaging if the \&quot;slack-webhook\&quot; type is selected | [optional] 
**text** | **str** | The simple text message to be sent, if the blocks message field is not in use.  Placeholders are available for this field. | [optional] 
**blocks** | **str** | The Blocks message to be sent.  If populated, this field overrides the text field within the Slack Messaging API.  Placeholders are available for this field. | [optional] 

## Example

```python
from notehub_py.models.slack import Slack

# TODO update the JSON string below
json = "{}"
# create an instance of Slack from a JSON string
slack_instance = Slack.from_json(json)
# print the JSON string representation of the object
print(Slack.to_json())

# convert the object into a dict
slack_dict = slack_instance.to_dict()
# create an instance of Slack from a dict
slack_from_dict = Slack.from_dict(slack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


