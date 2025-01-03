# GetActivity200ResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**key_id** | **int** |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**comment** | [**GetActivity200ResponseContentComment**](GetActivity200ResponseContentComment.md) |  | [optional] 
**changes** | [**List[GetActivity200ResponseContentChangesInner]**](GetActivity200ResponseContentChangesInner.md) |  | [optional] 

## Example

```python
from backlog_client.models.get_activity200_response_content import GetActivity200ResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetActivity200ResponseContent from a JSON string
get_activity200_response_content_instance = GetActivity200ResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetActivity200ResponseContent.to_json())

# convert the object into a dict
get_activity200_response_content_dict = get_activity200_response_content_instance.to_dict()
# create an instance of GetActivity200ResponseContent from a dict
get_activity200_response_content_from_dict = GetActivity200ResponseContent.from_dict(get_activity200_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


