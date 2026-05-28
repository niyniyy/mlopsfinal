# ML User Type Prediction System

## Overview

This project is an end-to-end Machine Learning deployment pipeline for predicting user types based on platform engagement metrics. The application allows users to upload CSV files and receive predictions through an interactive Streamlit web interface.

The project demonstrates core MLOps concepts including:

* Machine Learning model training
* Model serialization
* Streamlit deployment
* CI/CD workflow integration
* Docker support
* DVC (Data Version Control) integration
* Cloud deployment

---

# Features

* Upload CSV files for prediction
* Real-time ML inference
* Streamlit-based interactive UI
* Random Forest Classification model
* Model artifact versioning with DVC
* Deployment-ready architecture
* Docker container support

---

# Tech Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core programming language |
| Scikit-learn | Machine Learning          |
| Pandas       | Data processing           |
| Streamlit    | Web application frontend  |
| Joblib       | Model serialization       |
| DVC          | Data and model versioning |
| Docker       | Containerization          |
| GitHub       | Version control and CI/CD |

---

# Project Structure

```bash
mlopsfinal/
│
├── app.py
├── model.pkl
├── requirements.txt
├── Dockerfile
├── README.md
│
├── src/
│   └── model.py
│
├── data/
│   └── data.csv
│
├── .dvc/
└── .github/
    └── workflows/
```

---

# Machine Learning Workflow

## Training Phase

1. Dataset is loaded using Pandas
2. Features and labels are separated
3. Data is split into training and testing sets
4. Random Forest Classifier is trained
5. Model is evaluated
6. Trained model is saved as `model.pkl`

## Prediction Phase

1. User uploads CSV file
2. CSV is processed
3. Required features are extracted
4. Trained model predicts user type
5. Predictions are displayed in Streamlit

---

# Features Used

The model uses the following input features:

* `session_length`
* `articles_read`
* `comments_posted`
* `subscription_status`

Target column:

* `user_type`

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd mlopsfinal
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

---

# Docker Support

Build Docker image:

```bash
docker build -t mlops-app .
```

Run container:

```bash
docker run -p 8501:8501 mlops-app
```

---

# DVC Integration

Initialize DVC:

```bash
dvc init
```

Track model artifact:

```bash
dvc add model.pkl
```

Push artifacts to remote storage:

```bash
dvc push
```

---

# CI/CD Workflow

GitHub Actions is used to automate:

* Dependency installation
* Testing
* Build validation
* Deployment workflow

---

# Deployment

The application is deployed using Streamlit Community Cloud.

Users can upload CSV files directly through the web interface and receive predictions in real time.

---

# Future Improvements

* Add advanced preprocessing pipeline
* Improve model accuracy
* Add authentication
* Integrate database storage
* Add visualization dashboards
* Deploy with Kubernetes for scalability

---

# Author

Lily Michaelis

Data Science Undergraduate | Machine Learning & MLOps Enthusiast
