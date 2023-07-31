from datetime import datetime, timedelta 
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
def start():
    return str(datetime.now())

def end(ti):
    d=ti.xcom_pull(task_ids="firstTask")
    print("this value comes form first task",d)

def begin():
    print("start")

def done():
    print("done")    
default_arg={
    "start_date":datetime(2023,7,26),
    "email_on_failure": False,
    "retries":3,
    "retry_delay":timedelta(minutes=10),
    "email_on_retry":False,
    "project_id":1
}

create_table_qury=""" CREATE TABLE data (
    name VARCHAR(25)  NOT NULL,
    age  INT          NOT NULL); 
"""
inser_query=""" 
INSERT INTO public.data (name,age) VALUES ('boo',28);
"""


with DAG("first_data6_dag",schedule_interval="@once",default_args=default_arg)  as x:
    #task0=PythonOperator(task_id="firstTask",python_callable=start,do_xcom_push=True)
    #task1=PythonOperator(task_id="secondTask",python_callable=end)
    # airflow host value to connect to postgres through docker is : host.docker.internal
    task0=PythonOperator(task_id="begin",python_callable=begin)
    task2=PostgresOperator(task_id="createtable", sql=inser_query,postgres_conn_id="data6Connection")
    task1=PythonOperator(task_id="done",python_callable=done)

    task0>>[task2>>task1]