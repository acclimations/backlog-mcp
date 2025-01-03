# GetSpace200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**space_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**report_send_time** | **str** |  | [optional] 
**text_formatting_rule** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_space200_response import GetSpace200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpace200Response from a JSON string
get_space200_response_instance = GetSpace200Response.from_json(json)
# print the JSON string representation of the object
print(GetSpace200Response.to_json())

# convert the object into a dict
get_space200_response_dict = get_space200_response_instance.to_dict()
# create an instance of GetSpace200Response from a dict
get_space200_response_from_dict = GetSpace200Response.from_dict(get_space200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


