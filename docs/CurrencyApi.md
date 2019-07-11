# avazacli.CurrencyApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currency_get**](CurrencyApi.md#currency_get) | **GET** /api/Currency | Gets list of Currencies


# **currency_get**
> CurrencyList currency_get()

Gets list of Currencies

### Example
```python
from __future__ import print_function
import time
import avazacli
from avazacli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = avazacli.CurrencyApi()

try:
    # Gets list of Currencies
    api_response = api_instance.currency_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrencyApi->currency_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrencyList**](CurrencyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

