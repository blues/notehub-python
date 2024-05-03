# UpdateFleetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label for the Fleet. | [optional] 
**add_devices** | **List[str]** | List of DeviceUIDs to add to fleet | [optional] 
**remove_devices** | **List[str]** | List of DeviceUIDs to remove from fleet | [optional] 

## Example

```python
from notehub_py.models.update_fleet_request import UpdateFleetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFleetRequest from a JSON string
update_fleet_request_instance = UpdateFleetRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFleetRequest.to_json())

# convert the object into a dict
update_fleet_request_dict = update_fleet_request_instance.to_dict()
# create an instance of UpdateFleetRequest from a dict
update_fleet_request_from_dict = UpdateFleetRequest.from_dict(update_fleet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


