# GetGroups200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**members** | [**List[GetGroups200ResponseInnerMembersInner]**](GetGroups200ResponseInnerMembersInner.md) |  | [optional] 
**display_order** | **int** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroups200ResponseInner from a JSON string
get_groups200_response_inner_instance = GetGroups200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetGroups200ResponseInner.to_json())

# convert the object into a dict
get_groups200_response_inner_dict = get_groups200_response_inner_instance.to_dict()
# create an instance of GetGroups200ResponseInner from a dict
get_groups200_response_inner_from_dict = GetGroups200ResponseInner.from_dict(get_groups200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


