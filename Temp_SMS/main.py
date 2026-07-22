import requests
from twilio.rest import Client

api_key="NJ4MRKjpKcAdUM5WqCjNaMAP9lnJ4Lues6TKfv0m"
client_id="jvGY1TZ45MHGdPw9nINrm"


response=requests.get(f"https://data.api.xweather.com/conditions/new%20york%2C%20ny?client_id={client_id}&client_secret={api_key}")
response.raise_for_status()
data=response.json()
temperature=data["response"][0]["periods"][0]["tempC"]

account_sid = "AC074c585fd709977559b9008854bb7754"
auth_token = "5718b78ad6cb72d7aeeceba8e09da9dd"
client = Client(account_sid, auth_token)

if temperature>18:
    message = client.messages.create(
         body=f"Hello, the weather today is {temperature}",
         from_="+15734961525",
         to="+526143671100",
     )
else:
    print("All good with temp")

