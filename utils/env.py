import os
from typing import Any


HOMEWORK_PATH = "HOMEWORK_PATH"
DB_CONN_STR = "DB_CONN_STR"


def _get_or_exception(key: str) -> Any:
    v = os.getenv(key)
    if not v:
        raise Exception(f"No {v} given!")
    return v


def get_conn_str() -> str:
    return _get_or_exception(DB_CONN_STR)


def get_query_dir_path(week: int) -> str:
    path = _get_or_exception(HOMEWORK_PATH)
    return os.path.join(path, f"week{week}")