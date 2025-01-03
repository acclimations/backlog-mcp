# GetRateLimit200ResponseRateLimitUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**remaining** | **int** |  | [optional] 
**reset** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.get_rate_limit200_response_rate_limit_update import GetRateLimit200ResponseRateLimitUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateLimit200ResponseRateLimitUpdate from a JSON string
get_rate_limit200_response_rate_limit_update_instance = GetRateLimit200ResponseRateLimitUpdate.from_json(json)
# print the JSON string representation of the object
print(GetRateLimit200ResponseRateLimitUpdate.to_json())

# convert the object into a dict
get_rate_limit200_response_rate_limit_update_dict = get_rate_limit200_response_rate_limit_update_instance.to_dict()
# create an instance of GetRateLimit200ResponseRateLimitUpdate from a dict
get_rate_limit200_response_rate_limit_update_from_dict = GetRateLimit200ResponseRateLimitUpdate.from_dict(get_rate_limit200_response_rate_limit_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


