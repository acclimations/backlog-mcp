# GetGitRepository200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**hook_url** | **str** |  | [optional] 
**http_url** | **str** |  | [optional] 
**ssh_url** | **str** |  | [optional] 
**display_order** | **int** |  | [optional] 
**pushed_at** | **str** |  | [optional] 
**created_user** | [**GetGitRepository200ResponseCreatedUser**](GetGitRepository200ResponseCreatedUser.md) |  | [optional] 
**created** | **str** |  | [optional] 
**updated_user** | [**GetGitRepository200ResponseCreatedUser**](GetGitRepository200ResponseCreatedUser.md) |  | [optional] 
**updated** | **str** |  | [optional] 

## Example

```python
from backlog_client.models.get_git_repository200_response import GetGitRepository200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGitRepository200Response from a JSON string
get_git_repository200_response_instance = GetGitRepository200Response.from_json(json)
# print the JSON string representation of the object
print(GetGitRepository200Response.to_json())

# convert the object into a dict
get_git_repository200_response_dict = get_git_repository200_response_instance.to_dict()
# create an instance of GetGitRepository200Response from a dict
get_git_repository200_response_from_dict = GetGitRepository200Response.from_dict(get_git_repository200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


