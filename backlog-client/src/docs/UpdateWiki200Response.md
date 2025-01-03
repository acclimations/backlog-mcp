# UpdateWiki200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**tags** | [**List[GetIssue200ResponsePriority]**](GetIssue200ResponsePriority.md) |  | [optional] 
**attachments** | [**List[DeletePullRequestAttachment200Response]**](DeletePullRequestAttachment200Response.md) |  | [optional] 
**shared_files** | [**List[UpdateWiki200ResponseSharedFilesInner]**](UpdateWiki200ResponseSharedFilesInner.md) |  | [optional] 
**stars** | **List[object]** |  | [optional] 
**created_user** | [**User**](User.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**User**](User.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.update_wiki200_response import UpdateWiki200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWiki200Response from a JSON string
update_wiki200_response_instance = UpdateWiki200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateWiki200Response.to_json())

# convert the object into a dict
update_wiki200_response_dict = update_wiki200_response_instance.to_dict()
# create an instance of UpdateWiki200Response from a dict
update_wiki200_response_from_dict = UpdateWiki200Response.from_dict(update_wiki200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


