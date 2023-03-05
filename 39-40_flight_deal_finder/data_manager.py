from dotenv import load_dotenv
import os
import requests
import pandas


class DataManager:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('SHEETY_TOKEN')
        self.spreadsheet_id = os.getenv('SHEETY_SPREADSHEET_ID')
        self.endpoint = os.getenv('SHEETY_ENDPOINT')
        data = self.get_data()
        self.df = pandas.DataFrame(data['prices'])

    def get_data(self):
        payload = 'https://api.sheety.co/' + \
                  self.endpoint + \
                  '/flightDeals/prices'
        headers = {
            "Authorization": "Bearer " + self.token
        }
        # response = requests.get(payload, headers=headers).json()

        # this is test data to not fuck around with API
        response = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
                               {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
                               {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
                               {'city': 'Sydney', 'iataCode': '', 'lowestPrice': '', 'id': 5},
                               {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
                               {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': '', 'id': 7},
                               {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
                               {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
                               {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}
        return response

    def get_blanc_iatas(self):
        # return list

        blanc_iatas = []
        for index in range(len(self.df) - 1):
            iata_code = self.df.loc[index, 'iataCode']
            if iata_code == '':
                blanc_iatas.append(self.df.loc[index, 'city'])
        return blanc_iatas

    def get_blanc_prices(self):
        # return list

        blanc_prices = []
        for index in range(len(self.df) - 1):
            price = self.df.loc[index, 'lowestPrice']
            if price == '':
                blanc_prices.append(self.df.loc[index, 'city'])
        return blanc_prices
        # index = df[df['city'] == city].index[0]  # Get index of row where 'city' == city
        # lowest_price = df.loc[index].at['lowestPrice']  # Find lowestPrice in row with index == index
        # if lowest_price > 0:
        #     return lowest_price
        # else:
        #     return None
        # pass

    def update_prices(self, prices: dict):
        if len(prices) > 0:
            for curr_price in prices.items():
                city = curr_price[0]
                price = curr_price[1]
                index = self.df[self.df['city'] == city].index[0]
                self.df.loc[index, 'lowestPrice'] = price

    def update_iatas(self, iatas: dict):
        if len(iatas) > 0:
            for curr_price in iatas.items():
                city = curr_price[0]
                iata = curr_price[1]
                index = self.df[self.df['city'] == city].index[0]
                self.df.loc[index, 'iataCode'] = iata

    def upload_data(self):
        pass
