class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,data):
        self.price_google=data["best_flights"][0]["price"]
