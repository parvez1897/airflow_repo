from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime
import os
import sys

args = {
  'owner': 'airflow'
  , 'depends_on_past': False
  , 'retries': 1
  , 'retry_delay': timedelta(minutes=1)
  , 'start_date': datetime(2020, 2, 10)
  , 'provide_context': True
}
d = datetime(2020, 2, 10, 3, 15,00)


dag = DAG('usgs', start_date = d, schedule_interval = '16 * * * *', default_args = args)

t_main = BashOperator(
  task_id = 'usgs_fetch'
  , dag = dag
  , bash_command = 'java -cp /mnt/c/Users/img/Documents/GitHub/backbone/target/kafkaUSGS-1.0-SNAPSHOT.jar KafkaUSGS'
  #params = {'class': 'FetchJSON', 'path': 'jars/kafkaUSGS.jar'}
  )
