# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **int** |  | [optional] 
**account_idfk** | **int** |  | [optional] 
**transaction_prefix** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**company_idfk** | **int** |  | [optional] 
**company_name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**date_issued** | **datetime** |  | [optional] 
**date_sent** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**transaction_status_code** | **str** |  | [optional] 
**tax_amount** | **float** |  | [optional] 
**transaction_tax_config_code** | **str** |  | [optional] 
**balance** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**total_amount** | **float** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**notes** | **str** |  | [optional] 
**customer_po_number** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_updated** | **datetime** |  | [optional] 
**line_items** | [**list[InvoiceLineItem]**](InvoiceLineItem.md) |  | [optional] 
**links** | [**InvoiceLinks**](InvoiceLinks.md) |  | [optional] 
**issuer** | [**IssuerDetails**](IssuerDetails.md) |  | [optional] 
**recipient** | [**RecipientDetails**](RecipientDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


