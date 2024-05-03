# DFUState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**file** | **str** | Firmware filename | [optional] 
**length** | **float** | Length of firmware file | [optional] 
**crc32** | **float** | Used for image verification | [optional] 
**md5** | **str** | Used for image verification | [optional] 
**mode** | **str** | * \&quot;idle\&quot;          - nothing downloading or downloaded * \&quot;error\&quot;         - halted and in the error state * \&quot;downloading\&quot;   - transferring data from cloud to module * \&quot;sideloading\&quot;   - transferring data via request to module * \&quot;ready\&quot;         - DFU data is ready/verified and waiting on external storage * \&quot;ready-retry\&quot;   - DFU data is ready/verified and retrying * \&quot;updating\&quot;      - currently updating * \&quot;completed\&quot;     - DFU is done successfully  | [optional] 
**status** | **str** | Status message | [optional] 
**began** | **float** | The time when the DFU began | [optional] 
**retry** | **float** | Value of _fw_retry environment var at time of DFU initialization | [optional] 
**errors** | **float** | The number of consecutive errors the DFU process has encountered | [optional] 
**read** | **float** | The amount the notecard has read of the image from notehub | [optional] 
**updated** | **float** | Last updated timestamp | [optional] 
**version** | **str** | Last known version, which is generally a JSON object contained within the firmware image | [optional] 

## Example

```python
from notehub_py.models.dfu_state import DFUState

# TODO update the JSON string below
json = "{}"
# create an instance of DFUState from a JSON string
dfu_state_instance = DFUState.from_json(json)
# print the JSON string representation of the object
print(DFUState.to_json())

# convert the object into a dict
dfu_state_dict = dfu_state_instance.to_dict()
# create an instance of DFUState from a dict
dfu_state_from_dict = DFUState.from_dict(dfu_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


