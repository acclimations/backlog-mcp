# GetIssue200ResponseStarsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**presenter** | [**GetGroups200ResponseInnerCreatedUser**](GetGroups200ResponseInnerCreatedUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_issue200_response_stars_inner import GetIssue200ResponseStarsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssue200ResponseStarsInner from a JSON string
get_issue200_response_stars_inner_instance = GetIssue200ResponseStarsInner.from_json(json)
# print the JSON string representation of the object
print(GetIssue200ResponseStarsInner.to_json())

# convert the object into a dict
get_issue200_response_stars_inner_dict = get_issue200_response_stars_inner_instance.to_dict()
# create an instance of GetIssue200ResponseStarsInner from a dict
get_issue200_response_stars_inner_from_dict = GetIssue200ResponseStarsInner.from_dict(get_issue200_response_stars_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


