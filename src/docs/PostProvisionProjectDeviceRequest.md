# PostProvisionProjectDeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_uid** | **str** | The ProductUID that the device should use. | 
**device_sn** | **str** | The serial number to assign to the device. | [optional] 

## Example

```python
from notehub_py.models.post_provision_project_device_request import PostProvisionProjectDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostProvisionProjectDeviceRequest from a JSON string
post_provision_project_device_request_instance = PostProvisionProjectDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(PostProvisionProjectDeviceRequest.to_json())

# convert the object into a dict
post_provision_project_device_request_dict = post_provision_project_device_request_instance.to_dict()
# create an instance of PostProvisionProjectDeviceRequest from a dict
post_provision_project_device_request_from_dict = PostProvisionProjectDeviceRequest.from_dict(post_provision_project_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


