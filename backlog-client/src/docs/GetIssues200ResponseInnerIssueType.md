# GetIssues200ResponseInnerIssueType


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
from backlog_client.models.get_issues200_response_inner_issue_type import GetIssues200ResponseInnerIssueType

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssues200ResponseInnerIssueType from a JSON string
get_issues200_response_inner_issue_type_instance = GetIssues200ResponseInnerIssueType.from_json(json)
# print the JSON string representation of the object
print(GetIssues200ResponseInnerIssueType.to_json())

# convert the object into a dict
get_issues200_response_inner_issue_type_dict = get_issues200_response_inner_issue_type_instance.to_dict()
# create an instance of GetIssues200ResponseInnerIssueType from a dict
get_issues200_response_inner_issue_type_from_dict = GetIssues200ResponseInnerIssueType.from_dict(get_issues200_response_inner_issue_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


