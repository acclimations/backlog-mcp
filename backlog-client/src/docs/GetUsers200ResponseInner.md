# GetUsers200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role_type** | **int** | ユーザーの権限。利用するスペースの契約プランにより値の意味が異なります。クラシックプランの場合:1 管理者2 一般ユーザー3 レポーター4 ビューワー5 ゲストレポーター6 ゲストビューワー新プランの場合:1 管理者2 一般ユーザー、ゲスト（制限：制限なし）3 一般ユーザー、ゲスト（制限：課題の登録のみ）4 一般ユーザー、ゲスト（制限：課題の閲覧のみ） | [optional] 
**lang** | **str** | ユーザーの言語設定。\\\&quot;en\\\&quot; 英語\\\&quot;ja\\\&quot; 日本語null 未指定 | [optional] 
**nulab_account** | [**GetIssueCommentNotifications200ResponseInnerUserNulabAccount**](GetIssueCommentNotifications200ResponseInnerUserNulabAccount.md) |  | [optional] 
**mail_address** | **str** |  | [optional] 
**last_login_time** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_users200_response_inner import GetUsers200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsers200ResponseInner from a JSON string
get_users200_response_inner_instance = GetUsers200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetUsers200ResponseInner.to_json())

# convert the object into a dict
get_users200_response_inner_dict = get_users200_response_inner_instance.to_dict()
# create an instance of GetUsers200ResponseInner from a dict
get_users200_response_inner_from_dict = GetUsers200ResponseInner.from_dict(get_users200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


