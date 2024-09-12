# notehub_py.DeviceApi

All URIs are relative to *https://api.notefile.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_device_environment_variable**](DeviceApi.md#delete_device_environment_variable) | **DELETE** /v1/projects/{projectUID}/devices/{deviceUID}/environment_variables/{key} | 
[**delete_project_device**](DeviceApi.md#delete_project_device) | **DELETE** /v1/projects/{projectUID}/devices/{deviceUID} | 
[**disable_device**](DeviceApi.md#disable_device) | **POST** /v1/projects/{projectUID}/devices/{deviceUID}/disable | 
[**disable_device_connectivity_assurance**](DeviceApi.md#disable_device_connectivity_assurance) | **POST** /v1/projects/{projectUID}/devices/{deviceUID}/disable-connectivity-assurance | 
[**enable_device**](DeviceApi.md#enable_device) | **POST** /v1/projects/{projectUID}/devices/{deviceUID}/enable | 
[**enable_device_connectivity_assurance**](DeviceApi.md#enable_device_connectivity_assurance) | **POST** /v1/projects/{projectUID}/devices/{deviceUID}/enable-connectivity-assurance | 
[**get_device**](DeviceApi.md#get_device) | **GET** /v1/projects/{projectUID}/devices/{deviceUID} | 
[**get_device_environment_variables**](DeviceApi.md#get_device_environment_variables) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/environment_variables | 
[**get_device_environment_variables_by_pin**](DeviceApi.md#get_device_environment_variables_by_pin) | **GET** /v1/products/{productUID}/devices/{deviceUID}/environment_variables_with_pin | 
[**get_device_health_log**](DeviceApi.md#get_device_health_log) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/health-log | 
[**get_device_latest**](DeviceApi.md#get_device_latest) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/latest | 
[**get_device_public_key**](DeviceApi.md#get_device_public_key) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/public-key | 
[**get_device_sessions**](DeviceApi.md#get_device_sessions) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/sessions | 
[**get_project_device_public_keys**](DeviceApi.md#get_project_device_public_keys) | **GET** /v1/projects/{projectUID}/devices/public-keys | 
[**get_project_devices**](DeviceApi.md#get_project_devices) | **GET** /v1/projects/{projectUID}/devices | 
[**get_project_fleet_devices**](DeviceApi.md#get_project_fleet_devices) | **GET** /v1/projects/{projectUID}/fleets/{fleetUID}/devices | 
[**handle_note_add**](DeviceApi.md#handle_note_add) | **POST** /v1/projects/{projectUID}/devices/{deviceUID}/notes/{notefileID} | 
[**handle_note_changes**](DeviceApi.md#handle_note_changes) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/notes/{notefileID}/changes | 
[**handle_note_create_add**](DeviceApi.md#handle_note_create_add) | **POST** /v1/projects/{projectUID}/devices/{deviceUID}/notes/{notefileID}/{noteID} | 
[**handle_note_delete**](DeviceApi.md#handle_note_delete) | **DELETE** /v1/projects/{projectUID}/devices/{deviceUID}/notes/{notefileID}/{noteID} | 
[**handle_note_get**](DeviceApi.md#handle_note_get) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/notes/{notefileID}/{noteID} | 
[**handle_note_signal**](DeviceApi.md#handle_note_signal) | **POST** /v1/projects/{projectUID}/devices/{deviceUID}/signal | 
[**handle_note_update**](DeviceApi.md#handle_note_update) | **PUT** /v1/projects/{projectUID}/devices/{deviceUID}/notes/{notefileID}/{noteID} | 
[**handle_notefile_changes**](DeviceApi.md#handle_notefile_changes) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/files/changes | 
[**handle_notefile_changes_pending**](DeviceApi.md#handle_notefile_changes_pending) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/files/changes/pending | 
[**handle_notefile_delete**](DeviceApi.md#handle_notefile_delete) | **DELETE** /v1/projects/{projectUID}/devices/{deviceUID}/files | 
[**post_provision_project_device**](DeviceApi.md#post_provision_project_device) | **POST** /v1/projects/{projectUID}/devices/{deviceUID}/provision | 
[**put_device_environment_variables**](DeviceApi.md#put_device_environment_variables) | **PUT** /v1/projects/{projectUID}/devices/{deviceUID}/environment_variables | 
[**put_device_environment_variables_by_pin**](DeviceApi.md#put_device_environment_variables_by_pin) | **PUT** /v1/products/{productUID}/devices/{deviceUID}/environment_variables_with_pin | 


# **delete_device_environment_variable**
> EnvironmentVariables delete_device_environment_variable(project_uid, device_uid, key)



Delete environment variable of a device

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.environment_variables import EnvironmentVariables
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    key = 'key_example' # str | The environment variable key to delete.

    try:
        api_response = api_instance.delete_device_environment_variable(project_uid, device_uid, key)
        print("The response of DeviceApi->delete_device_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_device_environment_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **key** | **str**| The environment variable key to delete. | 

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from an environment variables request. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_device**
> delete_project_device(project_uid, device_uid, purge)



Delete Device

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    purge = False # bool |  (default to False)

    try:
        api_instance.delete_project_device(project_uid, device_uid, purge)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_project_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **purge** | **bool**|  | [default to False]

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_device**
> disable_device(project_uid, device_uid)



Disable Device

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_instance.disable_device(project_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->disable_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

void (empty response body)

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

# **disable_device_connectivity_assurance**
> disable_device_connectivity_assurance(project_uid, device_uid)



Disable Connectivity Assurance

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_instance.disable_device_connectivity_assurance(project_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->disable_device_connectivity_assurance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

void (empty response body)

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

# **enable_device**
> enable_device(project_uid, device_uid)



Enable Device

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_instance.enable_device(project_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->enable_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

void (empty response body)

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

# **enable_device_connectivity_assurance**
> enable_device_connectivity_assurance(project_uid, device_uid)



Enable Connectivity Assurance

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_instance.enable_device_connectivity_assurance(project_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->enable_device_connectivity_assurance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

void (empty response body)

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

# **get_device**
> Device get_device(project_uid, device_uid)



Get Device

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.device import Device
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_response = api_instance.get_device(project_uid, device_uid)
        print("The response of DeviceApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

[**Device**](Device.md)

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

# **get_device_environment_variables**
> GetDeviceEnvironmentVariables200Response get_device_environment_variables(project_uid, device_uid)



Get environment variables of a device

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_device_environment_variables200_response import GetDeviceEnvironmentVariables200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_response = api_instance.get_device_environment_variables(project_uid, device_uid)
        print("The response of DeviceApi->get_device_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_environment_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

[**GetDeviceEnvironmentVariables200Response**](GetDeviceEnvironmentVariables200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from a get device environment variables request. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_environment_variables_by_pin**
> GetDeviceEnvironmentVariables200Response get_device_environment_variables_by_pin(product_uid, device_uid)



Get environment variables of a device with device pin authorization

### Example

* Api Key Authentication (pin):

```python
import notehub_py
from notehub_py.models.get_device_environment_variables200_response import GetDeviceEnvironmentVariables200Response
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

# Configure API key authorization: pin
configuration.api_key['pin'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['pin'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    product_uid = 'com.blues.bridge:sensors' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_response = api_instance.get_device_environment_variables_by_pin(product_uid, device_uid)
        print("The response of DeviceApi->get_device_environment_variables_by_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_environment_variables_by_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

[**GetDeviceEnvironmentVariables200Response**](GetDeviceEnvironmentVariables200Response.md)

### Authorization

[pin](../README.md#pin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from a get device environment variables request. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_health_log**
> GetDeviceHealthLog200Response get_device_health_log(project_uid, device_uid)



Get Device Health Log

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_device_health_log200_response import GetDeviceHealthLog200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_response = api_instance.get_device_health_log(project_uid, device_uid)
        print("The response of DeviceApi->get_device_health_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_health_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

[**GetDeviceHealthLog200Response**](GetDeviceHealthLog200Response.md)

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

# **get_device_latest**
> GetDeviceLatest200Response get_device_latest(project_uid, device_uid)



Get Device Latest Events

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_device_latest200_response import GetDeviceLatest200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_response = api_instance.get_device_latest(project_uid, device_uid)
        print("The response of DeviceApi->get_device_latest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_latest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

[**GetDeviceLatest200Response**](GetDeviceLatest200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body for a Latest Events request. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_public_key**
> GetDevicePublicKey200Response get_device_public_key(project_uid, device_uid)



Get Device Public Key

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_device_public_key200_response import GetDevicePublicKey200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_response = api_instance.get_device_public_key(project_uid, device_uid)
        print("The response of DeviceApi->get_device_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

[**GetDevicePublicKey200Response**](GetDevicePublicKey200Response.md)

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

# **get_device_sessions**
> GetDeviceSessions200Response get_device_sessions(project_uid, device_uid, page_size=page_size, page_num=page_num)



Get Device Sessions

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_device_sessions200_response import GetDeviceSessions200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)

    try:
        api_response = api_instance.get_device_sessions(project_uid, device_uid, page_size=page_size, page_num=page_num)
        print("The response of DeviceApi->get_device_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 50]
 **page_num** | **int**|  | [optional] [default to 1]

### Return type

[**GetDeviceSessions200Response**](GetDeviceSessions200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body for a session request. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_device_public_keys**
> GetProjectDevicePublicKeys200Response get_project_device_public_keys(project_uid, page_size=page_size, page_num=page_num)



Get Device Public Keys of a Project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_project_device_public_keys200_response import GetProjectDevicePublicKeys200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)

    try:
        api_response = api_instance.get_project_device_public_keys(project_uid, page_size=page_size, page_num=page_num)
        print("The response of DeviceApi->get_project_device_public_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_project_device_public_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 50]
 **page_num** | **int**|  | [optional] [default to 1]

### Return type

[**GetProjectDevicePublicKeys200Response**](GetProjectDevicePublicKeys200Response.md)

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

# **get_project_devices**
> GetProjectDevices200Response get_project_devices(project_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)



Get Devices of a Project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_project_devices200_response import GetProjectDevices200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    tag = ['tag_example'] # List[str] | Tag filter (optional)
    serial_number = ['serial_number_example'] # List[str] | Serial number filter (optional)
    fleet_uid = 'fleet_uid_example' # str |  (optional)
    notecard_firmware = ['notecard_firmware_example'] # List[str] | Firmware version filter (optional)
    location = ['location_example'] # List[str] | Location filter (optional)
    host_firmware = ['host_firmware_example'] # List[str] | Host firmware filter (optional)
    product_uid = ['product_uid_example'] # List[str] |  (optional)
    sku = ['sku_example'] # List[str] | SKU filter (optional)

    try:
        api_response = api_instance.get_project_devices(project_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)
        print("The response of DeviceApi->get_project_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_project_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 50]
 **page_num** | **int**|  | [optional] [default to 1]
 **device_uid** | [**List[str]**](str.md)| A Device UID. | [optional] 
 **tag** | [**List[str]**](str.md)| Tag filter | [optional] 
 **serial_number** | [**List[str]**](str.md)| Serial number filter | [optional] 
 **fleet_uid** | **str**|  | [optional] 
 **notecard_firmware** | [**List[str]**](str.md)| Firmware version filter | [optional] 
 **location** | [**List[str]**](str.md)| Location filter | [optional] 
 **host_firmware** | [**List[str]**](str.md)| Host firmware filter | [optional] 
 **product_uid** | [**List[str]**](str.md)|  | [optional] 
 **sku** | [**List[str]**](str.md)| SKU filter | [optional] 

### Return type

[**GetProjectDevices200Response**](GetProjectDevices200Response.md)

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

# **get_project_fleet_devices**
> GetProjectDevices200Response get_project_fleet_devices(project_uid, fleet_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, tag=tag, serial_number=serial_number, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)



Get Devices of a Fleet within a Project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_project_devices200_response import GetProjectDevices200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    fleet_uid = 'fleet_uid_example' # str | 
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    tag = ['tag_example'] # List[str] | Tag filter (optional)
    serial_number = ['serial_number_example'] # List[str] | Serial number filter (optional)
    notecard_firmware = ['notecard_firmware_example'] # List[str] | Firmware version filter (optional)
    location = ['location_example'] # List[str] | Location filter (optional)
    host_firmware = ['host_firmware_example'] # List[str] | Host firmware filter (optional)
    product_uid = ['product_uid_example'] # List[str] |  (optional)
    sku = ['sku_example'] # List[str] | SKU filter (optional)

    try:
        api_response = api_instance.get_project_fleet_devices(project_uid, fleet_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, tag=tag, serial_number=serial_number, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)
        print("The response of DeviceApi->get_project_fleet_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_project_fleet_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **fleet_uid** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 50]
 **page_num** | **int**|  | [optional] [default to 1]
 **device_uid** | [**List[str]**](str.md)| A Device UID. | [optional] 
 **tag** | [**List[str]**](str.md)| Tag filter | [optional] 
 **serial_number** | [**List[str]**](str.md)| Serial number filter | [optional] 
 **notecard_firmware** | [**List[str]**](str.md)| Firmware version filter | [optional] 
 **location** | [**List[str]**](str.md)| Location filter | [optional] 
 **host_firmware** | [**List[str]**](str.md)| Host firmware filter | [optional] 
 **product_uid** | [**List[str]**](str.md)|  | [optional] 
 **sku** | [**List[str]**](str.md)| SKU filter | [optional] 

### Return type

[**GetProjectDevices200Response**](GetProjectDevices200Response.md)

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

# **handle_note_add**
> handle_note_add(project_uid, device_uid, notefile_id, note)



Adds a Note to a Notefile, creating the Notefile if it doesn't yet exist.

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.note import Note
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    notefile_id = 'notefile_id_example' # str | 
    note = notehub_py.Note() # Note | Body or payload of note to be added to the device

    try:
        api_instance.handle_note_add(project_uid, device_uid, notefile_id, note)
    except Exception as e:
        print("Exception when calling DeviceApi->handle_note_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **notefile_id** | **str**|  | 
 **note** | [**Note**](Note.md)| Body or payload of note to be added to the device | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An empty object means success |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_note_changes**
> HandleNoteChanges200Response handle_note_changes(project_uid, device_uid, notefile_id, tracker=tracker, max=max, start=start, stop=stop, deleted=deleted, delete=delete)



Incrementally retrieve changes within a specific Notefile.

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.handle_note_changes200_response import HandleNoteChanges200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    notefile_id = 'notefile_id_example' # str | 
    tracker = 'tracker_example' # str | The change tracker ID. (optional)
    max = 56 # int | The maximum number of Notes to return in the request. (optional)
    start = True # bool | true to reset the tracker to the beginning. (optional)
    stop = True # bool | true to delete the tracker. (optional)
    deleted = True # bool | true to return deleted notes. (optional)
    delete = True # bool | true to delete the notes returned by the request. (optional)

    try:
        api_response = api_instance.handle_note_changes(project_uid, device_uid, notefile_id, tracker=tracker, max=max, start=start, stop=stop, deleted=deleted, delete=delete)
        print("The response of DeviceApi->handle_note_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->handle_note_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **notefile_id** | **str**|  | 
 **tracker** | **str**| The change tracker ID. | [optional] 
 **max** | **int**| The maximum number of Notes to return in the request. | [optional] 
 **start** | **bool**| true to reset the tracker to the beginning. | [optional] 
 **stop** | **bool**| true to delete the tracker. | [optional] 
 **deleted** | **bool**| true to return deleted notes. | [optional] 
 **delete** | **bool**| true to delete the notes returned by the request. | [optional] 

### Return type

[**HandleNoteChanges200Response**](HandleNoteChanges200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The note changes object |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_note_create_add**
> handle_note_create_add(project_uid, device_uid, notefile_id, note_id, note)



Adds a Note to a Notefile, creating the Notefile if it doesn't yet exist.

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.note import Note
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    notefile_id = 'notefile_id_example' # str | 
    note_id = 'note_id_example' # str | 
    note = notehub_py.Note() # Note | Body or payload of note to be added to the device

    try:
        api_instance.handle_note_create_add(project_uid, device_uid, notefile_id, note_id, note)
    except Exception as e:
        print("Exception when calling DeviceApi->handle_note_create_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **notefile_id** | **str**|  | 
 **note_id** | **str**|  | 
 **note** | [**Note**](Note.md)| Body or payload of note to be added to the device | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An empty object means success |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_note_delete**
> handle_note_delete(project_uid, device_uid, notefile_id, note_id)



Delete a note from a DB notefile

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    notefile_id = 'notefile_id_example' # str | 
    note_id = 'note_id_example' # str | 

    try:
        api_instance.handle_note_delete(project_uid, device_uid, notefile_id, note_id)
    except Exception as e:
        print("Exception when calling DeviceApi->handle_note_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **notefile_id** | **str**|  | 
 **note_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An empty object means success |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_note_get**
> HandleNoteGet200Response handle_note_get(project_uid, device_uid, notefile_id, note_id, delete=delete, deleted=deleted)



Get a note from a DB notefile

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.handle_note_get200_response import HandleNoteGet200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    notefile_id = 'notefile_id_example' # str | 
    note_id = 'note_id_example' # str | 
    delete = True # bool | Whether to delete the note from the DB notefile (optional)
    deleted = True # bool | Whether to return deleted notes (optional)

    try:
        api_response = api_instance.handle_note_get(project_uid, device_uid, notefile_id, note_id, delete=delete, deleted=deleted)
        print("The response of DeviceApi->handle_note_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->handle_note_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **notefile_id** | **str**|  | 
 **note_id** | **str**|  | 
 **delete** | **bool**| Whether to delete the note from the DB notefile | [optional] 
 **deleted** | **bool**| Whether to return deleted notes | [optional] 

### Return type

[**HandleNoteGet200Response**](HandleNoteGet200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested note |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_note_signal**
> HandleNoteSignal200Response handle_note_signal(project_uid, device_uid, body)



Send a signal from Notehub to a Notecard.

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.body import Body
from notehub_py.models.handle_note_signal200_response import HandleNoteSignal200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    body = notehub_py.Body() # Body | Body or payload of singnal to be sent to the device

    try:
        api_response = api_instance.handle_note_signal(project_uid, device_uid, body)
        print("The response of DeviceApi->handle_note_signal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->handle_note_signal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **body** | [**Body**](Body.md)| Body or payload of singnal to be sent to the device | 

### Return type

[**HandleNoteSignal200Response**](HandleNoteSignal200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A status response. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_note_update**
> handle_note_update(project_uid, device_uid, notefile_id, note_id, note)



Update a note in a DB notefile

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.note import Note
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    notefile_id = 'notefile_id_example' # str | 
    note_id = 'note_id_example' # str | 
    note = notehub_py.Note() # Note | Body or payload of note to be added to the device

    try:
        api_instance.handle_note_update(project_uid, device_uid, notefile_id, note_id, note)
    except Exception as e:
        print("Exception when calling DeviceApi->handle_note_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **notefile_id** | **str**|  | 
 **note_id** | **str**|  | 
 **note** | [**Note**](Note.md)| Body or payload of note to be added to the device | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An empty object means success |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_notefile_changes**
> HandleNotefileChanges200Response handle_notefile_changes(project_uid, device_uid, tracker=tracker, files=files)



Used to perform queries on a single or multiple files to determine if new Notes are available to read

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.handle_notefile_changes200_response import HandleNotefileChanges200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    tracker = 'tracker_example' # str | The change tracker ID. (optional)
    files = ['files_example'] # List[str] | One or more files to obtain change information from. (optional)

    try:
        api_response = api_instance.handle_notefile_changes(project_uid, device_uid, tracker=tracker, files=files)
        print("The response of DeviceApi->handle_notefile_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->handle_notefile_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **tracker** | **str**| The change tracker ID. | [optional] 
 **files** | [**List[str]**](str.md)| One or more files to obtain change information from. | [optional] 

### Return type

[**HandleNotefileChanges200Response**](HandleNotefileChanges200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notefile changes object |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_notefile_changes_pending**
> HandleNotefileChangesPending200Response handle_notefile_changes_pending(project_uid, device_uid)



Returns info about file changes that are pending upload to Notehub or download to the Notecard.

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.handle_notefile_changes_pending200_response import HandleNotefileChangesPending200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_response = api_instance.handle_notefile_changes_pending(project_uid, device_uid)
        print("The response of DeviceApi->handle_notefile_changes_pending:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->handle_notefile_changes_pending: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

[**HandleNotefileChangesPending200Response**](HandleNotefileChangesPending200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notefile pending changes object |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_notefile_delete**
> handle_notefile_delete(project_uid, device_uid, handle_notefile_delete_request)



Deletes Notefiles and the Notes they contain.

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.handle_notefile_delete_request import HandleNotefileDeleteRequest
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    handle_notefile_delete_request = notehub_py.HandleNotefileDeleteRequest() # HandleNotefileDeleteRequest | 

    try:
        api_instance.handle_notefile_delete(project_uid, device_uid, handle_notefile_delete_request)
    except Exception as e:
        print("Exception when calling DeviceApi->handle_notefile_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **handle_notefile_delete_request** | [**HandleNotefileDeleteRequest**](HandleNotefileDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An empty object means success |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_provision_project_device**
> object post_provision_project_device(project_uid, device_uid, post_provision_project_device_request)



Provision Device for a Project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.post_provision_project_device_request import PostProvisionProjectDeviceRequest
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    post_provision_project_device_request = notehub_py.PostProvisionProjectDeviceRequest() # PostProvisionProjectDeviceRequest | Provision a device to a specific ProductUID

    try:
        api_response = api_instance.post_provision_project_device(project_uid, device_uid, post_provision_project_device_request)
        print("The response of DeviceApi->post_provision_project_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->post_provision_project_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **post_provision_project_device_request** | [**PostProvisionProjectDeviceRequest**](PostProvisionProjectDeviceRequest.md)| Provision a device to a specific ProductUID | 

### Return type

**object**

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

# **put_device_environment_variables**
> EnvironmentVariables put_device_environment_variables(project_uid, device_uid, environment_variables)



Put environment variables of a device

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.environment_variables import EnvironmentVariables
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    environment_variables = notehub_py.EnvironmentVariables() # EnvironmentVariables | Environment variables to be added to the device

    try:
        api_response = api_instance.put_device_environment_variables(project_uid, device_uid, environment_variables)
        print("The response of DeviceApi->put_device_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->put_device_environment_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **environment_variables** | [**EnvironmentVariables**](EnvironmentVariables.md)| Environment variables to be added to the device | 

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from an environment variables request. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_device_environment_variables_by_pin**
> EnvironmentVariables put_device_environment_variables_by_pin(product_uid, device_uid, environment_variables)



Put environment variables of a device with device pin authorization

### Example

* Api Key Authentication (pin):

```python
import notehub_py
from notehub_py.models.environment_variables import EnvironmentVariables
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

# Configure API key authorization: pin
configuration.api_key['pin'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['pin'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    product_uid = 'com.blues.bridge:sensors' # str | 
    device_uid = 'dev:000000000000000' # str | 
    environment_variables = notehub_py.EnvironmentVariables() # EnvironmentVariables | Environment variables to be added to the device

    try:
        api_response = api_instance.put_device_environment_variables_by_pin(product_uid, device_uid, environment_variables)
        print("The response of DeviceApi->put_device_environment_variables_by_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->put_device_environment_variables_by_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **environment_variables** | [**EnvironmentVariables**](EnvironmentVariables.md)| Environment variables to be added to the device | 

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[pin](../README.md#pin)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from an environment variables request. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

