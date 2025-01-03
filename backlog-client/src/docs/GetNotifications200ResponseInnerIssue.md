# GetNotifications200ResponseInnerIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**issue_key** | **str** |  | [optional] 
**key_id** | **int** |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**estimated_hours** | **float** |  | [optional] 
**actual_hours** | **float** |  | [optional] 
**parent_issue_id** | **int** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_notifications200_response_inner_issue import GetNotifications200ResponseInnerIssue

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotifications200ResponseInnerIssue from a JSON string
get_notifications200_response_inner_issue_instance = GetNotifications200ResponseInnerIssue.from_json(json)
# print the JSON string representation of the object
print(GetNotifications200ResponseInnerIssue.to_json())

# convert the object into a dict
get_notifications200_response_inner_issue_dict = get_notifications200_response_inner_issue_instance.to_dict()
# create an instance of GetNotifications200ResponseInnerIssue from a dict
get_notifications200_response_inner_issue_from_dict = GetNotifications200ResponseInnerIssue.from_dict(get_notifications200_response_inner_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


