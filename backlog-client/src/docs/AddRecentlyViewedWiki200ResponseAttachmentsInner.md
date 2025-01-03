# AddRecentlyViewedWiki200ResponseAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.add_recently_viewed_wiki200_response_attachments_inner import AddRecentlyViewedWiki200ResponseAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddRecentlyViewedWiki200ResponseAttachmentsInner from a JSON string
add_recently_viewed_wiki200_response_attachments_inner_instance = AddRecentlyViewedWiki200ResponseAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(AddRecentlyViewedWiki200ResponseAttachmentsInner.to_json())

# convert the object into a dict
add_recently_viewed_wiki200_response_attachments_inner_dict = add_recently_viewed_wiki200_response_attachments_inner_instance.to_dict()
# create an instance of AddRecentlyViewedWiki200ResponseAttachmentsInner from a dict
add_recently_viewed_wiki200_response_attachments_inner_from_dict = AddRecentlyViewedWiki200ResponseAttachmentsInner.from_dict(add_recently_viewed_wiki200_response_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


