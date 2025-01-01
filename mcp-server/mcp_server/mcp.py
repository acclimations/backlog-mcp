# server.py
from mcp.server.fastmcp import FastMCP
import os
import backlog_client

# Create an MCP server
mcp = FastMCP("Demo")

# # Add an addition tool
# @mcp.tool()
# def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b

# # Add a dynamic greeting resource
# @mcp.resource("greeting://{name}")
# def get_greeting(name: str) -> str:
#     """Get a personalized greeting"""
#     return f"Hello, {name}!"

configuration = backlog_client.Configuration(
    host = "https://testtechan.backlog.com"
)

configuration.api_key['apiKey'] = os.getenv("BACKLOG_API_KEY")

with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    # try:
    #     # プロジェクト一覧の取得
    #     api_response = api_instance.get_projects(archived=archived, all=all)
    #     print("The response of DefaultApi->get_projects:\n")
        
    # except Exception as e:
    #     print("Exception when calling DefaultApi->get_projects: %s\n" % e)