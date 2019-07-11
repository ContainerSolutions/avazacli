# avazacli.ContactApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_get**](ContactApi.md#contact_get) | **GET** /api/Contact | Gets list of Contacts
[**contact_get_by_id**](ContactApi.md#contact_get_by_id) | **GET** /api/Contact/{id} | Gets Contact by Contact ID
[**contact_post**](ContactApi.md#contact_post) | **POST** /api/Contact | Create a Contact


# **contact_get**
> ContactList contact_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort, company_idfk=company_idfk)

Gets list of Contacts

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
api_instance = avazacli.ContactApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)
sort = 'sort_example' # str |  (optional)
company_idfk = 56 # int |  (optional)

try:
    # Gets list of Contacts
    api_response = api_instance.contact_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort, company_idfk=company_idfk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**|  | [optional] 
 **page_size** | **int**| Number of items per page (max 1000) | [optional] 
 **page_number** | **int**| Page to display. Starts from 1. | [optional] 
 **sort** | **str**|  | [optional] 
 **company_idfk** | **int**|  | [optional] 

### Return type

[**ContactList**](ContactList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_get_by_id**
> CompanyContact contact_get_by_id(id)

Gets Contact by Contact ID

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
api_instance = avazacli.ContactApi(avazacli.ApiClient(configuration))
id = 789 # int | Contact ID number

try:
    # Gets Contact by Contact ID
    api_response = api_instance.contact_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Contact ID number | 

### Return type

[**CompanyContact**](CompanyContact.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_post**
> CompanyContact contact_post(model)

Create a Contact

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
api_instance = avazacli.ContactApi(avazacli.ApiClient(configuration))
model = avazacli.NewCompanyContact() # NewCompanyContact | 

try:
    # Create a Contact
    api_response = api_instance.contact_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**NewCompanyContact**](NewCompanyContact.md)|  | 

### Return type

[**CompanyContact**](CompanyContact.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

