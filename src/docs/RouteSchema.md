# RouteSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**filter** | [**HttpFilter**](HttpFilter.md) |  | [optional] 
**transform** | [**SnowflakeTransform**](SnowflakeTransform.md) |  | [optional] 
**throttle_ms** | **int** | Minimum time between requests in Miliseconds | [optional] 
**url** | **str** |  | [optional] 
**http_headers** | **Dict[str, str]** |  | [optional] 
**disable_http_headers** | **bool** |  | [optional] [default to False]
**timeout** | **int** | Timeout in seconds for each request | [optional] [default to 15]
**token** | **str** | Optional authentication token | [optional] 
**alias** | **str** |  | [optional] 
**broker** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**topic** | **str** |  | [optional] 
**certificate** | **str** | Certificate with \\n newlines.  This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**certificate_name** | **str** | Name of certificate. | [optional] 
**key** | **str** | Key with \\n newlines.  This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**private_key_name** | **str** | Name of PEM key.  If omitted, defaults to \&quot;present\&quot; | [optional] [default to 'present']
**region** | **str** |  | [optional] 
**access_key_id** | **str** |  | [optional] 
**access_key_secret** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**message_group_id** | **str** |  | [optional] 
**message_deduplication_id** | **str** |  | [optional] 
**channel** | **str** | The Channel ID for Bearer Token method, if the \&quot;slack-bearer\&quot; type is selected | [optional] 
**test_api** | **bool** |  | [optional] [default to False]
**data_feed_key** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**functions_key_secret** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**sas_policy_name** | **str** |  | [optional] 
**sas_policy_key** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**app_key** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**organization_name** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**pem** | **str** | PEM key with \\n newlines. This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**slack_type** | **str** | The type of Slack message.  Must be one of \&quot;slack-bearer\&quot; for Bearer Token or \&quot;slack-webhook\&quot; for Webhook messages | [optional] 
**bearer** | **str** | The Bearer Token for Slack messaging, if the \&quot;slack-bearer\&quot; type is selected | [optional] 
**webhook_url** | **str** | The Webhook URL for Slack Messaging if the \&quot;slack-webhook\&quot; type is selected | [optional] 
**text** | **str** | The simple text message to be sent, if the blocks message field is not in use.  Placeholders are available for this field. | [optional] 
**blocks** | **str** | The Blocks message to be sent.  If populated, this field overrides the text field within the Slack Messaging API.  Placeholders are available for this field. | [optional] 

## Example

```python
from notehub_py.models.route_schema import RouteSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RouteSchema from a JSON string
route_schema_instance = RouteSchema.from_json(json)
# print the JSON string representation of the object
print(RouteSchema.to_json())

# convert the object into a dict
route_schema_dict = route_schema_instance.to_dict()
# create an instance of RouteSchema from a dict
route_schema_from_dict = RouteSchema.from_dict(route_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


