# UpdateWiki200ResponseSharedFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**dir** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**created_user** | [**User**](User.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**User**](User.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.update_wiki200_response_shared_files_inner import UpdateWiki200ResponseSharedFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWiki200ResponseSharedFilesInner from a JSON string
update_wiki200_response_shared_files_inner_instance = UpdateWiki200ResponseSharedFilesInner.from_json(json)
# print the JSON string representation of the object
print(UpdateWiki200ResponseSharedFilesInner.to_json())

# convert the object into a dict
update_wiki200_response_shared_files_inner_dict = update_wiki200_response_shared_files_inner_instance.to_dict()
# create an instance of UpdateWiki200ResponseSharedFilesInner from a dict
update_wiki200_response_shared_files_inner_from_dict = UpdateWiki200ResponseSharedFilesInner.from_dict(update_wiki200_response_shared_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


