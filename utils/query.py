from utils.db import get_connection

def get_row_count():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM sensor_data;")
    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    print(f"Total rows in sensor_data: {count}")

if __name__ == "__main__":
    get_row_count()