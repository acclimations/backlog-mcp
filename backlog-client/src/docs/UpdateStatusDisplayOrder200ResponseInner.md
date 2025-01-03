# UpdateStatusDisplayOrder200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**display_order** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.update_status_display_order200_response_inner import UpdateStatusDisplayOrder200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStatusDisplayOrder200ResponseInner from a JSON string
update_status_display_order200_response_inner_instance = UpdateStatusDisplayOrder200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(UpdateStatusDisplayOrder200ResponseInner.to_json())

# convert the object into a dict
update_status_display_order200_response_inner_dict = update_status_display_order200_response_inner_instance.to_dict()
# create an instance of UpdateStatusDisplayOrder200ResponseInner from a dict
update_status_display_order200_response_inner_from_dict = UpdateStatusDisplayOrder200ResponseInner.from_dict(update_status_display_order200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


