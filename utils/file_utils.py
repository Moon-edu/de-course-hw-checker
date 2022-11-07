import os
from utils import env


def read_homework_file(week: int, fname: str) -> str:
    absolute_path = os.path.join(env.get_query_dir_path(week), fname)
    print(f"Reading file from {absolute_path} for Week{week}")
    with open(absolute_path, "r") as f:
        return f.read()
