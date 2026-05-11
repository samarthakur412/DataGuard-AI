# import streamlit as st
# import pandas as pd
# import psycopg2
# from streamlit_autorefresh import st_autorefresh

# # Auto refresh every 5 seconds
# st_autorefresh(interval=5000, key="refresh")

# # Page config
# st.set_page_config(
#     page_title="DataGuard Platform",
#     layout="wide"
# )

# # Title
# st.title("🚀 DataGuard Real-Time Monitoring Platform")

# # Database connection
# conn = psycopg2.connect(
#     host="localhost",
#     database="dataguard",
#     user="postgres",
#     password="6260347112S@m",
#     port="5432"
# )

# # Query
# query = """
# SELECT *
# FROM sensor_data_gold
# ORDER BY aggregation_time DESC
# LIMIT 50
# """

# # Load dataframe
# df = pd.read_sql(query, conn)

# # =========================
# # KPI SECTION
# # =========================

# st.subheader("📊 Pipeline KPIs")

# col1, col2, col3, col4 = st.columns(4)

# latest = df.iloc[0]

# col1.metric(
#     "Total Events",
#     int(latest["total_events"])
# )

# col2.metric(
#     "Avg Temperature",
#     round(latest["avg_temperature"], 2)
# )

# col3.metric(
#     "Avg Humidity",
#     round(latest["avg_humidity"], 2)
# )

# reliability_score = 100

# col4.metric(
#     "Reliability Score",
#     f"{reliability_score}/100"
# )

# # =========================
# # PIPELINE STATUS
# # =========================

# st.subheader("🟢 Pipeline Health")

# st.success("Kafka Streaming Pipeline Operational")

# # =========================
# # TEMPERATURE CHART
# # =========================

# st.subheader("🌡️ Temperature Trend")

# chart_data = df.sort_values("aggregation_time")

# st.line_chart(
#     chart_data.set_index("aggregation_time")["avg_temperature"]
# )

# # =========================
# # HUMIDITY CHART
# # =========================

# st.subheader("💧 Humidity Trend")

# st.line_chart(
#     chart_data.set_index("aggregation_time")["avg_humidity"]
# )

# # =========================
# # LIVE TABLE
# # =========================

# st.subheader("📄 Latest Streaming Records")

# st.dataframe(df, use_container_width=True)

# # =========================
# # ALERT PANEL
# # =========================

# st.subheader("🚨 Alert Status")

# st.info("No active critical alerts")

# conn.close()

import streamlit as st
import pandas as pd
import psycopg2
from streamlit_autorefresh import st_autorefresh

# =====================================
# AUTO REFRESH
# =====================================

st_autorefresh(interval=5000, key="refresh")

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="DataGuard Platform",
    layout="wide"
)

# =====================================
# TITLE
# =====================================

st.title("🚀 DataGuard Real-Time Monitoring Platform")

# =====================================
# DATABASE CONNECTION
# =====================================

conn = psycopg2.connect(
    host="localhost",
    database="dataguard",
    user="postgres",
    password="6260347112S@m",
    port="5432"
)

# =====================================
# LOAD GOLD DATA
# =====================================

query = """
SELECT *
FROM sensor_data_gold
ORDER BY minute_window DESC
LIMIT 50
"""

df = pd.read_sql(query, conn)

# =====================================
# HANDLE EMPTY DATA
# =====================================

if df.empty:
    st.warning("No Gold Layer data available yet.")
    st.stop()

# =====================================
# LATEST KPI RECORD
# =====================================

latest = df.iloc[0]

# =====================================
# KPI SECTION
# =====================================

st.subheader("📊 Pipeline KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Events",
    int(latest["total_events"])
)

col2.metric(
    "Avg Temperature",
    round(latest["avg_temperature"], 2)
)

col3.metric(
    "Avg Humidity",
    round(latest["avg_humidity"], 2)
)

# Reliability score placeholder
reliability_score = 100

col4.metric(
    "Reliability Score",
    f"{reliability_score}/100"
)

# =====================================
# PIPELINE STATUS
# =====================================

st.subheader("🟢 Pipeline Health")

st.success("Kafka Streaming Pipeline Operational")

# =====================================
# CHART DATA
# =====================================

chart_data = df.sort_values("minute_window")

# =====================================
# TEMPERATURE TREND
# =====================================

st.subheader("🌡️ Average Temperature Trend")

st.line_chart(
    chart_data.set_index("minute_window")["avg_temperature"]
)

# =====================================
# HUMIDITY TREND
# =====================================

st.subheader("💧 Average Humidity Trend")

st.line_chart(
    chart_data.set_index("minute_window")["avg_humidity"]
)

# =====================================
# PRESSURE TREND
# =====================================

st.subheader("📈 Maximum Pressure Trend")

st.line_chart(
    chart_data.set_index("minute_window")["max_pressure"]
)

# =====================================
# EVENT VOLUME TREND
# =====================================

st.subheader("📦 Event Volume Trend")

st.bar_chart(
    chart_data.set_index("minute_window")["total_events"]
)

# =====================================
# LIVE GOLD TABLE
# =====================================

st.subheader("📄 Gold Layer Aggregated Metrics")

st.dataframe(
    df,
    use_container_width=True
)

# =====================================
# ALERT PANEL
# =====================================

st.subheader("🚨 Alert Status")

st.info("No active critical alerts")

# =====================================
# ARCHITECTURE INFO
# =====================================

st.subheader("🏗️ Pipeline Architecture")

st.markdown("""
Kafka Producer  
⬇️  
Kafka Topic (`sensor-data`)  
⬇️  
Bronze Layer (`sensor_data_bronze`)  
⬇️  
Silver Layer (`sensor_data_silver`)  
⬇️  
Gold Layer (`sensor_data_gold`)  
⬇️  
Streamlit Monitoring Dashboard
""")

# =====================================
# CLOSE CONNECTION
# =====================================

conn.close()