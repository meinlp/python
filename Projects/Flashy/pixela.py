import os
import requests
from datetime import datetime as dt
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('PIXELA_API_KEY')
USERNAME = 'akaiumov'
PIXELA_ENDPOINT = 'https://pixe.la/'
GRAPH_ID = 'graph1'
TODAY = dt.now().strftime('%Y%m%d')
YESTERDAY = (dt.now() - timedelta(days=1)).strftime('%Y%m%d')


def get_pixel(graph_id, date):
    """Get registered quantity as 'Pixel'."""
    # date = dt.now().strftime("%Y%m%d")    # this is for today's date
    url = PIXELA_ENDPOINT + f'v1/users/{USERNAME}/graphs/{graph_id}/{date}'
    headers = {"X-USER-TOKEN": API_KEY}
    response = requests.get(url=url, headers=headers)
    return response


def update_pixel(graph_id, date, quantity):
    """Update the quantity already registered as a "Pixel".
    If target "Pixel" not exist, create a new "Pixel" and set quantity."""
    # date = dt.now().strftime("%Y%m%d") # this is for today's date
    url = PIXELA_ENDPOINT + f'v1/users/{USERNAME}/graphs/{graph_id}/{date}'
    headers = {"X-USER-TOKEN": API_KEY}
    graph_configs = {"quantity": quantity}
    response = requests.put(url=url, json=graph_configs, headers=headers)
    return response


def increment_todays_pixel():
    try:
        pixel_info = get_pixel(graph_id=GRAPH_ID, date=TODAY).json()
        current_quantity = int(pixel_info['quantity'])
        print(update_pixel(GRAPH_ID, TODAY, quantity=str(current_quantity + 1)).text)
    except KeyError:
        print(update_pixel(GRAPH_ID, TODAY, quantity='1').text)