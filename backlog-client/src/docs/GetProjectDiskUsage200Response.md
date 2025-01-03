# GetProjectDiskUsage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**issue** | **int** |  | [optional] 
**wiki** | **int** |  | [optional] 
**file** | **int** |  | [optional] 
**subversion** | **int** |  | [optional] 
**git** | **int** |  | [optional] 
**git_lfs** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.get_project_disk_usage200_response import GetProjectDiskUsage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectDiskUsage200Response from a JSON string
get_project_disk_usage200_response_instance = GetProjectDiskUsage200Response.from_json(json)
# print the JSON string representation of the object
print(GetProjectDiskUsage200Response.to_json())

# convert the object into a dict
get_project_disk_usage200_response_dict = get_project_disk_usage200_response_instance.to_dict()
# create an instance of GetProjectDiskUsage200Response from a dict
get_project_disk_usage200_response_from_dict = GetProjectDiskUsage200Response.from_dict(get_project_disk_usage200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


