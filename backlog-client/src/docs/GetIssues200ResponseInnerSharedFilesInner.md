# GetIssues200ResponseInnerSharedFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**dir** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**created_user** | **object** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | **object** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_issues200_response_inner_shared_files_inner import GetIssues200ResponseInnerSharedFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssues200ResponseInnerSharedFilesInner from a JSON string
get_issues200_response_inner_shared_files_inner_instance = GetIssues200ResponseInnerSharedFilesInner.from_json(json)
# print the JSON string representation of the object
print(GetIssues200ResponseInnerSharedFilesInner.to_json())

# convert the object into a dict
get_issues200_response_inner_shared_files_inner_dict = get_issues200_response_inner_shared_files_inner_instance.to_dict()
# create an instance of GetIssues200ResponseInnerSharedFilesInner from a dict
get_issues200_response_inner_shared_files_inner_from_dict = GetIssues200ResponseInnerSharedFilesInner.from_dict(get_issues200_response_inner_shared_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


