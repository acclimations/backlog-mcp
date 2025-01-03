import sys

from typing import Annotated
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union
from typing import get_args
from typing import get_origin


def unwrap_annotation(typ: Any) -> Any:  # noqa: PLR0911
    """
    あらゆる型注釈 (typ) から、Annotated や Optional(= Union[None, T]) 等の
    “ラッパ”を再帰的に取り除き、最終的な型を再構築して返す。
    
    例:
        Annotated[Optional[List[Annotated[int, ...]]], ...] 
        -> List[int]

        Union[None, int, str] -> Union[int, str]
        Tuple[Annotated[int, ...], Annotated[str, ...]] -> Tuple[int, str]
        Callable[[Annotated[int, ...], Annotated[str, ...]], None] -> Callable[[int, str], None]
    """

    # ----- 1) Annotated かどうかを再帰的に外す -----
    while get_origin(typ) is Annotated:
        # Annotated[T, ...] の場合、get_args(typ)[0] が実際の型
        typ = get_args(typ)[0]

    origin = get_origin(typ)

    # ----- 2) Union (Optional[T]含む) の処理 -----
    if origin is Union:
        # Union[...] の各要素を再帰的に外す
        args = [unwrap_annotation(a) for a in get_args(typ)]

        # Union[...] の中から NoneType を除去（Optional の除去）
        # NoneType は type(None) or types.NoneType (Pythonバージョンによって異なる)
        none_types = {type(None)}
        if sys.version_info < (3, 10):  # noqa: UP036
            # Python 3.9以下では types.NoneType が存在しないので、type(None) で判定
            none_types = {type(None)}
        else:
            # Python 3.10 以降でも一応 type(None) があれば十分
            none_types = {type(None)}

        non_none_args = [a for a in args if a not in none_types]

        # もし Union の中身が1つしか残らなければ、そのまま返す (Optional除去)
        if len(non_none_args) == 1:
            return non_none_args[0]
        # もし複数あれば Union[...] を再構築
        return Union[tuple(non_none_args)]  # noqa: UP007

    # ----- 3) ジェネリック (List, Dict, Tuple, Callable など) の処理 -----
    if origin is not None:
        # 例: List[int], Dict[str, int], Tuple[int, str], Callable[[int], str] ...
        # 中の引数を再帰的に unwrap して再度組み立てる
        args = get_args(typ)
        new_args = tuple(unwrap_annotation(a) for a in args)

        # origin が例えば list, dict, tuple, collections.abc.Callable などの場合に応じて再構築
        # （Python 3.9+ であれば、 `list[int]` のようなネイティブジェネリックを使う場合もある）
        if origin in (list, List):
            return List[new_args[0]] if len(new_args) == 1 else List[Any]
        if origin in (dict, Dict):
            return Dict[new_args] if len(new_args) == 2 else Dict[Any, Any]
        if origin in (tuple, Tuple):
            return Tuple[new_args]
        if origin in (callable, Callable):
            # Callable[[arg1, arg2, ...], ret]
            # ※ get_args(Callable[[...], ret]) は ([arg1, arg2, ...], ret) になる
            if len(new_args) == 2 and isinstance(new_args[0], tuple):
                return Callable[new_args[0], new_args[1]] # type: ignore
            return Callable[..., Any]
        # 上記以外のジェネリック型 (Set, FrozenSet, Type, etc.) にも対応したい場合は同様に分岐を足す

        # もしここに来たら何か独自のジェネリック (例: "MyGeneric[T]" など)
        # あるいはまだ対応書いていないジェネリックの場合
        # 可能であれば型を再構築して返す
        try:
            return origin[new_args]
        except TypeError:
            # Python のバージョンやカスタムクラスの実装状況によっては
            # `origin[new_args]` が失敗する場合がある
            return origin

    # ----- 4) ここまで来たら単純な型 (int, str, カスタムクラスなど) -----
    return typ

def is_finally_list_type(typ) -> bool:
    # unwrap_annotation で Annotated や Optional (= Union[None, T]) 等をすべて剥がす
    final_type = unwrap_annotation(typ)
    # それが List であれば True, それ以外なら False
    return get_origin(final_type) in (list, List)

# --- 動作確認例 ---

if __name__ == "__main__":

    # 1) Annotated[Optional[List[Annotated[int, ...]]], ...]
    #    -> List[int]
    Example1 = Annotated[List[Annotated[int, ...]] | None, "some meta"]
    print(unwrap_annotation(Example1), is_finally_list_type(Example1))
    # -> typing.List[int]

    # 2) Union[None, int, str] -> Union[int, str]
    Example2 = Union[None, int, str]  # noqa: UP007
    print(unwrap_annotation(Example2))
    # -> typing.Union[int, str]

    # 3) Tuple[Annotated[int, ...], Annotated[str, ...]] -> Tuple[int, str]
    Example3 = Tuple[Annotated[int, ...], Annotated[str, ...]]
    print(unwrap_annotation(Example3))
    # -> typing.Tuple[int, str]

    # 4) Callable[[Annotated[int, ...], Annotated[str, ...]], None]
    #    -> Callable[[int, str], None]
    from typing import Callable
    Example4 = Callable[[Annotated[int, ...], Annotated[str, ...]], None]
    print(unwrap_annotation(Example4))
    # -> typing.Callable[[int, str], None]
