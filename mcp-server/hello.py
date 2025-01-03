import inspect
import logging
import os

from dataclasses import dataclass
from functools import wraps
from typing import Annotated
from typing import Protocol

import backlog_client
import yaml

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from pydantic import Field

import annot


logging.basicConfig(level=logging.WARNING)


class IdNameMapper(Protocol):
    """ID-名前マッピングを生成する関数のプロトコル"""

    def __call__(self) -> dict[str, int]:
        ...


@dataclass
class ParameterMapping:
    """パラメータの変換に必要な情報を保持するクラス"""

    mapper: IdNameMapper  # ID-名前マッピングを生成する関数
    param_name: str  # 変換後のパラメータ名
    description: str  # パラメータの説明


configuration = backlog_client.Configuration(host="https://testtechan.backlog.com")

configuration.api_key["apiKey"] = os.getenv("BACKLOG_API_KEY")
api_client = backlog_client.ApiClient(configuration)
api_instance = backlog_client.DefaultApi(api_client)

mcp = FastMCP("Demo", log_level="WARNING")


def get_issue_type_map() -> dict[str, int]:
    """課題タイプのマッピングを生成"""
    items = api_instance.get_issue_types("DAMDAM")
    return {item.name: item.id for item in items}


def get_priority_map() -> dict[str, int]:
    """優先度のマッピングを生成"""
    items = api_instance.get_priorities()
    return {item.name: item.id for item in items}


def get_project_map() -> dict[str, int]:
    """プロジェクトのマッピングを生成"""
    items = api_instance.get_projects()
    return {item.name: item.id for item in items}


# パラメータとマッパー関数のマッピング
PARAMETER_MAPPINGS = {
    "issue_type_id": ParameterMapping(
        mapper=get_issue_type_map,
        param_name="issue_type_name",
        description="課題の種類",
    ),
    "priority_id": ParameterMapping(
        mapper=get_priority_map,
        param_name="priority_name",
        description="優先度",
    ),
    "project_id": ParameterMapping(
        mapper=get_project_map,
        param_name="project__name",
        description="プロジェクト名",
    ),
}

# 各パラメータの値を事前に取得
PARAMETER_VALUES = {}
for param_id, mapping in PARAMETER_MAPPINGS.items():
    PARAMETER_VALUES[param_id] = mapping.mapper()


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """２つの数字を足し合わせます。"""
    return a + b


def remove_underscore_args(func):
    """funcのシグネチャから、アンダースコア始まりの引数を取り除いた関数を返す。"""
    sig = inspect.signature(func)
    original_params = list(sig.parameters.values())

    # アンダースコアで始まる名前だけ除外
    new_params = [p for p in original_params if not p.name.startswith("_")]

    # docstringのタイトルと説明以外を削除
    docstring = "\n".join(func.__doc__.split("\n")[:2]) if func.__doc__ else ""

    # 変換が必要なパラメータを処理
    param_names = [p.name for p in original_params]
    for param_id, mapping in PARAMETER_MAPPINGS.items():
        if param_id in param_names:
            # IDパラメータを削除し、名前パラメータを追加
            new_params = [p for p in new_params if p.name != param_id]
            default_type = str

            # 対象のパラメータが配列かどうかを確認
            param_type = sig.parameters[param_id].annotation
            is_list = annot.is_finally_list_type(param_type)
            if is_list:
                default_type = list[str]

            # 新しいパラメータを追加
            new_params.append(
                inspect.Parameter(
                    name=mapping.param_name,
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=inspect.Parameter.empty,
                    annotation=Annotated[
                        default_type,
                        Field(
                            description=mapping.description,
                            enum=list(PARAMETER_VALUES[param_id].keys()),
                        ),
                    ],
                )
            )

    # 新しい signature を再構築
    new_sig = sig.replace(parameters=new_params)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # アンダースコア始まりの引数を削除
        remove_keys = [k for k in kwargs if k.startswith("_")]
        for k in remove_keys:
            kwargs.pop(k, None)

        # 各パラメータの変換処理
        for param_id, mapping in PARAMETER_MAPPINGS.items():
            name_param = mapping.param_name
            if name_param in kwargs:
                name_value = kwargs[name_param]
                # 配列を受け取った場合は、各要素を変換
                if isinstance(name_value, list):
                    kwargs[param_id] = [
                        PARAMETER_VALUES[param_id][v] for v in name_value
                    ]
                else:
                    kwargs[param_id] = PARAMETER_VALUES[param_id][name_value]
                kwargs.pop(name_param, None)

        result = func(*args, **kwargs)

        # 通常の戻り値の場合はそのまま返す
        if issubclass(type(result), BaseModel):
            return yaml.dump(result.model_dump(), allow_unicode=True)
        
        # リストかつ BaseModel のインスタンスの場合は、各要素を変換
        if isinstance(result, list) and all(issubclass(type(r), BaseModel) for r in result):
            return yaml.dump([r.model_dump() for r in result], allow_unicode=True)

        return result

    # 新しいシグネチャを付与する
    wrapper.__signature__ = new_sig
    wrapper.__doc__ = docstring

    return wrapper


mcp.tool()(remove_underscore_args(api_instance.get_projects))
mcp.tool()(remove_underscore_args(api_instance.get_issues))
mcp.tool()(remove_underscore_args(api_instance.get_issue_types))
mcp.tool()(remove_underscore_args(api_instance.get_priorities))
mcp.tool()(remove_underscore_args(api_instance.create_issue))
