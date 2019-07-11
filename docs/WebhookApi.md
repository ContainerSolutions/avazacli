# avazacli.WebhookApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_delete**](WebhookApi.md#webhook_delete) | **DELETE** /api/Webhook/{id} | Delete Webhook Subscription by ID
[**webhook_delete_by_url**](WebhookApi.md#webhook_delete_by_url) | **DELETE** /api/Webhook | Delete webhook subscription by URL
[**webhook_get**](WebhookApi.md#webhook_get) | **GET** /api/Webhook | Get list of Webhook Subscriptions
[**webhook_post**](WebhookApi.md#webhook_post) | **POST** /api/Webhook | Subscribe to Webhook. On success, returns ID of webhook subscription.


# **webhook_delete**
> object webhook_delete(id)

Delete Webhook Subscription by ID

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
api_instance = avazacli.WebhookApi(avazacli.ApiClient(configuration))
id = 56 # int | Subscription id to be deleted

try:
    # Delete Webhook Subscription by ID
    api_response = api_instance.webhook_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->webhook_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Subscription id to be deleted | 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_delete_by_url**
> object webhook_delete_by_url(target_url)

Delete webhook subscription by URL

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
api_instance = avazacli.WebhookApi(avazacli.ApiClient(configuration))
target_url = 'target_url_example' # str | Target URL that should be used to delete subscriptions

try:
    # Delete webhook subscription by URL
    api_response = api_instance.webhook_delete_by_url(target_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->webhook_delete_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_url** | **str**| Target URL that should be used to delete subscriptions | 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_get**
> WebhookList webhook_get()

Get list of Webhook Subscriptions

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
api_instance = avazacli.WebhookApi(avazacli.ApiClient(configuration))

try:
    # Get list of Webhook Subscriptions
    api_response = api_instance.webhook_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->webhook_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhookList**](WebhookList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_post**
> SubscribeResult webhook_post(model)

Subscribe to Webhook. On success, returns ID of webhook subscription.

When you receive a webhook, you should respond with Http 200 OK Status Code, otherwise we will retry. To create a webhook, you need both the webhook_notifications scope, as well as the scope for the required entity being monitored.  Event values are: \"company_created\", \"company_deleted\", \"company_updated\", \"contact_created\", \"contact_deleted\", \"contact_updated\", \"invoice_created\", \"invoice_sent\", \"project_created\", \"project_deleted\", \"project_updated\", \"task_created\", \"task_updated\", \"timesheet_created\", \"timesheet_deleted\", \"timesheet_updated\".  You can subscribe to any webhook, but you will only receive notifications for data appropriate to the roles of your user account. There is an optional  Secret parameter (string 255 char max). This allows for webhook authentication. If provided, the Secret will be BASE 64 encoded and passed with notications as a basic authentication http header. i.e. Authorization Basic [BASE64 of Secret]\"

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
api_instance = avazacli.WebhookApi(avazacli.ApiClient(configuration))
model = avazacli.CreateSubscription() # CreateSubscription | 

try:
    # Subscribe to Webhook. On success, returns ID of webhook subscription.
    api_response = api_instance.webhook_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->webhook_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**CreateSubscription**](CreateSubscription.md)|  | 

### Return type

[**SubscribeResult**](SubscribeResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

