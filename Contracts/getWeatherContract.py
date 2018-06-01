import requests
import json
from jsonschema import validate
from weatherSchema import getWeatherSchema
import jsonschema
import pytest



class TestWeatherContract(object):
    def test_weather_contract(self):
        data = requests.get(url='https://api.forecast.io/forecast/568b3c62adcc336da9b224de0dfaa31a/28.6139391,77.2090212')
        statusCode = data.status_code
        data = data.json()
        schema = getWeatherSchema
        if data['latitude'] == 28.6139391:
            try:
                myDict = {}
                v = jsonschema.Draft4Validator((schema))
                for error in sorted(v.iter_errors((data)), key=str):
                    myDict[str(error.path)] = str(error.message)
                    print(myDict)
                    assert len(myDict) == 0, "failures in contract"
            except jsonschema.ValidationError as e:
                print(e.message)
        elif statusCode not in [200,404]:
            pytest.xfail("Weather fetch failed for this city")
        else:
            pytest.skip("No config present on this city")

