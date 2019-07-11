# NewTimesheet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_idfk** | **int** | UserID for a Timesheet user in Avaza | [optional] 
**project_idfk** | **int** | The project to associate the timesheet with. | [optional] 
**timesheet_category_idfk** | **int** | The Project timesheet category to link the timesheet to | [optional] 
**duration** | **float** | The duration of the timesheet, in decimal hours. If null or 0, a timer will be started. | [optional] 
**is_invoiced** | **bool** | Optional. False by default. Allows you to mark the timesheet as invoiced in an external system. | [optional] 
**entry_date** | **datetime** | The date of the timesheet entry, with an optional start time component. | [optional] 
**has_start_end_time** | **bool** | If true, the start time will be take from the time component of the Entry Date field, and the end time will be calculated by adding the Duration to the StartDate | [optional] 
**notes** | **str** | Timesheet Notes | [optional] 
**task_idfk** | **int** | Optional. Link the timesheet to a specific task | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


