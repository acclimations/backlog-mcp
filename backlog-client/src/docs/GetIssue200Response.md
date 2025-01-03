# GetIssue200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**issue_key** | **str** |  | [optional] 
**key_id** | **int** |  | [optional] 
**issue_type** | [**GetIssue200ResponseIssueType**](GetIssue200ResponseIssueType.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**resolution** | **str** |  | [optional] 
**priority** | [**GetIssue200ResponsePriority**](GetIssue200ResponsePriority.md) |  | [optional] 
**status** | [**GetIssue200ResponseIssueType**](GetIssue200ResponseIssueType.md) |  | [optional] 
**assignee** | [**GetGroups200ResponseInnerMembersInner**](GetGroups200ResponseInnerMembersInner.md) |  | [optional] 
**category** | **List[object]** |  | [optional] 
**versions** | **List[object]** |  | [optional] 
**milestone** | [**List[GetIssue200ResponseMilestoneInner]**](GetIssue200ResponseMilestoneInner.md) |  | [optional] 
**start_date** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**estimated_hours** | **float** |  | [optional] 
**actual_hours** | **float** |  | [optional] 
**parent_issue_id** | **int** |  | [optional] 
**created_user** | [**GetGroups200ResponseInnerCreatedUser**](GetGroups200ResponseInnerCreatedUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetGroups200ResponseInnerCreatedUser**](GetGroups200ResponseInnerCreatedUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 
**custom_fields** | **List[object]** |  | [optional] 
**attachments** | [**List[GetIssue200ResponseAttachmentsInner]**](GetIssue200ResponseAttachmentsInner.md) |  | [optional] 
**shared_files** | **List[object]** |  | [optional] 
**stars** | [**List[GetIssue200ResponseStarsInner]**](GetIssue200ResponseStarsInner.md) |  | [optional] 

## Example

```python
from backlog_client.models.get_issue200_response import GetIssue200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssue200Response from a JSON string
get_issue200_response_instance = GetIssue200Response.from_json(json)
# print the JSON string representation of the object
print(GetIssue200Response.to_json())

# convert the object into a dict
get_issue200_response_dict = get_issue200_response_instance.to_dict()
# create an instance of GetIssue200Response from a dict
get_issue200_response_from_dict = GetIssue200Response.from_dict(get_issue200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


