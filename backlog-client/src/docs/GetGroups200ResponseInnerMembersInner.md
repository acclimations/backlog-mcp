# GetGroups200ResponseInnerMembersInner


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
from backlog_client.models.get_groups200_response_inner_members_inner import GetGroups200ResponseInnerMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroups200ResponseInnerMembersInner from a JSON string
get_groups200_response_inner_members_inner_instance = GetGroups200ResponseInnerMembersInner.from_json(json)
# print the JSON string representation of the object
print(GetGroups200ResponseInnerMembersInner.to_json())

# convert the object into a dict
get_groups200_response_inner_members_inner_dict = get_groups200_response_inner_members_inner_instance.to_dict()
# create an instance of GetGroups200ResponseInnerMembersInner from a dict
get_groups200_response_inner_members_inner_from_dict = GetGroups200ResponseInnerMembersInner.from_dict(get_groups200_response_inner_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


