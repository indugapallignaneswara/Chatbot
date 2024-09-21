import logging
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SessionStarted
from rasa.shared.core.events import SlotSet, UserUtteranceReverted

from rasa.shared.core.events import SlotSet

# Standard price for the book
STANDARD_PRICE = 500  # Standard price for the book

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Hello! Are you looking to buy a book or just browsing?")
        
        return [SessionStarted()]

class ActionHandleBuyerIntent(Action):
    def name(self) -> Text:
        return "action_handle_buyer_intent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text=f"The standard price for the book is {STANDARD_PRICE} rupees. What would you like to offer?")
        return []



class ActionHandleOffer(Action):
    def name(self) -> str:
        return "action_handle_offer"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the offer amount entity from the latest message
        offer_amount = next(tracker.get_latest_entity_values("amount"), None)

        if offer_amount is not None:
            try:
                # Convert the offer amount to a float
                offer_amount = float(offer_amount)
            except ValueError:
                dispatcher.utter_message(text="The offer amount is not valid.")
                return []

            # Check if the offer is below the standard price
            if offer_amount < STANDARD_PRICE:
                dispatcher.utter_message(text="Our manufacturing cost is more than the quoted amount. We can't sell our product for less than our profit margin.")
            # Offer is above the standard price
            elif offer_amount > STANDARD_PRICE:
                dispatcher.utter_message(text=f"The quoted value is more than the product cost of {STANDARD_PRICE}. Are you okay with proceeding?")
            # Offer is exactly the standard price
            else:
                dispatcher.utter_message(text=f"Your offer of {offer_amount} has been accepted. Shall we proceed further with the payment and address details?")
        else:
            # No offer amount provided in the message
            dispatcher.utter_message(text="No valid offer amount was found. Please provide an offer amount for the book.")

        return []

class ActionProceedStandardAmount(Action):

    def name(self) -> str:
        return "action_proceed_standard_amount"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        offer_amount = tracker.get_slot("offer_amount")

        if offer_amount is not None:
            try:
                offer_amount = float(offer_amount)
                if offer_amount >= STANDARD_PRICE:
                    dispatcher.utter_message(text="Great! Your order will be processed. Goodbye!")
                    return [SlotSet("offer_amount", None)]  # Resetting the slot
                else:
                    dispatcher.utter_message(text=f"Sorry, we cannot accept {offer_amount}. Our manufacturing cost is more than the quoted amount.")
            except ValueError:
                dispatcher.utter_message(text="Invalid offer amount provided.")
            return []
        else:
            dispatcher.utter_message(text="No offer amount provided.")
            return []

    
class ActionThankYou(Action):
    def name(self) -> Text:
        return "action_thank_you"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_thank_you")
        return []
