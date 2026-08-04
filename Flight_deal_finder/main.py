#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
from flight_data import FlightData
from notification_manager import NotificationManager

number_from="+15734961525"
number_to="+526143671100"

today = datetime.now()

notification_manager=NotificationManager()

data_manager=DataManager()

data_manager_sheety=data_manager.get_flights()
flight_info = FlightSearch()

for data in data_manager_sheety:
    IATA=data["iataCode"]
    price=data["lowestPrice"]
    contador=0

    while contador<6:
        contador+=2
        outbound = today + relativedelta(months=contador)
        day = outbound.strftime("%Y-%m-%d")
        return_date = outbound + timedelta(days=6)
        new_day = return_date.strftime("%Y-%m-%d")
        flight_search=flight_info.get_flights(IATA,day,new_day)

        if "error" in flight_search:
            continue
        flight_data = FlightData(flight_search)
        price_flight = flight_data.price_google
        if price_flight < price:
            arrival = IATA
            notification_manager.send_message(price_flight, arrival, number_to, number_from, day, new_day)




