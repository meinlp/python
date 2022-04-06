import requests, json
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')


endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
params = {
    'appid': api_key,
    'units': 'metric',
    'lat': 68.5844,
    'lon': 07.5442,
    'exclude': 'current,minutely,daily,alerts'
    # 'q': 'Санкт-Петербург'
}
print(account_sid, auth_token, api_key)
client = Client(account_sid, auth_token)
response = requests.get(url=endpoint, params=params)
response.raise_for_status()

data = response.json()

rain_expected = False
for hour_data in data['hourly'][:12]:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        rain_expected = True

if rain_expected:
    print('Bring an umbrella')
    message = client.messages.create(
        body="It's going to rain today. Don't forget to bring an umbrella!",
        from_="+19384444863",
        to='+79956003175'
    )
    print(message.status)

# print(json.dumps(data, indent=4))
