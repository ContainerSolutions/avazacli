# ProjectDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_idfk** | **int** |  | [optional] 
**project_status_code** | **str** | Possible values: NotStarted, InProgress, Complete | [optional] 
**is_archived** | **bool** |  | [optional] 
**project_billable_type_code** | **str** | Possible values: CategoryHourly, NoRate, NotBillable, PersonHourly, ProjectHourly | [optional] 
**project_budget_type_code** | **str** | Possible Values: CategoryHours, NoBudget, PersonHours, ProjectFees, ProjectHours | [optional] 
**budget_amount** | **float** |  | [optional] 
**budget_hours** | **float** |  | [optional] 
**project_hourly_rate** | **float** |  | [optional] 
**project_category_idfk** | **int** |  | [optional] 
**project_category_name** | **str** |  | [optional] 
**is_task_required_on_timesheet** | **bool** |  | [optional] 
**project_category_color** | **str** | Html Hex Color Code starting with # | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**sections** | [**list[ProjectSectionDetails]**](ProjectSectionDetails.md) |  | [optional] 
**members** | [**list[ProjectMemberDetails]**](ProjectMemberDetails.md) |  | [optional] 
**project_tags** | [**list[ProjectTagItem]**](ProjectTagItem.md) |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_updated** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


