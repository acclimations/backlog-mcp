# AddProjectCategory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_order** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.add_project_category200_response import AddProjectCategory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddProjectCategory200Response from a JSON string
add_project_category200_response_instance = AddProjectCategory200Response.from_json(json)
# print the JSON string representation of the object
print(AddProjectCategory200Response.to_json())

# convert the object into a dict
add_project_category200_response_dict = add_project_category200_response_instance.to_dict()
# create an instance of AddProjectCategory200Response from a dict
add_project_category200_response_from_dict = AddProjectCategory200Response.from_dict(add_project_category200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


