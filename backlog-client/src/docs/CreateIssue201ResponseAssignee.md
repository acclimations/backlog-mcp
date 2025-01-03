# CreateIssue201ResponseAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role_type** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.create_issue201_response_assignee import CreateIssue201ResponseAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIssue201ResponseAssignee from a JSON string
create_issue201_response_assignee_instance = CreateIssue201ResponseAssignee.from_json(json)
# print the JSON string representation of the object
print(CreateIssue201ResponseAssignee.to_json())

# convert the object into a dict
create_issue201_response_assignee_dict = create_issue201_response_assignee_instance.to_dict()
# create an instance of CreateIssue201ResponseAssignee from a dict
create_issue201_response_assignee_from_dict = CreateIssue201ResponseAssignee.from_dict(create_issue201_response_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


