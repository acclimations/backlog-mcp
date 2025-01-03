# AddCustomFieldListItem200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**type_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**applicable_issue_types** | **List[object]** |  | [optional] 
**allow_add_item** | **bool** |  | [optional] 
**items** | [**List[GetCustomFields200ResponseInnerItemsInner]**](GetCustomFields200ResponseInnerItemsInner.md) |  | [optional] 

## Example

```python
from backlog_client.models.add_custom_field_list_item200_response import AddCustomFieldListItem200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomFieldListItem200Response from a JSON string
add_custom_field_list_item200_response_instance = AddCustomFieldListItem200Response.from_json(json)
# print the JSON string representation of the object
print(AddCustomFieldListItem200Response.to_json())

# convert the object into a dict
add_custom_field_list_item200_response_dict = add_custom_field_list_item200_response_instance.to_dict()
# create an instance of AddCustomFieldListItem200Response from a dict
add_custom_field_list_item200_response_from_dict = AddCustomFieldListItem200Response.from_dict(add_custom_field_list_item200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


