from dotenv import load_dotenv
from datetime import datetime, date, timedelta
import os
import requests
from logger import log


class FlightSearch:
    def __init__(self, max_stopovers, time_delta, city_from):
        self.max_stopovers = max_stopovers
        self.city_from = city_from
        load_dotenv()
        self.airlabs_apikey = os.getenv('AIRLABS_APIKEY')
        self.airlabs_endpoint = os.getenv('AIRLABS_ENDPOINT')
        self.tequila_apikey = os.getenv('TEQUILA_APIKEY')
        self.tequila_endpoint = os.getenv('TEQUILA_ENDPOINT')
        self.date_from = datetime.today().strftime('%d/%m/%Y')
        self.date_to = (date.today() + timedelta(days=time_delta)).strftime('%d/%m/%Y')

    def get_iata_airlabs(self, city_name: str):
        url = self.airlabs_endpoint + 'suggest/'

        params = {
            'search': city_name,
            'api_key': self.airlabs_apikey
        }

        response = requests.get(url=url, params=params).json()
        try:
            return response['response']['cities'][0]['city_code']
        except Exception as e:
            log('error', f'An error happened during the checking the iata: {e}')
            log('debug', f"And here's the full response:\n {response}")
            return None

    def get_flight_info(self, city_to):
        url = self.tequila_endpoint + 'search'

        params = {
            'fly_from': self.city_from,
            'fly_to': city_to,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'adults': 1,
            'max_stopovers': self.max_stopovers,
            'limit': 1
        }
        headers = {
            'apikey': self.tequila_apikey
        }

        response = requests.get(url=url, headers=headers, params=params).json()
        try:
            return response
        except Exception as e:
            log('error', f'An error happened while fetching the flights data: {e}')
            log('error', f"And here's the full response:\n {response}")
            return None
