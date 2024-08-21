from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.monte_carlo_simulation import run_simulation
from scripts.generate_report import generate_report 

import yfinance as yf

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'risk_analysis',
    default_args=default_args,
    description='DAG for calculating VaR and ES using Monte Carlo simulations',
    schedule_interval='@monthly',
    catchup=False,
)

def fetch_data(**kwargs):
    symbols = ['AAPL', 'MSFT', 'GOOGL']
    data = yf.download(symbols, start="2020-01-01", end="2023-01-01")['Adj Close']
    data.index = data.index.astype(str)
    kwargs['ti'].xcom_push(key='portfolio_data', value=data.to_dict())
    
    return 'Data fetched successfully'

fetch_data_task = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    dag=dag,
)

run_simulation_task = PythonOperator(
    task_id='run_simulation',
    python_callable=run_simulation,
    dag=dag,
)

generate_report_task = PythonOperator(
    task_id='generate_report',
    python_callable=generate_report,  
    dag=dag,
)

fetch_data_task >> run_simulation_task >> generate_report_task
