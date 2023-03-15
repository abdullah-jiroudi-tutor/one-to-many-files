from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def get_date() ->str:
    return str(datetime.now())

def read_time(ti)->None:
    dt = ti.xcom_pull(task_ids=['task1'])
    print("the time coming from first task is :",dt)


default_arg={
    'start_date':datetime(2023,1,10),
    'email_on_failure':['abdullah.jiroudi@develhope.co'],
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1),
    'project_id':1
}

with DAG("Friday_meeting_D3",schedule_interval='@daily',catchup=False,default_args=default_arg) as dython_dag:
    task1=PythonOperator(task_id="task1",python_callable=get_date,do_xcom_push=True)
    task2 = PythonOperator(task_id="task2", python_callable=read_time)
    task3 = PythonOperator(task_id="task3", python_callable=read_time)
    task4 = PythonOperator(task_id="task4", python_callable=read_time)
    task5 = PythonOperator(task_id="task5", python_callable=read_time)
    task1 >> [task2 >>[task5] >> task3] >> task4