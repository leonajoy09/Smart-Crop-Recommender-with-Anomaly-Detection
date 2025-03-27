# app/data_loader.py

import pandas as pd


def load_sensor_data():
    df = pd.read_csv("data/Crop_recommendationV2.csv")
    df = df.rename(columns={"ph": "pH", "label": "crop"})
    df["timestamp"] = pd.date_range(
        end=pd.Timestamp.now(), periods=len(df), freq="T")
    return df
