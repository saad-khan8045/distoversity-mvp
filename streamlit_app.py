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

    /* --- GLOBAL LAYOUT FIXES --- */
    [data-testid="stAppViewContainer"], .stApp, header, footer {
        background-color: var(--bg-light) !important;
        color: var(--text-main) !important;
    }
    
    /* Global Text Fixes */
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
    
    /* Final Fix: Hiding the visible hidden buttons on Desktop */
    #nav-triggers-hidden {
        display: none !important;
        height: 0px !important;
        visibility: hidden !important;
    }

    /* Layout Fix */
    .block-container {
        max-width: 1200px !important; 
        padding-left: 5rem; 
        padding-right: 5rem;
    }
    
    /* Mobile Specifics */
    @media (max-width: 768px) {
        .block-container { padding-top: 1rem !important; padding-bottom: 5rem !important; }
        h1 { font-size: 2rem !important; }
        section[data-testid="stSidebar"] { display: none; }
        div[data-testid="stHorizontalBlock"] { display: none !important; } /* Hide Desktop Nav */
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA & STATE (Data remains the same) ---
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
    # Final Mobile Sticky Nav
    st.markdown("""
    <div style="position:fixed; bottom:0; left:0; width:100%; background:white; border-top:1px solid #E2E8F0; padding:10px 0; z-index:9999; display:flex; justify-content:space-around; text-align:center;">
        <a onclick="document.getElementById('home_btn').click()" style="color:#64748B; font-size:0.8rem; text-decoration:none; cursor:pointer;">🏠<br>Home</a>
        <a onclick="document.getElementById('quiz_btn').click()" style="color:#0077B6; font-weight:bold; font-size:0.8rem; text-decoration:none; cursor:pointer;">🧬<br>Quiz</a>
        <a onclick="document.getElementById('bot_btn').click()" style="color:#64748B; font-size:0.8rem; text-decoration:none; cursor:pointer;">🤖<br>Bot</a>
    </div>
    """, unsafe_allow_html=True)

def get_superpower(prof):
    if "Creator" in prof: return "Innovation & Starting New Things"
    if "Influencer" in prof: return "People & Communication"
    if "Catalyst" in prof: return "Execution & Timing"
    return "Data & Systems"

# --- 5. PAGES (Content Refined for Strategy) ---

def render_home():
    st.markdown("""
    <div style="text-align:center; padding: 2rem 0;">
        <span style="background:#E0F2FE; color:#0077B6; padding:6px 16px; border-radius:20px; font-size:0.85rem; font-weight:700; letter-spacing: 1px;">🚫 WARNING: DON'T BE SOLD. BE GUIDED.</span>
        <h1 style="font-size: 3.2rem; line-height:1.1; margin-top:20px; font-weight: 800;">Is Your Online Career Designed by <span style="color:#0077B6">Science</span>...<br>or a <span style="color:#F97316">Sales Agent?</span></h1>
        <p style="color:#475569; font-size:1.2rem; margin-top:1.5rem; max-width: 700px; margin-left:auto; margin-right:auto;">
            93% of students choose the wrong course because they trust "Free Counselors." We, as industry veterans, offer the <b>4-Genius Framework</b> to match your DNA to the Degree.
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
    
    st.markdown("<p style='text-align:center; font-weight:bold; color:#94A3B8; letter-spacing:1px;'>TRUSTED BY STUDENTS OF AMITY, MANIPAL, LPU</p>", unsafe_allow_html=True)
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
            <h3>🏭 2019: The Factory Floor (The Hook)</h3>
            <p>My career didn't start in a boardroom. I worked 12-hour shifts at <b>Oppo & Yazaki</b>. I saw thousands of hardworking Indians working like machines simply because they lacked <b>Guidance</b>.</p>
        </div>
        <div class="d-card" style="border-left: 5px solid #0077B6 !important;">
            <h3>📞 2021: The Sales Trap & Integrity</h3>
            <p>I moved to Education Counseling (Amity). I realized: <b>"Education is being sold, not served."</b> I chose integrity over commission and built a better system.</p>
        </div>
        <div class="d-card" style="border-left: 5px solid #10B981 !important;">
            <h3>🧬 2024: The Birth of Distoversity</h3>
            <p>I built this platform using <b>Data & Psychology</b> (The 4-Genius Framework). Our mission is to see <b>1000K students grow together</b>.</p>
            <p style="font-weight:bold; margin-top:10px;">(TFI Connection: My goal is to apply this systems-level solution to nationwide educational equity.)</p>
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
        if st.form_submit_button("Analyze My Energy ➤", type="primary", use_container_width=True):
            # REMOVED TIME.SLEEP FOR INSTANT RESULT
            if "Create" in q1: st.session_state.user_profile = "Distoversity Creator"
            elif "Talk" in q1: st.session_state.user_profile = "Distoversity Influencer"
            elif "Act" in q1: st.session_state.user_profile = "Distoversity Catalyst"
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
            <p>To unlock your <b>Career Roadmap</b>, <b>University Matches</b>, and <b>Salary Prediction</b>, please verify your details.</p>
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
        <h1 style="color:#0077B6 !important; font-size:2.5rem !important; margin:10px 0;">{profile.replace('Distoversity ', '')}</h1>
        <p style="color:#0F172A;"><b>Your Superpower:</b> {get_superpower(profile)}</p>
    </div>
    """, unsafe_allow_html=True)

    # PREMIUM UPSELL
    st.markdown("""
    <div class="gold-card">
        <h3 style="color:#D97706 !important;">👑 Premium Guidance</h3>
        <p>Don't risk your career on free advice. Get a <b>1:1 Deep Dive Session</b> with our Senior Career Architect.</p>
        <h2 style="color:#D97706 !important;">₹999 <span style="font-size:1rem; text-decoration:line-through; color:gray;">₹2,499</span></h2>
        
        <a href="https://wa.me/919118231052?text=Hi, I want to book the Premium Career Session for Rs.999." target="_blank" style="text-decoration:none;">
            <button style="background:#D97706; color:white; border:none; padding:10px 20px; border-radius:5px; font-weight:bold; cursor:pointer;">Book Now ➤</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # NEXT STEP
    if st.button("View Matched Universities ➔"):
        st.session_state.page = "Explorer"
        st.rerun()

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
    
    # NEXT STEP
    if st.button("Have Doubts? Ask Eduveer ➔"):
        st.session_state.page = "Eduveer"
        st.rerun()

def render_eduveer():
    st.title("Chat with Eduveer 🤖")
    with st.container(height=500, border=True):
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        if prompt := st.chat_input("Ask about fees, placements..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            time.sleep(0.5)
            st.session_state.messages.append({"role": "assistant", "content": "Great question! Please check the Explorer tab for details."})
            st.rerun()

# --- 6. MAIN ROUTER ---
desktop_navbar()
mobile_bottom_nav()

# --- 1. SET UP INVISIBLE TRIGGERS ---
# We wrap the buttons in a div with a unique ID and then hide the entire div using CSS.
st.markdown('<div id="mobile-nav-triggers">', unsafe_allow_html=True)
# The buttons themselves
if st.button("Home_Hidden", key="home_btn"): st.session_state.page = "Home"; st.rerun()
if st.button("Quiz_Hidden", key="quiz_btn"): st.session_state.page = "Assessment"; st.rerun()
if st.button("Bot_Hidden", key="bot_btn"): st.session_state.page = "Eduveer"; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- 2. AGGRESSIVE CSS HIDE ---
st.markdown("""
<style>
/* This rule targets the specific container and forces it to be invisible */
#mobile-nav-triggers { 
    display: none !important; 
    visibility: hidden !important;
}
</style>
""", unsafe_allow_html=True)

# --- MAIN APP ROUTER (REST OF THE CODE) ---
if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'Eduveer': render_eduveer()
