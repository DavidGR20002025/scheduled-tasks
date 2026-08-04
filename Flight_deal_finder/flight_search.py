import requests_cache
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.SERP_API=os.environ.get("SERP_API")
        self.session = requests_cache.CachedSession('flight_cache', expire_after=5184000)

    def get_flights(self,IATA,day,new_day):
        serp_parameters = {
            "engine": "google_flights",
            "departure_id": "CUU",
            "arrival_id": IATA,
            "outbound_date": day,
            "return_date": new_day,
            "currency": "USD",
            "api_key": self.SERP_API
        }
        response_serp = self.session.get(url="https://serpapi.com/search.json", params=serp_parameters)
        response_serp.raise_for_status()
        flight_data = response_serp.json()
        return flight_data
