# Weather Monitoring with Rollups and Aggregates

This project provides a system to monitor real-time weather data using the OpenWeatherMap API. The system fetches weather data for a given city, stores it in a database, and performs rollup and aggregate calculations such as average temperature, maximum humidity, and so on.

## Features

- Fetch real-time weather data using the [OpenWeatherMap API](https://openweathermap.org/api)
- Store weather data in a SQLite database
- Perform rollups and aggregates on the weather data
- Send alerts when thresholds are exceeded

## Prerequisites

To run this project, you need to have the following installed:

- Python 3.7+
- [OpenWeatherMap API Key](https://openweathermap.org/appid)
- Docker (optional for containerization)

## Project Structure

```bash
├── alerts.py              # Alert system for threshold checking
├── config.py              # Configuration file with API key and thresholds
├── database.py            # SQLite database setup and data storage
├── main.py                # Main script to fetch and store weather data
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker setup
├── weather_data.db        # SQLite database file (created automatically)
└── README.md              # Project documentation

Installation
Step 1: Clone the Repository
git clone https://github.com/Anmolcoding/Weather-Monitoring-with-Rollups-and-Aggregates.git
cd Weather-Monitoring-with-Rollups-and-Aggregates
Step 2: Set up a Virtual Environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Set Up the OpenWeatherMap API Key
Edit the config.py file and replace <YOUR_API_KEY> with your actual OpenWeatherMap API key.
# config.py
API_KEY = "<YOUR_API_KEY>"
Step 5: Run the Application
python main.py
Docker Setup (Optional)
You can also run the project inside a Docker container.

Step 1: Build the Docker Image
docker build -t weather-monitor .
Step 2: Run the Docker Container
docker run -d weather-monitor
Usage
The application fetches weather data, stores it in a local SQLite database, and performs rollups and aggregates.

Database Schema
The weather table contains the following fields:

city (TEXT)
temperature (REAL)
humidity (REAL)
pressure (REAL)
timestamp (TEXT)
Alerts
You can configure temperature thresholds in the config.py file:
TEMP_THRESHOLD = 35  # Trigger alert if temperature exceeds 35°C
Troubleshooting
Common Issues
Module Not Found: If you get a ModuleNotFoundError for any package, ensure that you've installed all the dependencies from requirements.txt.

API Key Issues: Ensure that you've correctly set up your API key in config.py.

Database Errors: If you encounter any SQLite database issues, try deleting weather_data.db and rerun the application to recreate the database.

Database Not Found
If you're facing errors like sqlite3.DatabaseError: file is not a database, make sure the weather_data.db is being created correctly, or try rebuilding the database using the provided scripts.
