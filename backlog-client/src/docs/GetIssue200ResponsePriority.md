# GetIssue200ResponsePriority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from backlog_client.models.get_issue200_response_priority import GetIssue200ResponsePriority

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssue200ResponsePriority from a JSON string
get_issue200_response_priority_instance = GetIssue200ResponsePriority.from_json(json)
# print the JSON string representation of the object
print(GetIssue200ResponsePriority.to_json())

# convert the object into a dict
get_issue200_response_priority_dict = get_issue200_response_priority_instance.to_dict()
# create an instance of GetIssue200ResponsePriority from a dict
get_issue200_response_priority_from_dict = GetIssue200ResponsePriority.from_dict(get_issue200_response_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


