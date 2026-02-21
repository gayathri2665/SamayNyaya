# ml/predict.py

import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load trained models
duration_model = joblib.load(os.path.join(BASE_DIR, "models/duration_model.pkl"))
adj_model = joblib.load(os.path.join(BASE_DIR, "models/adjournment_model.pkl"))
le_case = joblib.load(os.path.join(BASE_DIR, "models/le_case.pkl"))


def predict_case(  case_type,
    parties,
    complexity,
    evidence_count,
    lawyer_count,
    adjournments,
    filing_year
):

    # Ensure case_type format matches training
    case_type = case_type.strip().lower()

    case_type_encoded = le_case.transform([case_type])[0]

    # IMPORTANT: complexity is already numeric
    features = np.array([[case_type_encoded,
                          parties,
                          complexity,
                          evidence_count,
                          lawyer_count,
                          adjournments,
                          filing_year]])

    predicted_duration = duration_model.predict(features)[0]
    adj_probability = adj_model.predict_proba(features)[0][1]

    return predicted_duration, adj_probability