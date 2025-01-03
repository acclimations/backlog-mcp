# GetSpaceDiskUsage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** | 容量 | [optional] 
**issue** | **int** | 課題の使用容量 | [optional] 
**wiki** | **int** | Wikiの使用容量 | [optional] 
**file** | **int** | ファイルの使用容量 | [optional] 
**subversion** | **int** | Subversionの使用容量 | [optional] 
**git** | **int** | Gitの使用容量 | [optional] 
**git_lfs** | **int** | Git LFSの使用容量 | [optional] 
**details** | [**List[GetSpaceDiskUsage200ResponseDetailsInner]**](GetSpaceDiskUsage200ResponseDetailsInner.md) |  | [optional] 

## Example

```python
from backlog_client.models.get_space_disk_usage200_response import GetSpaceDiskUsage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpaceDiskUsage200Response from a JSON string
get_space_disk_usage200_response_instance = GetSpaceDiskUsage200Response.from_json(json)
# print the JSON string representation of the object
print(GetSpaceDiskUsage200Response.to_json())

# convert the object into a dict
get_space_disk_usage200_response_dict = get_space_disk_usage200_response_instance.to_dict()
# create an instance of GetSpaceDiskUsage200Response from a dict
get_space_disk_usage200_response_from_dict = GetSpaceDiskUsage200Response.from_dict(get_space_disk_usage200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


