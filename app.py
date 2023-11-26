import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()
CITY = 'London'

url= BASE_URL + "APPID=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

print(response)
