🌾 SMART CROP RECOMMENDER
This project is a smart AI assistant for modern agriculture. It:

✅ Loads real sensor data (temperature, humidity, pH, rainfall)

✅ Uses machine learning to recommend the best crop

✅ Detects anomalies in the environment (like extreme pH or temperature)

✅ Shows everything in a clean Streamlit dashboard with charts, summaries, and download options

📦 Libraries Used (and What They're For)
Library Purpose
pandas For handling datasets in table format (like Excel sheets)
numpy For numerical operations and handling arrays
scikit-learn For machine learning (crop prediction & anomaly detection)
joblib To save and load trained ML models
streamlit To build the interactive web dashboard

🤖 Algorithms Used (and Why)

1. Random Forest Classifier
   📄 Used in: predictor.py
   🧠 Purpose: Predict the best crop to grow based on environmental inputs
   📘 What it is: A powerful algorithm that uses many decision trees and takes a "vote" on the final answer
   ✅ Great for:

Classifying multiple crop types
Handling nonlinear relationships
Robust performance even with noisy data

2. Isolation Forest
   📄 Used in: anomaly_detector.py
   🧠 Purpose: Identify unusual or faulty sensor readings
   📘 What it is: An algorithm that isolates outliers by randomly selecting features and split values
   ✅ Great for:

Finding data points that are very different
No need for labeled "bad" data
Fast and efficient for large datasets

🧪 How the App Works (Behind the Scenes)
✅ Step 1: Load Real Data
The app loads a Kaggle dataset with 2,200+ rows of crop and sensor data — including temperature, pH, humidity, and rainfall.

✅ Step 2: Train a Machine Learning Model
The model learns which crop performs best under certain conditions.
For example:

High humidity + low pH → Rice

High temp + moderate pH → Cotton

✅ Step 3: Predict Crops on New Data
The model is used to make real-time predictions for new or test data.
You can also filter the results, view summaries, and download predictions.

✅ Step 4: Detect Anomalies
An Isolation Forest looks for strange patterns in the sensor data.

For example:

Extremely high temperature

Unusual rainfall or pH values
These are flagged as anomalies to alert users.

✅ Step 5: Visualize Everything in a Dashboard
Streamlit ties everything together in an interactive web app:

📊 Line charts of live sensor readings

🌱 Table of predicted crops

⚠️ List of detected anomalies

📥 Download option to export results
