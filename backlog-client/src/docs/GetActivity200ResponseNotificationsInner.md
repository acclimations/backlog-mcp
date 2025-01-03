# GetActivity200ResponseNotificationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**already_read** | **bool** |  | [optional] 
**reason** | **int** | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 | [optional] 
**user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 

## Example

```python
from backlog_client.models.get_activity200_response_notifications_inner import GetActivity200ResponseNotificationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetActivity200ResponseNotificationsInner from a JSON string
get_activity200_response_notifications_inner_instance = GetActivity200ResponseNotificationsInner.from_json(json)
# print the JSON string representation of the object
print(GetActivity200ResponseNotificationsInner.to_json())

# convert the object into a dict
get_activity200_response_notifications_inner_dict = get_activity200_response_notifications_inner_instance.to_dict()
# create an instance of GetActivity200ResponseNotificationsInner from a dict
get_activity200_response_notifications_inner_from_dict = GetActivity200ResponseNotificationsInner.from_dict(get_activity200_response_notifications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


