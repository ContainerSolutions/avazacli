# NewProjectModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_idfk** | **int** | An ID of a company in Avaza to create the Project under. You must provide either a CompanyID, or a CompanyName | [optional] 
**company_name** | **str** | The name for a Company to create the project under. Will create company unless it matches an existing company name | [optional] 
**currency_code** | **str** | The ISO 3 letter currency code to use when creating a new Company. If not provided, the account&#39;s default currency will be used. | [optional] 
**project_title** | **str** | The title of the new project. (255 characters max) | 
**project_notes** | **str** | Any descriptive notes about the project. (2000 characters max) | [optional] 
**timesheet_approval_requiredby_default** | **bool** |  | [optional] 
**populate_default_project_members** | **bool** |  | [optional] 
**is_task_required_on_timesheet** | **bool** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**budget_amount** | **float** |  | [optional] 
**budget_hours** | **float** |  | [optional] 
**project_status_code** | **str** |  | [optional] 
**project_category_idfk** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


