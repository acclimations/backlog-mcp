# GetProjectWebhooks200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**hook_url** | **str** |  | [optional] 
**all_event** | **bool** |  | [optional] 
**activity_type_ids** | **List[int]** |  | [optional] 
**created_user** | [**GetGroups200ResponseInnerCreatedUser**](GetGroups200ResponseInnerCreatedUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetGroups200ResponseInnerCreatedUser**](GetGroups200ResponseInnerCreatedUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_project_webhooks200_response_inner import GetProjectWebhooks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectWebhooks200ResponseInner from a JSON string
get_project_webhooks200_response_inner_instance = GetProjectWebhooks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectWebhooks200ResponseInner.to_json())

# convert the object into a dict
get_project_webhooks200_response_inner_dict = get_project_webhooks200_response_inner_instance.to_dict()
# create an instance of GetProjectWebhooks200ResponseInner from a dict
get_project_webhooks200_response_inner_from_dict = GetProjectWebhooks200ResponseInner.from_dict(get_project_webhooks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


