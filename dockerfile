FROM apache/airflow:2.7.3-python3.10

USER root

run apt-get update

USER airflow

ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/scripts"
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

COPY . .
