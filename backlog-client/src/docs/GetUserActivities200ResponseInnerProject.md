# GetUserActivities200ResponseInnerProject


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
**use_original_image_size_at_wiki** | **bool** |  | [optional] 
**text_formatting_rule** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 
**display_order** | **int** |  | [optional] 
**use_dev_attributes** | **bool** |  | [optional] 

## Example

```python
from backlog_client.models.get_user_activities200_response_inner_project import GetUserActivities200ResponseInnerProject

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserActivities200ResponseInnerProject from a JSON string
get_user_activities200_response_inner_project_instance = GetUserActivities200ResponseInnerProject.from_json(json)
# print the JSON string representation of the object
print(GetUserActivities200ResponseInnerProject.to_json())

# convert the object into a dict
get_user_activities200_response_inner_project_dict = get_user_activities200_response_inner_project_instance.to_dict()
# create an instance of GetUserActivities200ResponseInnerProject from a dict
get_user_activities200_response_inner_project_from_dict = GetUserActivities200ResponseInnerProject.from_dict(get_user_activities200_response_inner_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


