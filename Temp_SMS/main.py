import requests
from twilio.rest import Client
import os

api_key=os.environ.get("API_KEY")
client_id=os.environ.get("CLIENT_ID")


response=requests.get(f"https://data.api.xweather.com/conditions/new%20york%2C%20ny?client_id={client_id}&client_secret={api_key}")
response.raise_for_status()
data=response.json()
temperature=data["response"][0]["periods"][0]["tempC"]

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

if temperature>18:
    message = client.messages.create(
         body=f"Hello, the weather today is {temperature}",
         from_=os.environ.get("TWILIO_PHONE_NUMBER"),
         to=os.environ.get("PHONE_NUMBER"),
     )
else:
    print("All good with temp")

