from flask import Flask, request, jsonify
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import EndpointConfig
import asyncio

app = Flask(__name__)

# Load the trained Rasa model
agent = Agent.load("models")

@app.route('/negotiate', methods=['POST'])
async def negotiate():
    try:
        data = request.get_json()
        message = data.get('offer', "Hello")
        
        # Ensure the message is valid
        if not message:
            return jsonify({"error": "No offer provided."}), 400
        
        # Use asyncio to handle the message
        responses = await agent.handle_text(message)
        
        # Ensure we have a response
        if responses:
            return jsonify({"response": responses[0]['text']})
        else:
            return jsonify({"response": "I didn't understand that."}), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
