import sys

sys.path.append("/mnt/d/Placement Projects/data-engineering-project")

from utils.db import get_connection


def check_null_values():
    conn = get_connection()

    if conn is None:
        raise Exception("Database connection failed")

    cursor = conn.cursor()

    query = """
    SELECT COUNT(*)
    FROM sensor_data_silver
    WHERE temperature IS NULL
       OR humidity IS NULL
       OR pressure IS NULL
    """

    cursor.execute(query)

    null_count = cursor.fetchone()[0]

    print(f"Null values found: {null_count}")

    cursor.close()
    conn.close()


def check_duplicates():
    conn = get_connection()

    if conn is None:
        raise Exception("Database connection failed")

    cursor = conn.cursor()

    query = """
    SELECT COUNT(*)
    FROM (
        SELECT timestamp, COUNT(*)
        FROM sensor_data_silver
        GROUP BY timestamp
        HAVING COUNT(*) > 1
    ) duplicates
    """

    cursor.execute(query)

    duplicate_count = cursor.fetchone()[0]

    print(f"Duplicate rows found: {duplicate_count}")

    cursor.close()
    conn.close()


def check_row_count():
    conn = get_connection()

    if conn is None:
        raise Exception("Database connection failed")

    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM sensor_data_silver"

    cursor.execute(query)

    row_count = cursor.fetchone()[0]

    print(f"Total rows: {row_count}")

    cursor.close()
    conn.close()


def check_data_freshness():
    conn = get_connection()

    if conn is None:
        raise Exception("Database connection failed")

    cursor = conn.cursor()

    query = """
    SELECT MAX(timestamp)
    FROM sensor_data_silver
    """

    cursor.execute(query)

    latest_timestamp = cursor.fetchone()[0]

    print(f"Latest data timestamp: {latest_timestamp}")

    cursor.close()
    conn.close()