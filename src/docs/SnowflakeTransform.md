# SnowflakeTransform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Data transformation to apply.  Only \&quot;jsonata\&quot; is valid for Snowflake routes | [optional] [default to 'jsonata']
**jsonata** | **str** | JSONata transformation | [optional] 

## Example

```python
from notehub_py.models.snowflake_transform import SnowflakeTransform

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeTransform from a JSON string
snowflake_transform_instance = SnowflakeTransform.from_json(json)
# print the JSON string representation of the object
print(SnowflakeTransform.to_json())

# convert the object into a dict
snowflake_transform_dict = snowflake_transform_instance.to_dict()
# create an instance of SnowflakeTransform from a dict
snowflake_transform_from_dict = SnowflakeTransform.from_dict(snowflake_transform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


