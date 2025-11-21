import streamlit as st
import pandas as pd
import time
import random
import os

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Scientific Career Guidance",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. NUCLEAR CSS (Premium UI + Dark Mode Fix) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* --- GLOBAL VARIABLES --- */
    :root {
        --primary: #0077B6;
        --primary-dark: #023E8A;
        --text-main: #0F172A;
        --bg-light: #F4F9FD;
        --gold: #D97706;
    }

    /* --- FORCE LIGHT MODE (The Nuclear Fix) --- */
    [data-testid="stAppViewContainer"], .stApp, header, footer {
        background-color: var(--bg-light) !important;
        color: var(--text-main) !important;
    }
    
    /* Typography Fixes */
    h1, h2, h3, h4, p, div, span, label, li {
        color: var(--text-main) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        -webkit-text-fill-color: var(--text-main) !important;
    }
    h1, h2, h3 { font-family: 'Outfit', sans-serif !important; color: #003366 !important; -webkit-text-fill-color: #003366 !important; }

    /* Fix Inputs & Inputs in Dark Mode */
    input, textarea, select, div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #CBD5E1 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* Premium Cards */
    .d-card {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03) !important;
        margin-bottom: 1rem !important;
    }
    
    /* Gold Premium Card */
    .gold-card {
        background: linear-gradient(135deg, #FFFBEB 0%, #FFFFFF 100%) !important;
        border: 1px solid #FCD34D !important;
        border-left: 5px solid #D97706 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        margin-bottom: 1rem !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0077B6 0%, #00B4D8 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        -webkit-text-fill-color: white !important;
        box-shadow: 0 4px 15px rgba(0, 119, 182, 0.3) !important;
    }
    
    /* Mobile Fixes */
    @media (max-width: 768px) {
        .block-container { padding-top: 1rem !important; padding-bottom: 5rem !important; }
        h1 { font-size: 2rem !important; }
        section[data-testid="stSidebar"] { display: none; }
        div[data-testid="stHorizontalBlock"] { display: none !important; } /* Hide Desktop Nav */
    }
    
    /* Layout Fix */
    .block-container {
        max-width: 1200px !important; /* Final width fix */
        padding-left: 5rem;
        padding-right: 5rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA & STATE ---
@st.cache_data
def load_data():
    return pd.DataFrame([
        {"name": "Amity Online", "fees": 350000, "type": "Distoversity Analyst", "badge": "Top Ranked"},
        {"name": "Manipal Jaipur", "fees": 175000, "type": "Distoversity Creator", "badge": "NAAC A+"},
        {"name": "LPU Online", "fees": 160000, "type": "Distoversity Catalyst", "badge": "Affordable"},
        {"name": "NMIMS", "fees": 400000, "type": "Distoversity Influencer", "badge": "Premium"},
        {"name": "Jain University", "fees": 210000, "type": "Distoversity Influencer", "badge": "Placement Focus"}
    ])

df = load_data()

if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'lead_captured' not in st.session_state: st.session_state.lead_captured = False
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'messages' not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Hi! I am Eduveer. I can guide you to the right career path."}]

# --- 4. NAVIGATION & HELPER FUNCTIONS ---

def desktop_navbar():
    # Final Desktop Nav (Visible only on desktop)
    with st.container():
        c1, c2, c3, c4, c5, c6, c7 = st.columns([2, 1, 1, 1, 1, 1, 1])
        with c1:
            st.markdown("<h3 style='margin:0; padding:0;'>Distoversity<span style='color:#00B4D8'>.</span></h3>", unsafe_allow_html=True)
        
        # Desktop Buttons
        if c2.button("Home"): st.session_state.page = "Home"; st.rerun()
        if c3.button("About"): st.session_state.page = "About"; st.rerun()
        if c4.button("4D Quiz"): st.session_state.page = "Assessment"; st.rerun()
        if c5.button("Courses"): st.session_state.page = "Explorer"; st.rerun()
        if c6.button("Bot"): st.session_state.page = "Eduveer"; st.rerun()
        if c7.button("FAQ"): st.session_state.page = "FAQ"; st.rerun()
    st.markdown("---")

def mobile_bottom_nav():
    # Sticky Bottom Nav (Mobile)
    st.markdown("""
    <div style="position:fixed; bottom:0; left:0; width:100%; background:white; border-top:1px solid #E2E8F0; padding:10px 0; z-index:
