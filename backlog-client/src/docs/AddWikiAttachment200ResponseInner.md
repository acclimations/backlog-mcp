# AddWikiAttachment200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**created_user** | [**GetGroups200ResponseInnerMembersInner**](GetGroups200ResponseInnerMembersInner.md) |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.add_wiki_attachment200_response_inner import AddWikiAttachment200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddWikiAttachment200ResponseInner from a JSON string
add_wiki_attachment200_response_inner_instance = AddWikiAttachment200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(AddWikiAttachment200ResponseInner.to_json())

# convert the object into a dict
add_wiki_attachment200_response_inner_dict = add_wiki_attachment200_response_inner_instance.to_dict()
# create an instance of AddWikiAttachment200ResponseInner from a dict
add_wiki_attachment200_response_inner_from_dict = AddWikiAttachment200ResponseInner.from_dict(add_wiki_attachment200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


