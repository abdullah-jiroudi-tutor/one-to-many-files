from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator

def welcome_function():
    print("welcome world")
    


def get_date() ->str:
    return str(datetime.now())



def read_time(ti)->None:
    dt = ti.xcom_pull(task_ids='task0')
    print("the time coming from first task is :",dt)


default_arsg={
    'start_date':datetime(2023,1,10),
    'email_on_failure':['abdullah.jiroudi@develhope.co'],
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1),
    'project_id':1
}

createQuary=""" 
CREATE TABLE data5 (

    name VARCHAR(250) NOT NULL,
    age  INT          NOT NULL

);

"""

insertQueary=""" INSERT INTO data5(name,age) VALUES ('abdullah',27) """

with DAG("data5Dag",schedule_interval='@daily',catchup=False,default_args=default_arsg) as dag_pthon:
    #task0=PythonOperator(task_id="welcome",python_callable=welcome_function)
    #task1=PostgresOperator(task_id="insert_data",sql=insertQueary,postgres_conn_id="postgressdatabase")

    task0=PythonOperator(task_id="gettime",python_callable=get_date,do_xcom_push=True)
    task1=PythonOperator(task_id="printitme",python_callable=read_time)


    task0>>task1
