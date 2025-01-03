# GetNotifications200ResponseInnerSender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role_type** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 
**mail_address** | **str** |  | [optional] 
**last_login_time** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.get_notifications200_response_inner_sender import GetNotifications200ResponseInnerSender

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotifications200ResponseInnerSender from a JSON string
get_notifications200_response_inner_sender_instance = GetNotifications200ResponseInnerSender.from_json(json)
# print the JSON string representation of the object
print(GetNotifications200ResponseInnerSender.to_json())

# convert the object into a dict
get_notifications200_response_inner_sender_dict = get_notifications200_response_inner_sender_instance.to_dict()
# create an instance of GetNotifications200ResponseInnerSender from a dict
get_notifications200_response_inner_sender_from_dict = GetNotifications200ResponseInnerSender.from_dict(get_notifications200_response_inner_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


