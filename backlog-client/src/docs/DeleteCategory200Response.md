# DeleteCategory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_order** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.delete_category200_response import DeleteCategory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCategory200Response from a JSON string
delete_category200_response_instance = DeleteCategory200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteCategory200Response.to_json())

# convert the object into a dict
delete_category200_response_dict = delete_category200_response_instance.to_dict()
# create an instance of DeleteCategory200Response from a dict
delete_category200_response_from_dict = DeleteCategory200Response.from_dict(delete_category200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


