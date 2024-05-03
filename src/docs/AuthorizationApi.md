# notehub_py.AuthorizationApi

All URIs are relative to *https://api.notefile.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthorizationApi.md#login) | **POST** /auth/login | 


# **login**
> Login200Response login(login_request)



Gets a session token from the API from a username and password.

### Example


```python
import notehub_py
from notehub_py.models.login200_response import Login200Response
from notehub_py.models.login_request import LoginRequest
from notehub_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.notefile.net
# See configuration.py for a list of all supported configuration parameters.
configuration = notehub_py.Configuration(
    host = "https://api.notefile.net"
)


# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.AuthorizationApi(api_client)
    login_request = {"username":"name@example.com","password":"test-password"} # LoginRequest | 

    try:
        api_response = api_instance.login(login_request)
        print("The response of AuthorizationApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**Login200Response**](Login200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

