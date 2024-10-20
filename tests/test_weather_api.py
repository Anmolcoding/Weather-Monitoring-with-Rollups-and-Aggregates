from weather_api import get_weather_data

def test_get_weather_data():
    """Test the weather data retrieval."""
    city = 'Delhi'
    api_key = 'your_test_api_key'
    weather_data = get_weather_data(city, api_key)
    
    assert weather_data is not None, "Failed to fetch weather data"
    assert 'temp' in weather_data, "Temperature data missing"
