# NewExpense

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expense_date** | **datetime** | The date of the expense entry (Required) | [optional] 
**user_idfk** | **int** | UserID for a Timesheet/Expense user in Avaza. If not provided, UserEmail field must be provided | [optional] 
**user_email** | **str** | The email address of a Timesheet/Expense user in Avaza. If not provided, UserIDFK field must be provided. | [optional] 
**expense_category_idfk** | **int** | The expense category to link the Expense to. If not provided, ExpenseCategoryName must be provided | [optional] 
**expense_category_name** | **str** | Must match an existing expense category name otherwise a new category will be created. If left blank Expense Category ID must be provided. | [optional] 
**is_chargeable** | **bool** | aka Billable. Defaults to false if not provided. If set to true, a CustomerIDFK or CustomerName must be provided. | [optional] 
**is_reimbursable** | **bool** | Defaults to false if not provided. | [optional] 
**customer_idfk** | **int** | The Avaza Customer ID to associate the Expense with. Either this field or CustomerName can be provided. | [optional] 
**customer_name** | **str** | The name of an existing customer in Avaza. Must be an exact (case insensitive) match. | [optional] 
**project_idfk** | **int** | The Avaza project ID to associate the Expense with. | [optional] 
**project_name** | **str** | Can work for matching an expense to a project, but only if it&#39;s an exact match for a single project under the customer. | [optional] 
**currency_code** | **str** | A 3-letter ISO CurrencyCode for the expense currency. (e.g. USD). If not provided, defaults to the Account base currency. | [optional] 
**exchange_rate** | **float** | Optional (Only relevant if the expense currency is different to your account currency. If not provided we will look up the market exchange rate for you based on the expense date.) Exchange Rate &#x3D; Expense Currency Amount / Base Currency Amount (e.g. if Expense currency is in AUD, and Base Currency is in USD, Exchange Rate &#x3D; AUD $140 / USD $100 &#x3D; 1.4) | [optional] 
**amount** | **float** | Expense Amount (Required). Must be &amp;gt;&#x3D; 0 | [optional] 
**tax_idfk** | **int** | Avaza Tax ID the expense belongs to. If left blank then Tax Name must be provided. | [optional] 
**tax_name** | **str** | Must exactly match an existing Tax Name that you have configured in Avaza Tax settings. If left blank then Tax ID must be provided. | [optional] 
**transaction_tax_config_code** | **str** | Optional - Enter \&quot;INC\&quot; if the tax amount is included in the expense amount otherwise enter \&quot;EX\&quot; when the amount exlcudes the tax. Defaults to \&quot;Ex\&quot;. The tax amount on the expense will be autocalculated. | [optional] 
**group_trip_name** | **str** | Links the expense to a Grouping/Trip report. If no matching name found, creates a new Group/Trip Report name. | [optional] 
**merchant** | **str** | The name of the merchant. | [optional] 
**merchant_tax_numer** | **str** | A Tax number identifier for the merchant. | [optional] 
**notes** | **str** | Expense Notes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


