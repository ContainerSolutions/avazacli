# NewPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**payment_number** | **str** | Optional. If not specified will be automatically generated | [optional] 
**date_issued** | **datetime** | Date of Payment. If not specified, assumes today. | [optional] 
**transaction_prefix** | **str** | Optional to override the default prefix added to Payment Numbers | [optional] 
**customer_idfk** | **int** | Only required if no invoice allocations specified. | [optional] 
**exchange_rate** | **float** | Optional. Only used when the Customer&#39;s currecy is different from the Avaza account&#39;s base currency. Specifies the exchange rate that should apply between the customer currency and base currency. If not provided we will obtain an up to date exchange rate for the Payment Issue Date. | [optional] 
**transaction_reference** | **str** | Optional for storing the reference # of the payment method. | [optional] 
**notes** | **str** |  | [optional] 
**payment_provider_code** | **str** | Optional for storing the payment provider who was the source of funds. | [optional] 
**payment_allocations** | [**list[NewPaymentAllocation]**](NewPaymentAllocation.md) | List of amounts within this payment that are allocated to invoices. The sum of these be less than or equal to the payment amount. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


