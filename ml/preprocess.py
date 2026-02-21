# ml/preprocess.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def load_and_preprocess(filepath):

    df = pd.read_csv(filepath)

    print("Columns in dataset:", df.columns)

    # Convert filing_date to year
    df['filing_year'] = pd.to_datetime(df['filing_date']).dt.year

    # Rename columns to standard names for ML
    df = df.rename(columns={
        "complexity_score": "complexity",
        "witness_count": "parties",
        "adjournment_history": "adjournments",
        "estimated_duration": "actual_duration",
        "adjourned_today": "adjourned"
    })

    # Encode categorical column
    le_case = LabelEncoder()
    df['case_type'] = le_case.fit_transform(df['case_type'])

    # Convert adjourned yes/no to 1/0
    df['adjourned'] = df['adjourned'].map({'yes': 1, 'no': 0})

    # Create models folder safely
    os.makedirs("ml/models", exist_ok=True)

    # Save encoder
    joblib.dump(le_case, "ml/models/le_case.pkl")

    return df