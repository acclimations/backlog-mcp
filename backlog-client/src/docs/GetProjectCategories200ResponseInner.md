# GetProjectCategories200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**project_id** | **int** |  | 
**name** | **str** |  | 
**display_order** | **int** |  | 

## Example

```python
from backlog_client.models.get_project_categories200_response_inner import GetProjectCategories200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectCategories200ResponseInner from a JSON string
get_project_categories200_response_inner_instance = GetProjectCategories200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectCategories200ResponseInner.to_json())

# convert the object into a dict
get_project_categories200_response_inner_dict = get_project_categories200_response_inner_instance.to_dict()
# create an instance of GetProjectCategories200ResponseInner from a dict
get_project_categories200_response_inner_from_dict = GetProjectCategories200ResponseInner.from_dict(get_project_categories200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


