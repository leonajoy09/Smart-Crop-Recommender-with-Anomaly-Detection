# app/anomaly_detector.py

from sklearn.ensemble import IsolationForest


def train_anomaly_model(df):
    # Use environmental features relevant to the crop prediction
    model = IsolationForest(contamination=0.05)
    model.fit(df[["temperature", "pH", "humidity", "rainfall"]])
    return model


def detect_anomalies(model, df):
    # Predict if rows are normal (1) or anomalous (-1)
    df["anomaly"] = model.predict(
        df[["temperature", "pH", "humidity", "rainfall"]])
    return df
