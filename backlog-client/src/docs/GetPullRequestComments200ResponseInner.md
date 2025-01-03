# GetPullRequestComments200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**change_log** | [**List[GetPullRequestComments200ResponseInnerChangeLogInner]**](GetPullRequestComments200ResponseInnerChangeLogInner.md) |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**stars** | **List[object]** |  | [optional] 
**notifications** | **List[object]** |  | [optional] 

## Example

```python
from backlog_client.models.get_pull_request_comments200_response_inner import GetPullRequestComments200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPullRequestComments200ResponseInner from a JSON string
get_pull_request_comments200_response_inner_instance = GetPullRequestComments200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetPullRequestComments200ResponseInner.to_json())

# convert the object into a dict
get_pull_request_comments200_response_inner_dict = get_pull_request_comments200_response_inner_instance.to_dict()
# create an instance of GetPullRequestComments200ResponseInner from a dict
get_pull_request_comments200_response_inner_from_dict = GetPullRequestComments200ResponseInner.from_dict(get_pull_request_comments200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


