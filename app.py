import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("User Type Prediction")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.write("Uploaded Data")
    st.write(df)

    features = [
        "session_length",
        "articles_read",
        "comments_posted",
        "subscription_status"
    ]

    df_input = df[features]

    predictions = model.predict(df_input)

    df["Prediction"] = predictions

    st.write(df)
