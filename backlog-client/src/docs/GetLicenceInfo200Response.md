# GetLicenceInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**attachment_limit** | **int** |  | [optional] 
**attachment_limit_per_file** | **int** |  | [optional] 
**attachment_num_limit** | **int** |  | [optional] 
**attribute** | **bool** |  | [optional] 
**attribute_limit** | **int** |  | [optional] 
**burndown** | **bool** |  | [optional] 
**comment_limit** | **int** |  | [optional] 
**component_limit** | **int** |  | [optional] 
**file_sharing** | **bool** |  | [optional] 
**gantt** | **bool** |  | [optional] 
**git** | **bool** |  | [optional] 
**issue_limit** | **int** |  | [optional] 
**licence_type_id** | **int** |  | [optional] 
**limit_date** | **datetime** |  | [optional] 
**nulab_account** | **bool** |  | [optional] 
**parent_child_issue** | **bool** |  | [optional] 
**post_issue_by_mail** | **bool** |  | [optional] 
**project_limit** | **int** |  | [optional] 
**pull_request_attachment_limit_per_file** | **int** |  | [optional] 
**pull_request_attachment_num_limit** | **int** |  | [optional] 
**remote_address** | **bool** |  | [optional] 
**remote_address_limit** | **int** |  | [optional] 
**started_on** | **datetime** |  | [optional] 
**storage_limit** | **int** |  | [optional] 
**subversion** | **bool** |  | [optional] 
**subversion_external** | **bool** |  | [optional] 
**user_limit** | **int** |  | [optional] 
**version_limit** | **int** |  | [optional] 
**wiki_attachment** | **bool** |  | [optional] 
**wiki_attachment_limit_per_file** | **int** |  | [optional] 
**wiki_attachment_num_limit** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.get_licence_info200_response import GetLicenceInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLicenceInfo200Response from a JSON string
get_licence_info200_response_instance = GetLicenceInfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetLicenceInfo200Response.to_json())

# convert the object into a dict
get_licence_info200_response_dict = get_licence_info200_response_instance.to_dict()
# create an instance of GetLicenceInfo200Response from a dict
get_licence_info200_response_from_dict = GetLicenceInfo200Response.from_dict(get_licence_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


