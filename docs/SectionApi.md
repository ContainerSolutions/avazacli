# avazacli.SectionApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**section_get**](SectionApi.md#section_get) | **GET** /api/Section | Gets list of Sections
[**section_post**](SectionApi.md#section_post) | **POST** /api/Section | Create a Section


# **section_get**
> SectionList section_get(project_id)

Gets list of Sections

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
api_instance = avazacli.SectionApi(avazacli.ApiClient(configuration))
project_id = 56 # int | Get sections for Project with ProjectID

try:
    # Gets list of Sections
    api_response = api_instance.section_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionApi->section_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Get sections for Project with ProjectID | 

### Return type

[**SectionList**](SectionList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **section_post**
> SectionDetails section_post(model)

Create a Section

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
api_instance = avazacli.SectionApi(avazacli.ApiClient(configuration))
model = avazacli.NewSection() # NewSection | 

try:
    # Create a Section
    api_response = api_instance.section_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionApi->section_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**NewSection**](NewSection.md)|  | 

### Return type

[**SectionDetails**](SectionDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

