# avazacli.TimesheetSubmissionApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheet_submission_post**](TimesheetSubmissionApi.md#timesheet_submission_post) | **POST** /api/TimesheetSubmission | Submit Timesheets for Approval.


# **timesheet_submission_post**
> object timesheet_submission_post(send_notifications=send_notifications, whole_week_of=whole_week_of, whole_day_of=whole_day_of, user_id=user_id)

Submit Timesheets for Approval.

Either provide a a specific Day (WholeDayOf) or any day in a Week (WholeWeekOf) to submit all draft timesheets in that day or week

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
api_instance = avazacli.TimesheetSubmissionApi(avazacli.ApiClient(configuration))
send_notifications = true # bool | Send email alerts to timesheet approvers. Defaults to true (optional)
whole_week_of = '2013-10-20T19:20:30+01:00' # datetime | A date (yyyy-MM-dd) that falls within  a Week to have all timesheets in that week submitted. Respects the First Day of Week setting in your account Timesheet Settings to determine the week range. (optional)
whole_day_of = '2013-10-20T19:20:30+01:00' # datetime | A date (yyyy-MM-dd) to submit all timesheets on this day (optional)
user_id = 56 # int | The user to submit timesheets for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users. (optional)

try:
    # Submit Timesheets for Approval.
    api_response = api_instance.timesheet_submission_post(send_notifications=send_notifications, whole_week_of=whole_week_of, whole_day_of=whole_day_of, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetSubmissionApi->timesheet_submission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_notifications** | **bool**| Send email alerts to timesheet approvers. Defaults to true | [optional] 
 **whole_week_of** | **datetime**| A date (yyyy-MM-dd) that falls within  a Week to have all timesheets in that week submitted. Respects the First Day of Week setting in your account Timesheet Settings to determine the week range. | [optional] 
 **whole_day_of** | **datetime**| A date (yyyy-MM-dd) to submit all timesheets on this day | [optional] 
 **user_id** | **int**| The user to submit timesheets for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users. | [optional] 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

