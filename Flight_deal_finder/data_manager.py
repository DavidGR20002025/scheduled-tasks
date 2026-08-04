import requests_cache
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_URL = os.environ.get("SHEETY_URL")
        self.SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
        self.headers = {
            "Authorization": f"Basic {self.SHEETY_AUTH}"
        }
        self.sheety_session=requests_cache.CachedSession('Sheety',expire_after=604800)

    def get_flights(self):
        response = self.sheety_session.get(url=self.SHEETY_URL, headers=self.headers)
        response.raise_for_status()
        flights= response.json()
        return flights["flights"]
