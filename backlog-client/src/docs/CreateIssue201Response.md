# CreateIssue201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**issue_key** | **str** |  | [optional] 
**key_id** | **int** |  | [optional] 
**issue_type** | [**GetIssues200ResponseInnerIssueType**](GetIssues200ResponseInnerIssueType.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**resolution** | **str** |  | [optional] 
**priority** | [**GetIssues200ResponseInnerPriority**](GetIssues200ResponseInnerPriority.md) |  | [optional] 
**status** | [**GetIssues200ResponseInnerIssueType**](GetIssues200ResponseInnerIssueType.md) |  | [optional] 
**assignee** | [**GetGroups200ResponseInnerMembersInner**](GetGroups200ResponseInnerMembersInner.md) |  | [optional] 
**category** | **List[object]** |  | [optional] 
**versions** | **List[object]** |  | [optional] 
**milestone** | [**List[GetIssues200ResponseInnerMilestoneInner]**](GetIssues200ResponseInnerMilestoneInner.md) |  | [optional] 
**start_date** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**estimated_hours** | **float** |  | [optional] 
**actual_hours** | **float** |  | [optional] 
**parent_issue_id** | **int** |  | [optional] 
**custom_fields** | **List[object]** |  | [optional] 
**attachments** | [**List[GetIssues200ResponseInnerAttachmentsInner]**](GetIssues200ResponseInnerAttachmentsInner.md) |  | [optional] 
**shared_files** | **List[object]** |  | [optional] 
**stars** | **List[object]** |  | [optional] 

## Example

```python
from backlog_client.models.create_issue201_response import CreateIssue201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIssue201Response from a JSON string
create_issue201_response_instance = CreateIssue201Response.from_json(json)
# print the JSON string representation of the object
print(CreateIssue201Response.to_json())

# convert the object into a dict
create_issue201_response_dict = create_issue201_response_instance.to_dict()
# create an instance of CreateIssue201Response from a dict
create_issue201_response_from_dict = CreateIssue201Response.from_dict(create_issue201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


