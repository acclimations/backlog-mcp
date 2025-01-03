# DeleteWatching200ResponseIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**issue_key** | **str** |  | [optional] 
**key_id** | **int** |  | [optional] 
**issue_type** | [**GetIssues200ResponseInnerIssueType**](GetIssues200ResponseInnerIssueType.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**resolution** | **str** |  | [optional] 
**priority** | [**GetIssues200ResponseInnerPriority**](GetIssues200ResponseInnerPriority.md) |  | [optional] 
**status** | [**GetIssues200ResponseInnerIssueType**](GetIssues200ResponseInnerIssueType.md) |  | [optional] 
**assignee** | [**GetGroups200ResponseInnerMembersInner**](GetGroups200ResponseInnerMembersInner.md) |  | [optional] 
**category** | **List[str]** |  | [optional] 
**versions** | **List[str]** |  | [optional] 
**milestone** | **List[str]** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**estimated_hours** | **float** |  | [optional] 
**actual_hours** | **float** |  | [optional] 
**parent_issue_id** | **int** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 
**custom_fields** | **List[str]** |  | [optional] 
**attachments** | **List[str]** |  | [optional] 
**shared_files** | **List[str]** |  | [optional] 
**stars** | **List[str]** |  | [optional] 

## Example

```python
from backlog_client.models.delete_watching200_response_issue import DeleteWatching200ResponseIssue

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWatching200ResponseIssue from a JSON string
delete_watching200_response_issue_instance = DeleteWatching200ResponseIssue.from_json(json)
# print the JSON string representation of the object
print(DeleteWatching200ResponseIssue.to_json())

# convert the object into a dict
delete_watching200_response_issue_dict = delete_watching200_response_issue_instance.to_dict()
# create an instance of DeleteWatching200ResponseIssue from a dict
delete_watching200_response_issue_from_dict = DeleteWatching200ResponseIssue.from_dict(delete_watching200_response_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


