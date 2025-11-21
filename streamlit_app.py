import streamlit as st
import pandas as pd
import time
import random
import os

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Ethical Career Guidance",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. NUCLEAR CSS (Theme Fixes and Structural Hiding) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* --- GLOBAL VARIABLES & THEME LOCK --- */
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
    
    /* Typography Fixes */
    h1, h2, h3 { font-family: 'Outfit', sans-serif !important; color: #003366 !important; -webkit-text-fill-color: #003366 !important; }

    /* Premium Cards */
    .d-card {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03) !important;
        margin-bottom: 1rem !important;
    }
    
    /* WIDER LAYOUT FIX (Ensures content is not shrunk) */
    .block-container {
        max-width: 1200px !important;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0077B6 0%, #00B4D8 100%) !important;
        color: white !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
    }

    /* Mobile Specifics */
    @media (max-width: 768px) {
        .block-container { padding-top: 1rem !important; padding-bottom: 5rem !important; }
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
# --- REPLACE LINES 84-87 WITH THIS CORRECT STRUCTURE ---

if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'lead_captured' not in st.session_state: st.session_state.lead_captured = False
if 'user_profile' not in st.session_state: st.session_state.user_profile = None 
if 'messages' not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Hi! I am Eduveer. I can guide you to the right career path."}]

# --- END FIX ---
def get_superpower(prof):
    if "Creator" in prof: return "Innovation & Starting New Things"
    if "Influencer" in prof: return "People & Communication"
    if "Catalyst" in prof: return "Execution & Timing"
    return "Data & Systems"

def get_bot_response_smart(user_query):
    q = user_query.lower()
    
    if "fee" in q or "cost" in q or "emi" in q:
        max_fee = df['fees'].max()
        return f"Fees are competitive. We have options starting from ₹98,000 up to ₹{max_fee:,}. Check the Explorer tab for your exact budget."
        
    if "placement" in q or "job" in q or "roi" in q:
        top_uni = df.loc[df['fees'].idxmax()] # Simplified high fee uni as proxy for premium
        return f"High placement stats are critical! NMIMS recorded a highest package of ₹24 LPA. We track ROI, check the Explorer for more."
        
    if "valid" in q or "ugc" in q:
        return "100% valid. All universities we list are UGC/NAAC accredited. We only deal in approved degrees."

    return "That's a great question! Check out the Explorer tab for quick data or consider the Premium Session for detailed comparison."


# --- 4. NAVIGATION & HELPER FUNCTIONS ---

def desktop_navbar():
    with st.container():
        c1, c2, c3, c4, c5, c6, c7 = st.columns([2, 1, 1, 1, 1, 1, 1])
        with c1:
            st.markdown("<h3 style='margin:0; padding:0;'>Distoversity<span style='color:#00B4D8'>.</span></h3>", unsafe_allow_html=True)
        
        # New Flow: Home -> About (Trust) -> Explorer (Value) -> Assessment (Tool)
        if c2.button("Home"): st.session_state.page = "Home"; st.rerun()
        if c3.button("Story & Trust"): st.session_state.page = "About"; st.rerun()
        if c4.button("Explorer"): st.session_state.page = "Explorer"; st.rerun()
        if c5.button("4D Assessment"): st.session_state.page = "Assessment"; st.rerun()
        if c6.button("Bot"): st.session_state.page = "Eduveer"; st.rerun()
        if c7.button("FAQ"): st.session_state.page = "FAQ"; st.rerun()
    st.markdown("---")

def mobile_bottom_nav():
    # Sticky Bottom Nav (Mobile)
    st.markdown("""
    <div style="position:fixed; bottom:0; left:0; width:100%; background:white; border-top:1px solid #E2E8F0; padding:10px 0; z-index:9999; display:flex; justify-content:space-around; text-align:center;">
        <a onclick="document.getElementById('home_btn_trigger').click()" style="color:#64748B; font-size:0.8rem; text-decoration:none; cursor:pointer;">🏠<br>Home</a>
        <a onclick="document.getElementById('story_btn_trigger').click()" style="color:#64748B; font-weight:bold; font-size:0.8rem; text-decoration:none; cursor:pointer;">🧠<br>Story</a>
        <a onclick="document.getElementById('explorer_btn_trigger').click()" style="color:#0077B6; font-weight:bold; font-size:0.8rem; text-decoration:none; cursor:pointer;">🔍<br>Explorer</a>
        <a onclick="document.getElementById('bot_btn_trigger').click()" style="color:#64748B; font-size:0.8rem; text-decoration:none; cursor:pointer;">🤖<br>Bot</a>
    </div>
    """, unsafe_allow_html=True)

# --- 5. PAGES ---

def render_home():
    st.markdown("""
    <div style="text-align:center; padding: 2rem 0;">
        <span style="background:#E0F2FE; color:#0077B6; padding:6px 16px; border-radius:20px; font-size:0.85rem; font-weight:700; letter-spacing: 1px;">🤝 ETHICAL CAREER GUIDANCE FOR THE NEW INDIA</span>
        <h1 style="font-size: 3.2rem; line-height:1.1; margin-top:20px; font-weight: 800;">Stop Guessing.<br>Get a Strategy that Works.</h1>
        <p style="color:#475569; font-size:1.2rem; margin-top:1.5rem; max-width: 700px; margin-left:auto; margin-right:auto;">
            We provide **Personalized Clarity** so you never waste time or money again. Your future is too important for guesswork.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        # MAIN CTA POINTS TO FOUNDER STORY (Trust over Quiz)
        if st.button("Meet the Founder & Get Started ➔", type="primary", use_container_width=True):
            st.session_state.page = 'About'; st.rerun()

    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Explore Universities"):
            st.session_state.page = "Explorer"; st.rerun()

def render_about():
    st.markdown("<h2 style='text-align:center;'>The Man Who Rejected the 'System'</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748B;'>From the factory floor to fixing education: My problem shouldn't be yours.</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c2:
        st.markdown("""
        <div class="d-card" style="border-left: 5px solid #F97316 !important;">
            <h3>🏭 2019: The Factory Floor Reality (The Hook)</h3>
            <p>My career didn't start in a boardroom. I worked 12-hour shifts at <b>Oppo & Yazaki</b>. I learned that millions of hardworking Indians are treated like machines because they lacked <b>Guidance</b> at the right time.</p>
        </div>
        <div class="d-card" style="border-left: 5px solid #0077B6 !important;">
            <h3>📞 2021: The Sales Trap & Integrity</h3>
            <p>I spoke to <b>2,000+ students</b> at Amity/Manipal. I realized: <b>"Education is being sold, not served."</b> I quit because my integrity was worth more than commissions.</p>
        </div>
        <div class="d-card" style="border-left: 5px solid #10B981 !important;">
            <h3>🧬 2024: The Distoversity Solution</h3>
            <p>I built this platform using <b>Data & Psychology</b> (The 4-Genius Framework). Our mission is to ensure <b>your time and money are never wasted</b>.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # NEXT STEP: Assesssment is the tool needed now
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
    
    # PREMIUM UPSELL
    st.markdown("""
    <div class="gold-card">
        <h3 style="color:#D97706 !important;">👑 Premium Guidance: The 1 Hour That Saves You 4 Years</h3>
        <p>Your time is valuable. Get a **1:1 Strategic Session (60 Mins)** with the Founder to map your exact ROI and scholarship path.</p>
        <ul style="color:#4B5563; font-size:0.9rem;">
            <li>✅ **Ethical Consultation:** Unbiased advice (No commission pressure).</li>
            <li>✅ **Alison Course Alignment:** Use your free certificates for maximum impact.</li>
            <li>✅ **Custom ROI Report:** Which university is the best investment for *your* profile.</li>
        </ul>
        <h2 style="color:#D97706 !important;">₹999 <span style="font-size:1rem; text-decoration:line-through; color:gray;">₹2,499</span></h2>
        
        <a href="https://wa.me/919118231052?text=Hi, I want to book the Premium Career Session for Rs.999." target="_blank" style="text-decoration:none;">
            <button style="background:#D97706; color:white; border:none; padding:10px 20px; border-radius:5px; font-weight:bold; cursor:pointer;">Book Now ➤</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # NEXT STEP
    if st.button("View Matched Universities (Free) ➔"):
        st.session_state.page = "Explorer"; st.rerun()

def render_explorer():
    st.title("University Explorer: Unbiased Selection")
    st.markdown("<p style='color:green;'>We don't get commissions from these universities; our goal is your success.</p>", unsafe_allow_html=True)
    
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
    # ... (FAQ content remains the same)
    st.header("General Education & Career")
    with st.expander("❓ I'm confused about my career path after high school. How can Distoversity help?"):
        st.write("We help you discover your 'Genius Profile' (natural strengths) via AI, guiding you to academic fields and careers that truly fit you.")
    with st.expander("❓ Is the Distoversity 'Genius Profile' a psychological test?"):
        st.write("No, it is a self-discovery and guidance tool based on Wealth Dynamics, not a psychological diagnostic test.")
    
# --- 6. MAIN ROUTER ---
desktop_navbar()
mobile_bottom_nav()

# --- FINAL STRUCTURAL FIX FOR VISIBLE BUTTONS ---
st_hide_slot = st.empty() 
with st_hide_slot.container():
    if st.button("Home_Trigger", key="home_btn_trigger"): st.session_state.page = "Home"; st.rerun()
    if st.button("Quiz_Trigger", key="quiz_btn_trigger"): st.session_state.page = "Assessment"; st.rerun()
    if st.button("Bot_Trigger", key="bot_btn_trigger"): st.session_state.page = "Eduveer"; st.rerun()

# Main Logic Router
if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'Eduveer': render_eduveer()
elif st.session_state.page == 'FAQ': render_faq()
