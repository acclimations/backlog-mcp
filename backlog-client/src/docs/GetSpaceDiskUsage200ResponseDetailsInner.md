# GetSpaceDiskUsage200ResponseDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | プロジェクトID | [optional] 
**issue** | **int** | プロジェクトの課題使用容量 | [optional] 
**wiki** | **int** | プロジェクトのWiki使用容量 | [optional] 
**file** | **int** | プロジェクトのファイル使用容量 | [optional] 
**subversion** | **int** | プロジェクトのSubversion使用容量 | [optional] 
**git** | **int** | プロジェクトのGit使用容量 | [optional] 
**git_lfs** | **int** | プロジェクトのGit LFS使用容量 | [optional] 

## Example

```python
from backlog_client.models.get_space_disk_usage200_response_details_inner import GetSpaceDiskUsage200ResponseDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpaceDiskUsage200ResponseDetailsInner from a JSON string
get_space_disk_usage200_response_details_inner_instance = GetSpaceDiskUsage200ResponseDetailsInner.from_json(json)
# print the JSON string representation of the object
print(GetSpaceDiskUsage200ResponseDetailsInner.to_json())

# convert the object into a dict
get_space_disk_usage200_response_details_inner_dict = get_space_disk_usage200_response_details_inner_instance.to_dict()
# create an instance of GetSpaceDiskUsage200ResponseDetailsInner from a dict
get_space_disk_usage200_response_details_inner_from_dict = GetSpaceDiskUsage200ResponseDetailsInner.from_dict(get_space_disk_usage200_response_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


