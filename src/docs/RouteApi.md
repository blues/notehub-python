# notehub_py.RouteApi

All URIs are relative to *https://api.notefile.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_route**](RouteApi.md#create_route) | **POST** /v1/projects/{projectUID}/routes | 
[**delete_route**](RouteApi.md#delete_route) | **DELETE** /v1/projects/{projectUID}/routes/{routeUID} | 
[**get_route**](RouteApi.md#get_route) | **GET** /v1/projects/{projectUID}/routes/{routeUID} | 
[**get_route_logs_by_route**](RouteApi.md#get_route_logs_by_route) | **GET** /v1/projects/{projectUID}/routes/{routeUID}/route-logs | 
[**get_routes**](RouteApi.md#get_routes) | **GET** /v1/projects/{projectUID}/routes | 
[**update_route**](RouteApi.md#update_route) | **PUT** /v1/projects/{projectUID}/routes/{routeUID} | 


# **create_route**
> Route create_route(project_uid, route)



Create Route within a Project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.route import Route
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
    api_instance = notehub_py.RouteApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    route = {
  "label": "Route Label",
  "type":"http",
  "http": {
    "fleets": ["fleet:1042ddc5-3b2c-4cec-b1fb-d3040538094d"],
    "throttle_ms": 100,
    "url": "http://route.url"
  }
}
 # Route | Route to be Created

    try:
        api_response = api_instance.create_route(project_uid, route)
        print("The response of RouteApi->create_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->create_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **route** | [**Route**](Route.md)| Route to be Created | 

### Return type

[**Route**](Route.md)

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

# **delete_route**
> object delete_route(project_uid, route_uid)



Delete single route within a project

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
    api_instance = notehub_py.RouteApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str | 

    try:
        api_response = api_instance.delete_route(project_uid, route_uid)
        print("The response of RouteApi->delete_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->delete_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **route_uid** | **str**|  | 

### Return type

**object**

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

# **get_route**
> Route get_route(project_uid, route_uid)



Get single route within a project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.route import Route
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
    api_instance = notehub_py.RouteApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str | 

    try:
        api_response = api_instance.get_route(project_uid, route_uid)
        print("The response of RouteApi->get_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **route_uid** | **str**|  | 

### Return type

[**Route**](Route.md)

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

# **get_route_logs_by_route**
> List[GetRouteLogsByRoute200ResponseInner] get_route_logs_by_route(project_uid, route_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, system_files_only=system_files_only, files=files)



Get Route Logs by Route UID

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_route_logs_by_route200_response_inner import GetRouteLogsByRoute200ResponseInner
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
    api_instance = notehub_py.RouteApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str | 
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    sort_by = 'captured' # str |  (optional) (default to 'captured')
    sort_order = 'asc' # str |  (optional) (default to 'asc')
    start_date = 1628631763 # int | Unix timestamp (optional)
    end_date = 1657894210 # int | Unix timestamp (optional)
    system_files_only = True # bool |  (optional)
    files = '_health.qo, data.qo' # str |  (optional)

    try:
        api_response = api_instance.get_route_logs_by_route(project_uid, route_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, system_files_only=system_files_only, files=files)
        print("The response of RouteApi->get_route_logs_by_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_route_logs_by_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **route_uid** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 50]
 **page_num** | **int**|  | [optional] [default to 1]
 **device_uid** | [**List[str]**](str.md)| A Device UID. | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;captured&#39;]
 **sort_order** | **str**|  | [optional] [default to &#39;asc&#39;]
 **start_date** | **int**| Unix timestamp | [optional] 
 **end_date** | **int**| Unix timestamp | [optional] 
 **system_files_only** | **bool**|  | [optional] 
 **files** | **str**|  | [optional] 

### Return type

[**List[GetRouteLogsByRoute200ResponseInner]**](GetRouteLogsByRoute200ResponseInner.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body for a Route Logs request. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routes**
> List[UserDbRoute] get_routes(project_uid)



Get all Routes within a Project

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.user_db_route import UserDbRoute
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
    api_instance = notehub_py.RouteApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 

    try:
        api_response = api_instance.get_routes(project_uid)
        print("The response of RouteApi->get_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_routes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**List[UserDbRoute]**](UserDbRoute.md)

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

# **update_route**
> Route update_route(project_uid, route_uid, route)



Update route by UID

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.route import Route
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
    api_instance = notehub_py.RouteApi(api_client)
    project_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str | 
    route = {
  "http" {
    "filter": {
      "type": "include",
      "system_notefiles": true,
      "files": ["somefile.qo"],
    },
    "throttle_ms": 50,
    "url": "http://new-route.url",
  },
}
 # Route | Route settings to be updated

    try:
        api_response = api_instance.update_route(project_uid, route_uid, route)
        print("The response of RouteApi->update_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->update_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **route_uid** | **str**|  | 
 **route** | [**Route**](Route.md)| Route settings to be updated | 

### Return type

[**Route**](Route.md)

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

