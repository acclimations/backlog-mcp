# GetIssue200ResponseMilestoneInner


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
from backlog_client.models.get_issue200_response_milestone_inner import GetIssue200ResponseMilestoneInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssue200ResponseMilestoneInner from a JSON string
get_issue200_response_milestone_inner_instance = GetIssue200ResponseMilestoneInner.from_json(json)
# print the JSON string representation of the object
print(GetIssue200ResponseMilestoneInner.to_json())

# convert the object into a dict
get_issue200_response_milestone_inner_dict = get_issue200_response_milestone_inner_instance.to_dict()
# create an instance of GetIssue200ResponseMilestoneInner from a dict
get_issue200_response_milestone_inner_from_dict = GetIssue200ResponseMilestoneInner.from_dict(get_issue200_response_milestone_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


