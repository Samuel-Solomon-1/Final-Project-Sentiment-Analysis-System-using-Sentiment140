from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load model and vectorizer from the model directory
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'logistic_regression_model.joblib')
vectorizer_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'tfidf_vectorizer.joblib')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
        tweet = data.get('tweet')
            
                if not tweet:
                        return jsonify({'error': 'No tweet provided'}), 400

                            features = vectorizer.transform([tweet])
                                prediction = model.predict(features)[0]
                                    
                                        return jsonify({'tweet': tweet, 'sentiment': prediction})

                                        if __name__ == '__main__':
                                            app.run(debug=True, host='0.0.0.0')