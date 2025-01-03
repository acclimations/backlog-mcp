# GetMyRecentlyViewedWikis200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**GetMyRecentlyViewedWikis200ResponsePage**](GetMyRecentlyViewedWikis200ResponsePage.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_my_recently_viewed_wikis200_response import GetMyRecentlyViewedWikis200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyRecentlyViewedWikis200Response from a JSON string
get_my_recently_viewed_wikis200_response_instance = GetMyRecentlyViewedWikis200Response.from_json(json)
# print the JSON string representation of the object
print(GetMyRecentlyViewedWikis200Response.to_json())

# convert the object into a dict
get_my_recently_viewed_wikis200_response_dict = get_my_recently_viewed_wikis200_response_instance.to_dict()
# create an instance of GetMyRecentlyViewedWikis200Response from a dict
get_my_recently_viewed_wikis200_response_from_dict = GetMyRecentlyViewedWikis200Response.from_dict(get_my_recently_viewed_wikis200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


