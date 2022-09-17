# https://pixe.la/@akaiumov

import os
import requests
from datetime import datetime as dt
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('PIXELA_API_KEY')
USERNAME = 'akaiumov'
PIXELA_ENDPOINT = 'https://pixe.la/'


def create_user(username):
    params = {
        "token": API_KEY,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    url = PIXELA_ENDPOINT + 'v1/users'
    response = requests.post(url=url, json=params)
    return response


def create_graph(graph_id, graph_name):
    if not graph_id:
        graph_id = graph_name
    headers = {"X-USER-TOKEN": API_KEY}
    url = PIXELA_ENDPOINT + f'v1/users/{USERNAME}/graphs'
    graph_configs = {
        "id": graph_id,
        "name": graph_name,
        "unit": "Attempts",
        "type": "int",
        "color": "sora",
        "selfSufficient": "increment"
    }
    response = requests.post(url=url, json=graph_configs, headers=headers)
    return response


def get_pixel(graph_id, date):
    """Get registered quantity as 'Pixel'."""
    # date = dt.now().strftime("%Y%m%d")    # this is for today's date
    url = PIXELA_ENDPOINT + f'v1/users/{USERNAME}/graphs/{graph_id}/{date}'
    headers = {"X-USER-TOKEN": API_KEY}
    response = requests.get(url=url, headers=headers)
    return response


def post_pixel(graph_id):
    """It records the quantity of the specified date as a "Pixel"."""
    date = dt.now().strftime("%Y%m%d")
    url = PIXELA_ENDPOINT + f'v1/users/{USERNAME}/graphs/{graph_id}'
    headers = {"X-USER-TOKEN": API_KEY}
    graph_configs = {"date": date, "quantity": "1"}
    response = requests.post(url=url, json=graph_configs, headers=headers)
    return response


def update_pixel(graph_id, date, quantity):
    """Update the quantity already registered as a "Pixel".
    If target "Pixel" not exist, create a new "Pixel" and set quantity."""
    # date = dt.now().strftime("%Y%m%d") # this is for today's date
    url = PIXELA_ENDPOINT + f'v1/users/{USERNAME}/graphs/{graph_id}/{date}'
    headers = {"X-USER-TOKEN": API_KEY}
    graph_configs = {"quantity": quantity}
    response = requests.put(url=url , json=graph_configs, headers=headers)
    return response


# print(create_user(USERNAME).json())
# print(create_graph('graph1', 'LearnEnglish').text)
# print(post_pixel(graph_id='graph1').text)
# date = dt.now()
# date += timedelta(days=1)
# print(get_pixel(graph_id='graph1', date=dt.now().strftime("%Y%m%d")).text)
print(update_pixel(graph_id='graph1', date=dt.now().strftime("%Y%m%d"), quantity=2).json)
