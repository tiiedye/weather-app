from dotenv import load_dotenv
import os
import requests

load_dotenv()

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

data = response.json()['hourly']
print(data)
