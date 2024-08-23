FROM apache/airflow:2.7.3-python3.10

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/scripts"
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

COPY . .
