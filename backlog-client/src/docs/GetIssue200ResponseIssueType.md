# GetIssue200ResponseIssueType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**display_order** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.get_issue200_response_issue_type import GetIssue200ResponseIssueType

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssue200ResponseIssueType from a JSON string
get_issue200_response_issue_type_instance = GetIssue200ResponseIssueType.from_json(json)
# print the JSON string representation of the object
print(GetIssue200ResponseIssueType.to_json())

# convert the object into a dict
get_issue200_response_issue_type_dict = get_issue200_response_issue_type_instance.to_dict()
# create an instance of GetIssue200ResponseIssueType from a dict
get_issue200_response_issue_type_from_dict = GetIssue200ResponseIssueType.from_dict(get_issue200_response_issue_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


