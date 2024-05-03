# GetDevicePublicKey200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | 
**key** | **str** |  | 

## Example

```python
from notehub_py.models.get_device_public_key200_response import GetDevicePublicKey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDevicePublicKey200Response from a JSON string
get_device_public_key200_response_instance = GetDevicePublicKey200Response.from_json(json)
# print the JSON string representation of the object
print(GetDevicePublicKey200Response.to_json())

# convert the object into a dict
get_device_public_key200_response_dict = get_device_public_key200_response_instance.to_dict()
# create an instance of GetDevicePublicKey200Response from a dict
get_device_public_key200_response_from_dict = GetDevicePublicKey200Response.from_dict(get_device_public_key200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


