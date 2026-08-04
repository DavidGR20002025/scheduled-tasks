from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.ACCOUNT_SID = "AC074c585fd709977559b9008854bb7754"
        self.AUTH_TOKEN = "5718b78ad6cb72d7aeeceba8e09da9dd"
        self.client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

    def send_message(self,price_google,arrival,number_to,number_from,day,new_day):
        self.client.messages.create(
            body=f"Low price alert! Only {price_google} from CUU to {arrival} on {day} to {new_day}",
            from_=number_from,
            to=number_to,
        )
