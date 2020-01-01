from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from dags.operators.hello_operator import HelloOperator

default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('hello', default_args=default_args, schedule_interval=timedelta(days=1))

with dag:
    t1 = BashOperator(task_id='print_date', bash_command='date', dag=dag)
    t2 = HelloOperator(task_id='hello', name='foo_bar')

    t1 >> t2
