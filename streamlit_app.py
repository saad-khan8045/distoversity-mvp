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

    /* --- GLOBAL LAYOUT FIXES (CRITICAL FOR VISIBILITY) --- */
    :root {
        --primary: #0077B6;
        --primary-dark: #023E8A;
        --text-main: #0F172A;
        --bg-light: #F4F9FD;
        --gold: #D97706;
    }

    [data-testid="stAppViewContainer"], .stApp, header, footer {
        background-color: var(--bg-light) !important;
        color: var(--text-main) !important;
    }
    
    /* Typography Fixes */
    h1, h2, h3 { font-family: 'Outfit', sans-serif !important; color: #003366 !important; -webkit-text-fill-color: #003366 !important; }

    /* Fix Inputs & Inputs in Dark Mode */
    input, textarea, select, div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #CBD5E1 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* WIDER LAYOUT FIX */
    .block-container {
        max-width: 1200px !important;
        padding-left: 5rem;
        padding-right: 5rem;
        padding-top: 1rem;
        padding-bottom: 5rem;
    }
    
    /* Global Card Styles */
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
        border-radius: 50px !important;
        font-weight: 600 !important;
        -webkit-text-fill-color: white !important;
        box-shadow: 0 4px 15px rgba(0, 119, 182, 0.3) !important;
    }
    
    /* Mobile Fixes */
    @media (max-width: 768px) {
        .block-container { padding-left: 1rem !important; padding-right: 1rem !important; }
        h1 { font-size: 2rem !important; }
        div[data-testid="stHorizontalBlock"] { display: none !important; }
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA & STATE (Syntax Corrected) ---
@st.cache_data
def load_data():
    # FIX: Corrected indentation for function content and closed the list properly.
    return pd.DataFrame([
        {"name": "Amity Online", "fees": 350000, "type": "Distoversity Analyst", "badge": "Top Ranked"},
        {"name": "Manipal Jaipur", "fees": 175000, "type": "Distoversity Creator", "badge": "NAAC A+"},
        {"name": "LPU Online", "fees": 160000, "type": "Distoversity Catalyst", "badge": "Affordable"},
        {"name": "NMIMS", "fees": 400000, "type": "Distoversity Influencer", "badge": "Premium"},
        {"name": "Jain University", "fees": 210000, "type": "Distoversity Influencer", "badge": "Placement Focus"}
    ])

df = load_data()

# FIX: Corrected Syntax Error in Session State Initialization
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'lead_captured' not in st.session_state: st.session_state.lead_captured = False
if 'user_profile' not in st.session_state: st.session_state.user_profile = None # Syntax Error fixed
if 'messages' not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Hi! I am Eduveer. I can guide you to the right career path."}]

def get_superpower(prof):
    if "Creator" in prof: return "Innovation & Starting New Things"
    if "Influencer" in prof: return "People & Communication"
    if "Catalyst" in prof: return "Execution & Timing"
    return "Data & Systems"

def get_bot_response_smart(user_query):
    q = user_query.lower()
    if "fee" in q or "cost" in q or "emi" in q: return f"Fees are competitive. We have options starting from ₹98,000 up to ₹400,000. Check the Explorer tab for your exact budget."
    if "placement" in q or "job" in q or "roi" in q: return "High placement stats are critical! NMIMS recorded a highest package of ₹24 LPA. We track ROI, check the Explorer for more."
    if "valid" in q or "ugc" in q: return "100% valid. All universities we list are UGC-DEB/NAAC accredited. We only deal in approved degrees."
    return "That's a great question! Check out the Explorer tab for quick data or consider the Premium Session for detailed comparison."

# --- 4. NAVIGATION & JS TRIGGERS ---

def desktop_navbar():
    with st.container():
        c1, c2, c3, c4, c5, c6, c7 = st.columns([2, 1, 1, 1, 1, 1, 1])
        with c1:
            st.markdown("<h3 style='margin:0; padding:0;'>Distoversity<span style='color:#00B4D8'>.</span></h3>", unsafe_allow_html=True)
        
        if c2.button("Home"): st.session_state.page = "Home"; st.rerun()
        if c3.button("About"): st.session_state.page = "About"; st.rerun()
        if c4.button("4D Quiz"): st.session_state.page = "Assessment"; st.rerun()
        if c5.button("Courses"): st.session_state.page = "Explorer"; st.rerun()
        if c6.button("Bot"): st.session_state.page = "Eduveer"; st.rerun()
        if c7.button("FAQ"): st.session_state.page = "FAQ"; st.rerun()
    st.markdown("---")

def mobile_bottom_nav():
    st.markdown("""
    <div style="position:fixed; bottom:0; left:0; width:100%; background:white; border-top:1px solid #E2E8F0; padding:10px 0; z-index:9999; display:flex; justify-content:space-around; text-align:center;">
        <a onclick="document.getElementById('home_btn_trigger').click()" style="color:#64748B; font-size:0.8rem; text-decoration:none; cursor:pointer;">🏠<br>Home</a>
        <a onclick="document.getElementById('quiz_btn_trigger').click()" style="color:#0077B6; font-weight:bold; font-size:0.8rem; text-decoration:none; cursor:pointer;">🧬<br>Quiz</a>
        <a onclick="document.getElementById('bot_btn_trigger').click()" style="color:#64748B; font-size:0.8rem; text-decoration:none; cursor:pointer;">🤖<br>Bot</a>
    </div>
    """, unsafe_allow_html=True)

# --- 5. PAGES ---

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
            st.session_state.page = 'Assessment'; st.rerun()

    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Meet the Founder ➔"):
            st.session_state.page = "About"; st.rerun()

def render_about():
    st.markdown("<h2 style='text-align:center;'>The Man Who Rejected the 'System'</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748B;'>From the factory floor to fixing education.</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c2:
        st.markdown("""
        <div class="d-card" style="border-left: 5px solid #F97316 !important;">
            <h3>🏭 2019: The Factory Floor (The Hook)</h3>
            <p>My career didn't start in a boardroom. It started at <b>Oppo & Yazaki</b>. 
            I worked 12-hour shifts. I saw thousands of hardworking Indians working like machines simply because they lacked <b>Guidance</b>.</p>
        </div>
        <div class="d-card" style="border-left: 5px solid #0077B6 !important;">
            <h3>📞 2021: The Sales Trap & Integrity</h3>
            <p>I moved to Education Counseling (Amity). I spoke to <b>2,000+ students</b>. 
            But I realized: <b>"Education is being sold, not served."</b> I chose integrity over commission and built a better system.</p>
        </div>
        <div class="d-card" style="border-left: 5px solid #10B981 !important;">
            <h3>🧬 2024: The Birth of Distoversity</h3>
            <p>I built a platform that uses <b>Data & Psychology</b> (The 4-Genius Framework), not sales tactics. Our mission is to see <b>1000K students grow together</b>.</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("See How My Logic Works ➔", type="primary", use_container_width=True):
        st.session_state.page = "Assessment"; st.rerun()

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
            # Logic Mapping
            if "Create" in q1: st.session_state.user_profile = "Distoversity Creator"
            elif "Talk" in q1: st.session_state.user_profile = "Distoversity Influencer"
            elif "Act" in q1: st.session_state.user_profile = "Distoversity Catalyst"
            else: st.session_state.user_profile = "Distoversity Analyst"
            
            st.session_state.page = 'Result'; st.rerun()

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
                    st.session_state.lead_captured = True; st.rerun()
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
        st.session_state.page = "Explorer"; st.rerun()

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
        st.session_state.page = "Eduveer"; st.rerun()

def render_eduveer():
    st.title("Chat with Eduveer 🤖")
    with st.container(height=500, border=True):
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        if prompt := st.chat_input("Ask about fees, placements..."):
            st.session_state.messages.append({"role": "user", "content": prompt}); st.chat_message("user").write(prompt)
            # --- SMART LOGIC INTEGRATED ---
            response = get_bot_response_smart(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response}); st.rerun()

def render_faq():
    st.title("❓ Frequently Asked Questions")
    tab1, tab2, tab3 = st.tabs(["🌟 Career Guidance", "💻 Online Education", "🎓 Universities"])
    
    with tab1:
        st.header("General Education & Career")
        with st.expander("❓ I'm confused about my career path after high school. How can Distoversity help?"):
            st.write("We help you discover your 'Genius Profile' (natural strengths) via AI, guiding you to academic fields and careers that truly fit you.")
        with st.expander("❓ Is the Distoversity 'Genius Profile' a psychological test?"):
            st.write("No, it is a self-discovery and guidance tool based on Wealth Dynamics, not a psychological diagnostic test.")
        with st.expander("❓ What do Dynamo, Blaze, Tempo, and Steel mean?"):
            st.write("Dynamo = Ideas (Creator), Blaze = People (Influencer), Tempo = Timing (Catalyst), Steel = Details (Analyst).")
    
    with tab2:
        st.header("Online Education & Learning Trends")
        with st.expander("❓ Is online education a good option?"):
            st.write("Yes! Your profile determines your online fit. We match you to programs that suit your learning style.")

    with tab3:
        st.header("Universities & Admissions")
        with st.expander("❓ Which universities partner with Distoversity?"):
            st.write("We partner only with NAAC A+ and A++ accredited universities like Amity, Manipal, Jain, and NMIMS.")
        with st.expander("❓ How do I apply?"):
            st.write("Once you find your match, you can request a brochure or book a call. Our counselors will guide you through the application process.")
        
# --- 6. MAIN ROUTER ---
desktop_navbar()
mobile_bottom_nav()

# Hidden buttons for mobile nav trigger
st_hide_slot = st.empty() 
with st_hide_slot.container():
    if st.button("Home_Trigger", key="home_btn_trigger"): st.session_state.page = "Home"; st.rerun()
    if st.button("Quiz_Trigger", key="quiz_btn_trigger"): st.session_state.page = "Assessment"; st.rerun()
    if st.button("Bot_Trigger", key="bot_btn_trigger"): st.session_state.page = "Eduveer"; st.rerun()

# CSS to Hide the entire container block forcefully on desktop
st.markdown("""<style>div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stButton"]) {display: none !important;}</style>""", unsafe_allow_html=True)

# Main Logic Router
if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'Eduveer': render_eduveer()
elif st.session_state.page == 'FAQ': render_faq()
