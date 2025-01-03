# UpdateSpaceNotification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.update_space_notification200_response import UpdateSpaceNotification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSpaceNotification200Response from a JSON string
update_space_notification200_response_instance = UpdateSpaceNotification200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateSpaceNotification200Response.to_json())

# convert the object into a dict
update_space_notification200_response_dict = update_space_notification200_response_instance.to_dict()
# create an instance of UpdateSpaceNotification200Response from a dict
update_space_notification200_response_from_dict = UpdateSpaceNotification200Response.from_dict(update_space_notification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


