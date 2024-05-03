# Radresponder

Route settings specific to RadResponder routes.  Only used for RadResponder route types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**test_api** | **bool** |  | [optional] [default to False]
**data_feed_key** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 

## Example

```python
from notehub_py.models.radresponder import Radresponder

# TODO update the JSON string below
json = "{}"
# create an instance of Radresponder from a JSON string
radresponder_instance = Radresponder.from_json(json)
# print the JSON string representation of the object
print(Radresponder.to_json())

# convert the object into a dict
radresponder_dict = radresponder_instance.to_dict()
# create an instance of Radresponder from a dict
radresponder_from_dict = Radresponder.from_dict(radresponder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


