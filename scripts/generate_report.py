import pandas as pd
import matplotlib.pyplot as plt

def generate_report():
    # Carga los resultados de la simulación
    df = pd.read_csv('/opt/airflow/data/risk_metrics.csv')

    # Genera un gráfico de barras simple para VaR y ES
    df.plot(kind='bar')
    plt.title('Value at Risk (VaR) and Expected Shortfall (ES)')
    plt.ylabel('Risk Metrics')
    plt.savefig('/opt/airflow/data/risk_report.png')

    # Opcional: Generar un PDF o HTML report con más detalles
    # Implementa la lógica aquí si lo deseas

    return 'Report generated successfully'
