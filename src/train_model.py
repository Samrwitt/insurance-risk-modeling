# src/train_model.py
import json
import os
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load data
df = pd.read_csv('data/MachineLearningRating_v3.txt', delimiter='|', low_memory=False)

# Convert to numeric and clean
df['CustomValueEstimate'] = pd.to_numeric(df['CustomValueEstimate'], errors='coerce')
df = df[df['TotalClaims'] > 0].dropna(subset=['CustomValueEstimate', 'TotalClaims'])

print("Filtered sample count:", len(df))

# Exit early if no data
if df.empty:
    raise ValueError("No data available after filtering for model training.")

# Prepare features and target
X = df[['CustomValueEstimate']]
y = df['TotalClaims']

# Train model
model = LinearRegression()
model.fit(X, y)
preds = model.predict(X)

# Evaluate
rmse = np.sqrt(mean_squared_error(y, preds))
r2 = r2_score(y, preds)

# Save metrics
with open("metrics.json", "w") as f:
    json.dump({"rmse": rmse, "r2": r2}, f, indent=2)

# Ensure model directory exists
os.makedirs("models", exist_ok=True)

# Save model
with open("models/linear_model.pkl", "wb") as f:
    pickle.dump(model, f)
