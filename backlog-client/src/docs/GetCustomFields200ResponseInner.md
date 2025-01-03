# GetCustomFields200ResponseInner


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
**allow_add_item** | **bool** |  | [optional] 
**items** | [**List[GetCustomFields200ResponseInnerItemsInner]**](GetCustomFields200ResponseInnerItemsInner.md) |  | [optional] 

## Example

```python
from backlog_client.models.get_custom_fields200_response_inner import GetCustomFields200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomFields200ResponseInner from a JSON string
get_custom_fields200_response_inner_instance = GetCustomFields200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetCustomFields200ResponseInner.to_json())

# convert the object into a dict
get_custom_fields200_response_inner_dict = get_custom_fields200_response_inner_instance.to_dict()
# create an instance of GetCustomFields200ResponseInner from a dict
get_custom_fields200_response_inner_from_dict = GetCustomFields200ResponseInner.from_dict(get_custom_fields200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


