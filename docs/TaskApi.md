# avazacli.TaskApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_get**](TaskApi.md#task_get) | **GET** /api/Task | Gets list of Tasks
[**task_get_by_id**](TaskApi.md#task_get_by_id) | **GET** /api/Task/{id} | Gets Task by Task ID
[**task_post**](TaskApi.md#task_post) | **POST** /api/Task | Create a Task
[**task_put**](TaskApi.md#task_put) | **PUT** /api/Task | Update a Task.


# **task_get**
> TaskList task_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort, project_id=project_id)

Gets list of Tasks

### Example
```python
from __future__ import print_function
import time
import avazacli
from avazacli.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = avazacli.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = avazacli.TaskApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime | Optional filter to records updated after a specific date. (optional)
page_size = 56 # int | Number of items per page. Defaults to 20. (optional)
page_number = 56 # int | Page to display. Starts from 1. Defaults to 1 (optional)
sort = 'sort_example' # str | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\" (optional)
project_id = 56 # int | Optional filter to only display tasks belonging to a specific ProjectID (optional)

try:
    # Gets list of Tasks
    api_response = api_instance.task_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort, project_id=project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->task_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**| Optional filter to records updated after a specific date. | [optional] 
 **page_size** | **int**| Number of items per page. Defaults to 20. | [optional] 
 **page_number** | **int**| Page to display. Starts from 1. Defaults to 1 | [optional] 
 **sort** | **str**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot; | [optional] 
 **project_id** | **int**| Optional filter to only display tasks belonging to a specific ProjectID | [optional] 

### Return type

[**TaskList**](TaskList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_get_by_id**
> TaskDetails task_get_by_id(id)

Gets Task by Task ID

### Example
```python
from __future__ import print_function
import time
import avazacli
from avazacli.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = avazacli.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = avazacli.TaskApi(avazacli.ApiClient(configuration))
id = 789 # int | Task ID number

try:
    # Gets Task by Task ID
    api_response = api_instance.task_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->task_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID number | 

### Return type

[**TaskDetails**](TaskDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_post**
> TaskDetails task_post(model)

Create a Task

### Example
```python
from __future__ import print_function
import time
import avazacli
from avazacli.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = avazacli.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = avazacli.TaskApi(avazacli.ApiClient(configuration))
model = avazacli.NewTask() # NewTask | 

try:
    # Create a Task
    api_response = api_instance.task_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->task_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**NewTask**](NewTask.md)|  | 

### Return type

[**TaskDetails**](TaskDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_put**
> TaskDetails task_put(model)

Update a Task.

Requires TaskID and a list of field names to update. The FieldsToUpdate field accepts a string array containing field names that should be updated.

### Example
```python
from __future__ import print_function
import time
import avazacli
from avazacli.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = avazacli.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = avazacli.TaskApi(avazacli.ApiClient(configuration))
model = avazacli.UpdateTask() # UpdateTask | 

try:
    # Update a Task.
    api_response = api_instance.task_put(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->task_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**UpdateTask**](UpdateTask.md)|  | 

### Return type

[**TaskDetails**](TaskDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

