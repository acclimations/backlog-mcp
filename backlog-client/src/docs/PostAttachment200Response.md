# PostAttachment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.post_attachment200_response import PostAttachment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAttachment200Response from a JSON string
post_attachment200_response_instance = PostAttachment200Response.from_json(json)
# print the JSON string representation of the object
print(PostAttachment200Response.to_json())

# convert the object into a dict
post_attachment200_response_dict = post_attachment200_response_instance.to_dict()
# create an instance of PostAttachment200Response from a dict
post_attachment200_response_from_dict = PostAttachment200Response.from_dict(post_attachment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


