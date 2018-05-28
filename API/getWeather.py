import requests
import json
from jsonschema import validate
import jsonschema
import pytest
from nested_lookup import nested_lookup

def weather(latitude,longitude,case):
    
    url = "https://api.forecast.io/forecast/568b3c62adcc336da9b224de0dfaa31a/"+str(float(latitude))+","+str(float(longitude))
    getWeatherByLatLong = requests.get(url=url)
    response = getWeatherByLatLong.text
    data = getWeatherByLatLong.json()
    
    currentTemp = int(data['currently']['temperature'])
    
    if case == 1:
        
        minTemp = nested_lookup('temperatureMin',data['daily']['data'])
        minTemp = minTemp[1:6]
        for i in range(len(minTemp)):
            minTemp[i] = str(int(minTemp[i]))
        return minTemp

    elif case == 2:
        maxTemp = nested_lookup('temperatureMax',data['daily']['data'])
        maxTemp = maxTemp[1:6]
        for i in range(len(maxTemp)):
            maxTemp[i] = str(int(maxTemp[i]))

        return maxTemp

    else :
        currentTemp = str(int(data['currently']['temperature']))
        return currentTemp
    
