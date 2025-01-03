# GetPullRequest200ResponseCreatedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role_type** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 

## Example

```python
from backlog_client.models.get_pull_request200_response_created_user import GetPullRequest200ResponseCreatedUser

# TODO update the JSON string below
json = "{}"
# create an instance of GetPullRequest200ResponseCreatedUser from a JSON string
get_pull_request200_response_created_user_instance = GetPullRequest200ResponseCreatedUser.from_json(json)
# print the JSON string representation of the object
print(GetPullRequest200ResponseCreatedUser.to_json())

# convert the object into a dict
get_pull_request200_response_created_user_dict = get_pull_request200_response_created_user_instance.to_dict()
# create an instance of GetPullRequest200ResponseCreatedUser from a dict
get_pull_request200_response_created_user_from_dict = GetPullRequest200ResponseCreatedUser.from_dict(get_pull_request200_response_created_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


