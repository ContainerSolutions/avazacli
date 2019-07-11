# avazacli.CreditNoteApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_note_get**](CreditNoteApi.md#credit_note_get) | **GET** /api/CreditNote | Gets list of CreditNotes
[**credit_note_get_by_id**](CreditNoteApi.md#credit_note_get_by_id) | **GET** /api/CreditNote/{id} | Gets Credit Note by CreditNoteID


# **credit_note_get**
> CreditNoteList credit_note_get(updated_after=updated_after, page_size=page_size, page_number=page_number)

Gets list of CreditNotes

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
api_instance = avazacli.CreditNoteApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)

try:
    # Gets list of CreditNotes
    api_response = api_instance.credit_note_get(updated_after=updated_after, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNoteApi->credit_note_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**|  | [optional] 
 **page_size** | **int**| Number of items per page (max 1000) | [optional] 
 **page_number** | **int**| Page to display. Starts from 1. | [optional] 

### Return type

[**CreditNoteList**](CreditNoteList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_note_get_by_id**
> CreditNote credit_note_get_by_id(id)

Gets Credit Note by CreditNoteID

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
api_instance = avazacli.CreditNoteApi(avazacli.ApiClient(configuration))
id = 789 # int | Credit Note ID Number

try:
    # Gets Credit Note by CreditNoteID
    api_response = api_instance.credit_note_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNoteApi->credit_note_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Credit Note ID Number | 

### Return type

[**CreditNote**](CreditNote.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

