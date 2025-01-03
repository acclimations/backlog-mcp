# GetRateLimit200ResponseRateLimitRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**remaining** | **int** |  | [optional] 
**reset** | **int** |  | [optional] 

## Example

```python
from backlog_client.models.get_rate_limit200_response_rate_limit_read import GetRateLimit200ResponseRateLimitRead

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateLimit200ResponseRateLimitRead from a JSON string
get_rate_limit200_response_rate_limit_read_instance = GetRateLimit200ResponseRateLimitRead.from_json(json)
# print the JSON string representation of the object
print(GetRateLimit200ResponseRateLimitRead.to_json())

# convert the object into a dict
get_rate_limit200_response_rate_limit_read_dict = get_rate_limit200_response_rate_limit_read_instance.to_dict()
# create an instance of GetRateLimit200ResponseRateLimitRead from a dict
get_rate_limit200_response_rate_limit_read_from_dict = GetRateLimit200ResponseRateLimitRead.from_dict(get_rate_limit200_response_rate_limit_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


