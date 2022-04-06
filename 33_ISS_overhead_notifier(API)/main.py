# from tkinter import *
import requests, json
from datetime import *
import time

MY_LAT = '59.934280'
MY_LNG = '30.335098'


def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']['sunrise'].replace('T', ':').split(':')[1]) + 3
    sunset = int(data['results']['sunset'].replace('T', ':').split(':')[1]) + 3
    time_now = datetime.now().hour - 5
    if sunset >= time_now >= sunrise:
        return True


def is_oss_near():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])

    if abs(abs(iss_lat) - abs(float(MY_LAT))) < 5 and (abs(abs(iss_lng) - abs(float(MY_LNG)))) < 5:
        return True


while True:
    if is_oss_near() and is_night():
        print('yay')
    else:
        print('nay')
    time.sleep(60)
