import streamlit as st
import pandas as pd
import plotly.express as px

def show_home():

    # Ensure popup state exists
    if "popup" not in st.session_state:
        st.session_state.popup = None

    # ---------------- CSS ---------------- #

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        color: #2B2B2B !important;
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricValue"],
    [data-testid="stMetricDelta"] {
        color: #2B2B2B !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #2B2B2B !important;
    }

    .stApp {
        background-color: #E0E0E0;
    }

    .top-nav {
        position: absolute;
        right: 80px;
        font-size: 18px;
        font-weight: 500;
    }

    .top-nav span {
        margin-left: 20px;
        cursor: pointer;
        background-color: #2B2B2B;
        color: white !important;
        padding: 10px 22px;
        border-radius: 8px;
        display: inline-block;
        transition: 0.3s;
    }

    .main-container {
        text-align: center;
        margin-top: 120px;
        margin-bottom: 60px;
    }

    .title {
        font-size: 72px;
        font-weight: 700;
        color: #722F37;
    }

    .tagline {
        font-size: 22px;
        color: #722F37;
        margin-bottom: 50px;
    }

    div.stButton > button {
        background-color: #2B2B2B;
        color: white !important;
        width: 220px;
        height: 55px;
        font-size: 18px;
        border-radius: 8px;
        margin-top: 20px;
        padding: 22px 22px;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #B3B3B3 !important;
        color: #2B2B2B !important;
    }

    div.stButton > button:active,
    div.stButton > button:focus {
        background-color: #2B2B2B !important;
        color: #FFFFFF !important;
        box-shadow: none !important;
        outline: none !important;
    }

    .section-card {
        background-color: #A58570;
        padding: 40px;
        border-radius: 20px;
        margin-bottom: 40px;
    }

    hr {
        border: none;
        height: 3px;
        background-color: #2B2B2B;
        margin-top: 65px;
        margin-bottom: 65px;
    }

    .hero-section {
        position: relative;
        width: 100%;
        height: 500px;
        background-image: url("https://images.unsplash.com/photo-1589829545856-d10d557cf95f");
        background-size: cover;
        background-position: center;
        border-radius: 20px;
        margin-top: 40px;
        overflow: hidden;
    }

    .hero-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.45);
        border-radius: 20px;
    }

    .hero-content {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        color: white;
    }

    .hero-title {
        font-size: 100px;
        font-weight: 500;
    }

    .hero-tagline {
        font-size: 22px;
        margin-top: 20px;
    }

    .popup-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.4);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }

    .popup-card {
        background: rgba(255, 255, 255, 0.9);
        width: 70%;
        max-height: 80%;
        overflow-y: auto;
        padding: 40px;
        border-radius: 20px;
        color: #2B2B2B;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------------- NAV ---------------- #

    col_nav1, col_nav2, space, col_nav3, space, col_nav4, col_nav5 = st.columns([6,1,0.7,1,0.7,1,1])

    with col_nav2:
        if st.button("About"):
            st.session_state.popup = "about"

    with col_nav3:
        if st.button("How It Works"):
            st.session_state.popup = "how"

    with col_nav4:
        if st.button("Contact"):
            st.session_state.popup = "contact"

    # ---------------- HERO ---------------- #

    st.markdown("""
        <div class="hero-section">
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <div class="hero-title">⚖️SamayNyaya</div>
                <div class="hero-tagline">
                    Ensuring Justice Without Delay.<br>
                    AI-powered judicial workflow platform.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        c1, space, c2 = st.columns([1, 0.7, 1])

        with c1:
            if st.button("Sign In"):
                st.session_state.page = "login"
                st.rerun()

        with c2:
            if st.button("Sign Up"):
                st.session_state.page = "signup"
                st.rerun()

        # ---------------- POPUP ---------------- #

        if st.session_state.popup:
            content = ""
            if st.session_state.popup == "about":
                content = """<h2>About SamayNyaya</h2>
                SamayNyaya is an AI-powered judicial workflow optimization platform designed to reduce court delays and improve case-flow efficiency.
                Across judicial systems, case backlogs continue to grow — not due to lack of judges alone, but due to inefficient scheduling, unpredictable case durations, and reactive decision-making."""

            elif st.session_state.popup == "how":
                content = """<h2>How SamayNyaya Works</h2>
                Case Data Analysis: Incoming case details — type, complexity, evidence load, past adjournments — are analyzed using trained machine learning models.
                The system predicts:
                Estimated hearing duration
                Case complexity score
                Delay risk probability"""

            elif st.session_state.popup == "contact":
                content = """<h2>Contact</h2><p>Email: support@samaynyaya.ai</p><p>Phone: +91-XXXXXXXXXX</p>"""

            # Popup overlay
            st.markdown(f"""
            <div class="popup-overlay">
                <div class="popup-card">
                    {content}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # --- Back button inside the popup ---
            if st.button("← Back to Home"):
                st.session_state.popup = None  # clears popup
                st.experimental_rerun()        # refreshes page to show home

    # ---------------- DASHBOARD TITLE ---------------- #

    st.divider()

    st.markdown("""
        <div style='text-align:center;
                    font-size:42px;
                    font-weight:700;
                    color:#2B2B2B;
                    margin-bottom:40px;'>
             Judicial Intelligence Dashboard
        </div>
    """, unsafe_allow_html=True)

    # ---------------- DATA ---------------- #

    total_civil = 11141266
    total_criminal = 37338483
    total_cases = 48479749
    pre_litigation = 1297653

    civil_gt_1yr = 7892074
    criminal_gt_1yr = 27351361

    st.markdown("###  Overall Case Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("⚖️ Civil Cases", f"{total_civil:,}")
    col2.metric(" Criminal Cases", f"{total_criminal:,}")
    col3.metric(" Total Cases", f"{total_cases:,}")
    col4.metric(" Pre-Litigation", f"{pre_litigation:,}")

    st.divider()

    st.markdown("###  Cases Older Than 1 Year")

    col5, col6 = st.columns(2)

    col5.metric("Civil > 1 Year", f"{civil_gt_1yr:,}")
    col5.progress(0.708)

    col6.metric("Criminal > 1 Year", f"{criminal_gt_1yr:,}")
    col6.progress(0.732)

    st.divider()

    st.markdown("###  Age-wise Pending Cases")

    data = pd.DataFrame({
        "Age Group": ["<1 Year", "1-3 Years", "3-5 Years", "5-10 Years", ">10 Years"],
        "Civil (%)": [25, 25, 23, 20, 7],
        "Criminal (%)": [75, 75, 77, 80, 93]
    })

    fig = px.bar(
        data,
        x="Age Group",
        y=["Civil (%)", "Criminal (%)"],
        barmode="group",
        color_discrete_sequence=["#AC746C", "#3D0A05"]
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)