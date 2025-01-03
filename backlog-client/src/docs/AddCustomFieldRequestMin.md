# AddCustomFieldRequestMin

最小値（数値属性の場合は数値、日付属性の場合はyyyy-MM-dd形式）

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from backlog_client.models.add_custom_field_request_min import AddCustomFieldRequestMin

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomFieldRequestMin from a JSON string
add_custom_field_request_min_instance = AddCustomFieldRequestMin.from_json(json)
# print the JSON string representation of the object
print(AddCustomFieldRequestMin.to_json())

# convert the object into a dict
add_custom_field_request_min_dict = add_custom_field_request_min_instance.to_dict()
# create an instance of AddCustomFieldRequestMin from a dict
add_custom_field_request_min_from_dict = AddCustomFieldRequestMin.from_dict(add_custom_field_request_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


