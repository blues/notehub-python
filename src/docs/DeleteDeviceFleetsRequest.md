# DeleteDeviceFleetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleet_uids** | **List[str]** | The fleetUIDs to remove from the device. | 

## Example

```python
from notehub_py.models.delete_device_fleets_request import DeleteDeviceFleetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDeviceFleetsRequest from a JSON string
delete_device_fleets_request_instance = DeleteDeviceFleetsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteDeviceFleetsRequest.to_json())

# convert the object into a dict
delete_device_fleets_request_dict = delete_device_fleets_request_instance.to_dict()
# create an instance of DeleteDeviceFleetsRequest from a dict
delete_device_fleets_request_from_dict = DeleteDeviceFleetsRequest.from_dict(delete_device_fleets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


