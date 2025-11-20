import streamlit as st
import pandas as pd
import time
import plotly.express as px
import random

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS: PREMIUM DESIGN + MOBILE OPTIMIZATIONS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    :root {
        --primary: #0077B6;
        --primary-dark: #023E8A;
        --accent: #00B4D8;
        --text-main: #0F172A;
        --white: #FFFFFF;
        --hero-gradient: radial-gradient(circle at 50% 0%, #E0F2FE 0%, #FFFFFF 70%); 
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-main);
        background-color: #FFFFFF;
        scroll-behavior: smooth;
    }

    /* --- HEADERS --- */
    h1, h2, h3 { font-family: 'Outfit', sans-serif; color: var(--primary-dark); font-weight: 800; }
    h1 { font-size: 4rem !important; letter-spacing: -2px; line-height: 1.1; }

    /* --- PREMIUM GLASS CARD --- */
    .d-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    .d-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 50px -10px rgba(0, 119, 182, 0.15);
        border-color: var(--accent);
    }

    /* --- BUTTONS --- */
    .stButton>button {
        background: linear-gradient(90deg, #0077B6 0%, #0096C7 100%);
        color: white;
        border-radius: 50px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 119, 182, 0.2);
        transition: 0.2s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 8px 25px rgba(0, 119, 182, 0.3); }

    /* --- MOBILE OPTIMIZATIONS (From your Blueprint) --- */
    @media (max-width: 850px) {
        .hero-section { padding: 2.5rem 1rem !important; border-radius: 0 0 24px 24px !important; }
        h1 { font-size: 2.3rem !important; }
        .nav-logo { font-size: 1.15rem !important; }
        .d-card { padding: 1.2rem !important; margin-bottom: 1rem !important; }
        .stButton>button { width: 100% !important; padding: 0.5rem 1rem !important; }
        
        /* Hide sticky button on desktop, show on mobile */
        .sticky-cta { display: block !important; }
    }

    /* --- STICKY MOBILE BUTTON --- */
    .sticky-cta { 
        display: none; /* Hidden by default on desktop */
        position: fixed; 
        bottom: 20px; 
        left: 0; 
        right: 0; 
        z-index: 9999; 
        text-align: center;
    }
    .sticky-btn { 
        display: inline-block;
        width: 90%; 
        padding: 15px 0; 
        border-radius: 50px;  
        background: linear-gradient(90deg, #0077B6 0%, #023E8A 100%); 
        color: white;  
        font-weight: 700; 
        font-size: 1.1rem; 
        box-shadow: 0 10px 20px rgba(0,119,182,0.3);   
        text-decoration: none;
    }

    /* --- UTILS --- */
    .feature-tag { background: #F1F5F9; color: #475569; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; margin-right: 5px; }
    .match-tag { background: #DCFCE7; color: #166534; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #F8FAFC; border-right: 1px solid #E2E8F0; }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA ---
UNIVERSITY_DATA = [
    {"name": "Jain Online", "location": "Bangalore", "fees": 210000, "program": "MBA Marketing", "energy": "Distoversity Influencer", "placement": "98%", "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Jain_University_logo.png"},
    {"name": "Manipal Online", "location": "Jaipur", "fees": 175000, "program": "MCA Data Science", "energy": "Distoversity Analyst", "placement": "94%", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png"},
    {"name": "Amity Online", "location": "Global", "fees": 345000, "program": "BCA Cloud Security", "energy": "Distoversity Creator", "placement": "92%", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png"},
    {"name": "LPU Online", "location": "Global", "fees": 160000, "program": "MBA Operations", "energy": "Distoversity Catalyst", "placement": "91%", "img": "https://upload.wikimedia.org/wikipedia/en/d/d4/Lovely_Professional_University_logo.png"},
    {"name": "Chandigarh Univ", "location": "Online", "fees": 180000, "program": "MBA General", "energy": "Distoversity Influencer", "placement": "89%", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Chandigarh_University_logo.png/220px-Chandigarh_University_logo.png"},
    {"name": "NMIMS CDOL", "location": "Online", "fees": 400000, "program": "MBA Finance", "energy": "Distoversity Analyst", "placement": "93%", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/NMIMS_University_logo.png/220px-NMIMS_University_logo.png"}
]
df = pd.DataFrame(UNIVERSITY_DATA)

# --- 4. STATE ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'messages' not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Hello! I am Eduveer. I can help you find the perfect university based on your Genius Profile."}]

# --- 5. NAVIGATION (SIDEBAR + STICKY BUTTON) ---
with st.sidebar:
    st.markdown("<h3>Distoversity<span style='color:#00B4D8'>.</span></h3>", unsafe_allow_html=True)
    
    selected = st.radio("Menu", ["Home", "Explorer", "Eduveer AI", "FAQ", "Partners", "About", "Take Assessment"], label_visibility="collapsed")
    
    if selected == "Home": st.session_state.page = 'Home'
    elif selected == "Explorer": st.session_state.page = 'Explorer'
    elif selected == "Eduveer AI": st.session_state.page = 'Eduveer'
    elif selected == "FAQ": st.session_state.page = 'FAQ'
    elif selected == "Partners": st.session_state.page = 'Institutions'
    elif selected == "About": st.session_state.page = 'About'
    elif selected == "Take Assessment": st.session_state.page = 'Assessment'

    st.divider()
    st.info("Discover Your Spark.")

# STICKY BUTTON (Shows only on Mobile via CSS)
st.markdown("""
<div class="sticky-cta">
  <a class="sticky-btn" href="#" onclick="alert('Redirecting to Booking Page...');">🚀 Book Career Advice</a>
</div>
""", unsafe_allow_html=True)

# --- 6. PAGES ---

def render_home():
    st.markdown("""
    <div class="hero-section" style="background: radial-gradient(circle at 50% 0%, #E0F2FE 0%, #FFFFFF 70%); padding: 4rem 1rem; text-align: center; border-radius: 0 0 40px 40px; margin-bottom: 2rem;">
        <div style="background:rgba(0,119,182,0.1); color:#0077B6; padding:8px 20px; border-radius:30px; display:inline-block; font-weight:700; font-size:0.9rem; margin-bottom:20px;">CAREER ARCHITECTURE FOR PROFESSIONALS</div>
        <h1 style="color:#023E8A; margin-bottom: 1rem;">Upgrade Your Identity.</h1>
        <p style="color: #475569; font-size: 1.2rem; max-width: 600px; margin: 0 auto 2rem auto;">
            We match your <b>Core Professional Identity</b> to India's Top Online Universities.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🚀 Discover Your Spark (Free)", use_container_width=True, type="primary"):
            st.session_state.page = 'Assessment'
            st.rerun()

    st.markdown("<br><h3 style='text-align:center;'>Why Distoversity?</h3>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="d-card"><h4>🧠 Identity First</h4><p>We look at your Mind, not just your marks.</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="d-card"><h4>🤖 AI Powered</h4><p>Unbiased advice from Eduveer 24/7.</p></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="d-card"><h4>💼 Roadmap</h4><p>Don\'t just get a degree. Get a Strategy.</p></div>', unsafe_allow_html=True)

def render_explorer():
    st.markdown("## 🏫 University Explorer")
    
    # Filters
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1: budget = st.slider("Max Fees (₹)", 100000, 500000, 350000)
        with c2: energy = st.multiselect("Energy Fit", ["Distoversity Creator", "Distoversity Influencer", "Distoversity Catalyst", "Distoversity Analyst"])

    filtered = df[df['fees'] <= budget]
    if energy: filtered = filtered[filtered['energy'].isin(energy)]
    
    st.write(f"Found {len(filtered)} matches.")

    # MOBILE-FRIENDLY CARD STACK (Default view)
    for index, row in filtered.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="d-card" style="margin-bottom: 15px; padding: 1.5rem; border-left: 5px solid #0077B6;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div style="display:flex; gap: 15px; align-items:center;">
                        <img src="{row['img']}" style="height: 50px; width: 50px; object-fit: contain;">
                        <div>
                            <h3 style="margin:0; font-size:1.2rem; color:#0077B6;">{row['name']}</h3>
                            <span style="font-size:0.9rem; color:#64748B;">{row['program']}</span>
                        </div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-weight:bold; color:#023E8A;">₹{row['fees']/100000:.1f}L</div>
                        <span class="match-tag" style="font-size:0.7rem;">{row['placement']} Placed</span>
                    </div>
                </div>
                <div style="margin-top:15px; display:flex; gap:10px; flex-wrap:wrap;">
                    <span class="feature-tag">📍 {row['location']}</span>
                    <span class="feature-tag">⚡ {row['energy'].replace('Distoversity ', '')}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Buttons kept separate for Streamlit interactivity
            b1, b2 = st.columns(2)
            b1.button("Brochure", key=f"br_{index}", use_container_width=True)
            b2.button("Apply", key=f"ap_{index}", type="primary", use_container_width=True)

def render_assessment():
    st.markdown("<h2 style='text-align:center;'>Discover Your Spark</h2>", unsafe_allow_html=True)
    
    with st.form("assessment_form"):
        st.write("**1. When solving a problem, you naturally:**")
        q1 = st.radio("Q1", ["Create ideas (Creator)", "Talk to people (Influencer)", "Organize (Catalyst)", "Analyze (Analyst)"], label_visibility="collapsed")
        st.write("**2. Ideal work environment:**")
        q2 = st.radio("Q2", ["Freedom", "Social", "Structured", "Quiet"], label_visibility="collapsed")
        st.write("**3. Energized when:**")
        q3 = st.radio("Q3", ["Starting things", "Networking", "Completing tasks", "Solving puzzles"], label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.form_submit_button("Reveal My Spark ➤", type="primary", use_container_width=True):
            with st.spinner("Analyzing..."):
                time.sleep(1)
                # Simple Logic
                st.session_state.user_profile = "Distoversity Creator" if "Creator" in q1 else "Distoversity Analyst"
                st.session_state.page = 'Result'
                st.rerun()

def render_result():
    profile = st.session_state.user_profile
    if not profile: st.warning("Please take the assessment first."); st.stop()
    
    st.balloons()
    st.markdown(f"""
    <div style="text-align:center; padding:2rem; background:#F0F9FF; border-radius:24px; margin-bottom:2rem; border:1px solid #BAE6FD;">
        <span style="color:#0077B6; font-weight:700; letter-spacing:1px;">YOUR CORE ENERGY</span>
        <h1 style="color:#023E8A; margin: 10px 0;">{profile}</h1>
        <p>Your spark aligns with innovation and big-picture thinking.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # WHATSAPP SHARE BUTTON (Added as per request)
    wa_url = f"https://wa.me/?text=I%20am%20a%20{profile}%20on%20Distoversity!"
    st.markdown(f"""
    <div style="text-align:center; margin-bottom: 20px;">
        <a href="{wa_url}" target="_blank" style="background:#25D366; color:white; padding:10px 20px; border-radius:30px; text-decoration:none; font-weight:bold;">
            📲 Share Result on WhatsApp
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 Best Fits for You")
    matches = df[df['energy'] == profile]
    for idx, row in matches.iterrows():
        st.info(f"**{row['name']}** - {row['program']} (Fees: ₹{row['fees']})")

def render_eduveer():
    st.markdown("## 🤖 Eduveer AI")
    
    with st.container(border=True):
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
        
        if prompt := st.chat_input("Ask about fees, placements..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            resp = "That's a great question! Check the Explorer tab for details."
            st.session_state.messages.append({"role": "assistant", "content": resp})
            with st.chat_message("assistant"): st.markdown(resp)

def render_faq():
    st.header("❓ FAQ")
    # Custom touch-friendly FAQ list
    faqs = [("How do I choose?", "We use the 4 Genius framework."), ("Are degrees valid?", "Yes, UGC approved.")]
    for q, a in faqs:
        with st.expander(q): st.write(a)

# --- 7. ROUTER ---
if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'Eduveer': render_eduveer()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
elif st.session_state.page == 'FAQ': render_faq()
elif st.session_state.page == 'Institutions': st.title("Partner with us")
elif st.session_state.page == 'About': st.title("About Distoversity")
