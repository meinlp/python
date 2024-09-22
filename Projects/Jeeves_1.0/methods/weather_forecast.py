import requests

def get_weather_openweather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': location,
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None