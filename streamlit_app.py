import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Empowering India",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FORCE LIGHT THEME CSS ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"], .stApp, header, footer {
        background-color: #F4F9FD !important;
        color: #0F172A !important;
    }
    section[data-testid="stSidebar"] > div {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0;
    }
    h1, h2, h3, h4, h5, h6, p, span, div, label, li {
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
    }
    h1, h2, h3 {
        color: #003366 !important;
        -webkit-text-fill-color: #003366 !important;
    }
    input, textarea, select, div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 1px solid #CBD5E1 !important;
    }
    .d-card, .story-card, div[data-testid="stExpander"], .stMarkdown {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
    }
    button { color: #FFFFFF !important; -webkit-text-fill-color: #FFFFFF !important; }
    a { color: #0077B6 !important; -webkit-text-fill-color: #0077B6 !important; }
    .footer-note { font-size:0.9rem; color:#475569 !important; text-align:center; margin-top:20px; }
    </style>
""", unsafe_allow_html=True)

# --- UNIVERSITY & QUIZ DATA ---
UNIVERSITIES = [
    {"name": "Amity Online", "programs": ["MBA", "MCA"], "fee": "₹1.75L", "badges": ["UGC", "NAAC A+"], "best_for": ["Analyst"], "high_pkg": "₹18 LPA"},
    {"name": "Manipal Jaipur", "programs": ["MBA", "BCA"], "fee": "₹1.50L", "badges": ["AICTE", "NAAC A+"], "best_for": ["Creator"], "high_pkg": "₹14 LPA"},
    {"name": "LPU Online", "programs": ["MBA", "BA"], "fee": "₹98k", "badges": ["UGC", "AICTE"], "best_for": ["Catalyst"], "high_pkg": "₹12 LPA"},
    {"name": "NMIMS Global", "programs": ["MBA (Ex)"], "fee": "₹4.0L", "badges": ["Top Ranked"], "best_for": ["Influencer"], "high_pkg": "₹24 LPA"}
]
QUESTIONS = [
    {"q": "When solving problems, you prefer:", "options": [("💡 Innovation", "Creator"), ("🗣️ Discussion", "Influencer"), ("📊 Data", "Analyst"), ("⚡ Action", "Catalyst")]},
    {"q": "Your ideal workspace:", "options": [("🎨 Studio", "Creator"), ("📢 Boardroom", "Influencer"), ("💻 Lab", "Analyst"), ("🏗️ Field", "Catalyst")]},
    {"q": "What motivates you?", "options": [("🚀 Creating", "Creator"), ("🤝 Connecting", "Influencer"), ("🔍 Analyzing", "Analyst"), ("✅ Doing", "Catalyst")]}
]
PROFILE_DESCRIPTIONS = {
    "Creator": "New ideas, product design, brand building. Best: Innovator/Entrepreneur.",
    "Influencer": "Guides teams, motivates people. Best: PR, HR, Sales, Media.",
    "Catalyst": "Gets work finished fast & right. Best: Operations, Logistics, Execution.",
    "Analyst": "Loves data, research, finance. Best: Data Scientist, Finance, Engineering."
}

# --- SESSION STATE ---
if "step" not in st.session_state: st.session_state.step = 0
if "q_index" not in st.session_state: st.session_state.q_index = 0
if "scores" not in st.session_state: st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("Founder | Ed-Tech Intrapreneur")
    st.caption("📍 New Delhi, India")
    st.success("🎯 Mission: Replace 'Sales' in education with 'Science'")
    st.markdown("---")
    st.markdown("<b>Privacy Policy:</b> Hamara data confidential hai, koi third-party ko nahi dete.", unsafe_allow_html=True)
    st.markdown("<b>Copyright © 2025 Distoversity. All rights reserved.</b>", unsafe_allow_html=True)

# --- MAIN CONTENT ---
st.markdown("<h1 style='text-align:center;'>Distoversity MVP</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h2>", unsafe_allow_html=True)

tabs = st.tabs(["Story & Mission", "Genius Assessment", "Your Profile & Match"])

# --- TAB 1: STORY ---
with tabs[0]:
    st.header("From Factory Floor to Career Architect 🚀")
    st.markdown("""
    <div class="story-card">
        <div>2018-2020: 🏭 Oppo Mobile & Yazaki: Factory se shuruat hui, samjha ki youth ko guidance chahiye.</div>
        <div>2021-2024: 📞 Sales Trap: Students 'lead' ban gaye, sapne kho gaye. Counseling mein ethics ki kami dikhi.</div>
        <div>2024-Present: 🚀 Distoversity: Psychology + Tech = Career Architecture. Mission: Empowering India!</div>
    </div>""", unsafe_allow_html=True)

# --- TAB 2: ASSESSMENT ---
with tabs[1]:
    st.header("Genius Assessment: Find Your Core Strength")
    if st.session_state.step == 0:
        if st.button("Start Assessment ➔", type="primary"):
            st.session_state.step = 1
            st.rerun()
    elif st.session_state.step == 1:
        curr = QUESTIONS[st.session_state.q_index]
        st.markdown(f"**Q{st.session_state.q_index + 1}:** {curr['q']}")
        cols = st.columns(2)
        for i, (txt, en) in enumerate(curr["options"]):
            if cols[i%2].button(txt, key=f"btn_{i}_{st.session_state.q_index}"):
                st.session_state.scores[en] += 1
                if st.session_state.q_index < len(QUESTIONS)-1:
                    st.session_state.q_index += 1
                else:
                    st.session_state.step = 2
                st.rerun()
    elif st.session_state.step == 2:
        primary = max(st.session_state.scores, key=st.session_state.scores.get)
        st.success(f"🎉 Your Genius Profile: {primary}")
        st.write(PROFILE_DESCRIPTIONS[primary])

# --- TAB 3: PROFILE & MATCH ---
with tabs[2]:
    if st.session_state.step < 2:
        st.info("Please complete the assessment first!")
    else:
        primary = max(st.session_state.scores, key=st.session_state.scores.get)
        st.header(f"Your Genius Profile: {primary}")
        st.write(PROFILE_DESCRIPTIONS[primary])
        st.subheader("Matching Universities:")
        matches = [u for u in UNIVERSITIES if primary in u["best_for"]]
        for u in matches:
            st.markdown(f"""
            <div style="padding:15px; border:1px solid #ddd; border-radius:10px; margin-bottom:10px;">
                <h4>{u['name']}</h4>
                <p><b>Programs:</b> {', '.join(u['programs'])} | <b>Fee:</b> {u['fee']} | <b>Highest:</b> {u['high_pkg']}</p>
            </div>
            """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer-note">
<b>EMPOWERING INDIA 🇮🇳</b> <br>
<b>Privacy Policy:</b> Sab data confidential hai, kisi third-party ko share nahi hota.<br>
<b>Copyright © 2025 Distoversity. All rights reserved.</b>
</div>
""", unsafe_allow_html=True)
