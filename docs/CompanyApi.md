# avazacli.CompanyApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_get**](CompanyApi.md#company_get) | **GET** /api/Company | Gets list of Companies
[**company_get_by_id**](CompanyApi.md#company_get_by_id) | **GET** /api/Company/{id} | Gets Company by Company ID
[**company_post**](CompanyApi.md#company_post) | **POST** /api/Company | Create a Company
[**company_put**](CompanyApi.md#company_put) | **PUT** /api/Company | Update a Task.


# **company_get**
> CompanyList company_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort)

Gets list of Companies

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
api_instance = avazacli.CompanyApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_size = 56 # int | Number of results per page (optional)
page_number = 56 # int | 1 based page number to retrieve (optional)
sort = 'sort_example' # str |  (optional)

try:
    # Gets list of Companies
    api_response = api_instance.company_get(updated_after=updated_after, page_size=page_size, page_number=page_number, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**|  | [optional] 
 **page_size** | **int**| Number of results per page | [optional] 
 **page_number** | **int**| 1 based page number to retrieve | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**CompanyList**](CompanyList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_get_by_id**
> Company company_get_by_id(id)

Gets Company by Company ID

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
api_instance = avazacli.CompanyApi(avazacli.ApiClient(configuration))
id = 789 # int | Company ID Number

try:
    # Gets Company by Company ID
    api_response = api_instance.company_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Company ID Number | 

### Return type

[**Company**](Company.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_post**
> Company company_post(model)

Create a Company

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
api_instance = avazacli.CompanyApi(avazacli.ApiClient(configuration))
model = avazacli.NewCompany() # NewCompany | 

try:
    # Create a Company
    api_response = api_instance.company_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**NewCompany**](NewCompany.md)|  | 

### Return type

[**Company**](Company.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_put**
> Company company_put(model)

Update a Task.

Requires TaskID and a list of field names to update. The FieldsToUpdate field accepts a string array containing field names that should be updated.

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
api_instance = avazacli.CompanyApi(avazacli.ApiClient(configuration))
model = avazacli.UpdateCompany() # UpdateCompany | 

try:
    # Update a Task.
    api_response = api_instance.company_put(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**UpdateCompany**](UpdateCompany.md)|  | 

### Return type

[**Company**](Company.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

