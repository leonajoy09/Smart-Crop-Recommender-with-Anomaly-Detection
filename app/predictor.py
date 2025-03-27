
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib


def train_model(df: pd.DataFrame):
    # Features for prediction
    X = df[["temperature", "pH", "humidity", "rainfall"]]

    # Target variable (crop label)
    y = df["crop"]

    # Create and train the classifier model
    model = RandomForestClassifier()
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, "models/model.pkl")


def predict_crop(model, input_data: pd.DataFrame):
    # Predict the crop for new input data
    return model.predict(input_data)
