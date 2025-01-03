# DeleteWatching200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**issue** | [**DeleteWatching200ResponseIssue**](DeleteWatching200ResponseIssue.md) |  | [optional] 
**last_content_updated** | **datetime** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.delete_watching200_response import DeleteWatching200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWatching200Response from a JSON string
delete_watching200_response_instance = DeleteWatching200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteWatching200Response.to_json())

# convert the object into a dict
delete_watching200_response_dict = delete_watching200_response_instance.to_dict()
# create an instance of DeleteWatching200Response from a dict
delete_watching200_response_from_dict = DeleteWatching200Response.from_dict(delete_watching200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


