# AddIssueCommentNotification200ResponseNotificationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**already_read** | **bool** |  | [optional] 
**reason** | **int** | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 | [optional] 
**user** | [**GetGroups200ResponseInnerCreatedUser**](GetGroups200ResponseInnerCreatedUser.md) |  | [optional] 
**resource_already_read** | **bool** |  | [optional] 

## Example

```python
from backlog_client.models.add_issue_comment_notification200_response_notifications_inner import AddIssueCommentNotification200ResponseNotificationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddIssueCommentNotification200ResponseNotificationsInner from a JSON string
add_issue_comment_notification200_response_notifications_inner_instance = AddIssueCommentNotification200ResponseNotificationsInner.from_json(json)
# print the JSON string representation of the object
print(AddIssueCommentNotification200ResponseNotificationsInner.to_json())

# convert the object into a dict
add_issue_comment_notification200_response_notifications_inner_dict = add_issue_comment_notification200_response_notifications_inner_instance.to_dict()
# create an instance of AddIssueCommentNotification200ResponseNotificationsInner from a dict
add_issue_comment_notification200_response_notifications_inner_from_dict = AddIssueCommentNotification200ResponseNotificationsInner.from_dict(add_issue_comment_notification200_response_notifications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


