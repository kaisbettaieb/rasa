import requests
from typing import Text

API_URL = "http://api.openweathermap.org/data/2.5/weather?q="
API_KEY = "b30c3eae9436b68e48f27d8a0c2c5607"


class OpenWeatherAPI:
    """Class to connect to weatherApi to retrieve weather by city"""

    def __init__(self, city: Text) -> None:
        self.city = city

    @staticmethod
    def getWeather(city: Text):
        res = requests.get(API_URL + city + "&appid=" + API_KEY)
        if res.status_code == 200:
            weather = res.json()['weather'][0]["main"]
            return weather
        else:
            return None
