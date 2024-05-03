# CreateProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_uid** | **str** | The requested uid for the Product. Will be prefixed with the user&#39;s reversed email. | 
**label** | **str** | The label for the Product. | 
**auto_provision_fleets** | **List[str]** |  | [optional] 
**disable_devices_by_default** | **bool** | If &#x60;true&#x60;, devices provisioned to this product will be automatically disabled by default. | [optional] 

## Example

```python
from notehub_py.models.create_product_request import CreateProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductRequest from a JSON string
create_product_request_instance = CreateProductRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProductRequest.to_json())

# convert the object into a dict
create_product_request_dict = create_product_request_instance.to_dict()
# create an instance of CreateProductRequest from a dict
create_product_request_from_dict = CreateProductRequest.from_dict(create_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


