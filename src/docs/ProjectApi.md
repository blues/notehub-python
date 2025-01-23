# notehub_py.ProjectApi

All URIs are relative to *https://api.notefile.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_project**](ProjectApi.md#clone_project) | **POST** /v1/projects/{projectUID}/clone | 
[**create_fleet**](ProjectApi.md#create_fleet) | **POST** /v1/projects/{projectUID}/fleets | 
[**create_product**](ProjectApi.md#create_product) | **POST** /v1/projects/{projectUID}/products | 
[**create_project**](ProjectApi.md#create_project) | **POST** /v1/projects | 
[**delete_device_fleets**](ProjectApi.md#delete_device_fleets) | **DELETE** /v1/projects/{projectUID}/devices/{deviceUID}/fleets | 
[**delete_fleet**](ProjectApi.md#delete_fleet) | **DELETE** /v1/projects/{projectUID}/fleets/{fleetUID} | 
[**delete_fleet_environment_variable**](ProjectApi.md#delete_fleet_environment_variable) | **DELETE** /v1/projects/{projectUID}/fleets/{fleetUID}/environment_variables/{key} | 
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /v1/projects/{projectUID} | 
[**delete_project_environment_variable**](ProjectApi.md#delete_project_environment_variable) | **DELETE** /v1/projects/{projectUID}/environment_variables/{key} | 
[**dfu_action**](ProjectApi.md#dfu_action) | **POST** /v1/projects/{projectUID}/dfu/{firmwareType}/{action} | 
[**disable_global_transformation**](ProjectApi.md#disable_global_transformation) | **POST** /v1/projects/{projectUID}/global-transformation/disable | 
[**enable_global_transformation**](ProjectApi.md#enable_global_transformation) | **POST** /v1/projects/{projectUID}/global-transformation/enable | 
[**get_device_dfu_history**](ProjectApi.md#get_device_dfu_history) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/dfu/{firmwareType}/history | 
[**get_device_dfu_status**](ProjectApi.md#get_device_dfu_status) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/dfu/{firmwareType}/status | 
[**get_device_fleets**](ProjectApi.md#get_device_fleets) | **GET** /v1/projects/{projectUID}/devices/{deviceUID}/fleets | 
[**get_devices_dfu_history**](ProjectApi.md#get_devices_dfu_history) | **GET** /v1/projects/{projectUID}/dfu/{firmwareType}/history | 
[**get_devices_dfu_status**](ProjectApi.md#get_devices_dfu_status) | **GET** /v1/projects/{projectUID}/dfu/{firmwareType}/status | 
[**get_firmware_info**](ProjectApi.md#get_firmware_info) | **GET** /v1/projects/{projectUID}/firmware | 
[**get_fleet**](ProjectApi.md#get_fleet) | **GET** /v1/projects/{projectUID}/fleets/{fleetUID} | 
[**get_fleet_environment_variables**](ProjectApi.md#get_fleet_environment_variables) | **GET** /v1/projects/{projectUID}/fleets/{fleetUID}/environment_variables | 
[**get_project**](ProjectApi.md#get_project) | **GET** /v1/projects/{projectUID} | 
[**get_project_by_product**](ProjectApi.md#get_project_by_product) | **GET** /v1/products/{productUID}/project | 
[**get_project_environment_variables**](ProjectApi.md#get_project_environment_variables) | **GET** /v1/projects/{projectUID}/environment_variables | 
[**get_project_fleets**](ProjectApi.md#get_project_fleets) | **GET** /v1/projects/{projectUID}/fleets | 
[**get_project_members**](ProjectApi.md#get_project_members) | **GET** /v1/projects/{projectUID}/members | 
[**get_project_products**](ProjectApi.md#get_project_products) | **GET** /v1/projects/{projectUID}/products | 
[**get_projects**](ProjectApi.md#get_projects) | **GET** /v1/projects | 
[**put_device_fleets**](ProjectApi.md#put_device_fleets) | **PUT** /v1/projects/{projectUID}/devices/{deviceUID}/fleets | 
[**put_fleet_environment_variables**](ProjectApi.md#put_fleet_environment_variables) | **PUT** /v1/projects/{projectUID}/fleets/{fleetUID}/environment_variables | 
[**put_project_environment_variables**](ProjectApi.md#put_project_environment_variables) | **PUT** /v1/projects/{projectUID}/environment_variables | 
[**set_global_transformation**](ProjectApi.md#set_global_transformation) | **POST** /v1/projects/{projectUID}/global-transformation | 
[**update_fleet**](ProjectApi.md#update_fleet) | **PUT** /v1/projects/{projectUID}/fleets/{fleetUID} | 


# **clone_project**
> Project clone_project(project_uid, clone_project_request)



Clone a Project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.clone_project_request import CloneProjectRequest
from notehub_py.models.project import Project
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'project_uid_example' # str | The project UID to be cloned.
    clone_project_request = notehub_py.CloneProjectRequest() # CloneProjectRequest | Project to be cloned

    try:
        api_response = api_instance.clone_project(project_uid, clone_project_request)
        print("The response of ProjectApi->clone_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->clone_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**| The project UID to be cloned. | 
 **clone_project_request** | [**CloneProjectRequest**](CloneProjectRequest.md)| Project to be cloned | 

### Return type

[**Project**](Project.md)

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

# **create_fleet**
> Fleet create_fleet(project_uid, create_fleet_request)



Create Fleet

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.create_fleet_request import CreateFleetRequest
from notehub_py.models.fleet import Fleet
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    create_fleet_request = notehub_py.CreateFleetRequest() # CreateFleetRequest | Fleet to be added

    try:
        api_response = api_instance.create_fleet(project_uid, create_fleet_request)
        print("The response of ProjectApi->create_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **create_fleet_request** | [**CreateFleetRequest**](CreateFleetRequest.md)| Fleet to be added | 

### Return type

[**Fleet**](Fleet.md)

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

# **create_product**
> Product create_product(project_uid, create_product_request)



Create Product within a Project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.create_product_request import CreateProductRequest
from notehub_py.models.product import Product
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    create_product_request = notehub_py.CreateProductRequest() # CreateProductRequest | Product to be created

    try:
        api_response = api_instance.create_product(project_uid, create_product_request)
        print("The response of ProjectApi->create_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **create_product_request** | [**CreateProductRequest**](CreateProductRequest.md)| Product to be created | 

### Return type

[**Product**](Product.md)

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

# **create_project**
> Project create_project(create_project_request)



Create a Project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.create_project_request import CreateProjectRequest
from notehub_py.models.project import Project
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
    api_instance = notehub_py.ProjectApi(api_client)
    create_project_request = notehub_py.CreateProjectRequest() # CreateProjectRequest | Project to be created

    try:
        api_response = api_instance.create_project(create_project_request)
        print("The response of ProjectApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md)| Project to be created | 

### Return type

[**Project**](Project.md)

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

# **delete_device_fleets**
> GetProjectFleets200Response delete_device_fleets(project_uid, device_uid, delete_device_fleets_request)



Remove Device from Fleets

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.delete_device_fleets_request import DeleteDeviceFleetsRequest
from notehub_py.models.get_project_fleets200_response import GetProjectFleets200Response
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    delete_device_fleets_request = notehub_py.DeleteDeviceFleetsRequest() # DeleteDeviceFleetsRequest | The fleets to remove from the device. Note that the endpoint takes an array of fleetUIDs, to facilitate multi-fleet devices. Multi-fleet is not yet enabled on all SaaS plans - unless it is supported by the SaaS plan of the project, passing more than a single fleetUID in the array is an error. 

    try:
        api_response = api_instance.delete_device_fleets(project_uid, device_uid, delete_device_fleets_request)
        print("The response of ProjectApi->delete_device_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_device_fleets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **delete_device_fleets_request** | [**DeleteDeviceFleetsRequest**](DeleteDeviceFleetsRequest.md)| The fleets to remove from the device. Note that the endpoint takes an array of fleetUIDs, to facilitate multi-fleet devices. Multi-fleet is not yet enabled on all SaaS plans - unless it is supported by the SaaS plan of the project, passing more than a single fleetUID in the array is an error.  | 

### Return type

[**GetProjectFleets200Response**](GetProjectFleets200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from a fleets endpoint. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fleet**
> delete_fleet(project_uid, fleet_uid)



Delete Fleet

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    fleet_uid = 'fleet_uid_example' # str | 

    try:
        api_instance.delete_fleet(project_uid, fleet_uid)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **fleet_uid** | **str**|  | 

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

# **delete_fleet_environment_variable**
> EnvironmentVariables delete_fleet_environment_variable(project_uid, fleet_uid, key)



Delete environment variables of a fleet

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    fleet_uid = 'fleet_uid_example' # str | 
    key = 'key_example' # str | The environment variable key to delete.

    try:
        api_response = api_instance.delete_fleet_environment_variable(project_uid, fleet_uid, key)
        print("The response of ProjectApi->delete_fleet_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_fleet_environment_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **fleet_uid** | **str**|  | 
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

# **delete_project**
> delete_project(project_uid)



Delete a Project by ProjectUID

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 

    try:
        api_instance.delete_project(project_uid)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

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

# **delete_project_environment_variable**
> EnvironmentVariables delete_project_environment_variable(project_uid, key)



Delete an environment variable of a project by key

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    key = 'key_example' # str | The environment variable key to delete.

    try:
        api_response = api_instance.delete_project_environment_variable(project_uid, key)
        print("The response of ProjectApi->delete_project_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_project_environment_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
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

# **dfu_action**
> dfu_action(project_uid, firmware_type, action, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku, dfu_action_request=dfu_action_request)



Update/cancel host or notecard firmware updates

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.dfu_action_request import DfuActionRequest
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    firmware_type = 'firmware_type_example' # str | 
    action = 'action_example' # str | 
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    tag = ['tag_example'] # List[str] | Tag filter (optional)
    serial_number = ['serial_number_example'] # List[str] | Serial number filter (optional)
    fleet_uid = 'fleet_uid_example' # str |  (optional)
    notecard_firmware = ['notecard_firmware_example'] # List[str] | Firmware version filter (optional)
    location = ['location_example'] # List[str] | Location filter (optional)
    host_firmware = ['host_firmware_example'] # List[str] | Host firmware filter (optional)
    product_uid = ['product_uid_example'] # List[str] |  (optional)
    sku = ['sku_example'] # List[str] | SKU filter (optional)
    dfu_action_request = notehub_py.DfuActionRequest() # DfuActionRequest | Which firmware in the case of an update action (optional)

    try:
        api_instance.dfu_action(project_uid, firmware_type, action, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku, dfu_action_request=dfu_action_request)
    except Exception as e:
        print("Exception when calling ProjectApi->dfu_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **firmware_type** | **str**|  | 
 **action** | **str**|  | 
 **device_uid** | [**List[str]**](str.md)| A Device UID. | [optional] 
 **tag** | [**List[str]**](str.md)| Tag filter | [optional] 
 **serial_number** | [**List[str]**](str.md)| Serial number filter | [optional] 
 **fleet_uid** | **str**|  | [optional] 
 **notecard_firmware** | [**List[str]**](str.md)| Firmware version filter | [optional] 
 **location** | [**List[str]**](str.md)| Location filter | [optional] 
 **host_firmware** | [**List[str]**](str.md)| Host firmware filter | [optional] 
 **product_uid** | [**List[str]**](str.md)|  | [optional] 
 **sku** | [**List[str]**](str.md)| SKU filter | [optional] 
 **dfu_action_request** | [**DfuActionRequest**](DfuActionRequest.md)| Which firmware in the case of an update action | [optional] 

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
**200** | Success |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_global_transformation**
> disable_global_transformation(project_uid)



Disable the project-level event JSONata transformation

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 

    try:
        api_instance.disable_global_transformation(project_uid)
    except Exception as e:
        print("Exception when calling ProjectApi->disable_global_transformation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

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

# **enable_global_transformation**
> enable_global_transformation(project_uid)



Enable the project-level event JSONata transformation

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 

    try:
        api_instance.enable_global_transformation(project_uid)
    except Exception as e:
        print("Exception when calling ProjectApi->enable_global_transformation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

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

# **get_device_dfu_history**
> DeviceDfuHistory get_device_dfu_history(project_uid, device_uid, firmware_type)



Get device DFU history for host or Notecard firmware

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.device_dfu_history import DeviceDfuHistory
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    firmware_type = 'firmware_type_example' # str | 

    try:
        api_response = api_instance.get_device_dfu_history(project_uid, device_uid, firmware_type)
        print("The response of ProjectApi->get_device_dfu_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_device_dfu_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **firmware_type** | **str**|  | 

### Return type

[**DeviceDfuHistory**](DeviceDfuHistory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_dfu_status**
> DeviceDfuStatus get_device_dfu_status(project_uid, device_uid, firmware_type)



Get device DFU history for host or Notecard firmware

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.device_dfu_status import DeviceDfuStatus
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    firmware_type = 'firmware_type_example' # str | 

    try:
        api_response = api_instance.get_device_dfu_status(project_uid, device_uid, firmware_type)
        print("The response of ProjectApi->get_device_dfu_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_device_dfu_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **firmware_type** | **str**|  | 

### Return type

[**DeviceDfuStatus**](DeviceDfuStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_fleets**
> GetProjectFleets200Response get_device_fleets(project_uid, device_uid)



Get Device Fleets

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_project_fleets200_response import GetProjectFleets200Response
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 

    try:
        api_response = api_instance.get_device_fleets(project_uid, device_uid)
        print("The response of ProjectApi->get_device_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_device_fleets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 

### Return type

[**GetProjectFleets200Response**](GetProjectFleets200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from a fleets endpoint. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_dfu_history**
> DeviceDfuHistoryPage get_devices_dfu_history(project_uid, firmware_type, page_size=page_size, page_num=page_num, sort_by=sort_by, sort_order=sort_order, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)



Get host or Notecard DFU history for all devices that match the filter criteria

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.device_dfu_history_page import DeviceDfuHistoryPage
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    firmware_type = 'firmware_type_example' # str | 
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    sort_by = 'captured' # str |  (optional) (default to 'captured')
    sort_order = 'asc' # str |  (optional) (default to 'asc')
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
        api_response = api_instance.get_devices_dfu_history(project_uid, firmware_type, page_size=page_size, page_num=page_num, sort_by=sort_by, sort_order=sort_order, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)
        print("The response of ProjectApi->get_devices_dfu_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_devices_dfu_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **firmware_type** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 50]
 **page_num** | **int**|  | [optional] [default to 1]
 **sort_by** | **str**|  | [optional] [default to &#39;captured&#39;]
 **sort_order** | **str**|  | [optional] [default to &#39;asc&#39;]
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

[**DeviceDfuHistoryPage**](DeviceDfuHistoryPage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_dfu_status**
> DeviceDfuStatusPage get_devices_dfu_status(project_uid, firmware_type, page_size=page_size, page_num=page_num, sort_by=sort_by, sort_order=sort_order, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)



Get host or Notecard DFU history for all devices that match the filter criteria

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.device_dfu_status_page import DeviceDfuStatusPage
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    firmware_type = 'firmware_type_example' # str | 
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    sort_by = 'captured' # str |  (optional) (default to 'captured')
    sort_order = 'asc' # str |  (optional) (default to 'asc')
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
        api_response = api_instance.get_devices_dfu_status(project_uid, firmware_type, page_size=page_size, page_num=page_num, sort_by=sort_by, sort_order=sort_order, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)
        print("The response of ProjectApi->get_devices_dfu_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_devices_dfu_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **firmware_type** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 50]
 **page_num** | **int**|  | [optional] [default to 1]
 **sort_by** | **str**|  | [optional] [default to &#39;captured&#39;]
 **sort_order** | **str**|  | [optional] [default to &#39;asc&#39;]
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

[**DeviceDfuStatusPage**](DeviceDfuStatusPage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firmware_info**
> List[FirmwareInfo] get_firmware_info(project_uid, product=product, firmware_type=firmware_type, version=version, target=target, filename=filename, md5=md5, unpublished=unpublished)



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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    product = 'product_example' # str |  (optional)
    firmware_type = 'firmware_type_example' # str |  (optional)
    version = 'version_example' # str |  (optional)
    target = 'target_example' # str |  (optional)
    filename = 'notecard-7.2.2.16518$20240410043100.bin' # str |  (optional)
    md5 = 'md5_example' # str |  (optional)
    unpublished = True # bool |  (optional)

    try:
        api_response = api_instance.get_firmware_info(project_uid, product=product, firmware_type=firmware_type, version=version, target=target, filename=filename, md5=md5, unpublished=unpublished)
        print("The response of ProjectApi->get_firmware_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_firmware_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **product** | **str**|  | [optional] 
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
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet**
> Fleet get_fleet(project_uid, fleet_uid)



Get Fleet

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.fleet import Fleet
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    fleet_uid = 'fleet_uid_example' # str | 

    try:
        api_response = api_instance.get_fleet(project_uid, fleet_uid)
        print("The response of ProjectApi->get_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **fleet_uid** | **str**|  | 

### Return type

[**Fleet**](Fleet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_environment_variables**
> EnvironmentVariables get_fleet_environment_variables(project_uid, fleet_uid)



Get environment variables of a fleet

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    fleet_uid = 'fleet_uid_example' # str | 

    try:
        api_response = api_instance.get_fleet_environment_variables(project_uid, fleet_uid)
        print("The response of ProjectApi->get_fleet_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_fleet_environment_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **fleet_uid** | **str**|  | 

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

# **get_project**
> Project get_project(project_uid)



Get a Project by ProjectUID

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.project import Project
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 

    try:
        api_response = api_instance.get_project(project_uid)
        print("The response of ProjectApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**Project**](Project.md)

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

# **get_project_by_product**
> Project get_project_by_product(product_uid)



Get a Project by ProductUID

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.project import Project
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
    api_instance = notehub_py.ProjectApi(api_client)
    product_uid = 'com.blues.airnote' # str | 

    try:
        api_response = api_instance.get_project_by_product(product_uid)
        print("The response of ProjectApi->get_project_by_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_by_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_uid** | **str**|  | 

### Return type

[**Project**](Project.md)

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

# **get_project_environment_variables**
> EnvironmentVariables get_project_environment_variables(project_uid)



Get environment variables of a project

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 

    try:
        api_response = api_instance.get_project_environment_variables(project_uid)
        print("The response of ProjectApi->get_project_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_environment_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

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

# **get_project_fleets**
> GetProjectFleets200Response get_project_fleets(project_uid)



Get Project Fleets

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_project_fleets200_response import GetProjectFleets200Response
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 

    try:
        api_response = api_instance.get_project_fleets(project_uid)
        print("The response of ProjectApi->get_project_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_fleets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**GetProjectFleets200Response**](GetProjectFleets200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from a fleets endpoint. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_members**
> GetProjectMembers200Response get_project_members(project_uid)



Get Project Members

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_project_members200_response import GetProjectMembers200Response
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 

    try:
        api_response = api_instance.get_project_members(project_uid)
        print("The response of ProjectApi->get_project_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**GetProjectMembers200Response**](GetProjectMembers200Response.md)

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

# **get_project_products**
> GetProjectProducts200Response get_project_products(project_uid)



Get Products within a Project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_project_products200_response import GetProjectProducts200Response
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 

    try:
        api_response = api_instance.get_project_products(project_uid)
        print("The response of ProjectApi->get_project_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**GetProjectProducts200Response**](GetProjectProducts200Response.md)

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

# **get_projects**
> GetProjects200Response get_projects()



Get Projects accessible by the api_key

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_projects200_response import GetProjects200Response
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
    api_instance = notehub_py.ProjectApi(api_client)

    try:
        api_response = api_instance.get_projects()
        print("The response of ProjectApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_projects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetProjects200Response**](GetProjects200Response.md)

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

# **put_device_fleets**
> GetProjectFleets200Response put_device_fleets(project_uid, device_uid, put_device_fleets_request)



Add Device to Fleets

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_project_fleets200_response import GetProjectFleets200Response
from notehub_py.models.put_device_fleets_request import PutDeviceFleetsRequest
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    device_uid = 'dev:000000000000000' # str | 
    put_device_fleets_request = notehub_py.PutDeviceFleetsRequest() # PutDeviceFleetsRequest | The fleets to add to the device. Note that the endpoint takes an array of fleetUIDs, to facilitate multi-fleet devices. Multi-fleet is not yet enabled on all SaaS plans - unless it is supported by the SaaS plan of the project, passing more than a single fleetUID in the array is an error. 

    try:
        api_response = api_instance.put_device_fleets(project_uid, device_uid, put_device_fleets_request)
        print("The response of ProjectApi->put_device_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->put_device_fleets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **device_uid** | **str**|  | 
 **put_device_fleets_request** | [**PutDeviceFleetsRequest**](PutDeviceFleetsRequest.md)| The fleets to add to the device. Note that the endpoint takes an array of fleetUIDs, to facilitate multi-fleet devices. Multi-fleet is not yet enabled on all SaaS plans - unless it is supported by the SaaS plan of the project, passing more than a single fleetUID in the array is an error.  | 

### Return type

[**GetProjectFleets200Response**](GetProjectFleets200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body from a fleets endpoint. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fleet_environment_variables**
> EnvironmentVariables put_fleet_environment_variables(project_uid, fleet_uid, environment_variables)



Put environment variables of a fleet

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    fleet_uid = 'fleet_uid_example' # str | 
    environment_variables = notehub_py.EnvironmentVariables() # EnvironmentVariables | Environment variables to be added to the fleet

    try:
        api_response = api_instance.put_fleet_environment_variables(project_uid, fleet_uid, environment_variables)
        print("The response of ProjectApi->put_fleet_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->put_fleet_environment_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **fleet_uid** | **str**|  | 
 **environment_variables** | [**EnvironmentVariables**](EnvironmentVariables.md)| Environment variables to be added to the fleet | 

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

# **put_project_environment_variables**
> EnvironmentVariables put_project_environment_variables(project_uid, environment_variables=environment_variables)



Put environment variables of a project

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    environment_variables = notehub_py.EnvironmentVariables() # EnvironmentVariables |  (optional)

    try:
        api_response = api_instance.put_project_environment_variables(project_uid, environment_variables=environment_variables)
        print("The response of ProjectApi->put_project_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->put_project_environment_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **environment_variables** | [**EnvironmentVariables**](EnvironmentVariables.md)|  | [optional] 

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

# **set_global_transformation**
> set_global_transformation(project_uid, body)



Set the project-level event JSONata transformation

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    body = None # object | JSONata expression which will be applied to each event before it is persisted and routed

    try:
        api_instance.set_global_transformation(project_uid, body)
    except Exception as e:
        print("Exception when calling ProjectApi->set_global_transformation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | **object**| JSONata expression which will be applied to each event before it is persisted and routed | 

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
**200** | Successful operation |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fleet**
> Fleet update_fleet(project_uid, fleet_uid, update_fleet_request)



Update Fleet

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.fleet import Fleet
from notehub_py.models.update_fleet_request import UpdateFleetRequest
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
    api_instance = notehub_py.ProjectApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    fleet_uid = 'fleet_uid_example' # str | 
    update_fleet_request = notehub_py.UpdateFleetRequest() # UpdateFleetRequest | Fleet details to update

    try:
        api_response = api_instance.update_fleet(project_uid, fleet_uid, update_fleet_request)
        print("The response of ProjectApi->update_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **fleet_uid** | **str**|  | 
 **update_fleet_request** | [**UpdateFleetRequest**](UpdateFleetRequest.md)| Fleet details to update | 

### Return type

[**Fleet**](Fleet.md)

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

