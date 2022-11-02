from airflow import DAG
from datetime import datetime, timedelta
import json
from airflow.operators.python import PythonOperator
import dag_global_settings

dag_global_settings.init()

def greet(ti):
    name = ti.xcom_pull(task_ids="get_name", key="name")
    time = ti.xcom_pull(task_ids="get_time", key="curr_date")
    print("Hello World! My name is {} and it is currently {} where i'm at".format(name, time))

def get_name(ti):
    ti.xcom_push(key="name", value="ginraca")

def get_time(ti):
    curr_date = json.dumps(datetime.now(), default=str)
    ti.xcom_push(key="curr_date", value=curr_date)

with DAG(
    dag_id="my_python_op_dag",
    default_args=dag_global_settings.default_args,
    description="DAG using Python Operator Example",
    start_date=datetime(2022, 10, 31, 2),
    schedule_interval='@daily'
) as dag:
    task_one = PythonOperator(
        task_id="get_time",
        python_callable=get_time
    )

    task_two = PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )

    task_three = PythonOperator(
        task_id="finale",
        python_callable=greet
    )

    [task_one, task_two] >> task_three