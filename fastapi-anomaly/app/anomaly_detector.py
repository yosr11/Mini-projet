import yfinance as yf
import pandas as pd
import numpy as np
from app.model_loader import load_iforest_model

def download_symbol(symbol, start="2018-01-01", end="2025-12-01"):
    df = yf.download(symbol, start=start, end=end, progress=False)
    if df.empty or 'Close' not in df.columns:
        return None
    df = df.reset_index()[['Date', 'Close']]
    df.columns = ['date', 'close']
    df['date'] = pd.to_datetime(df['date'])
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    df.dropna(inplace=True)
    return df

def detect_anomalies(symbol, from_date="2018-01-01", to_date="2025-12-01"):
    df = download_symbol(symbol, from_date, to_date)
    if df is None or len(df) < 30:
        raise Exception(f"Pas assez de données pour {symbol}")

    model, scaler = load_iforest_model(symbol)
    X_scaled = scaler.transform(df[['close']])
    df['anomaly'] = model.predict(X_scaled)
    df['anomaly_flag'] = df['anomaly'] == -1

    return {
        "symbol": symbol,
        "dates": df['date'].astype(str).tolist(),
        "close_prices": df['close'].tolist(),
        "anomaly_flags": df['anomaly_flag'].tolist(),
        "anomalies_detected": int(df['anomaly_flag'].sum())
    }
