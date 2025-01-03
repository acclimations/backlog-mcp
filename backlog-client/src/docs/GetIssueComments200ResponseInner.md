# GetIssueComments200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**issue_id** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**change_log** | **object** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**stars** | **List[object]** |  | [optional] 
**notifications** | **List[object]** |  | [optional] 

## Example

```python
from backlog_client.models.get_issue_comments200_response_inner import GetIssueComments200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssueComments200ResponseInner from a JSON string
get_issue_comments200_response_inner_instance = GetIssueComments200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetIssueComments200ResponseInner.to_json())

# convert the object into a dict
get_issue_comments200_response_inner_dict = get_issue_comments200_response_inner_instance.to_dict()
# create an instance of GetIssueComments200ResponseInner from a dict
get_issue_comments200_response_inner_from_dict = GetIssueComments200ResponseInner.from_dict(get_issue_comments200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


