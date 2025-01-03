# UpdateIssue200ResponseStarsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**presenter** | **object** |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.update_issue200_response_stars_inner import UpdateIssue200ResponseStarsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIssue200ResponseStarsInner from a JSON string
update_issue200_response_stars_inner_instance = UpdateIssue200ResponseStarsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateIssue200ResponseStarsInner.to_json())

# convert the object into a dict
update_issue200_response_stars_inner_dict = update_issue200_response_stars_inner_instance.to_dict()
# create an instance of UpdateIssue200ResponseStarsInner from a dict
update_issue200_response_stars_inner_from_dict = UpdateIssue200ResponseStarsInner.from_dict(update_issue200_response_stars_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


