import random
from datetime import datetime

from utils.db import get_connection


def generate_sensor_data():
    conn = get_connection()

    if conn is None:
        print("Database connection failed")
        return

    cursor = conn.cursor()

    timestamp = datetime.now()

    temperature = round(random.uniform(20, 40), 2)
    humidity = round(random.uniform(30, 90), 2)
    pressure = round(random.uniform(900, 1100), 2)

    insert_query = """
    INSERT INTO sensor_data_bronze
    (timestamp, temperature, humidity, pressure)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        insert_query,
        (timestamp, temperature, humidity, pressure)
    )

    conn.commit()

    print("Data inserted into Bronze layer")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    generate_sensor_data()