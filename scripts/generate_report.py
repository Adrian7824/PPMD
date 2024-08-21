import pandas as pd
import matplotlib.pyplot as plt

def generate_report():
    df = pd.read_csv('/opt/airflow/data/risk_metrics.csv')

    df.plot(kind='bar')
    plt.title('Value at Risk (VaR) and Expected Shortfall (ES)')
    plt.ylabel('Risk Metrics')
    plt.savefig('/opt/airflow/data/risk_report.png')

    return 'Report generated successfully'
