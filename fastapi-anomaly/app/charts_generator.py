import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_plot_anomalies(dates, close_prices, anomaly_flags, symbol, output_dir=OUTPUT_DIR):
    plt.figure(figsize=(14, 6))
    dates = pd.to_datetime(dates)
    close_prices = np.array(close_prices)
    anomaly_flags = np.array(anomaly_flags)

    plt.plot(dates, close_prices, label='Close Price', color='blue', linewidth=1)
    if np.any(anomaly_flags):
        plt.scatter(dates[anomaly_flags], close_prices[anomaly_flags],
                    color='red', label='Anomalies détectées', s=30, zorder=5)

    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f"Détection d'anomalies - {symbol}")
    plt.legend()
    plt.grid(True, alpha=0.3)

    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

    plt.tight_layout()
    filename = os.path.join(output_dir, f"anomalies_{symbol}.png")
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    return filename
