# GetWikiHistory200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **int** |  | [optional] 
**version** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**created_user** | [**GetGroups200ResponseInnerMembersInner**](GetGroups200ResponseInnerMembersInner.md) |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_wiki_history200_response_inner import GetWikiHistory200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWikiHistory200ResponseInner from a JSON string
get_wiki_history200_response_inner_instance = GetWikiHistory200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetWikiHistory200ResponseInner.to_json())

# convert the object into a dict
get_wiki_history200_response_inner_dict = get_wiki_history200_response_inner_instance.to_dict()
# create an instance of GetWikiHistory200ResponseInner from a dict
get_wiki_history200_response_inner_from_dict = GetWikiHistory200ResponseInner.from_dict(get_wiki_history200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


