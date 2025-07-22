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
├── data/                           # Raw and cleaned datasets
├── notebooks/                      # Jupyter/Colab notebooks for EDA and modeling
│   ├── task1_data_exploration.ipynb
│   ├── task2_data_preprocessing.ipynb
│   ├── task3_model_training.ipynb
│   └── task4_model_saving.ipynb
├── model/                         # Saved models and vectorizers
│   ├── logistic_regression_model.joblib
│   └── tfidf_vectorizer.joblib
├── api/                           # Flask API code (to be added)
├── Dockerfile                     # Docker container definition (to be added)
├── .github/workflows/             # CI/CD workflows (to be added)
└── README.md                      # Project overview and instructions
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
