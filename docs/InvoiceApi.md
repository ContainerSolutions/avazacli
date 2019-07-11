# avazacli.InvoiceApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoice_get**](InvoiceApi.md#invoice_get) | **GET** /api/Invoice | Gets list of Invoices
[**invoice_get_by_id**](InvoiceApi.md#invoice_get_by_id) | **GET** /api/Invoice/{id} | Gets Invoice by Invoice ID
[**invoice_post**](InvoiceApi.md#invoice_post) | **POST** /api/Invoice | Create a new draft invoice


# **invoice_get**
> InvoiceList invoice_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort, company_idfk=company_idfk)

Gets list of Invoices

TransactionStatusCode values are: \"Draft\", \"Sent\", \"Late\", \"Paid\", \"Partial\", \"Void\"

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
api_instance = avazacli.InvoiceApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)
sort = 'sort_example' # str |  (optional)
company_idfk = 56 # int |  (optional)

try:
    # Gets list of Invoices
    api_response = api_instance.invoice_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort, company_idfk=company_idfk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceApi->invoice_get: %s\n" % e)
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

[**InvoiceList**](InvoiceList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_get_by_id**
> invoice_get_by_id(id)

Gets Invoice by Invoice ID

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
api_instance = avazacli.InvoiceApi(avazacli.ApiClient(configuration))
id = 789 # int | Invoice Transaction ID number

try:
    # Gets Invoice by Invoice ID
    api_instance.invoice_get_by_id(id)
except ApiException as e:
    print("Exception when calling InvoiceApi->invoice_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invoice Transaction ID number | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_post**
> Invoice invoice_post(model)

Create a new draft invoice

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
api_instance = avazacli.InvoiceApi(avazacli.ApiClient(configuration))
model = avazacli.NewInvoice() # NewInvoice | 

try:
    # Create a new draft invoice
    api_response = api_instance.invoice_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceApi->invoice_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**NewInvoice**](NewInvoice.md)|  | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

