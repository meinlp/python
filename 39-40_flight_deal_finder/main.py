from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime
from logger import log

DEPARTURE_CITY = 'Larnaca'
DEPARTURE_ID = 'LCA'
MAX_STOPOVERS = 0
TIMEDELTA = 6 * 30

if __name__ == '__main__':

    log('info', f'App is starting to work - {datetime.today().strftime("%Y/%m/%d %H:%M")}')
    notificator = NotificationManager()
    data_manager = DataManager()
    flight_search = FlightSearch(max_stopovers=MAX_STOPOVERS, time_delta=TIMEDELTA, city_from=DEPARTURE_ID)
    data = data_manager.df
    upload_flag = 0  # this one is for deciding if we want to change the data in google sheets
    blanc_iatas = data_manager.get_blanc_iatas()

    # if we've found blanc iatas, we're creating blanc dict and iterating through list of cities with blanc iatas
    if len(blanc_iatas) > 0:
        iatas_to_update = {}
        for city in blanc_iatas:
            try:
                iata = flight_search.get_iata_airlabs(city)
                log('info', f"{city}'s iata is going to be updated to {iata}")
                iatas_to_update[city] = iata
            except Exception as e:
                log('error', f"We got an exception, boss: {e}")
                pass
        log('debug', f'iatas to update: {iatas_to_update}')
        data_manager.update_iatas(iatas_to_update)  # dict with updated iatas
        upload_flag = 1

    for index in range(len(data)):
        flight = flight_search.get_flight_info(city_to=data.loc[index, 'iataCode'])
        log('debug', f'flight info: {flight}')
        if flight['_results'] > 0:
            flight_date = datetime.strptime(flight['data'][0]['local_departure'], '%Y-%m-%dT%H:%M:%S.%fZ')
            if data.loc[index, 'lowestPrice'] == '':
                price = flight['data'][0]['price']
                date = flight_date.strftime('%Y/%m/%d %H:%M')
                data.at[index, 'lowestPrice'] = price
                data.at[index, 'date'] = date
                upload_flag = 1
                notificator.send_message(f"✈️️✈️️✈️️\n"
                                         f"Sup! There a cheap flight from {DEPARTURE_CITY} to {data.at[index, 'city']}!\n"
                                         f"The price is {price}€\nThe departure date is {date}\n"
                                         f"check https://kiwi.com for more info")
            elif flight['data'][0]['price'] < data.loc[index, 'lowestPrice'] or flight_date < datetime.today():
                price = flight['data'][0]['price']
                date = flight_date.strftime('%Y/%m/%d %H:%M')
                data.at[index, 'lowestPrice'] = price
                data.at[index, 'date'] = date
                upload_flag = 1
                notificator.send_message(f"✈️️✈️️✈️️\n"
                                         f"Sup! There a cheap flight from {DEPARTURE_CITY} to {data.at[index, 'city']}!\n"
                                         f"The price is {price}€\nThe departure date is {date}\n"
                                         f"check https://kiwi.com for more info")

    if upload_flag:
        data_manager.upload_data()
