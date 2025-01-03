# GetPullRequest200ResponseIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**issue_key** | **str** |  | [optional] 
**key_id** | **int** |  | [optional] 
**issue_type** | [**GetIssues200ResponseInnerIssueType**](GetIssues200ResponseInnerIssueType.md) |  | [optional] 

## Example

```python
from backlog_client.models.get_pull_request200_response_issue import GetPullRequest200ResponseIssue

# TODO update the JSON string below
json = "{}"
# create an instance of GetPullRequest200ResponseIssue from a JSON string
get_pull_request200_response_issue_instance = GetPullRequest200ResponseIssue.from_json(json)
# print the JSON string representation of the object
print(GetPullRequest200ResponseIssue.to_json())

# convert the object into a dict
get_pull_request200_response_issue_dict = get_pull_request200_response_issue_instance.to_dict()
# create an instance of GetPullRequest200ResponseIssue from a dict
get_pull_request200_response_issue_from_dict = GetPullRequest200ResponseIssue.from_dict(get_pull_request200_response_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


