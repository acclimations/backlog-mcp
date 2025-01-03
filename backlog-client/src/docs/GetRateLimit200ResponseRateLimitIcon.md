# GetRateLimit200ResponseRateLimitIcon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**remaining** | **int** |  | [optional] 
**reset** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.get_rate_limit200_response_rate_limit_icon import GetRateLimit200ResponseRateLimitIcon

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateLimit200ResponseRateLimitIcon from a JSON string
get_rate_limit200_response_rate_limit_icon_instance = GetRateLimit200ResponseRateLimitIcon.from_json(json)
# print the JSON string representation of the object
print(GetRateLimit200ResponseRateLimitIcon.to_json())

# convert the object into a dict
get_rate_limit200_response_rate_limit_icon_dict = get_rate_limit200_response_rate_limit_icon_instance.to_dict()
# create an instance of GetRateLimit200ResponseRateLimitIcon from a dict
get_rate_limit200_response_rate_limit_icon_from_dict = GetRateLimit200ResponseRateLimitIcon.from_dict(get_rate_limit200_response_rate_limit_icon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


