from app.data_loader import load_sensor_data
from app.predictor import train_model
from sklearn.model_selection import train_test_split

# Load full dataset
df = load_sensor_data()

# Split into train and test (80% train, 20% test)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Train only on training data
train_model(train_df)

# Save test data to CSV so you can load it in dashboard later
test_df.to_csv("data/test_data.csv", index=False)

print("✅ Model trained on training set and test data saved.")
