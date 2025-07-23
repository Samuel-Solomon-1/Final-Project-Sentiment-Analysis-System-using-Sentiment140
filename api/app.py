from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), '../model/sentiment_model.pkl')
vectorizer_path = os.path.join(os.path.dirname(__file__), '../model/vectorizer.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(vectorizer_path, 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    tweet = data.get('tweet')

    if not tweet:
        return jsonify({'error': 'No tweet provided'}), 400

    X = vectorizer.transform([tweet])
    prediction = model.predict(X)

    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
