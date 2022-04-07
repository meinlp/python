import requests
import os
from dotenv import load_dotenv
import json
from datetime import *

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
MY_USER_ID = os.getenv('MY_USER_ID')
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
delta_message: str
yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
day_before_yesterday = (date.today() - timedelta(days=2)).strftime("%Y-%m-%d")


def send_message_with_tg_bot(bot_message: str):
    send_text = 'https://api.telegram.org/bot' + \
                BOT_TOKEN + '/sendMessage?chat_id=' + \
                MY_USER_ID + '&parse_mode=Markdown&text=' + \
                bot_message
    response = requests.get(send_text)
    return response.json()


def get_stock_data():
    endpoint = 'https://www.alphavantage.co/query'
    params = {
        'apikey': ALPHA_VANTAGE_API_KEY,
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK
    }
    response = requests.get(url=endpoint, params=params)
    response.raise_for_status()
    data = response.json()
    with open(f'{datetime.today().strftime("%Y-%m-%d")}.json', 'w') as file:
        json.dump(data, file, indent=4)
    return data


def compare_closings(first_date, second_date):
    data = get_stock_data()
    yesterday_closing_price = float(data['Time Series (Daily)'][first_date]['4. close'])

    day_before_yesterday_closing_price = float(data['Time Series (Daily)'][second_date]['4. close'])
    delta_in_percents = (day_before_yesterday_closing_price - yesterday_closing_price) * 100 / day_before_yesterday_closing_price
    return delta_in_percents


def get_news(q):
    endpoint = 'https://newsapi.org/v2/everything'
    params = {
        'apiKey': NEWSAPI_KEY,
        'q': q,
        'sortBy': 'popularity',
        'from': day_before_yesterday,
        'to': yesterday
    }
    response = requests.get(url=endpoint, params=params)
    response.raise_for_status()

    news_data = response.json()
    with open(f'{q}_{datetime.today().strftime("%Y-%m-%d")}.json', 'w') as file:
        json.dump(news_data, file, indent=4)
    return news_data


delta = compare_closings(yesterday, day_before_yesterday)
news = get_news(COMPANY_NAME)

if delta > 0:
    delta_message = f'TSLA: 💹{round(delta, 2)}%'
else:
    delta_message = f'TSLA: 🔻{round(delta, 2)}%'

send_message_with_tg_bot(delta_message)
for i in range(0, 3):
    send_message_with_tg_bot(f'{news["articles"][i]["title"]}:\n'
                             f'{news["articles"][i]["url"]}')
