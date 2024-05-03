# Product


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | 
**label** | **str** |  | 
**auto_provision_fleets** | **List[str]** |  | [optional] 
**disable_devices_by_default** | **bool** |  | 

## Example

```python
from notehub_py.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print(Product.to_json())

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_from_dict = Product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


