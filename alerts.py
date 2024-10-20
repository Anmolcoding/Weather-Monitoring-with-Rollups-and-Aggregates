from config import TEMP_THRESHOLD

def check_thresholds(weather_data):
    """Check if the weather exceeds the user-defined threshold."""
    if weather_data['temp'] > TEMP_THRESHOLD:
        print(f"Alert! {weather_data['city']} temperature exceeded {TEMP_THRESHOLD}°C!")

