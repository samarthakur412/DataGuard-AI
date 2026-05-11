import sys

sys.path.append("/mnt/d/Placement Projects/data-engineering-project")

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.transform_silver import transform_to_silver
from src.transform_gold import transform_to_gold

from quality_checks.checks import (
    check_null_values,
    check_duplicates,
    check_row_count,
    check_data_freshness
)

# =========================
# Default DAG Arguments
# =========================

default_args = {
    "owner": "samar",
    "start_date": datetime(2026, 5, 10),
    "retries": 1
}

# =========================
# DAG Definition
# =========================

with DAG(
    dag_id="dataguard_pipeline",
    default_args=default_args,
    schedule="*/1 * * * *",   # every 1 minute
    catchup=False,
    description="Real-Time Streaming Medallion Pipeline"
) as dag:

    # =========================
    # Silver Transformation
    # =========================

    silver_transformation = PythonOperator(
        task_id="silver_transformation",
        python_callable=transform_to_silver
    )

    # =========================
    # Gold Transformation
    # =========================

    gold_transformation = PythonOperator(
        task_id="gold_transformation",
        python_callable=transform_to_gold
    )

    # =========================
    # Data Quality Checks
    # =========================

    null_check = PythonOperator(
        task_id="null_check",
        python_callable=check_null_values
    )

    duplicate_check = PythonOperator(
        task_id="duplicate_check",
        python_callable=check_duplicates
    )

    row_count_check = PythonOperator(
        task_id="row_count_check",
        python_callable=check_row_count
    )

    freshness_check = PythonOperator(
        task_id="freshness_check",
        python_callable=check_data_freshness
    )

    # =========================
    # DAG Flow
    # =========================

    (
        silver_transformation
        >> gold_transformation
        >> [
            null_check,
            duplicate_check,
            row_count_check,
            freshness_check
        ]
    )