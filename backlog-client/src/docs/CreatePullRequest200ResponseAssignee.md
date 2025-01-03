# CreatePullRequest200ResponseAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role_type** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 

## Example

```python
from backlog_client.models.create_pull_request200_response_assignee import CreatePullRequest200ResponseAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePullRequest200ResponseAssignee from a JSON string
create_pull_request200_response_assignee_instance = CreatePullRequest200ResponseAssignee.from_json(json)
# print the JSON string representation of the object
print(CreatePullRequest200ResponseAssignee.to_json())

# convert the object into a dict
create_pull_request200_response_assignee_dict = create_pull_request200_response_assignee_instance.to_dict()
# create an instance of CreatePullRequest200ResponseAssignee from a dict
create_pull_request200_response_assignee_from_dict = CreatePullRequest200ResponseAssignee.from_dict(create_pull_request200_response_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


