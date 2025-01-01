# encoding: utf-8

# server.py
from typing import Annotated, Optional
from mcp.server.fastmcp import FastMCP
from functools import wraps
import os
import backlog_client
import inspect
import logging

from pydantic import Field, StrictBool
logging.basicConfig(level=logging.WARNING)

configuration = backlog_client.Configuration(
    host = "https://testtechan.backlog.com"
)

configuration.api_key['apiKey'] = os.getenv("BACKLOG_API_KEY")
api_client = backlog_client.ApiClient(configuration) 
api_instance = backlog_client.DefaultApi(api_client)

mcp = FastMCP("Demo", log_level="WARNING")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """２つの数字を足し合わせます。"""
    return a + b


def remove_underscore_args(func):
    """
    func のシグネチャから、アンダースコア始まりの引数を取り除いた関数を返す。
    """
    sig = inspect.signature(func)
    original_params = list(sig.parameters.values())

    # アンダースコアで始まる名前だけ除外
    new_params = [
        p for p in original_params
        if not p.name.startswith("_")
    ]

    # 新しい signature を再構築
    new_sig = sig.replace(parameters=new_params)
    
    # docstringのタイトルと説明以外を削除
    docstring = func.__doc__
    if docstring:
        docstring = "\n".join(docstring.split("\n")[:2])
    else:
        docstring = ""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # 実際には削除した引数が呼ばれてもエラーにならないように、kwargs から pop するなど
        remove_keys = [k for k in kwargs if k.startswith("_")]
        for k in remove_keys:
            kwargs.pop(k, None)
        
        return func(*args, **kwargs)
    # 新しいシグネチャを付与する
    wrapper.__signature__ = new_sig
    wrapper.__doc__ = docstring

    return wrapper

mcp.tool()(remove_underscore_args(api_instance.get_projects))
mcp.tool()(remove_underscore_args(api_instance.get_issues))
mcp.tool()(remove_underscore_args(api_instance.get_issue_types))
mcp.tool()(remove_underscore_args(api_instance.get_priorities))
mcp.tool()(remove_underscore_args(api_instance.create_issue))