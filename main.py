#!/usr/bin/env python3

import sqlite3
from database import initialize_database, save_weather_data
from alerts import check_thresholds
import requests
from config import API_KEY

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()  # Convert response to JSON format

    # Extract the relevant data from the API response
    weather_data = {
        'city': data['name'],  # City name
        'main': data['weather'][0]['main'],  # Main weather condition
        'temp': data['main']['temp'] - 273.15,  # Convert from Kelvin to Celsius
        'feels_like': data['main']['feels_like'] - 273.15,  # Convert from Kelvin to Celsius
        'timestamp': data['dt']  # Timestamp
    }

    return weather_data

def fetch_and_store_weather(conn):
    """Fetch and store weather data for a specified city."""
    city = "Delhi"  # Example city
    weather_data = get_weather_data(city)

    if weather_data:
        save_weather_data(conn, weather_data)  # Save data to database

if __name__ == "__main__":
    conn = initialize_database()  # Initialize database and get connection
    if conn is None:
        print("Error connecting to database")
    else:
        try:
            fetch_and_store_weather(conn)
        finally:
            conn.close()  # Always close the connection


