# GetWatching200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**already_read** | **bool** |  | [optional] 
**note** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**issue** | [**GetWatching200ResponseIssue**](GetWatching200ResponseIssue.md) |  | [optional] 
**last_content_updated** | **datetime** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_watching200_response import GetWatching200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWatching200Response from a JSON string
get_watching200_response_instance = GetWatching200Response.from_json(json)
# print the JSON string representation of the object
print(GetWatching200Response.to_json())

# convert the object into a dict
get_watching200_response_dict = get_watching200_response_instance.to_dict()
# create an instance of GetWatching200Response from a dict
get_watching200_response_from_dict = GetWatching200Response.from_dict(get_watching200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


