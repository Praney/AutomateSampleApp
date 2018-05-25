import requests
import json
from jsonschema import validate
import jsonschema
import pytest

def weather(latitude,longitude):
    url = "https://api.forecast.io/forecast/568b3c62adcc336da9b224de0dfaa31a/"+str(float(latitude))+","+str(float(longitude))
    getWeatherByLatLong = requests.get(url=url)
    response = getWeatherByLatLong.text
    data = getWeatherByLatLong.json()
    # print data
    currentTemp = int(data['currently']['temperature'])
    print str(currentTemp)
    return str(currentTemp)

