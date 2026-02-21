import streamlit as st
from ml.predict import predict_case

def show_case_management():

    st.markdown("""
                <style>
                .stApp {
                    background-color: #2B2B2B;
                }
                </style>
                """, unsafe_allow_html=True)

    st.title("Case Management")
    st.subheader("Enter Case Details")

    col1, col2 = st.columns(2)

    with col1:
        case_type = st.selectbox("Case Type", ["civil", "criminal", "commercial"])
        parties = st.number_input("Number of Parties", 1, 20)
        adjournments = st.number_input("Adjournments", 0, 50)
        evidence_count = st.number_input("Evidence Count", 0, 100)

    with col2:
        lawyer_count = st.number_input("Lawyer Count", 0, 10)
        filing_year = st.number_input("Filing Year", 2015, 2025)
        complexity = st.slider("Complexity Score", 1, 10, 5)

    if st.button("Analyze Case"):

        duration, adj_prob = predict_case(
            case_type,
            parties,
            complexity,
            evidence_count,
            lawyer_count,
            adjournments,
            filing_year
        )

        st.success(f"📅 Predicted Duration: {int(duration)} days")
        st.info(f"⚖ Adjournment Probability: {round(adj_prob * 100, 2)}%")

        if adj_prob > 0.6:
            st.warning("⚠ High Risk of Adjournment.")