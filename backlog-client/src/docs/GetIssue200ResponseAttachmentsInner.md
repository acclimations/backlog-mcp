# GetIssue200ResponseAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.get_issue200_response_attachments_inner import GetIssue200ResponseAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssue200ResponseAttachmentsInner from a JSON string
get_issue200_response_attachments_inner_instance = GetIssue200ResponseAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(GetIssue200ResponseAttachmentsInner.to_json())

# convert the object into a dict
get_issue200_response_attachments_inner_dict = get_issue200_response_attachments_inner_instance.to_dict()
# create an instance of GetIssue200ResponseAttachmentsInner from a dict
get_issue200_response_attachments_inner_from_dict = GetIssue200ResponseAttachmentsInner.from_dict(get_issue200_response_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


