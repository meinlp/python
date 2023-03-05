from dotenv import load_dotenv
import os
import requests
import pandas
# classes
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

DEPARTURE_CITY = 'Larnaca'
DEPARTURE_ID = 'LCA'

notificator = NotificationManager()
data_manager = DataManager()
flight_search = FlightSearch()
data = data_manager.df

# debug
# print(data)

# notificator.send_message("sup")

# print(data_manager.get_current_lowest_price(city='Paris'))
# print(flight_search.get_iata_airlabs('Larnaca'))

print(data_manager.get_blanc_iatas())
print(data_manager.get_blanc_prices())
data_manager.update_iatas(iatas={'Paris': 'PAR'})
data_manager.update_prices(prices={'Sydney': 666})

print(data_manager.get_blanc_iatas())
print(data_manager.get_blanc_prices())
print(data)