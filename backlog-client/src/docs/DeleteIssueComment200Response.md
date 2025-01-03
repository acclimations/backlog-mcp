# DeleteIssueComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**issue_id** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**change_log** | **object** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**stars** | **List[object]** |  | [optional] 
**notifications** | **List[object]** |  | [optional] 

## Example

```python
from backlog_client.models.delete_issue_comment200_response import DeleteIssueComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteIssueComment200Response from a JSON string
delete_issue_comment200_response_instance = DeleteIssueComment200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteIssueComment200Response.to_json())

# convert the object into a dict
delete_issue_comment200_response_dict = delete_issue_comment200_response_instance.to_dict()
# create an instance of DeleteIssueComment200Response from a dict
delete_issue_comment200_response_from_dict = DeleteIssueComment200Response.from_dict(delete_issue_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


