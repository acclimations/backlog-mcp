# DeleteIssueType200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**display_order** | **int** |  | [optional] 
**template_summary** | **str** |  | [optional] 
**template_description** | **str** |  | [optional] 

## Example

```python
from backlog_client.models.delete_issue_type200_response import DeleteIssueType200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteIssueType200Response from a JSON string
delete_issue_type200_response_instance = DeleteIssueType200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteIssueType200Response.to_json())

# convert the object into a dict
delete_issue_type200_response_dict = delete_issue_type200_response_instance.to_dict()
# create an instance of DeleteIssueType200Response from a dict
delete_issue_type200_response_from_dict = DeleteIssueType200Response.from_dict(delete_issue_type200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


