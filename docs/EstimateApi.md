# avazacli.EstimateApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**estimate_get**](EstimateApi.md#estimate_get) | **GET** /api/Estimate | Gets list of Estimates
[**estimate_get_by_id**](EstimateApi.md#estimate_get_by_id) | **GET** /api/Estimate/{id} | Gets Estimate by Estimate ID


# **estimate_get**
> EstimateList estimate_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort, company_idfk=company_idfk)

Gets list of Estimates

EstimateStatusCode values are: \"Draft\", \"Sent\", \"Late\", \"Paid\", \"Partial\", \"Void\"

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
api_instance = avazacli.EstimateApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)
sort = 'sort_example' # str |  (optional)
company_idfk = 56 # int |  (optional)

try:
    # Gets list of Estimates
    api_response = api_instance.estimate_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort, company_idfk=company_idfk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EstimateApi->estimate_get: %s\n" % e)
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

[**EstimateList**](EstimateList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_get_by_id**
> estimate_get_by_id(id)

Gets Estimate by Estimate ID

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
api_instance = avazacli.EstimateApi(avazacli.ApiClient(configuration))
id = 789 # int | Estimate Estimate ID number

try:
    # Gets Estimate by Estimate ID
    api_instance.estimate_get_by_id(id)
except ApiException as e:
    print("Exception when calling EstimateApi->estimate_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Estimate Estimate ID number | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

