# avazacli.TimesheetApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheet_delete**](TimesheetApi.md#timesheet_delete) | **DELETE** /api/Timesheet/{id} | Delete a Timesheet Entry
[**timesheet_get**](TimesheetApi.md#timesheet_get) | **GET** /api/Timesheet | Gets list of Timsheets
[**timesheet_get_by_id**](TimesheetApi.md#timesheet_get_by_id) | **GET** /api/Timesheet/{id} | Gets a Timesheet Entry by Timesheet ID
[**timesheet_post**](TimesheetApi.md#timesheet_post) | **POST** /api/Timesheet | Create a new Timesheet Entry
[**timesheet_put**](TimesheetApi.md#timesheet_put) | **PUT** /api/Timesheet | Update a Timesheet


# **timesheet_delete**
> object timesheet_delete(id)

Delete a Timesheet Entry

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
api_instance = avazacli.TimesheetApi(avazacli.ApiClient(configuration))
id = 789 # int | The TimesheetEntryID of the Timesheet Entry

try:
    # Delete a Timesheet Entry
    api_response = api_instance.timesheet_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->timesheet_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The TimesheetEntryID of the Timesheet Entry | 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timesheet_get**
> TimesheetList timesheet_get(updated_after=updated_after, entry_date_from=entry_date_from, entry_date_to=entry_date_to, user_id=user_id, user_email=user_email, category_name=category_name, project_id=project_id, is_billable=is_billable, is_invoiced=is_invoiced, is_timer_running=is_timer_running, page_size=page_size, page_number=page_number, sort=sort)

Gets list of Timsheets

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
api_instance = avazacli.TimesheetApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
entry_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
entry_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
user_id = 56 # int | The UserID of a timesheet user to filter timesheets for. Only api users with certain higher roles can see timesheets across multiple users. (optional)
user_email = 'user_email_example' # str |  (optional)
category_name = 'category_name_example' # str |  (optional)
project_id = 56 # int |  (optional)
is_billable = true # bool |  (optional)
is_invoiced = true # bool |  (optional)
is_timer_running = true # bool |  (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)
sort = 'sort_example' # str | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\",\"EntryDate\", \"EntryDate desc\", \"StartTimeLocal\",\"StartTimeLocal desc\", \"TimeSheetEntryID\", \"TimeSheetEntryID desc\" (optional)

try:
    # Gets list of Timsheets
    api_response = api_instance.timesheet_get(updated_after=updated_after, entry_date_from=entry_date_from, entry_date_to=entry_date_to, user_id=user_id, user_email=user_email, category_name=category_name, project_id=project_id, is_billable=is_billable, is_invoiced=is_invoiced, is_timer_running=is_timer_running, page_size=page_size, page_number=page_number, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->timesheet_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**|  | [optional] 
 **entry_date_from** | **datetime**|  | [optional] 
 **entry_date_to** | **datetime**|  | [optional] 
 **user_id** | **int**| The UserID of a timesheet user to filter timesheets for. Only api users with certain higher roles can see timesheets across multiple users. | [optional] 
 **user_email** | **str**|  | [optional] 
 **category_name** | **str**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **is_billable** | **bool**|  | [optional] 
 **is_invoiced** | **bool**|  | [optional] 
 **is_timer_running** | **bool**|  | [optional] 
 **page_size** | **int**| Number of items per page (max 1000) | [optional] 
 **page_number** | **int**| Page to display. Starts from 1. | [optional] 
 **sort** | **str**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;,\&quot;EntryDate\&quot;, \&quot;EntryDate desc\&quot;, \&quot;StartTimeLocal\&quot;,\&quot;StartTimeLocal desc\&quot;, \&quot;TimeSheetEntryID\&quot;, \&quot;TimeSheetEntryID desc\&quot; | [optional] 

### Return type

[**TimesheetList**](TimesheetList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timesheet_get_by_id**
> TimesheetDetails timesheet_get_by_id(id)

Gets a Timesheet Entry by Timesheet ID

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
api_instance = avazacli.TimesheetApi(avazacli.ApiClient(configuration))
id = 789 # int | Timesheet ID number

try:
    # Gets a Timesheet Entry by Timesheet ID
    api_response = api_instance.timesheet_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->timesheet_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Timesheet ID number | 

### Return type

[**TimesheetDetails**](TimesheetDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timesheet_post**
> TimesheetDetails timesheet_post(model)

Create a new Timesheet Entry

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
api_instance = avazacli.TimesheetApi(avazacli.ApiClient(configuration))
model = avazacli.NewTimesheet() # NewTimesheet | 

try:
    # Create a new Timesheet Entry
    api_response = api_instance.timesheet_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->timesheet_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**NewTimesheet**](NewTimesheet.md)|  | 

### Return type

[**TimesheetDetails**](TimesheetDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timesheet_put**
> TimesheetDetails timesheet_put(model)

Update a Timesheet

The FieldsToUpdate field expects a string array collection of the field names you would like updated.

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
api_instance = avazacli.TimesheetApi(avazacli.ApiClient(configuration))
model = avazacli.UpdateTimesheetModel() # UpdateTimesheetModel | 

try:
    # Update a Timesheet
    api_response = api_instance.timesheet_put(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->timesheet_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**UpdateTimesheetModel**](UpdateTimesheetModel.md)|  | 

### Return type

[**TimesheetDetails**](TimesheetDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

