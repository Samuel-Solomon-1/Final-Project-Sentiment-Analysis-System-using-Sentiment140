import joblib
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Updated paths and extensions
model_path = os.path.join(os.path.dirname(__file__), '../model/sentiment_model.joblib')
vectorizer_path = os.path.join(os.path.dirname(__file__), '../model/vectorizer.joblib')

# Load model and vectorizer
with open(model_path, 'rb') as f:
    model = joblib.load(f)

with open(vectorizer_path, 'rb') as f:
    vectorizer = joblib.load(f)

@app.route('/')
def index():
    return "Sentiment Analysis API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'Missing "text" in request body'}), 400

    text = data['text']
    features = vectorizer.transform([text])
    prediction = model.predict(features)[0]
    return jsonify({'text': text, 'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
