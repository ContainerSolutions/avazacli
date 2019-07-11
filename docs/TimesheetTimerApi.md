# avazacli.TimesheetTimerApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheet_timer_get_running_timer**](TimesheetTimerApi.md#timesheet_timer_get_running_timer) | **GET** /api/TimesheetTimer | Gets the  Running Timer if there is one for a user.
[**timesheet_timer_start_timer**](TimesheetTimerApi.md#timesheet_timer_start_timer) | **POST** /api/TimesheetTimer/{id} | Starts a Timer running on an existing Timesheet Entry
[**timesheet_timer_stop_timer**](TimesheetTimerApi.md#timesheet_timer_stop_timer) | **DELETE** /api/TimesheetTimer/{id} | Stop the timer running on an existing Timesheet Entry


# **timesheet_timer_get_running_timer**
> object timesheet_timer_get_running_timer(user_id=user_id)

Gets the  Running Timer if there is one for a user.

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
api_instance = avazacli.TimesheetTimerApi(avazacli.ApiClient(configuration))
user_id = 56 # int | Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users (optional)

try:
    # Gets the  Running Timer if there is one for a user.
    api_response = api_instance.timesheet_timer_get_running_timer(user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetTimerApi->timesheet_timer_get_running_timer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users | [optional] 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timesheet_timer_start_timer**
> object timesheet_timer_start_timer(id, user_id=user_id)

Starts a Timer running on an existing Timesheet Entry

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
api_instance = avazacli.TimesheetTimerApi(avazacli.ApiClient(configuration))
id = 789 # int | The ID of the existing timesheet entry on which to start a timer
user_id = 56 # int | Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users (optional)

try:
    # Starts a Timer running on an existing Timesheet Entry
    api_response = api_instance.timesheet_timer_start_timer(id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetTimerApi->timesheet_timer_start_timer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the existing timesheet entry on which to start a timer | 
 **user_id** | **int**| Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users | [optional] 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timesheet_timer_stop_timer**
> object timesheet_timer_stop_timer(id, user_id=user_id)

Stop the timer running on an existing Timesheet Entry

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
api_instance = avazacli.TimesheetTimerApi(avazacli.ApiClient(configuration))
id = 789 # int | The ID of the existing timesheet entry that needs its timer stopped
user_id = 56 # int | Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users (optional)

try:
    # Stop the timer running on an existing Timesheet Entry
    api_response = api_instance.timesheet_timer_stop_timer(id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetTimerApi->timesheet_timer_stop_timer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the existing timesheet entry that needs its timer stopped | 
 **user_id** | **int**| Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users | [optional] 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

