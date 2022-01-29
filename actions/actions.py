# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionCheckCapital(Action):

    def name(self) -> Text:
        return "action_display_of_check_capital"

    def run(self, dispatcher, tracker, domain):
        country_name= next(tracker.get_latest_entity_values("country_name"), None)
        country_name_lower = country_name.lower()
        src=requests.get('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries').json()
        countries_list = src["body"]
        countries_list_lower = [each_string.lower() for each_string in countries_list]
        # dispatcher.utter_message(countries_list[1])
        if country_name not in countries_list:
            msg = "Could You re-enter the Country?!"
            dispatcher.utter_message(text=msg)
            return []
        if country_name_lower in countries_list_lower:
            headers = {'content-type': 'application/json'}
            country_name_capitalize_to_match_api = country_name_lower.capitalize()
            capital=requests.post('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital',json={"country":country_name_capitalize_to_match_api}, headers=headers).json()
            msg=" The capital is {}".format(capital['body']['capital'])
            dispatcher.utter_message(text=msg)
            return []
        return []

class ActionCheckPopulation(Action):

    def name(self) -> Text:
        return "action_display_of_check_population"

    def run(self, dispatcher, tracker, domain):
        country_name= next(tracker.get_latest_entity_values("country_name"), None)
        country_name_lower = country_name.lower()
        src=requests.get('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries').json()
        countries_list = src["body"]
        countries_list_lower = [each_string.lower() for each_string in countries_list]
        # dispatcher.utter_message(countries_list[1])
        if country_name not in countries_list:
            msg = "Could You re-enter the Country?!"
            dispatcher.utter_message(text=msg)
            return []
        if country_name_lower in countries_list_lower:
            headers = {'content-type': 'application/json'}
            country_name_capitalize_to_match_api = country_name_lower.capitalize()
            population_value=requests.post('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getPopulation',json={"country": country_name_capitalize_to_match_api}).json()
            msg=" The population is {}".format(population_value['body']['population'])
            dispatcher.utter_message(text=msg)
            return []
        return []
