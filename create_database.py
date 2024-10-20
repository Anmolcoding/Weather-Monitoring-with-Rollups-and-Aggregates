import sqlite3

def initialize_database():
    # Connect to the SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect('weather_data.db')
    
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create the weather table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        main_condition TEXT NOT NULL,
        temperature REAL NOT NULL,
        feels_like REAL NOT NULL,
        timestamp INTEGER NOT NULL
    )
    ''')

    # Commit changes and close the connection
    conn.commit()
    return conn  # Return the connection for further use

def save_weather_data(conn, weather_data):
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO weather (city, main_condition, temperature, feels_like, timestamp)
    VALUES (?, ?, ?, ?, ?)
    ''', (weather_data['city'], weather_data['main'], weather_data['temp'], 
          weather_data['feels_like'], weather_data['timestamp']))

    conn.commit()
