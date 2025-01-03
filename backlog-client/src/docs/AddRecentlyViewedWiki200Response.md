# AddRecentlyViewedWiki200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**tags** | [**List[GetIssues200ResponseInnerPriority]**](GetIssues200ResponseInnerPriority.md) |  | [optional] 
**attachments** | [**List[AddRecentlyViewedWiki200ResponseAttachmentsInner]**](AddRecentlyViewedWiki200ResponseAttachmentsInner.md) |  | [optional] 
**shared_files** | [**List[GetRecentlyViewedIssues200ResponseIssueSharedFilesInner]**](GetRecentlyViewedIssues200ResponseIssueSharedFilesInner.md) |  | [optional] 
**stars** | **List[object]** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.add_recently_viewed_wiki200_response import AddRecentlyViewedWiki200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddRecentlyViewedWiki200Response from a JSON string
add_recently_viewed_wiki200_response_instance = AddRecentlyViewedWiki200Response.from_json(json)
# print the JSON string representation of the object
print(AddRecentlyViewedWiki200Response.to_json())

# convert the object into a dict
add_recently_viewed_wiki200_response_dict = add_recently_viewed_wiki200_response_instance.to_dict()
# create an instance of AddRecentlyViewedWiki200Response from a dict
add_recently_viewed_wiki200_response_from_dict = AddRecentlyViewedWiki200Response.from_dict(add_recently_viewed_wiki200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


