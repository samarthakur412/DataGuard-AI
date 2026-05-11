from numpy import rint

from kafka import KafkaConsumer
from quality_checks.schema_validator import validate_schema
from quality_checks.null_checker import check_nulls
from quality_checks.freshness_checker import check_freshness
from quality_checks.volume_monitor import check_volume
from quality_checks.reliability_score import calculate_reliability_score
from quality_checks.alert_manager import send_alert
import json
import psycopg2
from utils.db import get_connection

# PostgreSQL connection
# conn = psycopg2.connect(
#     host="localhost",
#     database="dataguard",
#     user="postgres",
#     password="*******",
#     port="5432"
# )
conn = get_connection()
cursor = conn.cursor()

# Kafka Consumer
consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='kafka:9092',
    api_version=(2, 0, 2),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='sensor-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Kafka Consumer Started...")

for message in consumer:
    data = message.value

    print(f"Consumed: {data}")

    is_valid, message = validate_schema(data)

    if not is_valid:

        send_alert(
            alert_type="SCHEMA_DRIFT",
            severity="CRITICAL",
            message=message
        )

        continue

    print("Schema validation passed")
    
    null_valid, null_message, null_percentage = check_nulls(data)

    if not null_valid:

        send_alert(
            alert_type="NULL_SPIKE",
            severity="HIGH",
            message=null_message
        )

        continue
    
    print(null_message)
    
    fresh_valid, fresh_message, freshness_delay = check_freshness(data)

    if not fresh_valid:

        send_alert(
            alert_type="STALE_DATA",
            severity="HIGH",
            message=fresh_message
        )

        continue

    print(fresh_message)
    
    volume_valid, volume_message, current_volume = check_volume()

    if not volume_valid:

        send_alert(
            alert_type="VOLUME_SPIKE",
            severity="MEDIUM",
            message=volume_message
        )
    
    print(volume_message)
    
    reliability_score = calculate_reliability_score(
        schema_valid=is_valid,
        null_percentage=null_percentage,
        freshness_delay=freshness_delay,
        volume_normal=volume_valid
    )

    print(f"DATA RELIABILITY SCORE: {reliability_score}/100")
        
    cursor.execute("""
        INSERT INTO sensor_data_bronze (
            timestamp,
            temperature,
            humidity,
            pressure
        )
        VALUES (%s, %s, %s, %s)
    """, (
        data['timestamp'],
        data['temperature'],
        data['humidity'],
        data['pressure']
    ))

    conn.commit()

    print("Inserted into Bronze Layer")
