import numpy as np
import pandas as pd
import yfinance as yf
import os

def run_simulation(**kwargs):
    symbols = ['AAPL', 'MSFT', 'GOOGL']
    weights = [0.4, 0.3, 0.3]
    simulation_runs = 10000

    data = yf.download(symbols, start="2020-01-01", end="2023-01-01")['Adj Close']

    returns = data.pct_change().dropna()

    simulation_results = []
    for i in range(simulation_runs):
        simulated_returns = returns.sample(frac=1, replace=True).dot(weights)
        simulation_results.append(simulated_returns.sum())

    VaR = pd.Series(simulation_results).quantile(0.05)
    ES = pd.Series(simulation_results)[pd.Series(simulation_results) <= VaR].mean()

    result_df = pd.DataFrame({'VaR': [VaR], 'ES': [ES]})

    output_dir = '/opt/airflow/data'
    os.makedirs(output_dir, exist_ok=True)

    result_df.to_csv(f'{output_dir}/risk_metrics.csv', index=False)

    return 'Simulation completed successfully'
