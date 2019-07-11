# NewInvoiceLineItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_idfk** | **int** | If not specified then Inventory Item Name must be specified. | [optional] 
**inventory_item_name** | **str** | If not specified then Inventory item ID must be specified. If specified and not matched to any existing inventory items then a new inventory item will be created. Max 200 characters. | [optional] 
**description** | **str** | Plain UTF8 text. (no HTML) | [optional] 
**quantity** | **float** | The quantity for the line item | 
**unit_price** | **float** | The unit price for the lineitem. | 
**tax_idfk** | **int** |  | [optional] 
**tax_name** | **str** | Must be specified if the Tax ID is blank. If the Tax Name is specified it will be matched to an existing Tax Name or else a new Tax will be created. | [optional] 
**tax_percent** | **float** | The Tax Percent will only be used if a new tax is being created. | [optional] 
**discount** | **float** | Enter 10.5 to give a 10.5% discount | [optional] 
**project_idfk** | **int** | Optional. Project ID of an Avaza Project that belongs to this customer, so line item is attributed to that Project for reporting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


