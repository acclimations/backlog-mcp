# GetStatuses200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from backlog_client.models.get_statuses200_response_inner import GetStatuses200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatuses200ResponseInner from a JSON string
get_statuses200_response_inner_instance = GetStatuses200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetStatuses200ResponseInner.to_json())

# convert the object into a dict
get_statuses200_response_inner_dict = get_statuses200_response_inner_instance.to_dict()
# create an instance of GetStatuses200ResponseInner from a dict
get_statuses200_response_inner_from_dict = GetStatuses200ResponseInner.from_dict(get_statuses200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


