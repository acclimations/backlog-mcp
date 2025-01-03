# GetWebhooks200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**hook_url** | **str** |  | [optional] 
**all_event** | **bool** |  | [optional] 
**activity_type_ids** | **List[int]** |  | [optional] 
**created_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated_user** | [**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md) |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_webhooks200_response_inner import GetWebhooks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooks200ResponseInner from a JSON string
get_webhooks200_response_inner_instance = GetWebhooks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetWebhooks200ResponseInner.to_json())

# convert the object into a dict
get_webhooks200_response_inner_dict = get_webhooks200_response_inner_instance.to_dict()
# create an instance of GetWebhooks200ResponseInner from a dict
get_webhooks200_response_inner_from_dict = GetWebhooks200ResponseInner.from_dict(get_webhooks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


