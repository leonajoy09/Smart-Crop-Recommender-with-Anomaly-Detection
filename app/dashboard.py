import streamlit as st
import joblib
import pandas as pd
from app.predictor import predict_crop
from app.anomaly_detector import train_anomaly_model, detect_anomalies


def run_dashboard():
    st.title("🌾 Smart Crop Recommender")

    # Load real sensor data from Kaggle
    df = pd.read_csv("data/test_data.csv")
    if "timestamp" not in df.columns:
        df["timestamp"] = pd.date_range(
            end=pd.Timestamp.now(), periods=len(df), freq="T")

    st.subheader("🌡️ Live Sensor Readings")
    st.line_chart(df[["temperature", "pH", "humidity", "rainfall"]])

    # Load trained model and make predictions
    model = joblib.load("models/model.pkl")
    df["predicted_crop"] = predict_crop(
        model, df[["temperature", "pH", "humidity", "rainfall"]]
    )

    st.subheader("🌱 Predicted Crops")
    st.dataframe(df[["timestamp", "temperature", "pH",
                 "humidity", "rainfall", "predicted_crop"]])

    # Show crop prediction count as a bar chart
    st.subheader("📊 Crop Prediction Summary")
    st.bar_chart(df["predicted_crop"].value_counts())

    # Anomaly detection based on environmental features
    anomaly_model = train_anomaly_model(df)
    df = detect_anomalies(anomaly_model, df)
    st.subheader("⚠️ Anomaly Detection")
    st.write(df[df["anomaly"] == -1])

    # Download button
    st.download_button("📥 Download Results", df.to_csv(
    ).encode(), file_name="crop_predictions.csv")
