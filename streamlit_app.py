import streamlit as st
import pandas as pd
import time
import random

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

    :root {
        --primary: #0077B6;
        --text-main: #0F172A;
        --bg-light: #F4F9FD;
    }

    /* Force Light Mode */
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

    /* Inputs Fix */
    input, textarea, select, div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 1px solid #CBD5E1 !important;
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

    /* Mobile Nav Styling */
    div[data-testid="stHorizontalBlock"] button {
        background-color: transparent !important;
        border: none !important;
        color: #64748B !important;
        -webkit-text-fill-color: #64748B !important;
    }

    /* Mobile Specifics */
    @media (max-width: 768px) {
        .block-container { padding-top: 1rem !important; padding-bottom: 5rem !important; }
        h1 { font-size: 2rem !important; }
        div[data-testid="stHorizontalBlock"] { display: none !important; } /* Hide Desktop Nav */
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

# --- 4. NAVIGATION FUNCTIONS ---

def desktop_navbar():
    # Visible only on Desktop via CSS
    with st.container():
        c1, c2, c3, c4, c5, c6 = st.columns([2, 1, 1, 1, 1, 1])
        with c1:
            st.markdown("<h3 style='margin:0; padding:0;'>Distoversity<span style='color:#00B4D8'>.</span></h3>", unsafe_allow_html=True)
        
        if c2.button("Home"): st.session_state.page = "Home"; st.rerun()
        if c3.button("About"): st.session_state.page = "About"; st.rerun()
        if c4.button("4D Quiz"): st.session_state.page = "Assessment"; st.rerun()
        if c5.button("Bot"): st.session_state.page = "Eduveer"; st.rerun()
        if c6.button("Courses"): st.session_state.page = "Explorer"; st.rerun()
    st.markdown("---")

def mobile_bottom_nav():
    # Sticky Bottom Nav for Mobile
    st.markdown("""
    <div style="position:fixed; bottom:0; left:0; width:100%; background:white; border-top:1px solid #eee; padding:10px; z-index:9999; display:flex; justify-content:space-around; text-align:center;">
        <a onclick="document.getElementById('home_btn').click()" style="color:#64748B; font-size:0.8rem; text-decoration:none; cursor:pointer;">🏠<br>Home</a>
        <a onclick="document.getElementById('quiz_btn').click()" style="color:#0077B6; font-weight:bold; font-size:0.8rem; text-decoration:none; cursor:pointer;">🧬<br>Quiz</a>
        <a onclick="document.getElementById('bot_btn').click()" style="color:#64748B; font-size:0.8rem; text-decoration:none; cursor:pointer;">🤖<br>Bot</a>
    </div>
    """, unsafe_allow_html=True)

# --- 5. PAGES ---

def render_home():
    st.markdown("""
    <div style="text-align:center; padding: 3rem 0;">
        <span style="background:#E0F2FE; color:#0077B6; padding:6px 16px; border-radius:20px; font-size:0.85rem; font-weight:700; letter-spacing: 1px;">🚫 WARNING: DON'T BE SOLD. BE GUIDED.</span>
        <h1 style="font-size: 3.2rem; line-height:1.1; margin-top:20px; font-weight: 800;">Is Your Career Designed by <span style="color:#0077B6">Science</span>...<br>or a <span style="color:#F97316">Sales Agent?</span></h1>
        <p style="color:#475569; font-size:1.2rem; margin-top:1.5rem; max-width: 700px; margin-left:auto; margin-right:auto;">
            93% of students choose the wrong course because they trust "Free Counselors" who work for commissions.<br>
            <b>Distoversity</b> uses the <b>4-Genius Framework</b> to match your DNA to the Degree.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🧬 Decode My Career DNA (Free)", type="primary", use_container_width=True):
            st.session_state.page = 'Assessment'
            st.rerun()
        st.markdown("<div style='text-align:center; font-size:0.85rem; color:#64748B; margin-top:8px;'>✅ 98% Accuracy • ⏱️ Takes 2 Minutes • 🔒 Private</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:bold; color:#94A3B8; letter-spacing:1px;'>WE GUIDE STUDENTS TO TOP UNIVERSITIES</p>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.info("AMITY")
    c2.info("MANIPAL")
    c3.info("NMIMS")
    c4.info("LPU")

    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Meet the Founder ➔"):
            st.session_state.page = "About"
            st.rerun()

def render_about():
    st.markdown("<h2 style='text-align:center;'>The Man Who Rejected the 'System'</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748B;'>From the factory floor to fixing education.</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c2:
        st.markdown("""
        <div class="d-card" style="border-left: 5px solid #F97316 !important;">
            <h3>🏭 2019: The Factory Floor</h3>
            <p>My career didn't start in a boardroom. It started at <b>Oppo & Yazaki</b>. 
            I worked <b>12-hour shifts</b>. I saw hardworking Indians working like machines simply because they lacked <b>Guidance</b>.</p>
        </div>
        <div class="d-card" style="border-left: 5px solid #0077B6 !important;">
            <h3>📞 2021: The Sales Trap</h3>
            <p>I moved to Education Counseling (Amity). I spoke to <b>2,000+ students</b>. 
            But I realized: <b>"Education is being sold, not served."</b> Counselors were pushing commissions, not careers.</p>
        </div>
        <div class="d-card" style="border-left: 5px solid #10B981 !important;">
            <h3>🧬 2024: The Birth of Distoversity</h3>
            <p>I built a platform that uses <b>Data & Psychology</b> (The 4-Genius Framework), not sales tactics.</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("See How My Logic Works ➔", type="primary", use_container_width=True):
        st.session_state.page = "Assessment"
        st.rerun()

def render_assessment():
    st.markdown("<h2 style='text-align:center;'>🧠 The 4-Genius Energy Analysis</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748B;'>Stop forcing yourself into careers that don't fit.</p>", unsafe_allow_html=True)
    
    with st.form("quiz"):
        st.markdown("### 1. When a problem arises, your FIRST instinct?")
        q1 = st.radio("q1", ["💡 Create Ideas", "🗣️ Talk to People", "⚡ Start Acting", "📊 Analyze Data"], label_visibility="collapsed")
        
        st.markdown("### 2. What drains your energy?")
        q2 = st.radio("q2", ["Routine Tasks", "Working Alone", "Vague Plans", "Sales Pressure"], label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.form_submit_button("🔍 Reveal My True Profile", type="primary", use_container_width=True):
            with st.spinner("Analyzing Neural Patterns..."):
                time.sleep(1.5)
                if "Create" in q1: st.session_state.user_profile = "Distoversity Creator"
                elif "Talk" in q1: st.session_state.user_profile = "Distoversity Influencer"
                elif "Start" in q1: st.session_state.user_profile = "Distoversity Catalyst"
                else: st.session_state.user_profile = "Distoversity Analyst"
                st.session_state.page = 'Result'
                st.rerun()

def render_result():
    profile = st.session_state.user_profile
    if not profile: st.warning("Please complete the assessment first."); return

    # --- LEAD GATE ---
    if not st.session_state.lead_captured:
        st.markdown(f"""
        <div class="d-card" style="text-align:center; padding: 3rem;">
            <h2 style="color:#0077B6;">🎉 Profile Identified!</h2>
            <p style="font-size:1.2rem;">Your Core Energy Type is: <b>{profile.split()[1]}</b></p>
            <hr>
            <p>To unlock your <b>Full Career Roadmap</b>, <b>University Matches</b>, and <b>Salary Prediction</b>, please verify your details.</p>
            <p style="font-size:0.8rem; color:gray;">(We respect your privacy. No spam.)</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("lead_gen"):
            name = st.text_input("Your Name")
            phone = st.text_input("WhatsApp Number")
            if st.form_submit_button("🔓 Unlock My Full Report"):
                if name and len(phone) > 9:
                    st.session_state.lead_captured = True
                    st.rerun()
                else:
                    st.error("Please enter valid details.")
        return

    # --- REAL RESULT ---
    st.balloons()
    st.markdown(f"""
    <div class="d-card" style="background:#F0F9FF !important; text-align:center; border-color:#BAE6FD !important;">
        <span style="font-size:1rem; color:#0077B6; font-weight:bold; letter-spacing:1px;">OFFICIAL DISTOVERSITY PROFILE</span>
        <h1 style="color:#0077B6 !important; font-size:3rem !important; margin:10px 0;">{profile.replace('Distoversity ', '')}</h1>
    </div>
    """, unsafe_allow_html=True)

    # PREMIUM UPSELL
    st.markdown("""
    <div class="gold-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="color:#D97706 !important; margin:0;">👑 Premium Guidance</h3>
            <span style="background:#FEF3C7; color:#D97706; padding:5px 10px; border-radius:10px; font-size:0.8rem; font-weight:bold;">LIMITED SLOTS</span>
        </div>
        <p style="margin-top:10px;">Free reports are generic. Get a <b>1:1 Deep Dive Session</b> with our Senior Career Architect.</p>
        <hr style="border-top: 1px dashed #FCD34D;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <span style="font-size:1.5rem; font-weight:800; color:#D97706;">₹999</span>
                <span style="text-decoration:line-through; color:#9CA3AF; font-size:0.9rem;">₹2,499</span>
            </div>
            <a href="https://wa.me/919118231052?text=Hi, I want to book the Premium Career Session for Rs.999." target="_blank" style="text-decoration:none;">
                <button style="background:#D97706; color:white; border:none; padding:10px 20px; border-radius:5px; font-weight:bold; cursor:pointer;">Book Now ➤</button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><h3>🎓 Your University Matches (Free)</h3>", unsafe_allow_html=True)
    matches = df[df['type'] == profile]
    if matches.empty: matches = df.head(2)
    
    for idx, row in matches.iterrows():
        wa_link = f"https://wa.me/919118231052?text=I am interested in {row['name']}."
        st.markdown(f"""
        <div class="d-card">
            <h4>{row['name']}</h4>
            <p style="color:green; font-weight:bold; font-size:0.9rem;">{row['badge']} Match</p>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px;">
                <span style="font-weight:bold; font-size:1.1rem;">₹{row['fees']:,}</span>
                <a href="{wa_link}" target="_blank" style="text-decoration:none; color:#0077B6; font-weight:bold; border:1px solid #0077B6; padding:5px 15px; border-radius:20px;">Apply ➤</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_explorer():
    st.title("University Explorer")
    budget = st.slider("Max Budget", 50000, 500000, 200000)
    filtered = df[df['fees'] <= budget]
    for idx, row in filtered.iterrows():
        wa_link = f"https://wa.me/919118231052?text=I am interested in {row['name']}."
        st.markdown(f"""
        <div class="d-card">
            <h4>{row['name']}</h4>
            <p>🏅 {row['badge']} | 💰 ₹{row['fees']:,}</p>
            <a href="{wa_link}" style="text-decoration:none;">
                <button style="background:#0077B6; color:white; width:100%; padding:10px; border:none; border-radius:5px; cursor:pointer;">👉 Apply on WhatsApp</button>
            </a>
        </div>
        """, unsafe_allow_html=True)

def render_eduveer():
    st.title("Chat with Eduveer 🤖")
    with st.container(height=500, border=True):
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        if prompt := st.chat_input("Ask anything..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            time.sleep(0.5)
            st.session_state.messages.append({"role": "assistant", "content": "Great question! Please check the Explorer tab for details."})
            st.rerun()

# --- 6. MAIN ROUTER ---
desktop_navbar()
mobile_bottom_nav()

# Hidden buttons for mobile triggers
if st.button("Home_Hidden", key="home_btn"): st.session_state.page = "Home"; st.rerun()
if st.button("Quiz_Hidden", key="quiz_btn"): st.session_state.page = "Assessment"; st.rerun()
if st.button("Bot_Hidden", key="bot_btn"): st.session_state.page = "Eduveer"; st.rerun()

# CSS to Hide Triggers
st.markdown("""<style>div[data-testid="stButton"] > button[key*="_btn"] {display: none;}</style>""", unsafe_allow_html=True)

if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'Eduveer': render_eduveer()
