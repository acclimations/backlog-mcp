# DeleteVersion200Response


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
from backlog_client.models.delete_version200_response import DeleteVersion200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVersion200Response from a JSON string
delete_version200_response_instance = DeleteVersion200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteVersion200Response.to_json())

# convert the object into a dict
delete_version200_response_dict = delete_version200_response_instance.to_dict()
# create an instance of DeleteVersion200Response from a dict
delete_version200_response_from_dict = DeleteVersion200Response.from_dict(delete_version200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


