# notehub_py.FirmwareApi

All URIs are relative to *https://api.notefile.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_firmware_info**](FirmwareApi.md#get_firmware_info) | **GET** /v1/projects/{projectUID}/firmware | 


# **get_firmware_info**
> List[FirmwareInfo] get_firmware_info(project_uid, product_uid=product_uid, firmware_type=firmware_type, version=version, target=target, filename=filename, md5=md5, unpublished=unpublished)



Get Available Firmware Information

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.firmware_info import FirmwareInfo
from notehub_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.notefile.net
# See configuration.py for a list of all supported configuration parameters.
configuration = notehub_py.Configuration(
    host = "https://api.notefile.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.FirmwareApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    product_uid = 'product_uid_example' # str |  (optional)
    firmware_type = 'firmware_type_example' # str |  (optional)
    version = 'version_example' # str |  (optional)
    target = 'target_example' # str |  (optional)
    filename = 'notecard-7.2.2.16518$20240410043100.bin' # str |  (optional)
    md5 = 'md5_example' # str |  (optional)
    unpublished = True # bool |  (optional)

    try:
        api_response = api_instance.get_firmware_info(project_uid, product_uid=product_uid, firmware_type=firmware_type, version=version, target=target, filename=filename, md5=md5, unpublished=unpublished)
        print("The response of FirmwareApi->get_firmware_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirmwareApi->get_firmware_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **product_uid** | **str**|  | [optional] 
 **firmware_type** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **target** | **str**|  | [optional] 
 **filename** | **str**|  | [optional] 
 **md5** | **str**|  | [optional] 
 **unpublished** | **bool**|  | [optional] 

### Return type

[**List[FirmwareInfo]**](FirmwareInfo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

