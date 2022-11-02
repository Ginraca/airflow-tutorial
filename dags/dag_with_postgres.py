from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
import dag_global_settings

dag_global_settings.init()

with DAG(
    dag_id="postgres_dag",
    default_args=dag_global_settings.default_args,
    description="DAG using Postgres Example",
    start_date=datetime(2022, 10, 31, 2),
    schedule_interval='@daily'
) as dag:
    task_one = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres_localhost",
        sql="""
            create table if not exists dag_coba(
                dt date,
                dag_id varchar,
                primary key (dt, dag_id)
            )
        """
    )

    task_two = PostgresOperator(
        task_id="insert_into_table",
        postgres_conn_id="postgres_localhost",
        sql="""
            insert into dag_runs(dt, dag_id)
            values ('{{ ds }}', '{{ dag.dag_id }}')
        """
    )

    task_one >> task_two
