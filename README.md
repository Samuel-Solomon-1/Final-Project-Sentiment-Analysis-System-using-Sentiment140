# Sentiment Analysis System using Sentiment140

## Project Overview

This repository contains an end-to-end sentiment analysis system that classifies tweets into **Positive**, **Neutral**, or **Negative** sentiments using the **Sentiment140** dataset.

The project is structured in phases:

- **Data Preprocessing**: Cleaning and preparing raw tweet data.
- **Model Training**: Building a Logistic Regression classifier using TF-IDF features.
- **Model Saving**: Persisting the trained model and vectorizer for deployment.
- **API Development**: Creating a Flask API to serve the model (to be implemented in GitHub Codespaces).
- **Containerization & Deployment**: Dockerizing the API and deploying with CI/CD pipelines (future steps).

---

## Dataset

- The Sentiment140 dataset contains 1.6 million labeled tweets.
- Labels:  
  - `0` = Negative  
  - `2` = Neutral  
  - `4` = Positive  
- Dataset source: [Sentiment140 official website](http://help.sentiment140.com/for-students/)

---

## Repository Structure

```plaintext
.
├── data/                    # datasets
├── notebooks/               # Jupyter notebooks
│   ├── Final Project: Sentiment Analysis System using Sentiment140.ipynb
├── model/                   # Saved models
│   ├── logistic_regression_model.joblib
│   └── tfidf_vectorizer.joblib
├── api/                     # Flask API code
├── Dockerfile               # Docker definition
├── .github/workflows/       # Workflows
└── README.md                # Project overview
```

---

How to Use

1. Data Preparation & Model Training
Explore and preprocess data, then train the model using the notebooks inside notebooks/.


2. Model Persistence
The trained model and vectorizer are saved in the model/ directory.


3. API Development & Deployment
The next steps involve developing a Flask API, containerizing it with Docker, and deploying with CI/CD pipelines.
---

Requirements

Python 3.8+

pandas

scikit-learn

Flask (for API development)

joblib
