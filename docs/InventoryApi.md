# avazacli.InventoryApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_get**](InventoryApi.md#inventory_get) | **GET** /api/Inventory | Gets list of Inventory
[**inventory_get_by_id**](InventoryApi.md#inventory_get_by_id) | **GET** /api/Inventory/{id} | Gets InventoryItem by InventoryItem ID


# **inventory_get**
> InventoryList inventory_get(updated_after=updated_after, page_size=page_size, page_number=page_number)

Gets list of Inventory



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
api_instance = avazacli.InventoryApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)

try:
    # Gets list of Inventory
    api_response = api_instance.inventory_get(updated_after=updated_after, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryApi->inventory_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**|  | [optional] 
 **page_size** | **int**| Number of items per page (max 1000) | [optional] 
 **page_number** | **int**| Page to display. Starts from 1. | [optional] 

### Return type

[**InventoryList**](InventoryList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_get_by_id**
> inventory_get_by_id(id)

Gets InventoryItem by InventoryItem ID

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
api_instance = avazacli.InventoryApi(avazacli.ApiClient(configuration))
id = 789 # int | InventoryItem ID number

try:
    # Gets InventoryItem by InventoryItem ID
    api_instance.inventory_get_by_id(id)
except ApiException as e:
    print("Exception when calling InventoryApi->inventory_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| InventoryItem ID number | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

