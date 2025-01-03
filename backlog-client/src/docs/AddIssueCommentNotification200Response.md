# AddIssueCommentNotification200Response


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
**notifications** | [**List[GetIssueCommentNotifications200ResponseInner]**](GetIssueCommentNotifications200ResponseInner.md) |  | [optional] 

## Example

```python
from backlog_client.models.add_issue_comment_notification200_response import AddIssueCommentNotification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddIssueCommentNotification200Response from a JSON string
add_issue_comment_notification200_response_instance = AddIssueCommentNotification200Response.from_json(json)
# print the JSON string representation of the object
print(AddIssueCommentNotification200Response.to_json())

# convert the object into a dict
add_issue_comment_notification200_response_dict = add_issue_comment_notification200_response_instance.to_dict()
# create an instance of AddIssueCommentNotification200Response from a dict
add_issue_comment_notification200_response_from_dict = AddIssueCommentNotification200Response.from_dict(add_issue_comment_notification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


