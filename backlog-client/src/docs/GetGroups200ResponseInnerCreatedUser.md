# GetGroups200ResponseInnerCreatedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role_type** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 
**nulab_account** | [**GetGroups200ResponseInnerMembersInnerNulabAccount**](GetGroups200ResponseInnerMembersInnerNulabAccount.md) |  | [optional] 
**mail_address** | **str** |  | [optional] 
**last_login_time** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_groups200_response_inner_created_user import GetGroups200ResponseInnerCreatedUser

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroups200ResponseInnerCreatedUser from a JSON string
get_groups200_response_inner_created_user_instance = GetGroups200ResponseInnerCreatedUser.from_json(json)
# print the JSON string representation of the object
print(GetGroups200ResponseInnerCreatedUser.to_json())

# convert the object into a dict
get_groups200_response_inner_created_user_dict = get_groups200_response_inner_created_user_instance.to_dict()
# create an instance of GetGroups200ResponseInnerCreatedUser from a dict
get_groups200_response_inner_created_user_from_dict = GetGroups200ResponseInnerCreatedUser.from_dict(get_groups200_response_inner_created_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


