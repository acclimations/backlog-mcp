import time
import os
import backlog_client
from backlog_client.models.get_projects200_response_inner import GetProjects200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "https://testtechan.backlog.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.getenv("BACKLOG_API_KEY")

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    archived = False # bool | 省略された場合は全てのプロジェクト、falseの場合はアーカイブされていないプロジェクト、trueの場合はアーカイブされたプロジェクトを返します。 (optional)
    all = True # bool | ユーザが管理者権限の場合のみ有効なパラメータです。trueの場合はすべてのプロジェクト、falseの場合は参加しているプロジェクトのみを返します。初期値はfalse。 (optional)

    try:
        # プロジェクト一覧の取得
        api_response = api_instance.get_projects(archived=archived, all=all)
        print("The response of DefaultApi->get_projects:\n")
        pprint(api_response)
        
    except Exception as e:
        print("Exception when calling DefaultApi->get_projects: %s\n" % e)