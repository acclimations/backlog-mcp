# GetUserActivities200ResponseInnerContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**key_id** | **int** |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**comment** | [**GetUserActivities200ResponseInnerContentComment**](GetUserActivities200ResponseInnerContentComment.md) |  | [optional] 
**changes** | [**List[GetUserActivities200ResponseInnerContentChangesInner]**](GetUserActivities200ResponseInnerContentChangesInner.md) |  | [optional] 

## Example

```python
from backlog_client.models.get_user_activities200_response_inner_content import GetUserActivities200ResponseInnerContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserActivities200ResponseInnerContent from a JSON string
get_user_activities200_response_inner_content_instance = GetUserActivities200ResponseInnerContent.from_json(json)
# print the JSON string representation of the object
print(GetUserActivities200ResponseInnerContent.to_json())

# convert the object into a dict
get_user_activities200_response_inner_content_dict = get_user_activities200_response_inner_content_instance.to_dict()
# create an instance of GetUserActivities200ResponseInnerContent from a dict
get_user_activities200_response_inner_content_from_dict = GetUserActivities200ResponseInnerContent.from_dict(get_user_activities200_response_inner_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


