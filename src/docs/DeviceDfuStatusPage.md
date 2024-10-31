# DeviceDfuStatusPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[DeviceDfuStatus]**](DeviceDfuStatus.md) |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]

## Example

```python
from notehub_py.models.device_dfu_status_page import DeviceDfuStatusPage

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDfuStatusPage from a JSON string
device_dfu_status_page_instance = DeviceDfuStatusPage.from_json(json)
# print the JSON string representation of the object
print(DeviceDfuStatusPage.to_json())

# convert the object into a dict
device_dfu_status_page_dict = device_dfu_status_page_instance.to_dict()
# create an instance of DeviceDfuStatusPage from a dict
device_dfu_status_page_from_dict = DeviceDfuStatusPage.from_dict(device_dfu_status_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


