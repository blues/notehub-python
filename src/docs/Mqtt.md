# Mqtt

Route settings specific to MQTT routes.  Only used for MQTT route types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**filter** | [**HttpFilter**](HttpFilter.md) |  | [optional] 
**transform** | [**HttpTransform**](HttpTransform.md) |  | [optional] 
**throttle_ms** | **int** |  | [optional] 
**timeout** | **int** | Timeout in seconds for each request | [optional] [default to 15]
**broker** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**topic** | **str** |  | [optional] 
**certificate** | **str** | Certificate with \\n newlines.  This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**certificate_name** | **str** | Name of certificate. | [optional] 
**key** | **str** | Key with \\n newlines.  This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**private_key_name** | **str** | Name of key | [optional] 

## Example

```python
from notehub_py.models.mqtt import Mqtt

# TODO update the JSON string below
json = "{}"
# create an instance of Mqtt from a JSON string
mqtt_instance = Mqtt.from_json(json)
# print the JSON string representation of the object
print(Mqtt.to_json())

# convert the object into a dict
mqtt_dict = mqtt_instance.to_dict()
# create an instance of Mqtt from a dict
mqtt_from_dict = Mqtt.from_dict(mqtt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


