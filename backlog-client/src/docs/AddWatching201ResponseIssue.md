# AddWatching201ResponseIssue


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
**category** | **List[object]** |  | [optional] 
**versions** | **List[object]** |  | [optional] 
**milestone** | **List[object]** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**estimated_hours** | **float** |  | [optional] 
**actual_hours** | **float** |  | [optional] 
**parent_issue_id** | **int** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 
**custom_fields** | **List[object]** |  | [optional] 
**attachments** | **List[object]** |  | [optional] 
**shared_files** | **List[object]** |  | [optional] 
**stars** | **List[object]** |  | [optional] 

## Example

```python
from backlog_client.models.add_watching201_response_issue import AddWatching201ResponseIssue

# TODO update the JSON string below
json = "{}"
# create an instance of AddWatching201ResponseIssue from a JSON string
add_watching201_response_issue_instance = AddWatching201ResponseIssue.from_json(json)
# print the JSON string representation of the object
print(AddWatching201ResponseIssue.to_json())

# convert the object into a dict
add_watching201_response_issue_dict = add_watching201_response_issue_instance.to_dict()
# create an instance of AddWatching201ResponseIssue from a dict
add_watching201_response_issue_from_dict = AddWatching201ResponseIssue.from_dict(add_watching201_response_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


