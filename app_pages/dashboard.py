import streamlit as st
import pandas as pd

def show_dashboard():

    st.markdown("""
                <style>
                .stApp {
                    background-color: #2B2B2B;
                }

                /* Main Heading */
                .main-title {
                    font-size: 42px;
                    font-weight: 700;
                    color: #B3B3B3;
                    margin-bottom: 5px;
                }

                /* Sub Heading */
                .subtitle {
                    font-size: 20px;
                    color: #B3B3B3;
                    margin-bottom: 30px;
                }

                /* Metric Card */
                .metric-card {
                    background-color: #B3B3B3;
                    padding: 20px;
                    border-radius: 12px;
                    text-align: center;
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
                }

                .metric-value {
                    font-size: 28px;
                    font-weight: 700;
                    color: #2B2B2B;
                }

                .metric-label {
                    font-size: 16px;
                    color: #2B2B2B;
                }
                </style>
                """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Overview of judicial workflow metrics</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown("""
                  <div class="metric-card">
                  <div class="metric-value">6,000</div>
                  <div class="metric-label">Total Cases</div>
                  </div>""", unsafe_allow_html=True)

    col2.markdown("""
                  <div class="metric-card">
                  <div class="metric-value">4,280</div>
                  <div class="metric-label">Active Cases</div>
                  </div>""", unsafe_allow_html=True)

    col3.markdown("""
                  <div class="metric-card">
                  <div class="metric-value">1,320</div>
                  <div class="metric-label">High Risk Cases</div>
                  </div>""", unsafe_allow_html=True)

    col4.markdown("""
                  <div class="metric-card">
                  <div class="metric-value">400</div>
                  <div class="metric-label">Completed Cases</div>
                  </div>""", unsafe_allow_html=True)

    st.divider()

    colA, colB = st.columns(2)

    with colA:
        st.subheader("Case Completion Trend")

        data = pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "Cases": [120, 190, 150, 220, 180, 250]
        })

        st.bar_chart(data.set_index("Month"))

    with colB:
        st.subheader("Judge Workload Distribution")

        judge_data = pd.DataFrame({
            "Judge": ["Justice Sharma", "Justice Patel", "Justice Kumar", "Justice Singh"],
            "Cases": [120, 80, 200, 95]
        })

        st.bar_chart(judge_data.set_index("Judge"))
