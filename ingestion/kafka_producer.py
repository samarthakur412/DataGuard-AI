from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    api_version=(2, 0, 2),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Kafka Producer Started...")

while True:
    sensor_data = {
        "timestamp": str(datetime.now()),
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(30, 80), 2),
        "pressure": round(random.uniform(900, 1100), 2)
    }

    producer.send("sensor-data", sensor_data)

    print(f"Produced: {sensor_data}")

    time.sleep(5)