# GetNotifications200ResponseInnerComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**issue_id** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_notifications200_response_inner_comment import GetNotifications200ResponseInnerComment

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotifications200ResponseInnerComment from a JSON string
get_notifications200_response_inner_comment_instance = GetNotifications200ResponseInnerComment.from_json(json)
# print the JSON string representation of the object
print(GetNotifications200ResponseInnerComment.to_json())

# convert the object into a dict
get_notifications200_response_inner_comment_dict = get_notifications200_response_inner_comment_instance.to_dict()
# create an instance of GetNotifications200ResponseInnerComment from a dict
get_notifications200_response_inner_comment_from_dict = GetNotifications200ResponseInnerComment.from_dict(get_notifications200_response_inner_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


