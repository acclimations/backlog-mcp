# GetRecentlyViewedIssues200ResponseIssueMilestoneInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**release_due_date** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 

## Example

```python
from backlog_client.models.get_recently_viewed_issues200_response_issue_milestone_inner import GetRecentlyViewedIssues200ResponseIssueMilestoneInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecentlyViewedIssues200ResponseIssueMilestoneInner from a JSON string
get_recently_viewed_issues200_response_issue_milestone_inner_instance = GetRecentlyViewedIssues200ResponseIssueMilestoneInner.from_json(json)
# print the JSON string representation of the object
print(GetRecentlyViewedIssues200ResponseIssueMilestoneInner.to_json())

# convert the object into a dict
get_recently_viewed_issues200_response_issue_milestone_inner_dict = get_recently_viewed_issues200_response_issue_milestone_inner_instance.to_dict()
# create an instance of GetRecentlyViewedIssues200ResponseIssueMilestoneInner from a dict
get_recently_viewed_issues200_response_issue_milestone_inner_from_dict = GetRecentlyViewedIssues200ResponseIssueMilestoneInner.from_dict(get_recently_viewed_issues200_response_issue_milestone_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


