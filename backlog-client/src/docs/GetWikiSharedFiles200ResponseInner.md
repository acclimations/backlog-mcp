# GetWikiSharedFiles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**dir** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | **object** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_wiki_shared_files200_response_inner import GetWikiSharedFiles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWikiSharedFiles200ResponseInner from a JSON string
get_wiki_shared_files200_response_inner_instance = GetWikiSharedFiles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetWikiSharedFiles200ResponseInner.to_json())

# convert the object into a dict
get_wiki_shared_files200_response_inner_dict = get_wiki_shared_files200_response_inner_instance.to_dict()
# create an instance of GetWikiSharedFiles200ResponseInner from a dict
get_wiki_shared_files200_response_inner_from_dict = GetWikiSharedFiles200ResponseInner.from_dict(get_wiki_shared_files200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


