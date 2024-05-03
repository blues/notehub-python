# PutDeviceFleetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleet_uids** | **List[str]** | The fleetUIDs to add to the device. | 

## Example

```python
from notehub_py.models.put_device_fleets_request import PutDeviceFleetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutDeviceFleetsRequest from a JSON string
put_device_fleets_request_instance = PutDeviceFleetsRequest.from_json(json)
# print the JSON string representation of the object
print(PutDeviceFleetsRequest.to_json())

# convert the object into a dict
put_device_fleets_request_dict = put_device_fleets_request_instance.to_dict()
# create an instance of PutDeviceFleetsRequest from a dict
put_device_fleets_request_from_dict = PutDeviceFleetsRequest.from_dict(put_device_fleets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


