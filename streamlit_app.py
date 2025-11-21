import streamlit as st
import pandas as pd
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
    "Creator": "Naye ideas, product design, brand building. (Best careers: Innovator/Entrepreneur)",
    "Influencer": "Logon ko guide karna, team motivate karna. (Best: PR, HR, Sales, Media)",
    "Catalyst": "Kaam ko jaldi aur sahi finish karna. (Best: Operations, Logistics, Project Manager)",
    "Analyst": "Data, problem solve karna, finance. (Best: Finance, Engineering, Data Science)"
}
if "messages" not in st.session_state: st.session_state.messages = []
if "step" not in st.session_state: st.session_state.step = 0
if "q_index" not in st.session_state: st.session_state.q_index = 0
if "scores" not in st.session_state: st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}
if "profile_result" not in st.session_state: st.session_state.profile_result = None

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("Founder | Ed-Tech Intrapreneur")
    st.caption("📍 New Delhi, India")
    st.success("🎯 Mission: Replace 'Sales' in education with 'Science'")
    st.markdown("### 🛠 Skills")
    st.code("Python & Streamlit")
    st.code("LLM & AI Agents")
    st.code("Franchise Expansion")
    st.code("Ed-Psychology")
    st.markdown("---")
    st.markdown("<b>Privacy Policy:</b> Hamara data confidential hai, kisi bhi third party ko share nahi hota.", unsafe_allow_html=True)
    st.markdown("<b>Copyright © 2025 Distoversity.</b> All rights reserved.", unsafe_allow_html=True)
    st.markdown("[LinkedIn](https://linkedin.com) | [Email](mailto:saad01489@gmail.com)")

# --- MAIN TABS ---
tab1, tab2, tab3 = st.tabs([
    "📖 Story", 
    "🧠 Genius Framework", 
    "🤖 Eduveer AI Demo"
])

# --- TAB 1: STORY ---
with tab1:
    st.header("From Factory Floor to Career Architect 🚀")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.divider()
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        <div class="story-card">
            <div>2018 - 2020: 🏭 Oppo Mobile & Yazaki</div>
            <div>Naukri ki shuruat ek factory se hui, 12 ghante shifts. Yaha samjha ki youth ko guidance ki kitni zaroorat hai.</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="story-card" style="border-left-color: #F97316;">
            <div>2021 - 2024: 📞 Sales Trap</div>
            <div>Amity/Manipal main 2,000+ students ko counsel kiya. Dekha, education ek transaction ban gayi hai. Students 'Lead' ban gaye, sapne kho gaye.</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="story-card" style="border-left-color: #10B981;">
            <div>2024 - Present: 🚀 Distoversity & Eduveer</div>
            <div>Ed-Tech ko ethical aur logical banana, wahi mission hai. Psychology + Tech = Career Architecture.</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.info("💡 Why TFI?")
        st.markdown("""
        - Factory ka hardwork
        - Counselor ka empathy
        - Founder ka vision
        Ye sab main Teach For India ke liye lana chahta hoon!
        """, unsafe_allow_html=True)

# --- TAB 2: FRAMEWORK ---
with tab2:
    st.header("We don't ask for marks, We map your energy!")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        energy = st.selectbox(
            "Apna Genius Profile dekhein:", 
            ["Creator", "Influencer", "Catalyst", "Analyst"]
        )
    with c2:
        if energy:
            st.markdown(f"**{energy}:** {PROFILE_DESCRIPTIONS[energy]}")
            if "Creator" == energy: st.success("🌟 Naye idea, freedom, routine se pareshaan.")
            if "Influencer" == energy: st.warning("🔥 Log, teamwork, isolation se pareshaan.")
            if "Catalyst" == energy: st.info("🤝 Jaldi result, structure, chaos se pareshaan.")
            if "Analyst" == energy: st.error("📊 Data, research, hype se pareshaan.")

# --- TAB 3: EDUVEER BOT/QUIZ ---
with tab3:
    st.title("Eduveer AI Demo")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.caption("Logic-based career test for every student.")
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
        st.success(f"🎉 Result: Aapka Genius Profile hai: {primary}!")
        st.write(PROFILE_DESCRIPTIONS[primary])
        st.write("Yeh universities aapke profile match karti hain:")
        matches = [u for u in UNIVERSITIES if primary in u["best_for"]]
        for u in matches:
            st.markdown(f"""
            <div style="padding:15px; border:1px solid #ddd; border-radius:10px; margin-bottom:10px;">
                <h4>{u['name']}</h4>
                <p><b>Programs:</b> {', '.join(u['programs'])} | <b>Fee:</b> {u['fee']} | <b>Highest:</b> {u['high_pkg']}</p>
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
<b>EMPOWERING INDIA 🇮🇳</b> <br>
<b>Privacy Policy:</b> Hum data kabhi kisi ko nahi dete, sab confidential hota hai.<br>
<b>Copyright © 2025 Distoversity. All rights reserved.</b>
</div>
""", unsafe_allow_html=True)
