# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("svm_model.pkl")

# Page setup
st.set_page_config(page_title="Single Transaction Checker")
st.title(" Predict a Single Transaction")

#  Input form
with st.form("txn_form"):
    amount = st.number_input("Amount", min_value=0.0, step=1.0)
    hour = st.slider("Hour", 0, 23, 12)
    day = st.slider("Day", 1, 31, 15)
    month = st.slider("Month", 1, 12, 6)

    user_id = st.number_input("User ID", min_value=0, step=1)
    access_point = st.number_input("Access Point ID", min_value=0, step=1)
    debit_acc = st.number_input("Debit Account", min_value=0, step=1)
    currency = st.number_input("Currency Code", min_value=0, step=1)
    payment_type = st.number_input("Payment Type Code", min_value=0, step=1)
    beneficiary = st.number_input("Beneficiary Code", min_value=0, step=1)

    submitted = st.form_submit_button("Predict")

#  Prediction
if submitted:
    row = pd.DataFrame([{
        "USER_ID": user_id,
        "ACCESS_POINT_ID": access_point,
        "DEBIT_ACCOUNT": debit_acc,
        "AMOUNT": amount,
        "CURRENCY": currency,
        "PAYMENTTYPE": payment_type,
        "BENEFICIARYNAME": beneficiary,
        "HOUR": hour,
        "DAY": day,
        "MONTH": month
    }])

    prediction = model.predict(row)[0]
    if prediction == -1:
        st.error(" Anomalous Transaction Detected")
    else:
        st.success(" Normal Transaction")
