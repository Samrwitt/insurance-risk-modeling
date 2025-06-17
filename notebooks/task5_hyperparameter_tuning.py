import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import mean_squared_error, r2_score

# === Load and preprocess the data ===
df = pd.read_csv('data/MachineLearningRating_v3.txt', delimiter='|')
df = df[df['TotalClaims'] > 0].dropna()

X = df[['CustomValueEstimate']]
y = df['TotalClaims']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# === Define parameter grid ===
rf_params = {
    'n_estimators': [100, 200, 300],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# === Run Randomized Search ===
rf = RandomForestRegressor(random_state=42)

rf_search = RandomizedSearchCV(
    estimator=rf,
    param_distributions=rf_params,
    n_iter=10,
    cv=3,
    scoring='neg_root_mean_squared_error',
    verbose=2,
    random_state=42,
    n_jobs=-1
)

rf_search.fit(X_train, y_train.ravel())
best_rf = rf_search.best_estimator_

# === Evaluate the tuned model ===
y_pred_best_rf = best_rf.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred_best_rf))
r2 = r2_score(y_test, y_pred_best_rf)

print(f"Tuned Random Forest - RMSE: {rmse:.2f}, R²: {r2:.2f}")

