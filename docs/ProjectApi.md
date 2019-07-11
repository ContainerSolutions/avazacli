# avazacli.ProjectApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_get**](ProjectApi.md#project_get) | **GET** /api/Project | Gets list of Projects
[**project_get_by_id**](ProjectApi.md#project_get_by_id) | **GET** /api/Project/{id} | Gets Project by Project ID
[**project_post**](ProjectApi.md#project_post) | **POST** /api/Project | Create a Project


# **project_get**
> ProjectList project_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort, timesheet_user_id=timesheet_user_id, include_archived=include_archived)

Gets list of Projects

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
api_instance = avazacli.ProjectApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime | Only show project records updated after a certain date (UTC) (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)
sort = 'sort_example' # str | A column to sort on. Current possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\" (optional)
timesheet_user_id = 56 # int | Filter to the projects that the supplied UserID can add timesheets to (optional)
include_archived = true # bool | Include Archived Projects in the results (optional)

try:
    # Gets list of Projects
    api_response = api_instance.project_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort, timesheet_user_id=timesheet_user_id, include_archived=include_archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->project_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**| Only show project records updated after a certain date (UTC) | [optional] 
 **page_size** | **int**| Number of items per page (max 1000) | [optional] 
 **page_number** | **int**| Page to display. Starts from 1. | [optional] 
 **sort** | **str**| A column to sort on. Current possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot; | [optional] 
 **timesheet_user_id** | **int**| Filter to the projects that the supplied UserID can add timesheets to | [optional] 
 **include_archived** | **bool**| Include Archived Projects in the results | [optional] 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_get_by_id**
> ProjectDetails project_get_by_id(id)

Gets Project by Project ID

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
api_instance = avazacli.ProjectApi(avazacli.ApiClient(configuration))
id = 789 # int | Project ID number

try:
    # Gets Project by Project ID
    api_response = api_instance.project_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->project_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Project ID number | 

### Return type

[**ProjectDetails**](ProjectDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_post**
> ProjectDetails project_post(model)

Create a Project

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
api_instance = avazacli.ProjectApi(avazacli.ApiClient(configuration))
model = avazacli.NewProjectModel() # NewProjectModel | 

try:
    # Create a Project
    api_response = api_instance.project_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->project_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**NewProjectModel**](NewProjectModel.md)|  | 

### Return type

[**ProjectDetails**](ProjectDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

