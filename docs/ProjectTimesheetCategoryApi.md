# avazacli.ProjectTimesheetCategoryApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_timesheet_category_get**](ProjectTimesheetCategoryApi.md#project_timesheet_category_get) | **GET** /api/ProjectTimesheetCategory | Gets list of Project Timesheet Categories


# **project_timesheet_category_get**
> ProjectTimesheetCategoryList project_timesheet_category_get(project_id=project_id)

Gets list of Project Timesheet Categories

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
api_instance = avazacli.ProjectTimesheetCategoryApi(avazacli.ApiClient(configuration))
project_id = 56 # int | Get categories filtered by ProjectID (optional)

try:
    # Gets list of Project Timesheet Categories
    api_response = api_instance.project_timesheet_category_get(project_id=project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTimesheetCategoryApi->project_timesheet_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Get categories filtered by ProjectID | [optional] 

### Return type

[**ProjectTimesheetCategoryList**](ProjectTimesheetCategoryList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

