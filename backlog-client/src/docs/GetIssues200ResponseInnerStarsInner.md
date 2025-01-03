# GetIssues200ResponseInnerStarsInner


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
from backlog_client.models.get_issues200_response_inner_stars_inner import GetIssues200ResponseInnerStarsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssues200ResponseInnerStarsInner from a JSON string
get_issues200_response_inner_stars_inner_instance = GetIssues200ResponseInnerStarsInner.from_json(json)
# print the JSON string representation of the object
print(GetIssues200ResponseInnerStarsInner.to_json())

# convert the object into a dict
get_issues200_response_inner_stars_inner_dict = get_issues200_response_inner_stars_inner_instance.to_dict()
# create an instance of GetIssues200ResponseInnerStarsInner from a dict
get_issues200_response_inner_stars_inner_from_dict = GetIssues200ResponseInnerStarsInner.from_dict(get_issues200_response_inner_stars_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


