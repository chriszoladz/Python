import requests
import sys

from pprint import pprint

API_Key = '2a929b0a380076763d38066ec1bd9700'


city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)

def pause_execution():
    input("Enter to Continue...")

pause_execution()

print("Thanks for using this!")