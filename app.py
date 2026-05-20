import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Prediction App")

uploaded_file = st.file_uploader("Upload CSV")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    predictions = model.predict(df)

    df["Prediction"] = predictions

    st.write(df)

    csv = df.to_csv(index=False)

    st.download_button(
        "Download Predictions",
        csv,
        "predictions.csv",
        "text/csv"
    )
