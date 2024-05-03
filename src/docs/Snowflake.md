# Snowflake

Route settings specific to Snowflake routes.  Only used for Snowflake route types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**filter** | [**HttpFilter**](HttpFilter.md) |  | [optional] 
**transform** | [**SnowflakeTransform**](SnowflakeTransform.md) |  | [optional] 
**timeout** | **int** | Timeout in seconds for each request | [optional] [default to 15]
**organization_name** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**private_key_name** | **str** | Name of PEM key.  If omitted, defaults to \&quot;present\&quot; | [optional] [default to 'present']
**pem** | **str** | PEM key with \\n newlines. This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 

## Example

```python
from notehub_py.models.snowflake import Snowflake

# TODO update the JSON string below
json = "{}"
# create an instance of Snowflake from a JSON string
snowflake_instance = Snowflake.from_json(json)
# print the JSON string representation of the object
print(Snowflake.to_json())

# convert the object into a dict
snowflake_dict = snowflake_instance.to_dict()
# create an instance of Snowflake from a dict
snowflake_from_dict = Snowflake.from_dict(snowflake_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


