
from flask import Flask, request, jsonify
import pickle

# Load trained model
with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

# Create Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Sentiment Analysis API!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    prediction = model.predict([text])[0]

    return jsonify({"text": text, "sentiment": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
