
# Negotiation Chatbot

## Overview
This negotiation chatbot simulates a price negotiation process between a customer and a supplier using a pre-trained AI model (e.g., ChatGPT or Gemini). The bot is designed to engage users in a conversational flow, manage offers, and simulate realistic negotiations for purchasing a product (a book in this case).

## Key Features

1. **Basic Conversation Flow**:
   - The chatbot initiates a conversation asking if the user is interested in purchasing a book.
   - Users can express their intent to buy, propose an offer, and negotiate prices.

2. **Pricing Logic**:
   - A standard price of 500 rupees is used for the book.
   - Offers below the standard price are rejected with a rationale on manufacturing costs.
   - Offers at or above the standard price are accepted, allowing the transaction to proceed.

3. **User Interaction**:
   - The bot accepts user input for desired prices and responds accordingly.
   - It provides tailored responses, simulating a realistic price negotiation.

4. **Model Integration**:
   - The chatbot integrates with a pre-trained AI model to handle conversational aspects.
   - API calls are used to process user inputs and generate bot responses.

## Integration Steps

### 1. Set Up the Environment
   - Ensure Python is installed, along with required libraries such as `rasa` and `rasa-sdk`.
   - Install any additional dependencies for the selected AI model (e.g., OpenAI API).

### 2. Define Intents and Entities
   - In `domain.yml`, define intents such as `greet`, `offer`, and `confirm`.
   - Use entities like `amount` to capture the user’s price offers.

### 3. Implement Actions
   - Implement custom actions (e.g., `ActionHandleOffer`) to manage negotiation logic.
   - Use the AI model to generate responses based on user inputs during the negotiation process.

### 4. Model Integration
   - Use the API of the pre-trained AI model to handle user inputs and generate responses.
   - Make sure to securely handle API keys and provide error handling for API requests.

### 5. Testing and Deployment
   - Test the chatbot locally to ensure it responds correctly during the negotiation process.
   - Deploy the chatbot on a web server or cloud service for accessibility.

## Key Functions

- **ActionHandleOffer**: Handles negotiation logic by comparing the user's offer against the standard price and generating responses.
- **utter_message**: Sends appropriate messages to the user based on their input and negotiation status.
- **API Calls**: Ensure API calls to the AI model are correctly set up to process and respond to user queries in real-time.

## Example Interaction

```text
User: "Hello"
Bot: "Hello! Are you looking to buy a book or just browsing?"

User: "I want to buy a book."
Bot: "The standard price for the book is 500 rupees. What would you like to offer?"

User: "I would like to offer 250 rupees."
Bot: "Our manufacturing cost is more than the quoted amount. We can't sell our product for less than our profit margin."

User: "Okay, then I will offer 550 rupees."
Bot: "Your offer of 550 has been accepted. Shall we proceed further with the payment and address details?"

User: "Let's proceed."
Bot: "Goodbye! Have a great day!"
```

## Conclusion
This README provides a high-level overview of the negotiation chatbot, covering core features and steps to integrate the AI model for negotiation. For further customization, you can modify the conversation flow or expand the action logic.
