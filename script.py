from flask import Flask, request, jsonify
from flask_cors import CORS
from gpt4all import GPT4All

app = Flask(__name__)
CORS(app)

model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
# Carregar modelo
model = GPT4All(model_name, device="cpu")

@app.route("/")
def home():
    return "Server running with Llama-3.2-1B!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Mensagem vazia"}), 400

    with model.chat_session():
        response = model.generate(user_message, max_tokens=512)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)