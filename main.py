from dotenv import load_dotenv
import os
import requests

load_dotenv()

# You will need your own .env file with YOUR environmental data
api_key = os.getenv('OWM_API_KEY')
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

if rain_today:
    print("Bring an umbrella.")
