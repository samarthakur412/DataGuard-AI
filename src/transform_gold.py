from utils.db import get_connection


def transform_to_gold():

    conn = get_connection()

    if conn is None:
        raise Exception("Database connection failed")

    cursor = conn.cursor()

    # =========================
    # Get Gold Watermark
    # =========================

    cursor.execute("""
        SELECT last_processed_timestamp
        FROM pipeline_watermark
        WHERE pipeline_name = 'gold_pipeline'
    """)

    last_watermark = cursor.fetchone()[0]

    print(f"Gold watermark: {last_watermark}")

    # =========================
    # Aggregate NEW Silver Data
    # =========================

    cursor.execute("""
        SELECT
            AVG(temperature),
            AVG(humidity),
            MAX(pressure),
            COUNT(*),
            MAX(timestamp)
        FROM sensor_data_silver
        WHERE timestamp > %s
    """, (last_watermark,))

    result = cursor.fetchone()

    avg_temperature = result[0]
    avg_humidity = result[1]
    max_pressure = result[2]
    total_events = result[3]
    latest_timestamp = result[4]

    # =========================
    # No New Data
    # =========================

    if total_events == 0:
        print("No new Silver data")

        conn.close()
        return

    # =========================
    # Insert Gold Metrics
    # =========================

    cursor.execute("""
        INSERT INTO sensor_data_gold (
            minute_window,
            avg_temperature,
            avg_humidity,
            max_pressure,
            total_events
        )
        VALUES (%s, %s, %s, %s, %s)
    """, (
        latest_timestamp,
        avg_temperature,
        avg_humidity,
        max_pressure,
        total_events
    ))

    # =========================
    # Update Watermark
    # =========================

    cursor.execute("""
        UPDATE pipeline_watermark
        SET last_processed_timestamp = %s
        WHERE pipeline_name = 'gold_pipeline'
    """, (latest_timestamp,))

    conn.commit()

    print("Gold aggregation inserted")

    print(f"""
    Avg Temperature: {avg_temperature}
    Avg Humidity   : {avg_humidity}
    Max Pressure   : {max_pressure}
    Total Events   : {total_events}
    """)

    cursor.close()
    conn.close()

    print("Streaming Gold Transformation Complete")