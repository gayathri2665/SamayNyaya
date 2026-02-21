# ml/train.py

import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score

from preprocess import load_and_preprocess
from model import train_duration_model, train_adjournment_model

# Create models folder if not exists
os.makedirs("ml/models", exist_ok=True)

# Load dataset
df = load_and_preprocess("data/synthetic_cases.csv")

# Select features based on YOUR dataset
X = df[['case_type',
        'parties',
        'complexity',
        'evidence_count',
        'lawyer_count',
        'adjournments',
        'filing_year']]

# Targets
y_duration = df['actual_duration']
y_adj = df['adjourned']

# -------- Duration Model --------
X_train, X_test, y_train, y_test = train_test_split(
    X, y_duration, test_size=0.2, random_state=42
)

duration_model = train_duration_model(X_train, y_train)

pred_duration = duration_model.predict(X_test)

# Manual RMSE calculation (compatible with older sklearn)
mse = mean_squared_error(y_test, pred_duration)
rmse = mse ** 0.5

print("Duration Model RMSE:", rmse)

# Save duration model
joblib.dump(duration_model, "ml/models/duration_model.pkl")


# -------- Adjournment Model --------
X_train, X_test, y_train, y_test = train_test_split(
    X, y_adj, test_size=0.2, random_state=42
)

adj_model = train_adjournment_model(X_train, y_train)

pred_adj = adj_model.predict(X_test)
accuracy = accuracy_score(y_test, pred_adj)

print("Adjournment Model Accuracy:", accuracy)

# Save adjournment model
joblib.dump(adj_model, "ml/models/adjournment_model.pkl")

print("✅ Models trained and saved successfully.")
