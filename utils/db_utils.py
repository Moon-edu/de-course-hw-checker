import psycopg
from utils import env
from typing import Any


def execute(query: str, has_result: bool = False) -> Any:
    conn_info = env.get_conn_str()
    with psycopg.connect(conninfo=conn_info) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            if has_result:
                return cur.fetchall()
            else:
                return
