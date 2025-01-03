# AddCustomField200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**type_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**applicable_issue_types** | **List[int]** |  | [optional] 

## Example

```python
from backlog_client.models.add_custom_field200_response import AddCustomField200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomField200Response from a JSON string
add_custom_field200_response_instance = AddCustomField200Response.from_json(json)
# print the JSON string representation of the object
print(AddCustomField200Response.to_json())

# convert the object into a dict
add_custom_field200_response_dict = add_custom_field200_response_instance.to_dict()
# create an instance of AddCustomField200Response from a dict
add_custom_field200_response_from_dict = AddCustomField200Response.from_dict(add_custom_field200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


