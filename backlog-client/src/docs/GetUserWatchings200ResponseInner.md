# GetUserWatchings200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**resource_already_read** | **bool** |  | [optional] 
**note** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**issue** | [**AddWatching201ResponseIssue**](AddWatching201ResponseIssue.md) |  | [optional] 
**last_content_updated** | **datetime** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_user_watchings200_response_inner import GetUserWatchings200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserWatchings200ResponseInner from a JSON string
get_user_watchings200_response_inner_instance = GetUserWatchings200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetUserWatchings200ResponseInner.to_json())

# convert the object into a dict
get_user_watchings200_response_inner_dict = get_user_watchings200_response_inner_instance.to_dict()
# create an instance of GetUserWatchings200ResponseInner from a dict
get_user_watchings200_response_inner_from_dict = GetUserWatchings200ResponseInner.from_dict(get_user_watchings200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


