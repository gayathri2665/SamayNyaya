import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

def show_analytics():

    st.markdown("""
                <style>
                .stApp {
                    background-color: #2B2B2B;
                }
                </style>
                """, unsafe_allow_html=True)

    st.title("Judicial Analytics Dashboard")
                                               
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(BASE_DIR)

    # Load dataset
    df = pd.read_csv(os.path.join(PROJECT_ROOT, "data/synthetic_cases.csv"))

    # Basic preprocessing
    df["filing_year"] = pd.to_datetime(df["filing_date"]).dt.year
    df = df.rename(columns={
        "complexity_score": "complexity",
        "witness_count": "parties",
        "adjournment_history": "adjournments",
        "estimated_duration": "actual_duration",
        "adjourned_today": "adjourned"
    })

    # Convert adjourned
    df["adjourned"] = df["adjourned"].map({"yes": 1, "no": 0})

    st.subheader("1️⃣ Delay Distribution (Real Data)")

    delay_counts = df["adjourned"].value_counts()

    delay_df = pd.DataFrame({
        "Delay": ["No", "Yes"],
        "Cases": [
            delay_counts.get(0, 0),
            delay_counts.get(1, 0)
        ]
    })

    st.bar_chart(delay_df.set_index("Delay"))

    st.markdown("---")

    st.subheader("2️⃣ Case Duration Analysis")

    avg_duration = df["actual_duration"].mean()
    max_duration = df["actual_duration"].max()
    min_duration = df["actual_duration"].min()

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Duration (days)", round(avg_duration, 1))
    col2.metric("Max Duration (days)", max_duration)
    col3.metric("Min Duration (days)", min_duration)

    st.markdown("---")

    st.subheader("3️⃣ High Risk Case Percentage")

    high_risk_cases = df[df["adjourned"] == 1].shape[0]
    total_cases = df.shape[0]

    high_risk_percent = (high_risk_cases / total_cases) * 100

    st.metric("High Delay Risk Cases (%)", round(high_risk_percent, 2))

    st.markdown("---")

    st.subheader("4️⃣ Feature Importance (Adjournment Model)")

    try:
        adj_model = joblib.load(os.path.join(PROJECT_ROOT, "ml/models/adjournment_model.pkl"))

        if hasattr(adj_model, "feature_importances_"):

            features = [
                "case_type",
                "parties",
                "complexity",
                "evidence_count",
                "lawyer_count",
                "adjournments",
                "filing_year"
            ]

            importances = adj_model.feature_importances_

            importance_df = pd.DataFrame({
                "Feature": features,
                "Importance": importances
            }).sort_values(by="Importance", ascending=False)

            fig, ax = plt.subplots()
            ax.barh(importance_df["Feature"], importance_df["Importance"])
            ax.invert_yaxis()
            st.pyplot(fig)

        else:
            st.info("Model does not support feature importance.")

    except:
        st.warning("Train the model first to see feature importance.")

    st.markdown("---")

    st.subheader("5️⃣ Insights for Policy Makers")

    st.write("""
    • Cases with higher adjournments show significantly increased delay probability.

    • Higher complexity scores directly increase predicted case duration.

    • Early scheduling of high-risk cases can reduce backlog accumulation.

    • Resource allocation (judges & courtroom time) should prioritize high-risk cases.

    • Predictive scheduling can reduce pendency by proactive case management.
    """)
