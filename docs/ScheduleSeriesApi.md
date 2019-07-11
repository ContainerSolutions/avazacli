# avazacli.ScheduleSeriesApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedule_series_get**](ScheduleSeriesApi.md#schedule_series_get) | **GET** /api/ScheduleSeries | Gets list of Schedule Series


# **schedule_series_get**
> ScheduleSeriesList schedule_series_get(updated_after=updated_after, schedule_start_date_from=schedule_start_date_from, schedule_start_date_to=schedule_start_date_to, schedule_end_date_from=schedule_end_date_from, schedule_end_date_to=schedule_end_date_to, user_id=user_id, user_email=user_email, time_sheet_category_id=time_sheet_category_id, time_sheet_category_name=time_sheet_category_name, leave_type_id=leave_type_id, project_id=project_id, company_id=company_id, page_size=page_size, page_number=page_number, sort=sort)

Gets list of Schedule Series

Schedule Series represents a strip of time assigned to a user over a date range, for a certain number of hours per day. They can be for Leave or for project work Bookings.

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
api_instance = avazacli.ScheduleSeriesApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime | Limit results to records updated after the specified date (optional)
schedule_start_date_from = '2013-10-20T19:20:30+01:00' # datetime | Filter for schedules that start on or after a specific date (optional)
schedule_start_date_to = '2013-10-20T19:20:30+01:00' # datetime | Filter for schedules that start on or before a specific date (optional)
schedule_end_date_from = '2013-10-20T19:20:30+01:00' # datetime | Filter for schedules that end on or after a specific date (optional)
schedule_end_date_to = '2013-10-20T19:20:30+01:00' # datetime | Filter for schedules that end on or before a specific date (optional)
user_id = 56 # int | The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries. (optional)
user_email = 'user_email_example' # str | The email of the user who has been scheduled (optional)
time_sheet_category_id = 56 # int | Filter for schedule records linked to a specific timesheeet category (optional)
time_sheet_category_name = 'time_sheet_category_name_example' # str | Filter for schedule records with a specific timesheeet category name (exact string match) (optional)
leave_type_id = 56 # int | Filter to records of a particular leave type (optional)
project_id = 56 # int | Filter to only include books linked to a specific project (optional)
company_id = 56 # int | Filter to only include records linked to projects, where that project belongs to a specific customer company (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)
sort = 'sort_example' # str | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\" (optional)

try:
    # Gets list of Schedule Series
    api_response = api_instance.schedule_series_get(updated_after=updated_after, schedule_start_date_from=schedule_start_date_from, schedule_start_date_to=schedule_start_date_to, schedule_end_date_from=schedule_end_date_from, schedule_end_date_to=schedule_end_date_to, user_id=user_id, user_email=user_email, time_sheet_category_id=time_sheet_category_id, time_sheet_category_name=time_sheet_category_name, leave_type_id=leave_type_id, project_id=project_id, company_id=company_id, page_size=page_size, page_number=page_number, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleSeriesApi->schedule_series_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**| Limit results to records updated after the specified date | [optional] 
 **schedule_start_date_from** | **datetime**| Filter for schedules that start on or after a specific date | [optional] 
 **schedule_start_date_to** | **datetime**| Filter for schedules that start on or before a specific date | [optional] 
 **schedule_end_date_from** | **datetime**| Filter for schedules that end on or after a specific date | [optional] 
 **schedule_end_date_to** | **datetime**| Filter for schedules that end on or before a specific date | [optional] 
 **user_id** | **int**| The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries. | [optional] 
 **user_email** | **str**| The email of the user who has been scheduled | [optional] 
 **time_sheet_category_id** | **int**| Filter for schedule records linked to a specific timesheeet category | [optional] 
 **time_sheet_category_name** | **str**| Filter for schedule records with a specific timesheeet category name (exact string match) | [optional] 
 **leave_type_id** | **int**| Filter to records of a particular leave type | [optional] 
 **project_id** | **int**| Filter to only include books linked to a specific project | [optional] 
 **company_id** | **int**| Filter to only include records linked to projects, where that project belongs to a specific customer company | [optional] 
 **page_size** | **int**| Number of items per page (max 1000) | [optional] 
 **page_number** | **int**| Page to display. Starts from 1. | [optional] 
 **sort** | **str**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot; | [optional] 

### Return type

[**ScheduleSeriesList**](ScheduleSeriesList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

