from dotenv import load_dotenv
import os
import requests


class FlightSearch:
    def __init__(self):
        load_dotenv()
        self.searching_for_correct_city = None
        self.token = os.getenv('AIRLABS_KEY')
        self.endpoint = os.getenv('AIRLABS_ENDPOINT')

    def get_iata_airlabs(self, city_name: str):
        url = self.endpoint + 'suggest/'

        params = {
            'search': city_name,
            'api_key': self.token
        }

        response = requests.get(url=url, params=params).json()
        index = 0
        self.searching_for_correct_city = True
        while self.searching_for_correct_city:
            if response['response']['cities'][index]['name'] == city_name:
                self.searching_for_correct_city = False
                return response['response']['cities'][index]['city_code']
            elif index >= 10:
                self.searching_for_correct_city = False
            else:
                index += 1
        return None

    def get_flight_info(self, city_from, city_to, date_from, date_to):
        # date dd/mm/yyyy
        # flight_type oneway
        # one_for_city 1
        # one_per_date 1
        # optional price_from, price_to
        # max_stopovers 0
        # curr EUR
        # json in, json out
        pass

    # def get_lowest_price(self, city_to):
    #     pass






