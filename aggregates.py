import pandas as pd
import sqlite3
from datetime import datetime

def calculate_daily_aggregates(conn):
    """Calculate daily aggregates like average temperature, min, max, and dominant weather condition."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather_data")
    rows = cursor.fetchall()
    
    # Convert to DataFrame
    df = pd.DataFrame(rows, columns=['city', 'main', 'temp', 'feels_like', 'timestamp'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['date'] = df['timestamp'].dt.date
    
    # Group by date for daily rollups
    daily_summary = df.groupby('date').agg({
        'temp': ['mean', 'min', 'max'],
        'main': lambda x: x.mode()[0]  # Most frequent weather condition
    })
    
    print(daily_summary)
    return daily_summary

if __name__ == "__main__":
    conn = sqlite3.connect('data/weather.db')
    calculate_daily_aggregates(conn)

