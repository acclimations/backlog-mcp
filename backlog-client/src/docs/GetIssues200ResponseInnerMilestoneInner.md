# GetIssues200ResponseInnerMilestoneInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**release_due_date** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 
**display_order** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.get_issues200_response_inner_milestone_inner import GetIssues200ResponseInnerMilestoneInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssues200ResponseInnerMilestoneInner from a JSON string
get_issues200_response_inner_milestone_inner_instance = GetIssues200ResponseInnerMilestoneInner.from_json(json)
# print the JSON string representation of the object
print(GetIssues200ResponseInnerMilestoneInner.to_json())

# convert the object into a dict
get_issues200_response_inner_milestone_inner_dict = get_issues200_response_inner_milestone_inner_instance.to_dict()
# create an instance of GetIssues200ResponseInnerMilestoneInner from a dict
get_issues200_response_inner_milestone_inner_from_dict = GetIssues200ResponseInnerMilestoneInner.from_dict(get_issues200_response_inner_milestone_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


