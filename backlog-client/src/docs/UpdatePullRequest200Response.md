# UpdatePullRequest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**repository_id** | **int** |  | [optional] 
**number** | **int** |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**base** | **str** |  | [optional] 
**branch** | **str** |  | [optional] 
**status** | [**GetIssues200ResponseInnerPriority**](GetIssues200ResponseInnerPriority.md) |  | [optional] 
**assignee** | [**GetGroups200ResponseInnerMembersInner**](GetGroups200ResponseInnerMembersInner.md) |  | [optional] 
**issue** | **object** |  | [optional] 
**base_commit** | **str** |  | [optional] 
**branch_commit** | **str** |  | [optional] 
**merge_commit** | **str** |  | [optional] 
**close_at** | **datetime** |  | [optional] 
**merge_at** | **datetime** |  | [optional] 
**created_user** | **object** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | **object** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**attachments** | **List[object]** |  | [optional] 
**stars** | **List[object]** |  | [optional] 

## Example

```python
from backlog_client.models.update_pull_request200_response import UpdatePullRequest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePullRequest200Response from a JSON string
update_pull_request200_response_instance = UpdatePullRequest200Response.from_json(json)
# print the JSON string representation of the object
print(UpdatePullRequest200Response.to_json())

# convert the object into a dict
update_pull_request200_response_dict = update_pull_request200_response_instance.to_dict()
# create an instance of UpdatePullRequest200Response from a dict
update_pull_request200_response_from_dict = UpdatePullRequest200Response.from_dict(update_pull_request200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

