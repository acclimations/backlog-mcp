# GetRecentlyViewedIssues200ResponseIssue


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
**milestone** | [**List[GetRecentlyViewedIssues200ResponseIssueMilestoneInner]**](GetRecentlyViewedIssues200ResponseIssueMilestoneInner.md) |  | [optional] 
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
**shared_files** | [**List[GetRecentlyViewedIssues200ResponseIssueSharedFilesInner]**](GetRecentlyViewedIssues200ResponseIssueSharedFilesInner.md) |  | [optional] 
**stars** | [**List[GetRecentlyViewedIssues200ResponseIssueStarsInner]**](GetRecentlyViewedIssues200ResponseIssueStarsInner.md) |  | [optional] 

## Example

```python
from backlog_client.models.get_recently_viewed_issues200_response_issue import GetRecentlyViewedIssues200ResponseIssue

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecentlyViewedIssues200ResponseIssue from a JSON string
get_recently_viewed_issues200_response_issue_instance = GetRecentlyViewedIssues200ResponseIssue.from_json(json)
# print the JSON string representation of the object
print(GetRecentlyViewedIssues200ResponseIssue.to_json())

# convert the object into a dict
get_recently_viewed_issues200_response_issue_dict = get_recently_viewed_issues200_response_issue_instance.to_dict()
# create an instance of GetRecentlyViewedIssues200ResponseIssue from a dict
get_recently_viewed_issues200_response_issue_from_dict = GetRecentlyViewedIssues200ResponseIssue.from_dict(get_recently_viewed_issues200_response_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


