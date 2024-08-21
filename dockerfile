FROM apache/airflow:2.7.0-python3.10

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY dags/ /opt/airflow/dags/
COPY scripts/ /opt/airflow/scripts/

USER root
RUN chown -R airflow: /opt/airflow/dags /opt/airflow/scripts
USER airflow

ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/scripts"
