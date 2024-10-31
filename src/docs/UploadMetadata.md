# UploadMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**md5** | **str** |  | [optional] 
**crc32** | **int** |  | [optional] 
**created** | **int** |  | [optional] 
**modified** | **int** |  | [optional] 
**source** | **str** |  | [optional] 
**contains** | **str** |  | [optional] 
**found** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**firmware** | [**Firmware**](Firmware.md) |  | [optional] 

## Example

```python
from notehub_py.models.upload_metadata import UploadMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UploadMetadata from a JSON string
upload_metadata_instance = UploadMetadata.from_json(json)
# print the JSON string representation of the object
print(UploadMetadata.to_json())

# convert the object into a dict
upload_metadata_dict = upload_metadata_instance.to_dict()
# create an instance of UploadMetadata from a dict
upload_metadata_from_dict = UploadMetadata.from_dict(upload_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


