# HttpFilter

Route filtering settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | What notefiles this route applies to. | [optional] 
**system_notefiles** | **bool** | Whether system notefiles should be affected by this route | [optional] 
**files** | **List[str]** |  | [optional] 

## Example

```python
from notehub_py.models.http_filter import HttpFilter

# TODO update the JSON string below
json = "{}"
# create an instance of HttpFilter from a JSON string
http_filter_instance = HttpFilter.from_json(json)
# print the JSON string representation of the object
print(HttpFilter.to_json())

# convert the object into a dict
http_filter_dict = http_filter_instance.to_dict()
# create an instance of HttpFilter from a dict
http_filter_from_dict = HttpFilter.from_dict(http_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


