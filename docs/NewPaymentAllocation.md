# NewPaymentAllocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_transaction_idfk** | **int** | The Avaza Invoice TransactionID that is having a payment amount allocated to it. | [optional] 
**allocation_amount** | **float** | The Amount being allocated to the invoice. Expects same currency as invoice currency | [optional] 
**allocation_date** | **datetime** | Optional. Defaults to the current time in the Avaza account&#39;s timezone. The date the allocation is applied to the invoice. Can be difference from the Payment Date when doing prepayments etc. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


