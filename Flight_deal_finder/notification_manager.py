from twilio.rest import Client
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
        self.AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
        self.client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

    def send_message(self,price_google,arrival,number_to,number_from,day,new_day):
        self.client.messages.create(
            body=f"Low price alert! Only {price_google} from CUU to {arrival} on {day} to {new_day}",
            from_=number_from,
            to=number_to,
        )
