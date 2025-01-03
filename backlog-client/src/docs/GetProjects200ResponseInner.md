# GetProjects200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**chart_enabled** | **bool** |  | [optional] 
**use_resolved_for_chart** | **bool** |  | [optional] 
**subtasking_enabled** | **bool** |  | [optional] 
**project_leader_can_edit_project_leader** | **bool** |  | [optional] 
**use_wiki** | **bool** |  | [optional] 
**use_file_sharing** | **bool** |  | [optional] 
**use_wiki_tree_view** | **bool** |  | [optional] 
**use_subversion** | **bool** |  | [optional] 
**use_git** | **bool** |  | [optional] 
**use_original_image_size_at_wiki** | **bool** |  | [optional] 
**text_formatting_rule** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 
**display_order** | **int** |  | [optional] 
**use_dev_attributes** | **bool** |  | [optional] 

## Example

```python
from backlog_client.models.get_projects200_response_inner import GetProjects200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjects200ResponseInner from a JSON string
get_projects200_response_inner_instance = GetProjects200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjects200ResponseInner.to_json())

# convert the object into a dict
get_projects200_response_inner_dict = get_projects200_response_inner_instance.to_dict()
# create an instance of GetProjects200ResponseInner from a dict
get_projects200_response_inner_from_dict = GetProjects200ResponseInner.from_dict(get_projects200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


