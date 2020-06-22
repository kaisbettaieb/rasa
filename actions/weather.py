from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from actions.api.openweather import OpenWeatherAPI

class WeatherForm(FormAction):
    """Collect the name of city for the weather api"""

    def name(self):
        return "weather_form"
    @staticmethod
    def required_slots(tracker):
        return ["city_name"]

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Getting The weather....")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {"city_name": self.from_text(intent="inform")}

class getWeatherAction(Action):
    def name(self):
        return "get_weather_action"

    def run(
        self, dispatcher, tracker, domain):
        city_name = tracker.get_slot('city_name')
        weather=  OpenWeatherAPI.getWeather(city_name)
        if weather is not None:
            out_messsage = "the weather today in {} is {}".format(city_name, weather)
            dispatcher.utter_message(out_messsage)
        else:
            dispatcher.utter_message("I'm sorry, I can't handle your request. Please try again later.")
        return []