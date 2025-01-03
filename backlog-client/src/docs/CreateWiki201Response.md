# CreateWiki201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**tags** | [**List[GetIssues200ResponseInnerPriority]**](GetIssues200ResponseInnerPriority.md) |  | [optional] 
**attachments** | **List[object]** |  | [optional] 
**shared_files** | **List[object]** |  | [optional] 
**stars** | **List[object]** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.create_wiki201_response import CreateWiki201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWiki201Response from a JSON string
create_wiki201_response_instance = CreateWiki201Response.from_json(json)
# print the JSON string representation of the object
print(CreateWiki201Response.to_json())

# convert the object into a dict
create_wiki201_response_dict = create_wiki201_response_instance.to_dict()
# create an instance of CreateWiki201Response from a dict
create_wiki201_response_from_dict = CreateWiki201Response.from_dict(create_wiki201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


