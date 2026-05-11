from utils.db import get_connection

def log_quality_check(check_name, status, issue_count, message):

    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO data_quality_logs
    (check_name, status, issue_count, message)
    VALUES (%s, %s, %s, %s)
    """

    cur.execute(
        query,
        (check_name, status, issue_count, message)
    )

    conn.commit()

    cur.close()
    conn.close()