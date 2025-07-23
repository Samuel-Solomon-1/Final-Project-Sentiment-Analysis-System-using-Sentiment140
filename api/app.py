from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Paths
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, '..', 'model', 'logistic_regression_model.joblib')
vectorizer_path = os.path.join(base_dir, '..', 'model', 'tfidf_vectorizer.joblib')

# Load model and vectorizer
with open(model_path, 'rb') as f:
    model = joblib.load(f)

with open(vectorizer_path, 'rb') as f:
    vectorizer = joblib.load(f)

@app.route('/')
def home():
    return 'Sentiment Analysis API is running!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if 'text' not in data:
        return jsonify({'error': 'Missing "text" field'}), 400

    text = data['text']
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]  # prediction is already a string like "positive" or "negative"

    return jsonify({'sentiment': prediction})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
