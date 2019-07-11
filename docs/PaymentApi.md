# avazacli.PaymentApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_get**](PaymentApi.md#payment_get) | **GET** /api/Payment | Gets list of Payments
[**payment_get_by_id**](PaymentApi.md#payment_get_by_id) | **GET** /api/Payment/{id} | Gets Payment by Payment Transaction ID
[**payment_post**](PaymentApi.md#payment_post) | **POST** /api/Payment | Create new Payment and optionally assign payment allocations to Invoices


# **payment_get**
> PaymentList payment_get(updated_after=updated_after, page_size=page_size, page_number=page_number)

Gets list of Payments

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
api_instance = avazacli.PaymentApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)

try:
    # Gets list of Payments
    api_response = api_instance.payment_get(updated_after=updated_after, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->payment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**|  | [optional] 
 **page_size** | **int**| Number of items per page (max 1000) | [optional] 
 **page_number** | **int**| Page to display. Starts from 1. | [optional] 

### Return type

[**PaymentList**](PaymentList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_get_by_id**
> Payment payment_get_by_id(id)

Gets Payment by Payment Transaction ID

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
api_instance = avazacli.PaymentApi(avazacli.ApiClient(configuration))
id = 789 # int | Invoice Transaction ID Number

try:
    # Gets Payment by Payment Transaction ID
    api_response = api_instance.payment_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->payment_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invoice Transaction ID Number | 

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_post**
> Payment payment_post(model)

Create new Payment and optionally assign payment allocations to Invoices

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
api_instance = avazacli.PaymentApi(avazacli.ApiClient(configuration))
model = avazacli.NewPayment() # NewPayment | 

try:
    # Create new Payment and optionally assign payment allocations to Invoices
    api_response = api_instance.payment_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->payment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**NewPayment**](NewPayment.md)|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

