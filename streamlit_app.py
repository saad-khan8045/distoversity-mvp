import streamlit as st
import pandas as pd
import time
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Empowering India",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FORCE LIGHT THEME CSS (NUCLEAR OPTION) ---
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
    .stChatMessage[data-testid="user-message"] {
        background-color: #E0F2FE !important;
        color: #000000 !important;
    }
    .stChatMessage[data-testid="assistant-message"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #E2E8F0 !important;
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
    "Creator": "Innovative, big-picture, loves launching ideas. Best fit: Product Designer, Brand Builder, Strategy.",
    "Influencer": "Natural leader, communicator, energizes teams. Best fit: PR, HR, Client Relations, Media.",
    "Catalyst": "Efficient, action-oriented, gets results. Best fit: Ops Manager, Logistics, Project Execution.",
    "Analyst": "Precise, data-driven, solves puzzles. Best fit: Finance, Data, Engineering."
}
# --- SESSION STATE ---
if "messages" not in st.session_state: st.session_state.messages = []
if "step" not in st.session_state: st.session_state.step = 0
if "q_index" not in st.session_state: st.session_state.q_index = 0
if "scores" not in st.session_state: st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}
if "profile_result" not in st.session_state: st.session_state.profile_result = None

# --- SIDEBAR: BIO, PRIVACY & COPYRIGHT ---
with st.sidebar:
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("Founder | Ed-Tech Intrapreneur")
    st.caption("📍 New Delhi, India")
    st.success("🎯 Mission: To replace 'Sales' in education with 'Science'.")
    st.markdown("### 🛠 Skills")
    st.code("Python & Streamlit")
    st.code("LLM & AI Agents")
    st.code("Franchise Expansion")
    st.code("Ed-Psychology")
    st.markdown("---")
    st.markdown("<b>Privacy Policy:</b> Your data is always safe and confidential. We never sell or share personal information.", unsafe_allow_html=True)
    st.markdown("<b>Copyright © 2025 Distoversity.</b> All rights reserved.", unsafe_allow_html=True)
    st.markdown("[LinkedIn](https://linkedin.com) | [Email](mailto:saad01489@gmail.com)")

# --- MAIN TABS ---
tab1, tab2, tab3 = st.tabs([
    "📖 My Story (The Hook)", 
    "🧠 The 4-Genius Framework", 
    "🤖 Eduveer AI (Live Demo)"
])

# --- TAB 1: STORY ---
with tab1:
    st.header("From Assembly Lines to Assembling Futures 🚀")
    st.markdown("##### *Why I quit a stable job to fix the Education System.*")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.divider()
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        <div class="story-card">
            <div class="story-year">2018 - 2020</div>
            <div class="story-title">🏭 The Factory Floor Reality</div>
            <div class="story-text">
                My journey began at <b>Oppo Mobile & Yazaki</b>, 12-hour shifts as Line Engineer, assembling SMT boards.<br><br>
                <b>Lesson:</b> India has millions of youth with grit but lacking guidance. I felt trapped, assembling products instead of building lives.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="story-card" style="border-left-color: #F97316;">
            <div class="story-year">2021 - 2024</div>
            <div class="story-title">📞 The "Sales" Trap</div>
            <div class="story-text">
                I moved to Education Counseling (Amity/Manipal), helped 2,000+ students. Realized education was transactional, not transformational. Students became "Leads"; counselors closed deals, not dreams.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="story-card" style="border-left-color: #10B981;">
            <div class="story-year">2024 - Present</div>
            <div class="story-title">🚀 Distoversity & Eduveer</div>
            <div class="story-text">
                I chose to build. Distoversity merges <b>Psychology (4-Genius)</b> and <b>Tech (AI)</b>. I don't sell degrees; I architect futures.
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.info("💡 Why TFI?")
        st.markdown("""
        - Grit of a factory worker  
        - Empathy of a counselor  
        - Vision of a founder  
        I want to bring <b>Operations + Tech + Heart</b> to Teach For India.
        """, unsafe_allow_html=True)

# --- TAB 2: FRAMEWORK ---
with tab2:
    st.header("We don't ask for Marks. We ask for Energy.")
    st.write("Distoversity philosophy: You cannot judge a fish by its ability to climb a tree.")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        energy = st.selectbox(
            "Select a Profile to Analyze:", 
            ["Creator", "Influencer", "Catalyst", "Analyst"]
        )
    with c2:
        if energy:
            st.markdown(f"**{energy}:** {PROFILE_DESCRIPTIONS[energy]}")
            if "Creator" == energy: st.success("🌟 Vision-driven. Loves freedom. Struggles with routine.")
            if "Influencer" == energy: st.warning("🔥 People-driven. Needs collaboration. Avoids isolation.")
            if "Catalyst" == energy: st.info("🤝 Results-driven. Needs structure, hates chaos.")
            if "Analyst" == energy: st.error("📊 Data-driven. Needs clarity, hates hype.")

# --- TAB 3: EDUVEER BOT/QUIZ ---
with tab3:
    st.title("🤖 Eduveer AI Demo")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.caption("Logic-based career counselor for every Indian student.")

    if st.session_state.step == 0:
        if st.button("Start AI Assessment ➔", type="primary"):
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
        st.success(f"🎉 Result: You are a {primary}!")
        st.write(PROFILE_DESCRIPTIONS[primary])
        st.write("Universities matching your profile:")
        matches = [u for u in UNIVERSITIES if primary in u["best_for"]]
        for u in matches:
            st.markdown(f"""
            <div style="padding:15px; border:1px solid #ddd; border-radius:10px; margin-bottom:10px;">
                <h4>{u['name']}</h4>
                <p><b>Programs:</b> {', '.join(u['programs'])} | <b>Fee:</b> {u['fee']} | <b>Highest Pkg:</b> {u['high_pkg']}</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Restart Demo"):
            st.session_state.step = 0
            st.session_state.q_index = 0
            st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}
            st.rerun()

# --- FOOTER: PRIVACY & COPYRIGHT ---
st.markdown("""
<div class="footer-note">
<b>EMPOWERING INDIA 🇮🇳</b><br>
<b>Privacy Policy:</b> We do NOT collect, share, or sell your personal data. All information is confidential.<br>
<b>Copyright © 2025 Distoversity. All rights reserved.</b>
</div>
""", unsafe_allow_html=True)
