# GetIssueTypes200ResponseInner


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
from backlog_client.models.get_issue_types200_response_inner import GetIssueTypes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssueTypes200ResponseInner from a JSON string
get_issue_types200_response_inner_instance = GetIssueTypes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetIssueTypes200ResponseInner.to_json())

# convert the object into a dict
get_issue_types200_response_inner_dict = get_issue_types200_response_inner_instance.to_dict()
# create an instance of GetIssueTypes200ResponseInner from a dict
get_issue_types200_response_inner_from_dict = GetIssueTypes200ResponseInner.from_dict(get_issue_types200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


