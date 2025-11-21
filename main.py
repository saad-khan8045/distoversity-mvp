import streamlit as st
import pandas as pd
import time
import plotly.express as px
import random

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Discover Your Spark",
    page_icon="✨",
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
        --white: #FFFFFF;
    }

    /* Force White Background & Dark Text Everywhere */
    [data-testid="stAppViewContainer"], .stApp, header, footer {
        background-color: var(--bg-light) !important;
        color: var(--text-main) !important;
    }
    
    /* Force Inputs to be White */
    input, textarea, select, div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #CBD5E1 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* Typography Fixes */
    h1, h2, h3, h4, h5, h6, p, span, div, label {
        color: var(--text-main) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        -webkit-text-fill-color: var(--text-main) !important;
    }
    
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif !important;
        color: var(--primary-dark) !important;
        -webkit-text-fill-color: var(--primary-dark) !important;
    }

    /* --- PREMIUM COMPONENTS --- */
    
    /* Glass Cards */
    .d-card {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.05) !important;
        margin-bottom: 1rem !important;
        transition: transform 0.2s ease;
    }
    .d-card:hover {
        transform: translateY(-3px);
        border-color: var(--primary) !important;
    }

    /* Navbar Styling */
    .nav-btn {
        border: 1px solid #E2E8F0 !important;
        background: white !important;
        border-radius: 10px !important;
        padding: 0.5rem !important;
        text-align: center !important;
        cursor: pointer !important;
        transition: 0.2s;
    }
    .nav-btn:hover {
        border-color: var(--primary) !important;
        color: var(--primary) !important;
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

    /* Mobile Optimizations */
    @media (max-width: 768px) {
        .block-container { padding-top: 1rem !important; padding-left: 1rem !important; padding-right: 1rem !important; }
        h1 { font-size: 2rem !important; }
        .stButton > button { width: 100% !important; }
        /* Hide Sidebar on Mobile */
        section[data-testid="stSidebar"] { display: none; }
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA LOAD ---
@st.cache_data
def load_data():
    return pd.DataFrame([
        {"name": "Jain Online", "location": "Bangalore", "naac": "A++", "nirf": "Top 100", "fees": 210000, "program": "MBA Marketing", "energy": "Distoversity Influencer", "type": "Online Degree", "approvals": "UGC-DEB, AICTE", "placement": "98%", "avg_pkg": "6.2 LPA", "highest_pkg": "32 LPA", "highlights": "Strong Alumni, Live Classes", "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Jain_University_logo.png"},
        {"name": "Manipal University Online", "location": "Jaipur", "naac": "A+", "nirf": "Rank 76", "fees": 175000, "program": "MCA Data Science", "energy": "Distoversity Analyst", "type": "Online Degree", "approvals": "UGC, NAAC", "placement": "94%", "avg_pkg": "5.5 LPA", "highest_pkg": "18 LPA", "highlights": "Global Access, Coursera Free", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png"},
        {"name": "Amity University Online", "location": "Global", "naac": "A+", "nirf": "Top 50", "fees": 345000, "program": "BCA Cloud Security", "energy": "Distoversity Creator", "type": "Online Degree", "approvals": "UGC-DEB, WES", "placement": "92%", "avg_pkg": "4.8 LPA", "highest_pkg": "15 LPA", "highlights": "Virtual Job Fairs, Portfolio Building", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png"},
        {"name": "LPU Online", "location": "Global", "naac": "A++", "nirf": "Rank 47", "fees": 160000, "program": "MBA Operations", "energy": "Distoversity Catalyst", "type": "Online Degree", "approvals": "UGC, AICTE", "placement": "91%", "avg_pkg": "5.0 LPA", "highest_pkg": "21 LPA", "highlights": "Affordable, Mentor Support", "img": "https://upload.wikimedia.org/wikipedia/en/d/d4/Lovely_Professional_University_logo.png"},
        {"name": "NMIMS CDOL", "location": "Online", "naac": "A+", "nirf": "Top 20 B-School", "fees": 400000, "program": "MBA Finance", "energy": "Distoversity Analyst", "type": "Online Degree", "approvals": "UGC-DEB, AICTE", "placement": "93%", "avg_pkg": "7.0 LPA", "highest_pkg": "45 LPA", "highlights": "Premium Brand, Leadership Focus", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/NMIMS_University_logo.png/220px-NMIMS_University_logo.png"},
        {"name": "DY Patil Online", "location": "Pune", "naac": "A++", "nirf": "Rank 46", "fees": 120000, "program": "BBA General", "energy": "Distoversity Catalyst", "type": "Online Degree", "approvals": "UGC, AICTE", "placement": "90%", "avg_pkg": "4.2 LPA", "highest_pkg": "12 LPA", "highlights": "Flexible Exams, Mentor Support", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Dr._D._Y._Patil_Vidyapeeth_logo.png/220px-Dr._D._Y._Patil_Vidyapeeth_logo.png"}
    ])

df = load_data()

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'user_scores' not in st.session_state: st.session_state.user_scores = {}
if 'messages' not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Hello! I am Eduveer. I can help you find the perfect university based on your Genius Profile. What's on your mind?"}]

# --- 5. COMPONENT FUNCTIONS ---

def navbar():
    # Simplified Mobile-Friendly Navbar
    with st.container():
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown("<h3 style='margin:0; padding:0;'>Distoversity<span style='color:#00B4D8'>.</span></h3>", unsafe_allow_html=True)
        with c2:
            # A simple dropdown for mobile navigation
            page = st.selectbox("", ["Home", "About", "Explorer", "Eduveer Bot", "Assessment"], label_visibility="collapsed")
            if page != st.session_state.page:
                st.session_state.page = page
                st.rerun()
    st.markdown("---")

def render_home():
    st.markdown("""
    <div style="text-align:center; padding: 3rem 1rem;">
        <div style="background:#E0F2FE; color:#0077B6; padding:5px 15px; border-radius:20px; display:inline-block; font-weight:700; font-size:0.8rem; margin-bottom:15px;">SCIENTIFIC CAREER CERTAINTY</div>
        <h1 style="font-size: 2.8rem; line-height:1.2;">STOP GUESSING.<br>START ENGINEERING.</h1>
        <p style="color:#475569; font-size:1.1rem; margin-top:1rem;">
            The Era of Subjective Career Advice is Obsolete.<br>
            We provide <b>Strategic Clarity</b> via <b>Computational Rigor</b> using our proprietary 4D Energy Model.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🚀 Start Strategic Assessment", use_container_width=True):
            st.session_state.page = 'Assessment'
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Stats / Trust Section
    st.markdown("#### Trusted By Top Grade 'A' Universities")
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown("**AMITY ONLINE**")
    c2.markdown("**MANIPAL**")
    c3.markdown("**NMIMS**")
    c4.markdown("**JAIN**")

def render_assessment():
    st.markdown("<h2 style='text-align:center;'>Discover Your Core Genius</h2>", unsafe_allow_html=True)
    
    with st.form("assessment_form"):
        st.markdown("#### 1. When solving a problem, you naturally:")
        q1 = st.radio("q1", ["Generate ideas (Creator)", "Discuss with others (Influencer)", "Follow steps (Catalyst)", "Analyze data (Analyst)"], label_visibility="collapsed")
        
        st.markdown("#### 2. You feel most energized when:")
        q2 = st.radio("q2", ["Creating something new", "Presenting ideas", "Completing tasks", "Solving puzzles"], label_visibility="collapsed")
        
        st.markdown("#### 3. In a team, you are the:")
        q3 = st.radio("q3", ["Visionary", "Connector", "Implementer", "Auditor"], label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.form_submit_button("Reveal My Spark ➤", type="primary", use_container_width=True):
            with st.spinner("Analyzing Neural Patterns..."):
                time.sleep(1.5)
                # Mock Logic for Demo
                scores = {"Distoversity Creator": 0, "Distoversity Influencer": 0, "Distoversity Catalyst": 0, "Distoversity Analyst": 0}
                map_key = {"Generate": "Distoversity Creator", "Discuss": "Distoversity Influencer", "Follow": "Distoversity Catalyst", "Analyze": "Distoversity Analyst"}
                
                # Simple scoring based on Q1
                selected = q1.split(" ")[0]
                for k, v in map_key.items():
                    if k in selected: scores[v] += 5
                
                st.session_state.user_profile = max(scores, key=scores.get)
                st.session_state.user_scores = scores
                st.session_state.page = 'Result'
                st.rerun()

def render_result():
    profile = st.session_state.user_profile
    if not profile: st.warning("Take assessment first!"); return
    
    st.balloons()
    st.markdown(f"""
    <div class="d-card" style="text-align:center; background:#F0F9FF !important; border-color:#BAE6FD !important;">
        <h4 style="color:#0077B6 !important;">YOUR CORE GENIUS IS</h4>
        <h1 style="color:#0077B6 !important; font-size:3rem !important;">{profile.replace('Distoversity ', '')}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 University Matches for You")
    matches = df[df['energy'] == profile]
    for idx, row in matches.iterrows():
        st.markdown(f"""
        <div class="d-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <img src="{row['img']}" height="50">
                <div style="text-align:right;">
                    <h3 style="margin:0;">{row['name']}</h3>
                    <p style="margin:0; color:green;">{row['placement']} Placement</p>
                </div>
            </div>
            <hr>
            <p><b>Fee:</b> ₹{row['fees']:,} | <b>Pkg:</b> {row['highest_pkg']}</p>
            <button style="width:100%; background:#0077B6; color:white; border:none; padding:10px; border-radius:5px;">View Details</button>
        </div>
        """, unsafe_allow_html=True)

def render_explorer():
    st.title("🏫 University Explorer")
    
    # Search & Filter
    col1, col2 = st.columns(2)
    with col1:
        budget = st.slider("Max Budget (₹)", 50000, 500000, 250000)
    with col2:
        sort = st.selectbox("Sort By", ["Fees: Low to High", "Placement %"])
    
    filtered = df[df['fees'] <= budget]
    
    if sort == "Fees: Low to High":
        filtered = filtered.sort_values("fees")
    else:
        filtered = filtered.sort_values("placement", ascending=False)
        
    for idx, row in filtered.iterrows():
        st.markdown(f"""
        <div class="d-card">
            <h4>{row['name']}</h4>
            <p>📍 {row['location']} | 🏆 {row['naac']}</p>
            <div style="display:flex; justify-content:space-between; font-weight:bold;">
                <span>₹{row['fees']:,}</span>
                <span style="color:#0077B6;">{row['energy']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_eduveer():
    st.title("Chat with Eduveer 🤖")
    
    with st.container(height=500, border=True):
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
            
        if prompt := st.chat_input("Ask about fees, placements..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            # Basic Response Logic
            time.sleep(0.5)
            response = "That's a great question! I recommend checking the Explorer tab for exact fee structures. Generally, EMI options start at ₹3000/month."
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)

def render_about():
    st.title("The Founder's Story")
    st.markdown("""
    <div class="d-card" style="border-left: 5px solid #F97316 !important;">
        <h3>The Struggle</h3>
        <p><b>2019:</b> Arrived in Delhi. Worked in factories (Oppo/Yazaki). 
        Saw hardworking people stuck because they lacked guidance.</p>
    </div>
    <div class="d-card" style="border-left: 5px solid #10B981 !important;">
        <h3>The Solution</h3>
        <p>Founded <b>Distoversity</b> to combine Psychology (Wealth Dynamics) + AI. 
        We don't just sell degrees; we architect careers.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 6. MAIN ROUTER ---
navbar()

if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'Eduveer Bot': render_eduveer()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
elif st.session_state.page == 'FAQ': render_faq() # (Add FAQ function if needed or remove)
