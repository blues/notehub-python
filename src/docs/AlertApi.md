# notehub_py.AlertApi

All URIs are relative to *https://api.notefile.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alerts**](AlertApi.md#get_alerts) | **GET** /v1/projects/{projectUID}/alerts | 


# **get_alerts**
> GetAlerts200Response get_alerts(project_uid, page_size=page_size, page_num=page_num)



Get list of defined Alerts

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_alerts200_response import GetAlerts200Response
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
    api_instance = notehub_py.AlertApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)

    try:
        api_response = api_instance.get_alerts(project_uid, page_size=page_size, page_num=page_num)
        print("The response of AlertApi->get_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 50]
 **page_num** | **int**|  | [optional] [default to 1]

### Return type

[**GetAlerts200Response**](GetAlerts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from GET /alerts |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

