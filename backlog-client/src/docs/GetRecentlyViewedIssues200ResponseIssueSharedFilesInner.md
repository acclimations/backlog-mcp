# GetRecentlyViewedIssues200ResponseIssueSharedFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**dir** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_recently_viewed_issues200_response_issue_shared_files_inner import GetRecentlyViewedIssues200ResponseIssueSharedFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecentlyViewedIssues200ResponseIssueSharedFilesInner from a JSON string
get_recently_viewed_issues200_response_issue_shared_files_inner_instance = GetRecentlyViewedIssues200ResponseIssueSharedFilesInner.from_json(json)
# print the JSON string representation of the object
print(GetRecentlyViewedIssues200ResponseIssueSharedFilesInner.to_json())

# convert the object into a dict
get_recently_viewed_issues200_response_issue_shared_files_inner_dict = get_recently_viewed_issues200_response_issue_shared_files_inner_instance.to_dict()
# create an instance of GetRecentlyViewedIssues200ResponseIssueSharedFilesInner from a dict
get_recently_viewed_issues200_response_issue_shared_files_inner_from_dict = GetRecentlyViewedIssues200ResponseIssueSharedFilesInner.from_dict(get_recently_viewed_issues200_response_issue_shared_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


