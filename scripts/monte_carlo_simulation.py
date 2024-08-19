import numpy as np
import pandas as pd
import yfinance as yf

def run_simulation():
    # Define los parámetros de la cartera
    symbols = ['AAPL', 'MSFT', 'GOOGL']  # Ejemplo de tickers
    weights = np.array([0.4, 0.3, 0.3])  # Pesos en la cartera
    simulation_runs = 10000  # Número de simulaciones

    # Extrae datos de Yahoo Finance
    data = yf.download(symbols, start="2020-01-01", end="2023-01-01")['Adj Close']

    # Calcula los rendimientos diarios
    returns = data.pct_change().dropna()

    # Realiza las simulaciones de Monte Carlo
    simulation_results = np.zeros(simulation_runs)
    for i in range(simulation_runs):
        simulated_returns = np.random.multivariate_normal(returns.mean(), returns.cov(), len(returns))
        portfolio_return = np.dot(simulated_returns, weights)
        simulation_results[i] = portfolio_return.sum()

    # Calcula el VaR y ES
    VaR = np.percentile(simulation_results, 5)
    ES = simulation_results[simulation_results <= VaR].mean()

    # Guardar los resultados en un CSV o DataFrame
    result_df = pd.DataFrame({'VaR': [VaR], 'ES': [ES]})
    result_df.to_csv('/opt/airflow/data/risk_metrics.csv', index=False)

    return result_df
