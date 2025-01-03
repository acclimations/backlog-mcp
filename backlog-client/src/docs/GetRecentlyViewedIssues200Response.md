# GetRecentlyViewedIssues200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue** | [**GetRecentlyViewedIssues200ResponseIssue**](GetRecentlyViewedIssues200ResponseIssue.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_recently_viewed_issues200_response import GetRecentlyViewedIssues200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecentlyViewedIssues200Response from a JSON string
get_recently_viewed_issues200_response_instance = GetRecentlyViewedIssues200Response.from_json(json)
# print the JSON string representation of the object
print(GetRecentlyViewedIssues200Response.to_json())

# convert the object into a dict
get_recently_viewed_issues200_response_dict = get_recently_viewed_issues200_response_instance.to_dict()
# create an instance of GetRecentlyViewedIssues200Response from a dict
get_recently_viewed_issues200_response_from_dict = GetRecentlyViewedIssues200Response.from_dict(get_recently_viewed_issues200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


