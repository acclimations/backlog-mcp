# GetMyRecentlyViewedWikis200ResponsePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**tags** | [**List[GetIssues200ResponseInnerPriority]**](GetIssues200ResponseInnerPriority.md) |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_my_recently_viewed_wikis200_response_page import GetMyRecentlyViewedWikis200ResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyRecentlyViewedWikis200ResponsePage from a JSON string
get_my_recently_viewed_wikis200_response_page_instance = GetMyRecentlyViewedWikis200ResponsePage.from_json(json)
# print the JSON string representation of the object
print(GetMyRecentlyViewedWikis200ResponsePage.to_json())

# convert the object into a dict
get_my_recently_viewed_wikis200_response_page_dict = get_my_recently_viewed_wikis200_response_page_instance.to_dict()
# create an instance of GetMyRecentlyViewedWikis200ResponsePage from a dict
get_my_recently_viewed_wikis200_response_page_from_dict = GetMyRecentlyViewedWikis200ResponsePage.from_dict(get_my_recently_viewed_wikis200_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


