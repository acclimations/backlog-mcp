# DeletePullRequestAttachment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**created_user** | [**GetGroups200ResponseInnerCreatedUser**](GetGroups200ResponseInnerCreatedUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from backlog_client.models.delete_pull_request_attachment200_response import DeletePullRequestAttachment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePullRequestAttachment200Response from a JSON string
delete_pull_request_attachment200_response_instance = DeletePullRequestAttachment200Response.from_json(json)
# print the JSON string representation of the object
print(DeletePullRequestAttachment200Response.to_json())

# convert the object into a dict
delete_pull_request_attachment200_response_dict = delete_pull_request_attachment200_response_instance.to_dict()
# create an instance of DeletePullRequestAttachment200Response from a dict
delete_pull_request_attachment200_response_from_dict = DeletePullRequestAttachment200Response.from_dict(delete_pull_request_attachment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


