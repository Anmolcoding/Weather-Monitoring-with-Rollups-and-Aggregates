import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

def plot_temperature_trends(conn):
    """Plot temperature trends using stored weather data."""
    df = pd.read_sql_query("SELECT * FROM weather_data", conn)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.set_index('timestamp', inplace=True)
    
    # Plot temperature trends
    df['temp'].plot(title='Temperature Trends', figsize=(10, 5))
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.show()

if __name__ == "__main__":
    conn = sqlite3.connect('data/weather.db')
    plot_temperature_trends(conn)

