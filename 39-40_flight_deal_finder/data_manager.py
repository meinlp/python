from dotenv import load_dotenv
import os
import requests
import pandas
from logger import log


class DataManager:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('SHEETY_TOKEN')
        self.spreadsheet_id = os.getenv('SHEETY_SPREADSHEET_ID')
        self.endpoint = os.getenv('SHEETY_ENDPOINT')
        data = self.get_data()
        self.df = pandas.DataFrame(data['prices'])
        required_columns = ['city', 'iataCode', 'lowestPrice', 'date']
        for col in required_columns:
            if col not in self.df.columns:
                self.df[col] = None
        self.df.fillna('', inplace=True) # заменяет все nan на пустые ячейки. Без этого получается хуета

    def get_data(self):
        endpoint = 'https://api.sheety.co/' + \
                  self.endpoint + \
                  '/flightDeals/prices'
        headers = {
            "Authorization": "Bearer " + self.token
        }
        response = requests.get(endpoint, headers=headers).json()
        return response

    def get_blanc_iatas(self):
        blanc_iatas = []
        for index in range(len(self.df)):
            iata_code = self.df.loc[index, 'iataCode']
            if iata_code == '':
                blanc_iatas.append(self.df.loc[index, 'city'])
        return blanc_iatas

    def get_blanc_prices(self):
        blanc_prices = []
        for index in range(len(self.df) - 1):
            price = self.df.loc[index, 'lowestPrice']
            if not price:
                blanc_prices.append(self.df.loc[index, 'city'])
        return blanc_prices

    def update_prices(self, prices: dict):
        if len(prices) > 0:
            for curr_price in prices.items():
                city = curr_price[0]
                price = curr_price[1]
                index = self.df[self.df['city'] == city].index[0]
                self.df.loc[index, 'lowestPrice'] = price

    def update_iatas(self, iatas: dict):
        if len(iatas) > 0:
            for curr in iatas.items():
                city = curr[0]
                iata = curr[1]
                index = self.df[self.df['city'] == city].index[0]
                self.df.loc[index, 'iataCode'] = iata

    def upload_data(self):
        log('debug', f'Dataframe is going to upload: {self.df}')
        for price_dict in self.df.to_dict(orient='records'):
            string_id = str(price_dict['id'])
            endpoint = 'https://api.sheety.co/' + \
                      self.endpoint + \
                      '/flightDeals/prices/' + \
                      string_id
            headers = {
                "Authorization": "Bearer " + self.token,
                'Content-Type': 'application/json'
            }
            payload = {'price': price_dict}
            response = requests.put(endpoint, json=payload, headers=headers).json()
            log('info', response)
        pass
