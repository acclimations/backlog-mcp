# AddWatching201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**issue** | [**AddWatching201ResponseIssue**](AddWatching201ResponseIssue.md) |  | [optional] 
**last_content_updated** | **datetime** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.add_watching201_response import AddWatching201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddWatching201Response from a JSON string
add_watching201_response_instance = AddWatching201Response.from_json(json)
# print the JSON string representation of the object
print(AddWatching201Response.to_json())

# convert the object into a dict
add_watching201_response_dict = add_watching201_response_instance.to_dict()
# create an instance of AddWatching201Response from a dict
add_watching201_response_from_dict = AddWatching201Response.from_dict(add_watching201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


