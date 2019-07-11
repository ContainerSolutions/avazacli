# avazacli.UserProfileApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_profile_get**](UserProfileApi.md#user_profile_get) | **GET** /api/UserProfile | Get Collection of Users who have roles in the current Avaza account.


# **user_profile_get**
> UserList user_profile_get(roles=roles, tags=tags, current_user_only=current_user_only, company_idfk=company_idfk)

Get Collection of Users who have roles in the current Avaza account.

Admin and Invoice Managers can see all. Other users are limited to seeing their own profile.

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
api_instance = avazacli.UserProfileApi(avazacli.ApiClient(configuration))
roles = 'roles_example' # str | Optional list of comma separated role codes to filter users by (e.g. \"TimesheetUser,Admin\") (optional)
tags = 'tags_example' # str |  (optional)
current_user_only = true # bool | Optional boolean (true/false) to filter to only show current authenticated user (always true for non Admin/InvoiceManager users) (optional)
company_idfk = 56 # int | Optionally filter by Company ID (optional)

try:
    # Get Collection of Users who have roles in the current Avaza account.
    api_response = api_instance.user_profile_get(roles=roles, tags=tags, current_user_only=current_user_only, company_idfk=company_idfk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserProfileApi->user_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles** | **str**| Optional list of comma separated role codes to filter users by (e.g. \&quot;TimesheetUser,Admin\&quot;) | [optional] 
 **tags** | **str**|  | [optional] 
 **current_user_only** | **bool**| Optional boolean (true/false) to filter to only show current authenticated user (always true for non Admin/InvoiceManager users) | [optional] 
 **company_idfk** | **int**| Optionally filter by Company ID | [optional] 

### Return type

[**UserList**](UserList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

