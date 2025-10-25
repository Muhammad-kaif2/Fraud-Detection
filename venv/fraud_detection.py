import streamlit as st
import pandas as pd
import joblib
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'fraud_detection_model.pkl')
model = joblib.load(model_path)
st.title("Fraud Detection Model App")
st.markdown("Please enter the transaction details and use the predict button.")

st.divider()
transaction_type = st.selectbox("Transaction Type", ['CASH_OUT', 'DEPOSIT', 'PAYMENT', 'TRANSFER'])
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=1000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=1000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)
if st.button("Predict Fraud"):
    input_data = pd.DataFrame([{
        'type': transaction_type,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
        'balanceDiffOrig': oldbalanceOrg - newbalanceOrig,  # Calculate balance difference for sender
        'balanceDiffDest': newbalanceDest - oldbalanceDest  # Calculate balance difference for receiver
    }])
    prediction = model.predict(input_data)[0]
    st.subheader(f"Prediction : {int(prediction)}")
    if prediction == 1:
        st.error("The transaction is predicted to be FRAUDULENT.")
    else:
        st.success("The transaction is Look like it is not fraudulent.")

# D:/furad_detiction/venv/Scripts/python.exe -m streamlit run venv/fraud_detection.py