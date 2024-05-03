# Twilio

Route settings specific to Twilio routes.  Only used for Twilio route types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**filter** | [**HttpFilter**](HttpFilter.md) |  | [optional] 
**timeout** | **int** | Timeout in seconds for each request | [optional] [default to 15]
**account_sid** | **str** | Twilio Account SID | [optional] 
**auth_token** | **str** | Twilio Auth Token.  This value will be omitted from the response and replaced with a placeholder. | [optional] 
**to** | **str** | Phone number to send SMS to, leave blank to use notefile, must use E.164 format | [optional] 
**var_from** | **str** | Phone number to send SMS from, leave blank to use notefile, must use E.164 format | [optional] 
**message** | **str** | Message to send, leave blank to use notefile. | [optional] 
**throttle_ms** | **int** |  | [optional] 

## Example

```python
from notehub_py.models.twilio import Twilio

# TODO update the JSON string below
json = "{}"
# create an instance of Twilio from a JSON string
twilio_instance = Twilio.from_json(json)
# print the JSON string representation of the object
print(Twilio.to_json())

# convert the object into a dict
twilio_dict = twilio_instance.to_dict()
# create an instance of Twilio from a dict
twilio_from_dict = Twilio.from_dict(twilio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


