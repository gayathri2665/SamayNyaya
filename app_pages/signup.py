import streamlit as st

def show_signup():

    st.markdown("""
    <style>

    /* Same Background */
    .stApp {
        background-color:  #E0E0E0;
    }

    /* Center card */
    .signup-container {
        display: flex;
        justify-content: center;
        margin-top: 130px;
    }

    .signup-title {
        text-align: center;
        font-size: 40px;
        font-weight: 600;
        color:#2B2B2B;
        margin-bottom: 30px;
    }

    /* Inputs*/
    .stTextInput {
        width: 420px;
        margin: 0 auto 18px auto;
    }

    .stTextInput label {
        display: block !important;
        text-align: left;
        margin-bottom: 6px;
        color:#2B2B2B !important;
        width: 420;
        font-weight: 600;
        font-size: 15px;
    }

    .stTextInput > div {
        display: flex;
        justify-content: center;
    }
    
    .stTextInput > div > div {
        width: 100%;
        max-width: 420px;
    }

    /* Force ALL input container layers */
    div[data-baseweb="input"],
    div[data-baseweb="input"] > div {
        background-color: #2B2B2B !important;
        border-radius: 6px !important;
        border: 1px solid #2B2B2B !important;
    }

    /* Focus + hover states */
    div[data-baseweb="input"]:focus-within,
    div[data-baseweb="input"]:hover,
    div[data-baseweb="input"][data-focus="true"] {
        background-color: #2B2B2B !important;
        border: 1px solid #2B2B2B !important;
        box-shadow: none !important;
    }

    /* Actual text input */
    div[data-baseweb="input"] input {
        background-color: #2B2B2B !important;
        color: white !important;
        caret-color: white !important;
        font-size: 16px !important;
        outline: none !important;
        box-shadow: none !important;
    }

    /* Override Chrome autofill COMPLETELY */
    input:-webkit-autofill,
    input:-webkit-autofill:focus,
    input:-webkit-autofill:hover,
    input:-webkit-autofill:active {
        -webkit-box-shadow: 0 0 0 1000px #2B2B2B inset !important;
        -webkit-text-fill-color: #2B2B2B !important;
        caret-color: #2B2B2B !important;
        border: 1px solid #2B2B2B !important;
    }

    /* Password eye button (BaseWeb icon wrapper) */
    div[data-baseweb="input"] button,
    div[data-baseweb="input"] button:hover,
    div[data-baseweb="input"] button:focus {
        background-color:#E0E0E0 !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* SVG icon color */
    div[data-baseweb="input"] svg {
        fill: #2B2B2B !important;
    }
    
    /* Button styling */
    div.stButton {
        display: flex;
        justify-content: center;
    }
    div.stButton > button {
        background-color: #2B2B2B;
        align-items: center;
        justify-content: center;
        color: white;
        width: 500px;
        height: 48px;
        font-size: 16px;
        border-radius: 6px;
        border: none;
        font-weight: 500;
        margin-top: 15px;
        transition: all 0.2s ease-in-out;
    }

    div.stButton > button:hover {
        background-color: #2B2B2B;
        color: white;
        transform: translateY(-2px);
    }
    
    /* ===== NAVBAR ===== */
    .navbar {
        width: 100%;
        height: 60px;
        background-color: #2B2B2B;
        display: flex;
        align-items: center;
        padding-left: 25px;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 999;
    }

    /* Back link style */
    .back-link {
        color: #2B2B2B;
        text-decoration: none;
        font-size: 18px;
        font-weight: 600;
        transition: 0.2s ease;
    }

    .back-link:hover {
        color:#2B2B2B;
    }

    /* Push page content below navbar */
    .page-content {
        margin-top: 80px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---- TOP LEFT BACK BUTTON ----
    col1, col2 = st.columns([1, 8])

    with col1:
        if st.button("← Back"):
            st.session_state.page = "home"
            st.rerun()

    st.markdown('<div class="signup-title">Create Account</div>', unsafe_allow_html=True)

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password != confirm:
            st.error("Passwords do not match")
        elif name and email and password:
            st.success("Account created. Please login.")
        else:
            st.warning("Fill all fields")

    st.markdown('</div></div>', unsafe_allow_html=True)