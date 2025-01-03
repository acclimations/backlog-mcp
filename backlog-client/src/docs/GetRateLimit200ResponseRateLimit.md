# GetRateLimit200ResponseRateLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | [**GetRateLimit200ResponseRateLimitRead**](GetRateLimit200ResponseRateLimitRead.md) |  | [optional] 
**update** | [**GetRateLimit200ResponseRateLimitUpdate**](GetRateLimit200ResponseRateLimitUpdate.md) |  | [optional] 
**search** | [**GetRateLimit200ResponseRateLimitUpdate**](GetRateLimit200ResponseRateLimitUpdate.md) |  | [optional] 
**icon** | [**GetRateLimit200ResponseRateLimitIcon**](GetRateLimit200ResponseRateLimitIcon.md) |  | [optional] 

## Example

```python
from backlog_client.models.get_rate_limit200_response_rate_limit import GetRateLimit200ResponseRateLimit

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateLimit200ResponseRateLimit from a JSON string
get_rate_limit200_response_rate_limit_instance = GetRateLimit200ResponseRateLimit.from_json(json)
# print the JSON string representation of the object
print(GetRateLimit200ResponseRateLimit.to_json())

# convert the object into a dict
get_rate_limit200_response_rate_limit_dict = get_rate_limit200_response_rate_limit_instance.to_dict()
# create an instance of GetRateLimit200ResponseRateLimit from a dict
get_rate_limit200_response_rate_limit_from_dict = GetRateLimit200ResponseRateLimit.from_dict(get_rate_limit200_response_rate_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


