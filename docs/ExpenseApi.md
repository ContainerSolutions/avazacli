# avazacli.ExpenseApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expense_get**](ExpenseApi.md#expense_get) | **GET** /api/Expense | Gets list of Expenses
[**expense_get_by_id**](ExpenseApi.md#expense_get_by_id) | **GET** /api/Expense/{id} | Gets an Expense Entry by Expense ID
[**expense_post**](ExpenseApi.md#expense_post) | **POST** /api/Expense | Create an Expense


# **expense_get**
> ExpenseList expense_get(updated_after=updated_after, expense_date_from=expense_date_from, expense_date_to=expense_date_to, user_email=user_email, category_name=category_name, customer_id=customer_id, project_id=project_id, is_chargeable=is_chargeable, is_invoiced=is_invoiced, page_size=page_size, page_number=page_number, sort=sort)

Gets list of Expenses

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
api_instance = avazacli.ExpenseApi(avazacli.ApiClient(configuration))
updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
expense_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
expense_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
user_email = 'user_email_example' # str |  (optional)
category_name = 'category_name_example' # str |  (optional)
customer_id = 56 # int |  (optional)
project_id = 56 # int |  (optional)
is_chargeable = true # bool |  (optional)
is_invoiced = true # bool |  (optional)
page_size = 56 # int | Number of items per page (max 1000) (optional)
page_number = 56 # int | Page to display. Starts from 1. (optional)
sort = 'sort_example' # str |  (optional)

try:
    # Gets list of Expenses
    api_response = api_instance.expense_get(updated_after=updated_after, expense_date_from=expense_date_from, expense_date_to=expense_date_to, user_email=user_email, category_name=category_name, customer_id=customer_id, project_id=project_id, is_chargeable=is_chargeable, is_invoiced=is_invoiced, page_size=page_size, page_number=page_number, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseApi->expense_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **datetime**|  | [optional] 
 **expense_date_from** | **datetime**|  | [optional] 
 **expense_date_to** | **datetime**|  | [optional] 
 **user_email** | **str**|  | [optional] 
 **category_name** | **str**|  | [optional] 
 **customer_id** | **int**|  | [optional] 
 **project_id** | **int**|  | [optional] 
 **is_chargeable** | **bool**|  | [optional] 
 **is_invoiced** | **bool**|  | [optional] 
 **page_size** | **int**| Number of items per page (max 1000) | [optional] 
 **page_number** | **int**| Page to display. Starts from 1. | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**ExpenseList**](ExpenseList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expense_get_by_id**
> ExpenseDetails expense_get_by_id(id)

Gets an Expense Entry by Expense ID

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
api_instance = avazacli.ExpenseApi(avazacli.ApiClient(configuration))
id = 789 # int | Expense ID number

try:
    # Gets an Expense Entry by Expense ID
    api_response = api_instance.expense_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseApi->expense_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Expense ID number | 

### Return type

[**ExpenseDetails**](ExpenseDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expense_post**
> ExpenseDetails expense_post(model)

Create an Expense

Create an Expense

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
api_instance = avazacli.ExpenseApi(avazacli.ApiClient(configuration))
model = avazacli.NewExpense() # NewExpense | 

try:
    # Create an Expense
    api_response = api_instance.expense_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseApi->expense_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**NewExpense**](NewExpense.md)|  | 

### Return type

[**ExpenseDetails**](ExpenseDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

