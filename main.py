import streamlit as st
import pandas as pd
import time
import random

# --- 1. CONFIGURATION (Mobile Optimized) ---
st.set_page_config(
    page_title="Distoversity | Scientific Career Guidance",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. NUCLEAR CSS (Samsung Dark Mode Fix + Premium UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* --- FORCE LIGHT THEME (The Nuclear Option) --- */
    :root {
        --primary: #0077B6;
        --primary-dark: #023E8A;
        --text-main: #0F172A;
        --bg-light: #F4F9FD;
        --gold: #D97706;
    }

    /* Force White Background Everywhere */
    [data-testid="stAppViewContainer"], .stApp, header, footer {
        background-color: var(--bg-light) !important;
        color: var(--text-main) !important;
    }
    
    /* Force Inputs White */
    input, textarea, select, div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #CBD5E1 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* Typography */
    h1, h2, h3, h4, p, span, div, label {
        color: var(--text-main) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        -webkit-text-fill-color: var(--text-main) !important;
    }
    h1, h2, h3 { font-family: 'Outfit', sans-serif !important; color: var(--primary-dark) !important; }

    /* Premium Cards */
    .d-card {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        margin-bottom: 1rem !important;
    }

    /* Gold Premium Card */
    .gold-card {
        background: linear-gradient(135deg, #FFFBEB 0%, #FFFFFF 100%) !important;
        border: 1px solid #FCD34D !important;
        border-left: 5px solid #D97706 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0077B6 0%, #00B4D8 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        width: 100% !important;
        -webkit-text-fill-color: white !important;
    }
    
    /* Mobile Fixes */
    @media (max-width: 768px) {
        .block-container { padding-top: 1rem !important; padding-left: 1rem !important; padding-right: 1rem !important; }
        h1 { font-size: 2rem !important; }
        section[data-testid="stSidebar"] { display: none; }
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA & STATE ---
@st.cache_data
def load_data():
    # Simulated DB
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

# --- 4. COMPONENT FUNCTIONS ---

def navbar():
    with st.container():
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown("<h3 style='margin:0;'>Distoversity<span style='color:#00B4D8'>.</span></h3>", unsafe_allow_html=True)
        with c2:
            page = st.selectbox("", ["Home", "About Founder", "Explorer", "4D Assessment"], label_visibility="collapsed")
            if page != st.session_state.page:
                st.session_state.page = page
                st.rerun()
    st.markdown("---")

def render_home():
    st.markdown("""
    <div style="text-align:center; padding: 2rem 0;">
        <span style="background:#E0F2FE; color:#0077B6; padding:5px 15px; border-radius:20px; font-size:0.8rem; font-weight:700;">STOP GUESSING. START ENGINEERING.</span>
        <h1 style="font-size: 2.8rem; line-height:1.2; margin-top:15px;">Your Career is a <span style="color:#0077B6">Science</span>.<br>Not a Sales Pitch.</h1>
        <p style="color:#475569; font-size:1.1rem; margin-top:1rem;">
            90% of students choose the wrong course because they were "Sold" by agents.<br>
            We use <b>Psychology & AI</b> to find your perfect fit.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🧬 Find My 4D Profile (Free)", type="primary", use_container_width=True):
            st.session_state.page = 'Assessment'
            st.rerun()
        st.markdown("<div style='text-align:center; font-size:0.8rem; color:gray;'>Takes 2 mins • AI Analysis</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### Trusted By")
    c1, c2, c3, c4 = st.columns(4)
    c1.info("AMITY")
    c2.info("MANIPAL")
    c3.info("NMIMS")
    c4.info("LPU")

def render_assessment():
    st.markdown("<h2 style='text-align:center;'>Find Your Distoversity DNA 🧬</h2>", unsafe_allow_html=True)
    
    with st.form("quiz"):
        st.write("**1. When solving a problem, you naturally:**")
        q1 = st.radio("q1", ["Generate Ideas (Creator)", "Talk to People (Influencer)", "Make a Plan (Catalyst)", "Check Data (Analyst)"], label_visibility="collapsed")
        
        st.write("**2. You work best when:**")
        q2 = st.radio("q2", ["Allowed to Experiment", "Leading a Team", "Things are Organized", "Working Alone Deeply"], label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.form_submit_button("Analyze My Energy ➤", type="primary"):
            with st.spinner("Mapping Neural Pathways..."):
                time.sleep(1.5)
                # Simple Logic
                if "Creator" in q1: st.session_state.user_profile = "Distoversity Creator"
                elif "Influencer" in q1: st.session_state.user_profile = "Distoversity Influencer"
                elif "Catalyst" in q1: st.session_state.user_profile = "Distoversity Catalyst"
                else: st.session_state.user_profile = "Distoversity Analyst"
                
                st.session_state.page = 'Result'
                st.rerun()

def render_result():
    profile = st.session_state.user_profile
    if not profile: st.warning("Take quiz first!"); return

    # --- STEP 1: LEAD CAPTURE (The Gate) ---
    if not st.session_state.lead_captured:
        st.markdown(f"""
        <div class="d-card" style="text-align:center;">
            <h2 style="color:#0077B6;">🎉 Analysis Complete!</h2>
            <p>Your Neural Profile matched: <b>{profile}</b></p>
            <hr>
            <p>To unlock your <b>Career Roadmap</b> and <b>University Matches</b>, enter your details.</p>
            <p style="font-size:0.8rem; color:gray;">(We will WhatsApp you the PDF Report)</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("lead_gen"):
            name = st.text_input("Your Name")
            phone = st.text_input("WhatsApp Number")
            if st.form_submit_button("🔓 Unlock Report Now"):
                if name and len(phone) > 9:
                    st.session_state.lead_captured = True
                    st.rerun()
                else:
                    st.error("Please enter valid details.")
        return

    # --- STEP 2: THE RESULT & REVENUE ENGINE ---
    st.balloons()
    
    # 1. The Profile Reveal
    st.markdown(f"""
    <div class="d-card" style="background:#F0F9FF !important; text-align:center;">
        <span style="font-size:1.2rem; color:#0077B6;">YOU ARE A</span>
        <h1 style="color:#0077B6 !important; font-size:2.5rem !important;">{profile.replace('Distoversity ', '')}</h1>
        <p>Your Superpower: <b>{get_superpower(profile)}</b></p>
    </div>
    """, unsafe_allow_html=True)

    # 2. The Monetization Block (₹999)
    st.markdown("""
    <div class="gold-card">
        <h3 style="color:#D97706 !important;">🚀 Need Professional Guidance?</h3>
        <p>Don't risk your career on free advice. Get a <b>1:1 Strategic Session</b> with our experts.</p>
        <ul>
            <li>✅ 45-Min Deep Dive Call</li>
            <li>✅ Customized University ROI Report</li>
            <li>✅ Scholarship Assistance</li>
        </ul>
        <h2 style="color:#D97706 !important;">₹999 <span style="font-size:1rem; text-decoration:line-through; color:gray;">₹2499</span></h2>
    </div>
    """, unsafe_allow_html=True)
    
    # WhatsApp Direct Link
    wa_msg = f"Hi, I am a {profile}. I want to book the Premium Counseling Session for 999."
    st.link_button("👉 Book Premium Session (WhatsApp)", f"https://wa.me/919118231052?text={wa_msg}", type="primary", use_container_width=True)

    st.markdown("<br><h3>🎓 Your Free University Matches</h3>", unsafe_allow_html=True)
    matches = df[df['type'] == profile]
    if matches.empty: matches = df.head(2)
    
    for idx, row in matches.iterrows():
        st.markdown(f"""
        <div class="d-card">
            <h4>{row['name']}</h4>
            <p style="color:green; font-weight:bold;">Best for {profile.split()[1]}</p>
            <div style="display:flex; justify-content:space-between;">
                <span>₹{row['fees']:,}</span>
                <a href="https://wa.me/919118231052?text=Tell me more about {row['name']}" style="color:#0077B6; font-weight:bold;">Enquire ➤</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

def get_superpower(prof):
    if "Creator" in prof: return "Innovation & Starting New Things"
    if "Influencer" in prof: return "People & Communication"
    if "Catalyst" in prof: return "Execution & Timing"
    return "Data & Systems"

def render_about():
    st.title("The Founder's Story")
    st.markdown("""
    <div class="d-card" style="border-left: 5px solid #F97316 !important;">
        <h3>The Struggle</h3>
        <p><b>2019:</b> I was on the factory floor at <b>Oppo & Yazaki</b>. 
        12-hour shifts. I saw hardworking Indians being treated like machines because they lacked guidance.</p>
    </div>
    <div class="d-card" style="border-left: 5px solid #10B981 !important;">
        <h3>The Solution</h3>
        <p>I worked as a counselor at <b>Amity</b> but realized education was just "Sales". 
        So I built <b>Distoversity</b>. We use Data, not agents.</p>
    </div>
    """, unsafe_allow_html=True)

def render_explorer():
    st.title("University Explorer")
    col1, col2 = st.columns(2)
    with col1: budget = st.slider("Max Budget", 50000, 500000, 200000)
    
    filtered = df[df['fees'] <= budget]
    for idx, row in filtered.iterrows():
        wa_link = f"https://wa.me/919118231052?text=I am interested in {row['name']}. Please guide."
        st.markdown(f"""
        <div class="d-card">
            <h4>{row['name']}</h4>
            <p>🏅 {row['badge']} | 💰 ₹{row['fees']:,}</p>
            <a href="{wa_link}" style="text-decoration:none;">
                <button style="background:#0077B6; color:white; width:100%; padding:10px; border:none; border-radius:5px; cursor:pointer;">
                    👉 Apply on WhatsApp
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

# --- 6. MAIN ROUTER ---
navbar()

if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About Founder': render_about()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
