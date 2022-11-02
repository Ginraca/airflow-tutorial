from airflow.decorators import dag, task
from datetime import datetime, timedelta
import dag_global_settings
import json

dag_global_settings.init()

@dag(
    dag_id="dag_with_taskflow_example",
    default_args=dag_global_settings.default_args,
    description="DAG Example using Taskflow API",
    start_date=datetime(2022, 10, 31),
    schedule_interval="@daily"
)
def hello_world_etl():

    @task
    def get_name():
        return "Alwan"

    @task
    def get_date():
        curr_date = json.dumps(datetime.now(), default=str)
        return curr_date

    @task
    def greet(name, date):
        print(f"Hello World! My name is {name} and it is currently {date} where i'm at")
    
    name = get_name()
    date = get_date()
    greet(name, date)

greet_dag = hello_world_etl()
