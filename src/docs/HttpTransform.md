# HttpTransform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Data transformation to apply.  Options of \&quot;\&quot; for none, \&quot;bridge\&quot; for Azure IoT, \&quot;jsonata\&quot; for JSONata expression, or \&quot;flatten\&quot;, \&quot;simple\&quot;, \&quot;body\&quot; or \&quot;payload\&quot; | [optional] 
**jsonata** | **str** | JSONata transformation, if JSONata | [optional] 

## Example

```python
from notehub_py.models.http_transform import HttpTransform

# TODO update the JSON string below
json = "{}"
# create an instance of HttpTransform from a JSON string
http_transform_instance = HttpTransform.from_json(json)
# print the JSON string representation of the object
print(HttpTransform.to_json())

# convert the object into a dict
http_transform_dict = http_transform_instance.to_dict()
# create an instance of HttpTransform from a dict
http_transform_from_dict = HttpTransform.from_dict(http_transform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


