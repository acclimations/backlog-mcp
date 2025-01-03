# GetWikiAttachments200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**size** | **int** |  | 

## Example

```python
from backlog_client.models.get_wiki_attachments200_response_inner import GetWikiAttachments200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWikiAttachments200ResponseInner from a JSON string
get_wiki_attachments200_response_inner_instance = GetWikiAttachments200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetWikiAttachments200ResponseInner.to_json())

# convert the object into a dict
get_wiki_attachments200_response_inner_dict = get_wiki_attachments200_response_inner_instance.to_dict()
# create an instance of GetWikiAttachments200ResponseInner from a dict
get_wiki_attachments200_response_inner_from_dict = GetWikiAttachments200ResponseInner.from_dict(get_wiki_attachments200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

