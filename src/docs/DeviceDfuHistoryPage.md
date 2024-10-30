# DeviceDfuHistoryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[DeviceDfuHistory]**](DeviceDfuHistory.md) |  | [optional] 
**has_more** | **bool** |  | [optional] [default to False]

## Example

```python
from notehub_py.models.device_dfu_history_page import DeviceDfuHistoryPage

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDfuHistoryPage from a JSON string
device_dfu_history_page_instance = DeviceDfuHistoryPage.from_json(json)
# print the JSON string representation of the object
print(DeviceDfuHistoryPage.to_json())

# convert the object into a dict
device_dfu_history_page_dict = device_dfu_history_page_instance.to_dict()
# create an instance of DeviceDfuHistoryPage from a dict
device_dfu_history_page_from_dict = DeviceDfuHistoryPage.from_dict(device_dfu_history_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


