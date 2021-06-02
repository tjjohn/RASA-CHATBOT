# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionResult(Action):

     def name(self) -> Text:
         return "action_result"    # define in stories & doamin

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text=" result on loading")

         return []
     
        
        
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "nameaction"      

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
          entities = tracker.latest_message['entities']
          n=''
          for e in entities:
            if e['entity']=='person':
                n=e['value']
                
            if n=='john':
                m="hey young boy"
            if n=='mary':
                m="hey young girl"
            if n=='jose':
                m="hey "+n +"how are youl"
                

          dispatcher.utter_message(text=m)

          return []
