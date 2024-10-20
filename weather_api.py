import requests


def get_weather_data(city, api_key):
    """Fetch weather data for a city from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # Celsius
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': city,
            'main': data['weather'][0]['main'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'timestamp': data['dt']
        }
        return weather
    else:
        print(f"Error fetching data for {city}")
        return None