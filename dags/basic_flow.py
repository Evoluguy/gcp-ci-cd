from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args={
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay':timedelta(minutes=5)
}

dag = DAG('basic_dag',
        default_args=default_args,
        description='Simple Dag',
        schedule_interval=timedelta(days=1)
        )

task1 = BashOperator(task_id='print_date',
                    bash_command='date',
                    dag=dag)

task2 = BashOperator(task_id='print_msg',
                    bash_command='echo "Hello world from task2"' ,
                    dag=dag)

task1.set_downstream(task2)

