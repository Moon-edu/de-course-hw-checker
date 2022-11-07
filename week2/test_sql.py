from utils import file_utils, db_utils
from pytest_unordered import unordered


WEEK = 2
EMPLOYEE_TABLE = "employee"


class DBColumn:
    def __init__(self, col_name, col_type, nullable, max_length):
        self.col_name = col_name
        self.col_type = col_type
        self.nullable = nullable
        self.max_length = max_length


def test_create_employee_table():
    filename = "q1_create_employee_table.sql"
    query = file_utils.read_homework_file(WEEK, filename).strip()
    db_utils.execute(query, False)

    # Get all columns
    query = f"""
        SELECT column_name, data_type, is_nullable, character_maximum_length
        FROM information_schema.columns
        WHERE table_name = '{EMPLOYEE_TABLE}';
    """
    columns = db_utils.execute(query, True)

    expected_cols = [
        ("emp_id", "character", "NO", 6),
        ("gender", "character varying", "NO", 6),
        ("name", "character varying", "NO", 20),
        ("address", "character varying", "YES", 100),
        ("department", "integer", "YES", None),
        ("manager", "character", "YES", 6),
        ("age", "integer", "NO", None),
        ("position", "character varying", "YES", 30)
    ]
    assert columns == unordered(expected_cols)