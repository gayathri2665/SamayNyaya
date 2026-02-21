import streamlit as st
import plotly.graph_objects as go
import numpy as np


def show_judge_assistant():

    # ---------------- PAGE STYLE ----------------
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #232526, #414345);
        color: white;
    }

    h1, h2, h3 {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- TITLE ----------------
    st.title("Policy Simulator")

    st.write("Simulate judicial policy decisions and visualize backlog reduction.")

    st.divider()

    # ---------------- SLIDER ----------------
    slider_value = st.slider(
        "Shift % Civil Cases to Mediation",
        min_value=0,
        max_value=50,
        value=20
    )

    # ---------------- AI RECOMMENDATION ----------------
    st.subheader("AI Recommendation")

    if slider_value < 15:
        st.warning("⚠️ Low impact policy. Consider increasing mediation diversion.")
    elif slider_value < 30:
        st.info("✅ Moderate backlog reduction expected.")
    else:
        st.success("🚀 High impact policy. Strongly recommended.")

    st.divider()

    # ---------------- METRICS ----------------
    st.subheader("Policy Impact Metrics")

    col1, col2, col3 = st.columns(3)

    cases_diverted = slider_value * 1200
    judge_hours_saved = slider_value * 85
    efficiency_gain = slider_value * 0.8

    col1.metric("Cases Diverted", f"{cases_diverted:,}")
    col2.metric("Judge Hours Saved", f"{judge_hours_saved:,}")
    col3.metric("Efficiency Gain", f"{efficiency_gain:.1f}%")

    st.divider()

    # ---------------- EFFECTIVENESS SCORE ----------------
    st.subheader("Policy Effectiveness Score")

    score = min(100, slider_value * 3)

    st.progress(score / 100)

    st.metric("Effectiveness Score", f"{score}/100")

    st.divider()

    # ---------------- BACKLOG PROJECTION ----------------
    st.subheader("Backlog Projection (12 Months)")

    months = np.arange(0, 12)

    current_backlog = 100

    reduction_rate = slider_value * 0.5

    projected_backlog = current_backlog - (months * reduction_rate)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=months,
        y=[current_backlog] * len(months),
        name="Without Policy",
        line=dict(color="red", dash="dash")
    ))

    fig.add_trace(go.Scatter(
        x=months,
        y=projected_backlog,
        name="With Policy",
        line=dict(color="green", width=3)
    ))

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Months",
        yaxis_title="Backlog Index",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ---------------- JUDGE WORKLOAD ----------------
    st.subheader("Judge Workload Reduction")

    judges = [
        "Justice Rao",
        "Justice Mehra",
        "Justice Iyer",
        "Justice Kapoor"
    ]

    before = [85, 78, 92, 88]

    after = [max(10, j - slider_value * 0.5) for j in before]

    fig2 = go.Figure()

    fig2.add_trace(go.Bar(
        name="Before Policy",
        x=judges,
        y=before,
        marker_color="indianred"
    ))

    fig2.add_trace(go.Bar(
        name="After Policy",
        x=judges,
        y=after,
        marker_color="seagreen"
    ))

    fig2.update_layout(
        template="plotly_dark",
        barmode="group",
        height=400
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # ---------------- FINAL AI INSIGHT ----------------
    st.subheader("AI Insight")

    reduction_percent = slider_value * 0.5

    st.success(
        f"This policy could reduce backlog by approximately "
        f"{reduction_percent:.1f}% over the next 12 months and improve judicial efficiency."
    )
