# GetIssues200ResponseInner


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
**resolution** | **object** |  | [optional] 
**priority** | [**GetIssues200ResponseInnerPriority**](GetIssues200ResponseInnerPriority.md) |  | [optional] 
**status** | [**GetIssues200ResponseInnerIssueType**](GetIssues200ResponseInnerIssueType.md) |  | [optional] 
**assignee** | [**GetGroups200ResponseInnerMembersInner**](GetGroups200ResponseInnerMembersInner.md) |  | [optional] 
**category** | **List[object]** |  | [optional] 
**versions** | **List[object]** |  | [optional] 
**milestone** | [**List[GetIssues200ResponseInnerMilestoneInner]**](GetIssues200ResponseInnerMilestoneInner.md) |  | [optional] 
**start_date** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**estimated_hours** | **float** |  | [optional] 
**actual_hours** | **float** |  | [optional] 
**parent_issue_id** | **int** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 
**custom_fields** | **List[object]** |  | [optional] 
**attachments** | [**List[GetIssues200ResponseInnerAttachmentsInner]**](GetIssues200ResponseInnerAttachmentsInner.md) |  | [optional] 
**shared_files** | [**List[GetIssues200ResponseInnerSharedFilesInner]**](GetIssues200ResponseInnerSharedFilesInner.md) |  | [optional] 
**stars** | [**List[GetIssues200ResponseInnerStarsInner]**](GetIssues200ResponseInnerStarsInner.md) |  | [optional] 

## Example

```python
from backlog_client.models.get_issues200_response_inner import GetIssues200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssues200ResponseInner from a JSON string
get_issues200_response_inner_instance = GetIssues200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetIssues200ResponseInner.to_json())

# convert the object into a dict
get_issues200_response_inner_dict = get_issues200_response_inner_instance.to_dict()
# create an instance of GetIssues200ResponseInner from a dict
get_issues200_response_inner_from_dict = GetIssues200ResponseInner.from_dict(get_issues200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


