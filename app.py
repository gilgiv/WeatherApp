import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin-273.15
    fahrenheit = celsius*(9/5)+32
    return celsius, fahrenheit


city = input("what city do you want to check? ")
url = BASE_URL + "APPID=" + API_KEY + "&q=" + city
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(
    feels_like_kelvin)

humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(
    response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(
    response['sys']['sunset'] + response['timezone'])

print(f'Temperature in {city}: {temp_celsius:.2f}\N{DEGREE SIGN}C')
print(
    f'Temperature in {city} feels like: {feels_like_celsius:.2f}\N{DEGREE SIGN}C')
print(f'Humidity in {city}: {humidity}%')
print(f'General weather in {city}: {description}')

print(f'Sun rises in {city} at {sunrise_time}')
print(f'Sun sets in {city} at {sunset_time}')
