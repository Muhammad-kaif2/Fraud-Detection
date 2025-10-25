# Fraud-Detection
🧠 Fraud Detection Machine Learning Model — Project Description
🔍 Project Overview

This project focuses on building a Fraud Detection System using Machine Learning techniques.
The main goal of this model is to identify and prevent fraudulent financial transactions by analyzing transaction-related features such as transaction type, amount, and account balances.

Fraud detection is a critical task for banks, payment systems, and online platforms to minimize financial loss and enhance security.

🎯 Objective

To develop a machine learning model that can accurately classify whether a given transaction is fraudulent (1) or genuine (0) based on historical data.

📊 Dataset

Dataset Name: AIML Dataset.csv

Features Used:

type → Transaction type (e.g., CASH_OUT, TRANSFER, PAYMENT, etc.)

amount → Transaction amount

oldbalanceOrg → Original balance of the sender before the transaction

newbalanceOrig → New balance of the sender after the transaction

oldbalanceDest → Original balance of the receiver before the transaction

newbalanceDest → New balance of the receiver after the transaction

Target Variable:

isFraud → 1 (Fraudulent) or 0 (Genuine)

⚙️ Tech Stack

Language: Python 🐍

Libraries:

pandas – for data manipulation

numpy – for numerical operations

matplotlib / seaborn – for visualization

scikit-learn – for model training (e.g., Logistic Regression, KNN, Random Forest, etc.)

joblib – for saving the trained model

streamlit – for building the interactive web application

🧩 Model Workflow

Data Preprocessing

Handled missing values and outliers

Converted categorical data (transaction type) into numerical format using encoding

Scaled numeric features for better model performance

Model Training

Trained multiple ML models (e.g., KNN, Logistic Regression, Random Forest)

Evaluated models using accuracy, precision, recall, and confusion matrix

Selected the best performing model for deployment

Model Saving

The final trained model was saved as a .pkl file using joblib.dump()

Deployment

The saved model is integrated into a Streamlit web app (fraud_detection.py)

The user can input transaction details and get real-time fraud predictions

🚀 How It Works

User opens the Streamlit app

Inputs transaction details (amount, type, balances, etc.)

The app loads the trained model (fraud_detection_model.pkl)

Model predicts if the transaction is fraudulent or not

The app displays:

✅ “Transaction looks genuine”

❌ “Transaction is predicted to be fraudulen
