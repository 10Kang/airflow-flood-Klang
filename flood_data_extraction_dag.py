# import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.python import PythonOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago
# import the own written function
from extract_load_data import extract_load_flood_data
# import timenow 
from datetime import datetime

# defining DAG arguments
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Zhi Yong',
    'start_date': datetime(2023,9,24),
    'email': ['kangzhiyong@xxxmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# define the DAG
dag = DAG(
    dag_id='flood-data-extraction-Klang',
    default_args=default_args,
    catchup=False,
    description='A ETL to load flood monitoring data to postgresql',
    schedule_interval=timedelta(minutes=15), # choose 15 minutes as the arrival of new data is in 15 minutes interval
)

# define the first task in pipeline 
extract_load = PythonOperator( 
    task_id='extract_load',
    python_callable=extract_load_flood_data,
    dag=dag,
)

# data pipeline

extract_load