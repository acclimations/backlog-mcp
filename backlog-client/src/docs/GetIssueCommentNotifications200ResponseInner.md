# GetIssueCommentNotifications200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**already_read** | **bool** |  | [optional] 
**reason** | **int** | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 | [optional] 
**user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**resource_already_read** | **bool** |  | [optional] 

## Example

```python
from backlog_client.models.get_issue_comment_notifications200_response_inner import GetIssueCommentNotifications200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssueCommentNotifications200ResponseInner from a JSON string
get_issue_comment_notifications200_response_inner_instance = GetIssueCommentNotifications200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetIssueCommentNotifications200ResponseInner.to_json())

# convert the object into a dict
get_issue_comment_notifications200_response_inner_dict = get_issue_comment_notifications200_response_inner_instance.to_dict()
# create an instance of GetIssueCommentNotifications200ResponseInner from a dict
get_issue_comment_notifications200_response_inner_from_dict = GetIssueCommentNotifications200ResponseInner.from_dict(get_issue_comment_notifications200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


