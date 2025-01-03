# GetProjectVersions200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**release_due_date** | **date** |  | [optional] 
**archived** | **bool** |  | [optional] 
**display_order** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.get_project_versions200_response_inner import GetProjectVersions200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectVersions200ResponseInner from a JSON string
get_project_versions200_response_inner_instance = GetProjectVersions200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectVersions200ResponseInner.to_json())

# convert the object into a dict
get_project_versions200_response_inner_dict = get_project_versions200_response_inner_instance.to_dict()
# create an instance of GetProjectVersions200ResponseInner from a dict
get_project_versions200_response_inner_from_dict = GetProjectVersions200ResponseInner.from_dict(get_project_versions200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


