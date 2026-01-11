from airflow import DAG
from airflow.models import Variable
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime, timedelta

ENV = "dev"

with DAG(
    dag_id="stock_lakehouse_pipeline",
    start_date=datetime.now() - timedelta(days=1),
    schedule_interval= None,
    catchup=False,
    max_active_runs = 1
) as dag:

    bronze = DatabricksRunNowOperator(
        task_id="bronze_ingestion",
        databricks_conn_id="databricks_auth",
        job_id=Variable.get("DATABRICKS_JOB_ID_BRONZE" , default_var="DUMMY_JOB_ID"),
        notebook_params={
            "env": ENV
        }
    )

    silver = DatabricksRunNowOperator(
        task_id="silver_processing",
        databricks_conn_id="databricks_auth",
        job_id=Variable.get("DATABRICKS_JOB_ID_SILVER" , default_var="DUMMY_JOB_ID"),
        notebook_params={
            "env": ENV
        }
    )

    gold = DatabricksRunNowOperator(
        task_id="gold_modeling",
        databricks_conn_id="databricks_auth",
        job_id=Variable.get("DATABRICKS_JOB_ID_GOLD" , default_var="DUMMY_JOB_ID"),
        notebook_params={
            "env": ENV
        }
    )


    bronze >> silver >> gold

