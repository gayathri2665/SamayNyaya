import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from ml.predict import predict_case
import random

# -----------------------------
# SAFE SESSION INITIALIZATION (FIXED)
# -----------------------------
if "hearings" not in st.session_state:
    st.session_state.hearings = []

# -----------------------------
# MOCK JUDGE DATABASE
# -----------------------------
JUDGES = [
    {"name": "Hon. Justice Rao", "expertise": "civil", "workload": 70},
    {"name": "Hon. Justice Mehra", "expertise": "criminal", "workload": 50},
    {"name": "Hon. Justice Iyer", "expertise": "commercial", "workload": 40},
    {"name": "Hon. Justice Kapoor", "expertise": "civil", "workload": 60},
]

# -----------------------------
# Priority Logic
# -----------------------------
def assign_priority(adj_prob):
    if adj_prob > 0.7:
        return "High"
    elif adj_prob > 0.4:
        return "Medium"
    else:
        return "Low"

# -----------------------------
# Judge Allocation Logic
# -----------------------------
def assign_judge(case_type):

    eligible = [j for j in JUDGES if j["expertise"] == case_type]

    if not eligible:
        eligible = JUDGES

    judge = min(eligible, key=lambda x: x["workload"])

    return judge["name"]

# -----------------------------
# Auto Scheduling Logic
# -----------------------------
def auto_schedule(case_id, case_type, duration, priority, adj_prob):

    base_date = datetime.today().date()

    if priority == "High":
        hearing_date = base_date
    elif priority == "Medium":
        hearing_date = base_date + timedelta(days=1)
    else:
        hearing_date = base_date + timedelta(days=2)

    judge = assign_judge(case_type)

    hearing = {
        "case_id": case_id,
        "date": hearing_date.strftime("%d/%m/%Y"),
        "time": "10:00 AM",
        "duration": duration,
        "priority": priority,
        "delay_prob": round(adj_prob * 100, 2),
        "judge": judge
    }

    st.session_state.hearings.append(hearing)

# -----------------------------
# Judge Reallocation Logic
# -----------------------------
def reassign_judge(current_judge):

    alternatives = [j["name"] for j in JUDGES if j["name"] != current_judge]

    return random.choice(alternatives)

# -----------------------------
# MAIN PAGE
# -----------------------------
def show_scheduling():

    st.markdown("""
                <style>
                .stApp {
                    background-color: #2B2B2B;
                }
                </style>
                """, unsafe_allow_html=True)

    st.title("Hearing Schedule")
    st.caption("AI Optimized Scheduling System")

    st.subheader("Schedule New Case")

    col1, col2 = st.columns(2)

    with col1:
        case_id = st.text_input("Case ID", "CASE-2024-001")
        case_type = st.selectbox("Case Type", ["civil", "criminal", "commercial"])
        parties = st.number_input("Parties", 1, 20)
        adjournments = st.number_input("Adjournments", 0, 50)
        evidence_count = st.number_input("Evidence Count", 0, 100)

    with col2:
        lawyer_count = st.number_input("Lawyer Count", 0, 10)
        filing_year = st.number_input("Filing Year", 2015, 2025)
        complexity = st.slider("Complexity Score", 1, 10, 5)

    if st.button("Auto Schedule Case"):

        duration, adj_prob = predict_case(
            case_type,
            parties,
            complexity,
            evidence_count,
            lawyer_count,
            adjournments,
            filing_year
        )

        priority = assign_priority(adj_prob)

        auto_schedule(
            case_id,
            case_type,
            int(duration),
            priority,
            adj_prob
        )

        st.success("Case Scheduled Successfully!")

    st.divider()

    # DISPLAY SCHEDULE
    if st.session_state.hearings:

        df = pd.DataFrame(st.session_state.hearings)
        grouped = df.groupby("date")

        col_main, col_side = st.columns([3, 1])

        with col_main:

            for date, group in grouped:

                st.subheader(f"📅 {date}")

                for index, row in group.iterrows():

                    with st.expander(f"{row['case_id']} | {row['duration']} min"):

                        st.write("Status: Scheduled")
                        st.write(f"Time: {row['time']}")
                        st.write(f"Judge: {row['judge']}")
                        st.write(f"Priority: {row['priority']}")
                        st.write(f"Delay Risk: {row['delay_prob']}%")

                        st.divider()

                        reason = st.selectbox(
                            f"Request Reallocation ({row['case_id']})",
                            [
                                "No Request",
                                "Conflict of Interest",
                                "Bias Concern",
                                "Scheduling Conflict",
                                "Other"
                            ],
                            key=f"reason_{index}"
                        )

                        if reason != "No Request":

                            if st.button(
                                f"Confirm Reallocation {row['case_id']}",
                                key=f"btn_{index}"
                            ):

                                new_judge = reassign_judge(row["judge"])

                                st.session_state.hearings[index]["judge"] = new_judge

                                st.success(
                                    f"Judge reassigned to {new_judge}"
                                )

        with col_side:

            st.subheader("Priority Legend")
            st.write("🔴 High Priority")
            st.write("🟡 Medium Priority")
            st.write("🟢 Low Priority")

            st.divider()

            total = len(df)
            avg_duration = int(df["duration"].mean())
            avg_delay = round(df["delay_prob"].mean(), 2)

            st.subheader("Schedule Statistics")
            st.metric("Total Hearings", total)
            st.metric("Avg Duration (min)", avg_duration)
            st.metric("Avg Delay Risk (%)", avg_delay)

    else:
        st.info("No hearings scheduled yet.")