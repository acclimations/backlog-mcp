# GetProjectStatuses200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**display_order** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.get_project_statuses200_response_inner import GetProjectStatuses200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectStatuses200ResponseInner from a JSON string
get_project_statuses200_response_inner_instance = GetProjectStatuses200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectStatuses200ResponseInner.to_json())

# convert the object into a dict
get_project_statuses200_response_inner_dict = get_project_statuses200_response_inner_instance.to_dict()
# create an instance of GetProjectStatuses200ResponseInner from a dict
get_project_statuses200_response_inner_from_dict = GetProjectStatuses200ResponseInner.from_dict(get_project_statuses200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


