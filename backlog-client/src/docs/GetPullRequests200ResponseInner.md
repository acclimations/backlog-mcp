# GetPullRequests200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**repository_id** | **int** |  | [optional] 
**number** | **int** |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**base** | **str** |  | [optional] 
**branch** | **str** |  | [optional] 
**status** | [**GetIssues200ResponseInnerPriority**](GetIssues200ResponseInnerPriority.md) |  | [optional] 
**assignee** | [**GetGroups200ResponseInnerMembersInner**](GetGroups200ResponseInnerMembersInner.md) |  | [optional] 
**issue** | [**GetPullRequests200ResponseInnerIssue**](GetPullRequests200ResponseInnerIssue.md) |  | [optional] 
**base_commit** | **str** |  | [optional] 
**branch_commit** | **str** |  | [optional] 
**merge_commit** | **str** |  | [optional] 
**close_at** | **datetime** |  | [optional] 
**merge_at** | **datetime** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_pull_requests200_response_inner import GetPullRequests200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPullRequests200ResponseInner from a JSON string
get_pull_requests200_response_inner_instance = GetPullRequests200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetPullRequests200ResponseInner.to_json())

# convert the object into a dict
get_pull_requests200_response_inner_dict = get_pull_requests200_response_inner_instance.to_dict()
# create an instance of GetPullRequests200ResponseInner from a dict
get_pull_requests200_response_inner_from_dict = GetPullRequests200ResponseInner.from_dict(get_pull_requests200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


