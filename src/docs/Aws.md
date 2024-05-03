# Aws

Route settings specific to AWS routes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleets** | **List[str]** | list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets | [optional] 
**filter** | [**HttpFilter**](HttpFilter.md) |  | [optional] 
**transform** | [**HttpTransform**](HttpTransform.md) |  | [optional] 
**throttle_ms** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**http_headers** | **Dict[str, str]** |  | [optional] 
**disable_http_headers** | **bool** |  | [optional] [default to False]
**timeout** | **int** | Timeout in seconds for each request | [optional] [default to 15]
**region** | **str** |  | [optional] 
**access_key_id** | **str** |  | [optional] 
**access_key_secret** | **str** | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional] 
**message_group_id** | **str** |  | [optional] 
**message_deduplication_id** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 

## Example

```python
from notehub_py.models.aws import Aws

# TODO update the JSON string below
json = "{}"
# create an instance of Aws from a JSON string
aws_instance = Aws.from_json(json)
# print the JSON string representation of the object
print(Aws.to_json())

# convert the object into a dict
aws_dict = aws_instance.to_dict()
# create an instance of Aws from a dict
aws_from_dict = Aws.from_dict(aws_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


