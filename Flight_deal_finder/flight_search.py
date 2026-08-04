import requests_cache

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.SERP_API="7ec13980d365ec35ef5028911fd9334364d58825311dda4ffe6e63eab93479a8"
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
