# CreateFleetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label, or name,  for the Fleet. | [optional] 
**smart_rule** | **str** | JSONata expression that will be evaluated to determine device membership into this fleet, if the expression evaluates to a 1, the device will be included, if it evaluates to -1 it will be removed, and if it evaluates to 0 or errors it will be left unchanged. | [optional] 

## Example

```python
from notehub_py.models.create_fleet_request import CreateFleetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFleetRequest from a JSON string
create_fleet_request_instance = CreateFleetRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFleetRequest.to_json())

# convert the object into a dict
create_fleet_request_dict = create_fleet_request_instance.to_dict()
# create an instance of CreateFleetRequest from a dict
create_fleet_request_from_dict = CreateFleetRequest.from_dict(create_fleet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


