Weather Monitoring with Rollups and Aggregates
This project is a real-time weather monitoring system that collects data from the OpenWeatherMap API. It fetches weather information for major Indian metros (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad), processes the data, and stores it in an SQLite database. The system also calculates daily rollups and aggregates like the average temperature, dominant weather condition, and can trigger alerts based on user-defined thresholds.

Features
Fetches weather data in real-time at configurable intervals.
Processes weather data for daily rollups (e.g., average temperature, max/min temperature).
Supports user-defined alert thresholds (e.g., temperature crossing 35°C).
Stores weather data in a SQLite database.
Extensible for additional weather parameters like humidity, wind speed, etc.
Prerequisites
To run this project, ensure you have the following installed:

Python 3.6+
Virtual Environment for Python (recommended).
OpenWeatherMap API Key (Sign up at https://openweathermap.org/ to get your API key).
Docker (Optional, if you want to run the project using Docker).
Project Setup
1. Clone the Repository
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/weather-monitor.git
cd weather-monitor
2. Create and Activate a Virtual Environment (Optional but recommended)
Linux/MacOS:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Windows:

bash
Copy code
python -m venv venv
.\venv\Scripts\activate
3. Install Dependencies
Install all required Python packages using pip:

bash
Copy code
pip install -r requirements.txt
4. Set up API Key
Create a config.py file inside the project directory (if not already present). Add your OpenWeatherMap API key in the following format:

python
Copy code
# config.py
API_KEY = 'your_openweathermap_api_key'
TEMP_THRESHOLD = 35  # Set your temperature alert threshold here (in Celsius)
Replace 'your_openweathermap_api_key' with your actual API key from OpenWeatherMap.

5. Initialize Database
To create the database file (weather_data.db), run:

bash
Copy code
python create_database.py
This will generate the required SQLite database and tables.

6. Running the Application
To start fetching weather data and storing it in the database, simply run:

bash
Copy code
python main.py
The system will continuously fetch weather data at intervals defined in the script, process it, and store it in the SQLite database.

Docker Setup (Optional)
If you want to run the project inside a Docker container, follow these steps:

1. Build the Docker Image
bash
Copy code
docker build -t weather-monitor .
2. Run the Docker Container
bash
Copy code
docker run -d weather-monitor
This will run the weather monitoring service in a containerized environment.

Test Cases
To ensure the system works as expected, a few test cases are available:

System Setup: Ensure the system starts correctly and connects to the OpenWeatherMap API.
Data Retrieval: Validate that weather data is fetched at the correct intervals.
Temperature Conversion: Check if temperature is converted from Kelvin to Celsius properly.
Daily Summary: Verify that daily weather summaries are calculated and stored accurately.
Alerting Thresholds: Ensure alerts are triggered when the temperature exceeds the configured threshold.
Troubleshooting
ModuleNotFoundError for requests: Ensure that the virtual environment is activated and requests is installed using pip install requests.
API Key Issues: Double-check that you have set the correct API key in config.py.
SQLite Database Issues: Make sure the database is initialized properly by running python create_database.py.
Future Improvements
Add support for more cities or regions.
Implement more weather parameters like humidity, wind speed.
Add a web dashboard for visualizing weather trends.
Extend alerting system to send email notifications.
