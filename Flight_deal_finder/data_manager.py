import requests_cache

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_URL = "https://api.sheety.co/251b076827ac869d85536234688ac5e5/flightPrices/flights"
        self.SHEETY_AUTH = "RGF2aWQ6RGV2b2x0IzY0MDc="
        self.headers = {
            "Authorization": f"Basic {self.SHEETY_AUTH}"
        }
        self.sheety_session=requests_cache.CachedSession('Sheety',expire_after=604800)

    def get_flights(self):
        response = self.sheety_session.get(url=self.SHEETY_URL, headers=self.headers)
        response.raise_for_status()
        flights= response.json()
        return flights["flights"]