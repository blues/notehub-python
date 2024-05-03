# notehub_py.BillingAccountApi

All URIs are relative to *https://api.notefile.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_billing_accounts**](BillingAccountApi.md#get_billing_accounts) | **GET** /v1/billing-accounts | 


# **get_billing_accounts**
> GetBillingAccounts200Response get_billing_accounts()



Get Billing Accounts accessible by the api_key

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_billing_accounts200_response import GetBillingAccounts200Response
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
    api_instance = notehub_py.BillingAccountApi(api_client)

    try:
        api_response = api_instance.get_billing_accounts()
        print("The response of BillingAccountApi->get_billing_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingAccountApi->get_billing_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetBillingAccounts200Response**](GetBillingAccounts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

