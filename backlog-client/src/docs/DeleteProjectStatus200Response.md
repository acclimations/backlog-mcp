# DeleteProjectStatus200Response


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
from backlog_client.models.delete_project_status200_response import DeleteProjectStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteProjectStatus200Response from a JSON string
delete_project_status200_response_instance = DeleteProjectStatus200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteProjectStatus200Response.to_json())

# convert the object into a dict
delete_project_status200_response_dict = delete_project_status200_response_instance.to_dict()
# create an instance of DeleteProjectStatus200Response from a dict
delete_project_status200_response_from_dict = DeleteProjectStatus200Response.from_dict(delete_project_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


