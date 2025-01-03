# AddCustomFieldRequestMax

最大値（数値属性の場合は数値、日付属性の場合はyyyy-MM-dd形式）

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from backlog_client.models.add_custom_field_request_max import AddCustomFieldRequestMax

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomFieldRequestMax from a JSON string
add_custom_field_request_max_instance = AddCustomFieldRequestMax.from_json(json)
# print the JSON string representation of the object
print(AddCustomFieldRequestMax.to_json())

# convert the object into a dict
add_custom_field_request_max_dict = add_custom_field_request_max_instance.to_dict()
# create an instance of AddCustomFieldRequestMax from a dict
add_custom_field_request_max_from_dict = AddCustomFieldRequestMax.from_dict(add_custom_field_request_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


