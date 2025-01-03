# UpdateCategory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_order** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.update_category200_response import UpdateCategory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCategory200Response from a JSON string
update_category200_response_instance = UpdateCategory200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateCategory200Response.to_json())

# convert the object into a dict
update_category200_response_dict = update_category200_response_instance.to_dict()
# create an instance of UpdateCategory200Response from a dict
update_category200_response_from_dict = UpdateCategory200Response.from_dict(update_category200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


