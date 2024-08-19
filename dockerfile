FROM apache/airflow:2.7.0-python3.10

# Instalar dependencias adicionales
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copiar los DAGs y scripts al contenedor
COPY dags/ /opt/airflow/dags/
COPY scripts/ /opt/airflow/scripts/

# Asegurar permisos correctos
USER root
RUN chown -R airflow: /opt/airflow/dags /opt/airflow/scripts
USER airflow

# Configurar PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/scripts"
