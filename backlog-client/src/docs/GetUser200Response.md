# GetUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role_type** | **int** | クラシックプランの場合:1 管理者2 一般ユーザー3 レポーター4 ビューワー5 ゲストレポーター6 ゲストビューワー新プランの場合:1 管理者2 一般ユーザー、ゲスト（制限：制限なし）3 一般ユーザー、ゲスト（制限：課題の登録のみ）4 一般ユーザー、ゲスト（制限：課題の閲覧のみ） | [optional] 
**lang** | **str** | \\\&quot;en\\\&quot; 英語\\\&quot;ja\\\&quot; 日本語null 未指定 | [optional] 
**nulab_account** | [**GetGroups200ResponseInnerMembersInnerNulabAccount**](GetGroups200ResponseInnerMembersInnerNulabAccount.md) |  | [optional] 
**mail_address** | **str** |  | [optional] 
**last_login_time** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_user200_response import GetUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUser200Response from a JSON string
get_user200_response_instance = GetUser200Response.from_json(json)
# print the JSON string representation of the object
print(GetUser200Response.to_json())

# convert the object into a dict
get_user200_response_dict = get_user200_response_instance.to_dict()
# create an instance of GetUser200Response from a dict
get_user200_response_from_dict = GetUser200Response.from_dict(get_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


