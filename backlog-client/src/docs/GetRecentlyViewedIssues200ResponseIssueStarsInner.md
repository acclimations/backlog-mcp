# GetRecentlyViewedIssues200ResponseIssueStarsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**presenter** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_recently_viewed_issues200_response_issue_stars_inner import GetRecentlyViewedIssues200ResponseIssueStarsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecentlyViewedIssues200ResponseIssueStarsInner from a JSON string
get_recently_viewed_issues200_response_issue_stars_inner_instance = GetRecentlyViewedIssues200ResponseIssueStarsInner.from_json(json)
# print the JSON string representation of the object
print(GetRecentlyViewedIssues200ResponseIssueStarsInner.to_json())

# convert the object into a dict
get_recently_viewed_issues200_response_issue_stars_inner_dict = get_recently_viewed_issues200_response_issue_stars_inner_instance.to_dict()
# create an instance of GetRecentlyViewedIssues200ResponseIssueStarsInner from a dict
get_recently_viewed_issues200_response_issue_stars_inner_from_dict = GetRecentlyViewedIssues200ResponseIssueStarsInner.from_dict(get_recently_viewed_issues200_response_issue_stars_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


