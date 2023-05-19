from flask import Flask, request, jsonify
import chatbot

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    response = chatbot.get_response(chatbot.model, message)
    return jsonify({'response': response})

if __name__ == '__main__':
    chatbot.load_intents()
    chatbot.load_model_files()
    model = chatbot.model
    app.run()
