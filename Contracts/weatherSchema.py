getWeatherSchema = {
  "$id": "http://example.com/example.json", 
  "type": "object", 
  "definitions": {}, 
  "$schema": "http://json-schema.org/draft-07/schema#", 
  "additionalProperties": False, 
  "properties": {
    "latitude": {
      "$id": "/properties/latitude", 
      "type": "number"
    }, 
    "longitude": {
      "$id": "/properties/longitude", 
      "type": "number"
    }, 
    "timezone": {
      "$id": "/properties/timezone", 
      "type": "string"
    }, 
    "currently": {
      "$id": "/properties/currently", 
      "type": "object", 
      "additionalProperties": False, 
      "properties": {
        "time": {
          "$id": "/properties/currently/properties/time", 
          "type": "integer"
        }, 
        "summary": {
          "$id": "/properties/currently/properties/summary", 
          "type": "string"
        }, 
        "icon": {
          "$id": "/properties/currently/properties/icon", 
          "type": "string"
        }, 
        "precipIntensity": {
          "$id": "/properties/currently/properties/precipIntensity", 
          "type": "number"
        }, 
        "precipProbability": {
          "$id": "/properties/currently/properties/precipProbability", 
          "type": "number"
        }, 
        "temperature": {
          "$id": "/properties/currently/properties/temperature", 
          "type": "number"
        }, 
        "apparentTemperature": {
          "$id": "/properties/currently/properties/apparentTemperature", 
          "type": "number"
        }, 
        "dewPoint": {
          "$id": "/properties/currently/properties/dewPoint", 
          "type": "number"
        }, 
        "humidity": {
          "$id": "/properties/currently/properties/humidity", 
          "type": "number"
        }, 
        "pressure": {
          "$id": "/properties/currently/properties/pressure", 
          "type": "number"
        }, 
        "windSpeed": {
          "$id": "/properties/currently/properties/windSpeed", 
          "type": "number"
        }, 
        "windGust": {
          "$id": "/properties/currently/properties/windGust", 
          "type": "number"
        }, 
        "windBearing": {
          "$id": "/properties/currently/properties/windBearing", 
          "type": "integer"
        }, 
        "cloudCover": {
          "$id": "/properties/currently/properties/cloudCover", 
          "type": "number"
        }, 
        "uvIndex": {
          "$id": "/properties/currently/properties/uvIndex", 
          "type": "integer"
        }, 
        "visibility": {
          "$id": "/properties/currently/properties/visibility", 
          "type": "number"
        }, 
        "ozone": {
          "$id": "/properties/currently/properties/ozone", 
          "type": "number"
        }
      }
    }, 
    "hourly": {
      "$id": "/properties/hourly", 
      "type": "object", 
      "additionalProperties": False, 
      "properties": {
        "summary": {
          "$id": "/properties/hourly/properties/summary", 
          "type": "string"
        }, 
        "icon": {
          "$id": "/properties/hourly/properties/icon", 
          "type": "string"
        }, 
        "data": {
          "$id": "/properties/hourly/properties/data", 
          "type": "array", 
          "additionalItems": False, 
          "items": {
            "$id": "/properties/hourly/properties/data/items", 
            "type": "object", 
            "additionalProperties": False, 
            "properties": {
              "time": {
                "$id": "/properties/hourly/properties/data/items/properties/time", 
                "type": "integer"
              }, 
              "summary": {
                "$id": "/properties/hourly/properties/data/items/properties/summary", 
                "type": "string"
              }, 
              "icon": {
                "$id": "/properties/hourly/properties/data/items/properties/icon", 
                "type": "string"
              }, 
              "precipIntensity": {
                "$id": "/properties/hourly/properties/data/items/properties/precipIntensity", 
                "type": "number"
              }, 
              "precipProbability": {
                "$id": "/properties/hourly/properties/data/items/properties/precipProbability", 
                "type": "number"
              }, 
              "temperature": {
                "$id": "/properties/hourly/properties/data/items/properties/temperature", 
                "type": "number"
              }, 
              "apparentTemperature": {
                "$id": "/properties/hourly/properties/data/items/properties/apparentTemperature", 
                "type": "number"
              }, 
              "dewPoint": {
                "$id": "/properties/hourly/properties/data/items/properties/dewPoint", 
                "type": "number"
              }, 
              "humidity": {
                "$id": "/properties/hourly/properties/data/items/properties/humidity", 
                "type": "number"
              }, 
              "pressure": {
                "$id": "/properties/hourly/properties/data/items/properties/pressure", 
                "type": "number"
              }, 
              "windSpeed": {
                "$id": "/properties/hourly/properties/data/items/properties/windSpeed", 
                "type": "number"
              }, 
              "windGust": {
                "$id": "/properties/hourly/properties/data/items/properties/windGust", 
                "type": "number"
              }, 
              "windBearing": {
                "$id": "/properties/hourly/properties/data/items/properties/windBearing", 
                "type": "integer"
              }, 
              "cloudCover": {
                "$id": "/properties/hourly/properties/data/items/properties/cloudCover", 
                "type": "number"
              }, 
              "uvIndex": {
                "$id": "/properties/hourly/properties/data/items/properties/uvIndex", 
                "type": "integer"
              }, 
              "visibility": {
                "$id": "/properties/hourly/properties/data/items/properties/visibility", 
                "type": "number"
              }, 
              "ozone": {
                "$id": "/properties/hourly/properties/data/items/properties/ozone", 
                "type": "number"
              }
            }
          }
        }
      }
    }, 
    "daily": {
      "$id": "/properties/daily", 
      "type": "object", 
      "additionalProperties": False, 
      "properties": {
        "summary": {
          "$id": "/properties/daily/properties/summary", 
          "type": "string"
        }, 
        "icon": {
          "$id": "/properties/daily/properties/icon", 
          "type": "string"
        }, 
        "data": {
          "$id": "/properties/daily/properties/data", 
          "type": "array", 
          "additionalItems": False, 
          "items": {
            "$id": "/properties/daily/properties/data/items", 
            "type": "object", 
            "additionalProperties": False, 
            "properties": {
              "time": {
                "$id": "/properties/daily/properties/data/items/properties/time", 
                "type": "integer"
              }, 
              "summary": {
                "$id": "/properties/daily/properties/data/items/properties/summary", 
                "type": "string"
              }, 
              "icon": {
                "$id": "/properties/daily/properties/data/items/properties/icon", 
                "type": "string"
              }, 
              "sunriseTime": {
                "$id": "/properties/daily/properties/data/items/properties/sunriseTime", 
                "type": "integer"
              }, 
              "sunsetTime": {
                "$id": "/properties/daily/properties/data/items/properties/sunsetTime", 
                "type": "integer"
              }, 
              "moonPhase": {
                "$id": "/properties/daily/properties/data/items/properties/moonPhase", 
                "type": "number"
              }, 
              "precipIntensity": {
                "$id": "/properties/daily/properties/data/items/properties/precipIntensity", 
                "type": "number"
              }, 
              "precipIntensityMax": {
                "$id": "/properties/daily/properties/data/items/properties/precipIntensityMax", 
                "type": "number"
              }, 
              "precipIntensityMaxTime": {
                "$id": "/properties/daily/properties/data/items/properties/precipIntensityMaxTime", 
                "type": "integer"
              }, 
              "precipProbability": {
                "$id": "/properties/daily/properties/data/items/properties/precipProbability", 
                "type": "number"
              }, 
              "temperatureHigh": {
                "$id": "/properties/daily/properties/data/items/properties/temperatureHigh", 
                "type": "number"
              },
              "precipType": {
                "$id": "/properties/daily/properties/data/items/properties/precipType", 
                "type": "string"
              }, 
              "temperatureHighTime": {
                "$id": "/properties/daily/properties/data/items/properties/temperatureHighTime", 
                "type": "integer"
              }, 
              "temperatureLow": {
                "$id": "/properties/daily/properties/data/items/properties/temperatureLow", 
                "type": "number"
              }, 
              "temperatureLowTime": {
                "$id": "/properties/daily/properties/data/items/properties/temperatureLowTime", 
                "type": "integer"
              }, 
              "apparentTemperatureHigh": {
                "$id": "/properties/daily/properties/data/items/properties/apparentTemperatureHigh", 
                "type": "number"
              }, 
              "apparentTemperatureHighTime": {
                "$id": "/properties/daily/properties/data/items/properties/apparentTemperatureHighTime", 
                "type": "integer"
              }, 
              "apparentTemperatureLow": {
                "$id": "/properties/daily/properties/data/items/properties/apparentTemperatureLow", 
                "type": "number"
              }, 
              "apparentTemperatureLowTime": {
                "$id": "/properties/daily/properties/data/items/properties/apparentTemperatureLowTime", 
                "type": "integer"
              }, 
              "dewPoint": {
                "$id": "/properties/daily/properties/data/items/properties/dewPoint", 
                "type": "number"
              }, 
              "humidity": {
                "$id": "/properties/daily/properties/data/items/properties/humidity", 
                "type": "number"
              }, 
              "pressure": {
                "$id": "/properties/daily/properties/data/items/properties/pressure", 
                "type": "number"
              }, 
              "windSpeed": {
                "$id": "/properties/daily/properties/data/items/properties/windSpeed", 
                "type": "number"
              }, 
              "windGust": {
                "$id": "/properties/daily/properties/data/items/properties/windGust", 
                "type": "number"
              }, 
              "windGustTime": {
                "$id": "/properties/daily/properties/data/items/properties/windGustTime", 
                "type": "integer"
              }, 
              "windBearing": {
                "$id": "/properties/daily/properties/data/items/properties/windBearing", 
                "type": "integer"
              }, 
              "cloudCover": {
                "$id": "/properties/daily/properties/data/items/properties/cloudCover", 
                "type": "number"
              }, 
              "uvIndex": {
                "$id": "/properties/daily/properties/data/items/properties/uvIndex", 
                "type": "integer"
              }, 
              "uvIndexTime": {
                "$id": "/properties/daily/properties/data/items/properties/uvIndexTime", 
                "type": "integer"
              }, 
              "ozone": {
                "$id": "/properties/daily/properties/data/items/properties/ozone", 
                "type": "number"
              }, 
              "temperatureMin": {
                "$id": "/properties/daily/properties/data/items/properties/temperatureMin", 
                "type": "number"
              }, 
              "temperatureMinTime": {
                "$id": "/properties/daily/properties/data/items/properties/temperatureMinTime", 
                "type": "integer"
              }, 
              "temperatureMax": {
                "$id": "/properties/daily/properties/data/items/properties/temperatureMax", 
                "type": "number"
              }, 
              "temperatureMaxTime": {
                "$id": "/properties/daily/properties/data/items/properties/temperatureMaxTime", 
                "type": "integer"
              }, 
              "apparentTemperatureMin": {
                "$id": "/properties/daily/properties/data/items/properties/apparentTemperatureMin", 
                "type": "number"
              }, 
              "apparentTemperatureMinTime": {
                "$id": "/properties/daily/properties/data/items/properties/apparentTemperatureMinTime", 
                "type": "integer"
              }, 
              "apparentTemperatureMax": {
                "$id": "/properties/daily/properties/data/items/properties/apparentTemperatureMax", 
                "type": "number"
              }, 
              "apparentTemperatureMaxTime": {
                "$id": "/properties/daily/properties/data/items/properties/apparentTemperatureMaxTime", 
                "type": "integer"
              }
            }
          }
        }
      }
    }, 
    "flags": {
      "$id": "/properties/flags", 
      "type": "object", 
      "additionalProperties": False, 
      "properties": {
        "sources": {
          "$id": "/properties/flags/properties/sources", 
          "type": "array", 
          "additionalItems": False, 
          "items": {
            "$id": "/properties/flags/properties/sources/items", 
            "type": "string"
          }
        }, 
        "isd-stations": {
          "$id": "/properties/flags/properties/isd-stations", 
          "type": "array", 
          "additionalItems": False, 
          "items": {
            "$id": "/properties/flags/properties/isd-stations/items", 
            "type": "string"
          }
        }, 
        "units": {
          "$id": "/properties/flags/properties/units", 
          "type": "string"
        }
      }
    }, 
    "offset": {
      "$id": "/properties/offset", 
      "type": "integer"
    }
  }
}