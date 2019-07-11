# avazacli.TaxApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tax_get**](TaxApi.md#tax_get) | **GET** /api/Tax | Get List of Taxes configured in the Avaza account.


# **tax_get**
> TaxList tax_get()

Get List of Taxes configured in the Avaza account.

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
api_instance = avazacli.TaxApi(avazacli.ApiClient(configuration))

try:
    # Get List of Taxes configured in the Avaza account.
    api_response = api_instance.tax_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->tax_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxList**](TaxList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

