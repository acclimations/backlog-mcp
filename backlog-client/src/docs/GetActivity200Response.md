# GetActivity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project** | [**DeleteProject200Response**](DeleteProject200Response.md) |  | [optional] 
**type** | **int** | 最近の更新の種別：1:課題の追加2:課題の更新3:課題にコメント4:課題の削除5:Wikiを追加6:Wikiを更新7:Wikiを削除8:共有ファイルを追加9:共有ファイルを更新10:共有ファイルを削除11:Subversionコミット12:GITプッシュ13:GITリポジトリ作成14:課題をまとめて更新15:ユーザーがプロジェクトに参加16:ユーザーがプロジェクトから脱退17:コメントにお知らせを追加18:プルリクエストの追加19:プルリクエストの更新20:プルリクエストにコメント21:プルリクエストの削除22:マイルストーンの追加23:マイルストーンの更新24:マイルストーンの削除25:グループがプロジェクトに参加26:グループがプロジェクトから脱退 | [optional] 
**content** | [**GetActivity200ResponseContent**](GetActivity200ResponseContent.md) |  | [optional] 
**notifications** | [**List[GetActivity200ResponseNotificationsInner]**](GetActivity200ResponseNotificationsInner.md) |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_activity200_response import GetActivity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetActivity200Response from a JSON string
get_activity200_response_instance = GetActivity200Response.from_json(json)
# print the JSON string representation of the object
print(GetActivity200Response.to_json())

# convert the object into a dict
get_activity200_response_dict = get_activity200_response_instance.to_dict()
# create an instance of GetActivity200Response from a dict
get_activity200_response_from_dict = GetActivity200Response.from_dict(get_activity200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


