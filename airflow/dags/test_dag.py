from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'jupyter',
    'start_date': datetime(2025, 2, 8)
}

with DAG(
    dag_id='data_pipeline',
    default_args=default_args,
    schedule_interval=None
) as dag:

    task_request = BashOperator(
        task_id='run_data_request',
        bash_command='spark-submit /home/jupyter/app/data_request.py'
    )

    task_processing = BashOperator(
        task_id='run_data_processing',
        bash_command='spark-submit /home/jupyter/app/data_processing.py'
    )

    task_request >> task_processing