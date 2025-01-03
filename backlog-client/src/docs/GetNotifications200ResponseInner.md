# GetNotifications200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**already_read** | **bool** |  | [optional] 
**reason** | **int** | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 | [optional] 
**resource_already_read** | **bool** |  | [optional] 
**project** | [**DeleteProject200Response**](DeleteProject200Response.md) |  | [optional] 
**issue** | [**GetNotifications200ResponseInnerIssue**](GetNotifications200ResponseInnerIssue.md) |  | [optional] 
**comment** | [**GetNotifications200ResponseInnerComment**](GetNotifications200ResponseInnerComment.md) |  | [optional] 
**sender** | [**GetNotifications200ResponseInnerSender**](GetNotifications200ResponseInnerSender.md) |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_notifications200_response_inner import GetNotifications200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotifications200ResponseInner from a JSON string
get_notifications200_response_inner_instance = GetNotifications200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetNotifications200ResponseInner.to_json())

# convert the object into a dict
get_notifications200_response_inner_dict = get_notifications200_response_inner_instance.to_dict()
# create an instance of GetNotifications200ResponseInner from a dict
get_notifications200_response_inner_from_dict = GetNotifications200ResponseInner.from_dict(get_notifications200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


