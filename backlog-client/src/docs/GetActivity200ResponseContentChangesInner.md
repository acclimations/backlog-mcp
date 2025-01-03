# GetActivity200ResponseContentChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**new_value** | **str** |  | [optional] 
**old_value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from backlog_client.models.get_activity200_response_content_changes_inner import GetActivity200ResponseContentChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetActivity200ResponseContentChangesInner from a JSON string
get_activity200_response_content_changes_inner_instance = GetActivity200ResponseContentChangesInner.from_json(json)
# print the JSON string representation of the object
print(GetActivity200ResponseContentChangesInner.to_json())

# convert the object into a dict
get_activity200_response_content_changes_inner_dict = get_activity200_response_content_changes_inner_instance.to_dict()
# create an instance of GetActivity200ResponseContentChangesInner from a dict
get_activity200_response_content_changes_inner_from_dict = GetActivity200ResponseContentChangesInner.from_dict(get_activity200_response_content_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


