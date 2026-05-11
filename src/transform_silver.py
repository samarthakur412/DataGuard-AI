from utils.db import get_connection


def transform_to_silver():

    conn = get_connection()

    if conn is None:
        raise Exception("Database connection failed")

    cursor = conn.cursor()

    # =========================
    # Get Watermark
    # =========================

    cursor.execute("""
        SELECT last_processed_timestamp
        FROM pipeline_watermark
        WHERE pipeline_name = 'silver_pipeline'
    """)

    last_watermark = cursor.fetchone()[0]

    print(f"Last watermark: {last_watermark}")

    # =========================
    # Read ONLY new Bronze records
    # =========================

    cursor.execute("""
        SELECT
            timestamp,
            temperature,
            humidity,
            pressure
        FROM sensor_data_bronze
        WHERE timestamp > %s
        ORDER BY timestamp
    """, (last_watermark,))

    rows = cursor.fetchall()

    print(f"New Bronze records found: {len(rows)}")

    if len(rows) == 0:
        print("No new records")
        conn.close()
        return

    # =========================
    # Process records
    # =========================

    inserted_count = 0

    for row in rows:

        timestamp, temperature, humidity, pressure = row

        # -------------------------
        # Business Rule Validation
        # -------------------------

        if temperature < -50 or temperature > 100:
            print(f"Invalid temperature skipped: {temperature}")
            continue

        if humidity < 0 or humidity > 100:
            print(f"Invalid humidity skipped: {humidity}")
            continue

        # -------------------------
        # Insert into Silver
        # -------------------------

        cursor.execute("""
            INSERT INTO sensor_data_silver (
                timestamp,
                temperature,
                humidity,
                pressure
            )
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (timestamp)
            DO NOTHING
        """, (
            timestamp,
            temperature,
            humidity,
            pressure
        ))

        inserted_count += 1

    # =========================
    # Update Watermark
    # =========================

    latest_timestamp = rows[-1][0]

    cursor.execute("""
        UPDATE pipeline_watermark
        SET last_processed_timestamp = %s
        WHERE pipeline_name = 'silver_pipeline'
    """, (latest_timestamp,))

    conn.commit()

    print(f"Inserted into Silver: {inserted_count}")
    print(f"Watermark updated to: {latest_timestamp}")

    cursor.close()
    conn.close()

    print("Streaming Silver Transformation Complete")