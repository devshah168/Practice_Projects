import requests
from twilio.rest import Client

URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY="YOUR_API_KEY"
account_sid = "YOUR TWILIO ACCOUNT ID"
auth_token = "YOUR TWILIO AUTH TOKEN"
parameters={
    "lat":"20.593683",
    "lon":"78.962883",
    "appid":API_KEY,
    "cnt":4,
}
response=requests.get(url=URL,params=parameters)
response.raise_for_status()
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='YOUR TWILIO NUMBER',
    body='Its going to rain today.Remember to bring an umbrella.',
    to='YOUR OWN PERSONAL NUMBER'
    )
    print(message.status)
