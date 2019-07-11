# avazacli.ScheduleAssignmentApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedule_assignment_get**](ScheduleAssignmentApi.md#schedule_assignment_get) | **GET** /api/ScheduleAssignment | Gets list of Schedule Assignments.


# **schedule_assignment_get**
> ScheduleAssignmentList schedule_assignment_get(updated_after=updated_after, schedule_date_from=schedule_date_from, schedule_date_to=schedule_date_to, schedule_series_id=schedule_series_id, user_id=user_id, user_email=user_email, page_size=page_size, page_number=page_number, sort=sort)

Gets list of Schedule Assignments.

Schedule assignments are per-day, and link to a parent Schedule Series.

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
api_instance = avazacli.ScheduleAssignmentApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime | Limit results to records updated after the specified date (optional)
schedule_date_from = '2013-10-20T19:20:30+01:00' # datetime | Filter for schedule assignement  that are  on or after a specific date (optional)
schedule_date_to = '2013-10-20T19:20:30+01:00' # datetime | Filter for schedules that are on or before a specific date (optional)
schedule_series_id = 789 # int | Filter to records for a particular Schedule Series (optional)
user_id = 56 # int | The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries. (optional)
user_email = 'user_email_example' # str | The email of the user who has been scheduled (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)
sort = 'sort_example' # str | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\" (optional)

try:
    # Gets list of Schedule Assignments.
    api_response = api_instance.schedule_assignment_get(updated_after=updated_after, schedule_date_from=schedule_date_from, schedule_date_to=schedule_date_to, schedule_series_id=schedule_series_id, user_id=user_id, user_email=user_email, page_size=page_size, page_number=page_number, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleAssignmentApi->schedule_assignment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**| Limit results to records updated after the specified date | [optional] 
 **schedule_date_from** | **datetime**| Filter for schedule assignement  that are  on or after a specific date | [optional] 
 **schedule_date_to** | **datetime**| Filter for schedules that are on or before a specific date | [optional] 
 **schedule_series_id** | **int**| Filter to records for a particular Schedule Series | [optional] 
 **user_id** | **int**| The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries. | [optional] 
 **user_email** | **str**| The email of the user who has been scheduled | [optional] 
 **page_size** | **int**| Number of items per page (max 1000) | [optional] 
 **page_number** | **int**| Page to display. Starts from 1. | [optional] 
 **sort** | **str**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot; | [optional] 

### Return type

[**ScheduleAssignmentList**](ScheduleAssignmentList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

