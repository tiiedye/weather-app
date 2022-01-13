from dotenv import load_dotenv
from twilio.rest import Client
import os
import requests

load_dotenv()

# You will need your own .env file with YOUR authentication data
api_key = os.getenv('OWM_API_KEY')
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_num = os.getenv("TWILIO_NUM")
my_num = os.getenv("MY_NUM")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": "34.2346",
    "lon": "-118.5369",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()["hourly"][:12]

rain_today = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        rain_today = True

client = Client(account_sid, auth_token)

if rain_today:
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=twilio_num,
        to=my_num
    )
else:
    message = client.messages \
        .create(
        body="All clear today 🔆",
        from_=twilio_num,
        to=my_num
    )

print(message.status)
