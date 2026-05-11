# 🚀 DataGuard — Real-Time Streaming Data Reliability Platform

## 📌 Overview

DataGuard is a real-time streaming data engineering platform built using Kafka, Airflow, PostgreSQL, Docker, and Streamlit.

The platform simulates enterprise-grade streaming pipelines using a Bronze/Silver/Gold medallion architecture while implementing reliability engineering concepts such as:

- Schema Drift Detection
- Null Spike Monitoring
- Freshness Monitoring
- Volume Spike Detection
- Reliability Scoring
- Incremental Processing with Watermarks
- Real-Time Monitoring Dashboard

This project demonstrates end-to-end distributed data engineering workflows including ingestion, transformation, orchestration, observability, and monitoring.

---

# 🏗️ Architecture

```text
Kafka Producer
    ↓
Kafka Topic (sensor-data)
    ↓
Kafka Consumer
    ↓
Bronze Layer (Raw Streaming Data)
    ↓
Airflow DAG Orchestration
    ↓
Silver Layer (Validated & Cleaned Data)
    ↓
Gold Layer (Aggregated Analytics)
    ↓
Streamlit Monitoring Dashboard
```

---

# ⚙️ Tech Stack

| Category         | Technologies                     |
| ---------------- | -------------------------------- |
| Streaming        | Apache Kafka                     |
| Orchestration    | Apache Airflow                   |
| Database         | PostgreSQL                       |
| Dashboard        | Streamlit                        |
| Containerization | Docker & Docker Compose          |
| Language         | Python                           |
| Monitoring       | Custom Reliability Framework     |
| Architecture     | Bronze / Silver / Gold Medallion |

---

# ✨ Key Features

## 🔄 Real-Time Streaming Pipeline

- Kafka producer generates simulated IoT sensor data
- Kafka consumer ingests streaming events continuously
- Real-time ingestion into Bronze layer

---

## 🥉 Bronze Layer

Stores raw streaming events exactly as received.

### Responsibilities

- Raw event ingestion
- Immutable streaming storage
- Initial reliability scoring

---

## 🥈 Silver Layer

Validated and cleaned data layer.

### Reliability Checks

- Schema validation
- Null monitoring
- Freshness checks
- Volume anomaly detection
- Duplicate handling

---

## 🥇 Gold Layer

Business-level aggregated analytics.

### Aggregations

- Average temperature
- Average humidity
- Maximum pressure
- Total streaming events

---

## 🚨 Reliability Engineering Framework

Implemented custom monitoring system for:

### ✅ Schema Drift Detection

Detects datatype changes in streaming events.

### ✅ Null Spike Detection

Detects sudden increase in missing values.

### ✅ Freshness Monitoring

Ensures streaming events arrive within acceptable delay windows.

### ✅ Volume Monitoring

Detects abnormal event spikes or drops.

### ✅ Reliability Score

Calculates data quality score based on:

```text
Reliability Score =
Freshness + Completeness + Consistency
```

---

# 📊 Monitoring Dashboard

The Streamlit dashboard provides:

- Live pipeline KPIs
- Temperature trends
- Humidity trends
- Pressure trends
- Event volume metrics
- Pipeline health monitoring
- Real-time Gold layer analytics

---

# 🔁 Incremental Processing with Watermarks

The platform uses watermark-based incremental processing to:

- Prevent duplicate processing
- Support idempotent transformations
- Process only new incoming records
- Improve scalability and efficiency

---

# 📂 Project Structure

```text
DataGuard/
│
├── dags/
├── dashboard/
├── ingestion/
├── quality_checks/
├── src/
├── utils/
├── docs/
├── screenshots/
├── sql/
├── tests/
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env.example
```

---

# 🚀 Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/dataguard-streaming-platform.git

cd dataguard-streaming-platform
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv airflow_venv

source airflow_venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Start Docker Services

```bash
docker compose up -d
```

Services started:

- PostgreSQL
- Kafka
- Zookeeper
- Airflow

---

## 5️⃣ Start Kafka Producer

Inside Airflow container:

```bash
docker exec -it dataguard_airflow bash

cd /opt/airflow/project
python -m ingestion.kafka_producer
```

---

## 6️⃣ Start Kafka Consumer

Open second terminal:

```bash
docker exec -it dataguard_airflow bash

cd /opt/airflow/project
python -m ingestion.kafka_consumer
```

---

## 7️⃣ Open Airflow

```text
http://localhost:8080
```

Enable DAG:

```text
dataguard_pipeline
```

---

## 8️⃣ Launch Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

# 📈 Example Pipeline Flow

```text
Producer generates sensor event
        ↓
Kafka topic receives event
        ↓
Consumer validates event
        ↓
Bronze stores raw event
        ↓
Airflow triggers transformations
        ↓
Silver cleans and validates data
        ↓
Gold aggregates analytics
        ↓
Dashboard visualizes metrics
```

---

# 🧠 Engineering Concepts Demonstrated

This project demonstrates:

- Real-time streaming pipelines
- Distributed systems debugging
- Incremental ETL processing
- Medallion architecture
- Reliability engineering
- Observability frameworks
- Data quality monitoring
- Containerized infrastructure
- Cross-container networking
- Workflow orchestration

---

# 🖼️ Screenshots

Add screenshots here:

```text
screenshots/
├── airflow_dag.png
├── dashboard.png
├── kafka_producer.png
├── kafka_consumer.png
└── lineage.png
```

---

# 🔥 Future Improvements

## Data Engineering

- PySpark Streaming
- dbt Transformations
- MinIO/S3 Data Lake
- Delta Lake

## Observability

- Grafana
- Prometheus
- Slack Alerts
- Email Notifications

## DevOps

- CI/CD Pipelines
- Kubernetes Deployment
- Terraform Infrastructure
- Custom Docker Images

---

# 📌 Resume Highlights

- Built a real-time streaming data platform using Kafka, Airflow, PostgreSQL, Docker, and Streamlit implementing Bronze/Silver/Gold medallion architecture.
- Implemented reliability engineering features including schema drift detection, freshness monitoring, null spike detection, and volume anomaly detection.
- Designed incremental ETL pipelines using watermark-based processing to ensure idempotent transformations and prevent duplicate processing.
- Developed live observability dashboards for monitoring streaming analytics and pipeline health.

---

# 👨‍💻 Author

Samarjeet Singh

---

# ⭐ Final Note

This project was designed to simulate production-inspired streaming data engineering systems with a strong focus on reliability, observability, and scalable architecture.
