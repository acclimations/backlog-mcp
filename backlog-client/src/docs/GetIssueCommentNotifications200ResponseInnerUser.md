# GetIssueCommentNotifications200ResponseInnerUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role_type** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 
**nulab_account** | [**GetIssueCommentNotifications200ResponseInnerUserNulabAccount**](GetIssueCommentNotifications200ResponseInnerUserNulabAccount.md) |  | [optional] 
**mail_address** | **str** |  | [optional] 
**last_login_time** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssueCommentNotifications200ResponseInnerUser from a JSON string
get_issue_comment_notifications200_response_inner_user_instance = GetIssueCommentNotifications200ResponseInnerUser.from_json(json)
# print the JSON string representation of the object
print(GetIssueCommentNotifications200ResponseInnerUser.to_json())

# convert the object into a dict
get_issue_comment_notifications200_response_inner_user_dict = get_issue_comment_notifications200_response_inner_user_instance.to_dict()
# create an instance of GetIssueCommentNotifications200ResponseInnerUser from a dict
get_issue_comment_notifications200_response_inner_user_from_dict = GetIssueCommentNotifications200ResponseInnerUser.from_dict(get_issue_comment_notifications200_response_inner_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


