# notehub_py.MonitorApi

All URIs are relative to *https://api.notefile.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_monitor**](MonitorApi.md#create_monitor) | **POST** /v1/projects/{projectUID}/monitors | 
[**delete_monitor**](MonitorApi.md#delete_monitor) | **DELETE** /v1/projects/{projectUID}/monitors/{monitorUID} | 
[**get_monitor**](MonitorApi.md#get_monitor) | **GET** /v1/projects/{projectUID}/monitors/{monitorUID} | 
[**get_monitors**](MonitorApi.md#get_monitors) | **GET** /v1/projects/{projectUID}/monitors | 
[**update_monitor**](MonitorApi.md#update_monitor) | **PUT** /v1/projects/{projectUID}/monitors/{monitorUID} | 


# **create_monitor**
> Monitor create_monitor(project_uid, create_monitor)



Create a new Monitor

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.create_monitor import CreateMonitor
from notehub_py.models.monitor import Monitor
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
    api_instance = notehub_py.MonitorApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    create_monitor = notehub_py.CreateMonitor() # CreateMonitor | Body or payload of monitor to be created

    try:
        api_response = api_instance.create_monitor(project_uid, create_monitor)
        print("The response of MonitorApi->create_monitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->create_monitor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **create_monitor** | [**CreateMonitor**](CreateMonitor.md)| Body or payload of monitor to be created | 

### Return type

[**Monitor**](Monitor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_monitor**
> Monitor delete_monitor(project_uid, monitor_uid)



Delete Monitor

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.monitor import Monitor
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
    api_instance = notehub_py.MonitorApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    monitor_uid = 'monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad' # str | 

    try:
        api_response = api_instance.delete_monitor(project_uid, monitor_uid)
        print("The response of MonitorApi->delete_monitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->delete_monitor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **monitor_uid** | **str**|  | 

### Return type

[**Monitor**](Monitor.md)

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

# **get_monitor**
> Monitor get_monitor(project_uid, monitor_uid)



Get Monitor

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.monitor import Monitor
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
    api_instance = notehub_py.MonitorApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    monitor_uid = 'monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad' # str | 

    try:
        api_response = api_instance.get_monitor(project_uid, monitor_uid)
        print("The response of MonitorApi->get_monitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->get_monitor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **monitor_uid** | **str**|  | 

### Return type

[**Monitor**](Monitor.md)

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

# **get_monitors**
> List[Monitor] get_monitors(project_uid)



Get list of defined Monitors

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.monitor import Monitor
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
    api_instance = notehub_py.MonitorApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 

    try:
        api_response = api_instance.get_monitors(project_uid)
        print("The response of MonitorApi->get_monitors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->get_monitors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**List[Monitor]**](Monitor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from GET /monitors |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_monitor**
> Monitor update_monitor(project_uid, monitor_uid, monitor)



Update Monitor

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.monitor import Monitor
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
    api_instance = notehub_py.MonitorApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    monitor_uid = 'monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad' # str | 
    monitor = notehub_py.Monitor() # Monitor | Body or payload of monitor to be created

    try:
        api_response = api_instance.update_monitor(project_uid, monitor_uid, monitor)
        print("The response of MonitorApi->update_monitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->update_monitor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **monitor_uid** | **str**|  | 
 **monitor** | [**Monitor**](Monitor.md)| Body or payload of monitor to be created | 

### Return type

[**Monitor**](Monitor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

