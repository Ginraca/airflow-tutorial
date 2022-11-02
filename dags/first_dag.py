from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator
import dag_global_settings

dag_global_settings.init()

with DAG(
    dag_id="my_first_dag",
    default_args=dag_global_settings.default_args,
    description="First DAG Example",
    start_date=datetime(2022, 10, 31, 2),
    schedule_interval='@daily'
) as dag:
    task_one = BashOperator(
        task_id="first_task",
        bash_command="echo Hello World!"
    )

    task_two = BashOperator(
        task_id="second_task",
        bash_command="echo Hello Again World!"
    )

    task_three = BashOperator(
        task_id="third_task",
        bash_command="echo Hello Too World!"
    )

    task_one >> [task_two, task_three]