import streamlit as st
import pandas as pd
import time
import plotly.express as px
import random

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Career Architecture",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. ULTRA-PREMIUM SKY BLUE & GREY DESIGN SYSTEM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Inter:wght@300;400;500;600&display=swap');

    :root {
        --primary: #0EA5E9;       /* Sky Blue */
        --primary-dark: #0284C7;  /* Darker Sky Blue for Hover */
        --text-main: #0F172A;     /* Slate 900 */
        --text-light: #475569;    /* Slate 600 */
        --bg-grey: #F8FAFC;       /* Very Light Grey Background */
        --white: #FFFFFF;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--text-main);
        background-color: var(--white);
        scroll-behavior: smooth;
    }

    /* HEADERS - OUTFIT FONT */
    h1, h2, h3, h4 { font-family: 'Outfit', sans-serif; color: var(--text-main); font-weight: 700; }
    h1 { font-size: 3.5rem !important; letter-spacing: -1.5px; }
    
    /* MOBILE TYPOGRAPHY */
    @media (max-width: 768px) {
        h1 { font-size: 2.2rem !important; }
        .nav-logo { font-size: 1.4rem !important; }
        .hero-section { padding: 2rem 1rem !important; }
        .sticky-cta { display: block !important; }
    }

    /* GLASS CARDS */
    .d-card {
        background: var(--white);
        border: 1px solid #E2E8F0; /* Light Grey Border */
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px -5px rgba(14, 165, 233, 0.05); /* Subtle Blue Shadow */
        transition: all 0.3s ease;
        height: 100%;
    }
    .d-card:hover {
        transform: translateY(-5px);
        border-color: var(--primary);
        box-shadow: 0 15px 30px -10px rgba(14, 165, 233, 0.15);
    }
    
    /* CHAT INTERFACE (WHATSAPP STYLE) */
    /* Container for messages */
    .stChatMessage {
        background-color: var(--white);
        border-radius: 15px;
        border: 1px solid #F1F5F9;
        padding: 10px;
        margin-bottom: 10px;
    }
    /* User Message Style Override (simulated via avatar distinction mostly, but CSS helps) */
    div[data-testid="chatAvatarIcon-user"] {
        background-color: var(--primary) !important;
    }

    /* NAVIGATION (HORIZONTAL PILLS) */
    div[role="radiogroup"] {
        display: flex;
        flex-direction: row;
        overflow-x: auto;
        white-space: nowrap;
        padding: 5px;
        background: var(--bg-grey);
        border-radius: 50px;
        justify-content: center;
        border: 1px solid #E2E8F0;
        margin-bottom: 30px;
    }
    div[role="radiogroup"] label {
        padding: 8px 20px;
        border-radius: 40px;
        margin: 0 2px;
        transition: all 0.3s;
        border: none;
        background: transparent;
        color: var(--text-light);
        font-weight: 500;
    }
    div[role="radiogroup"] label:hover {
        color: var(--primary);
        background: #E0F2FE; /* Very Light Blue */
    }
    /* Active State Styling is handled by Streamlit's internal classes usually, 
       but the hover effect gives good feedback */

    /* ASSESSMENT FORM FIX (VERTICAL RESET) */
    [data-testid="stForm"] div[role="radiogroup"] {
        flex-direction: column !important;
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        align-items: stretch !important;
    }
    [data-testid="stForm"] div[role="radiogroup"] label {
        background: var(--white) !important;
        border: 1px solid #E2E8F0 !important;
        margin-bottom: 8px !important;
        border-radius: 12px !important;
        padding: 12px 15px !important;
        width: 100% !important;
        text-align: left !important;
    }
    [data-testid="stForm"] div[role="radiogroup"] label:hover {
        border-color: var(--primary) !important;
        background: #F0F9FF !important;
    }

    /* BUTTONS */
    .stButton>button {
        background: var(--primary);
        color: white;
        border-radius: 50px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        border: none;
        transition: 0.2s;
        box-shadow: 0 4px 12px rgba(14, 165, 233, 0.3);
    }
    .stButton>button:hover {
        background: var(--primary-dark);
        transform: scale(1.02);
        box-shadow: 0 6px 16px rgba(14, 165, 233, 0.4);
    }
    
    /* UTILS */
    .feature-tag { background: #F1F5F9; color: #475569; padding: 4px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: 600; margin-right: 5px; border: 1px solid #E2E8F0; }
    .match-tag { background: #E0F2FE; color: #0284C7; padding: 4px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: 700; border: 1px solid #BAE6FD; }
    
    /* HIDE DEFAULT */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    /* SCROLL CONTAINER */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 20px;
        border-color: #E2E8F0;
    }
    
    /* STICKY BUTTON (MOBILE) */
    .sticky-cta {
        display: none;
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 9999;
        width: 90%;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .sticky-btn {
        display: block;
        background: var(--primary);
        color: white;
        text-align: center;
        padding: 15px;
        border-radius: 50px;
        font-weight: 700;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA ENGINE (Cached) ---
@st.cache_data
def load_data():
    return pd.DataFrame([
        {"name": "Jain Online", "location": "Bangalore", "naac": "A++", "nirf": "Top 100", "fees": 210000, "program": "MBA Marketing", "energy": "Distoversity Influencer", "type": "Online Degree", "approvals": "UGC-DEB, AICTE", "placement": "98%", "avg_pkg": "6.2 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Jain_University_logo.png"},
        {"name": "Manipal University", "location": "Jaipur", "naac": "A+", "nirf": "Rank 76", "fees": 175000, "program": "MCA Data Science", "energy": "Distoversity Analyst", "type": "Online Degree", "approvals": "UGC, NAAC", "placement": "94%", "avg_pkg": "5.5 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png"},
        {"name": "Amity Online", "location": "Global", "naac": "A+", "nirf": "Top 50", "fees": 345000, "program": "BCA Cloud Security", "energy": "Distoversity Creator", "type": "Online Degree", "approvals": "UGC-DEB, WES", "placement": "92%", "avg_pkg": "4.8 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png"},
        {"name": "LPU Online", "location": "Global", "naac": "A++", "nirf": "Rank 47", "fees": 160000, "program": "MBA Operations", "energy": "Distoversity Catalyst", "type": "Online Degree", "approvals": "UGC, AICTE", "placement": "91%", "avg_pkg": "5.0 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/d/d4/Lovely_Professional_University_logo.png"},
        {"name": "NMIMS CDOL", "location": "Online", "naac": "A+", "nirf": "Top 20 B-School", "fees": 400000, "program": "MBA Finance", "energy": "Distoversity Analyst", "type": "Online Degree", "approvals": "UGC-DEB, AICTE", "placement": "93%", "avg_pkg": "7.0 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/NMIMS_University_logo.png/220px-NMIMS_University_logo.png"},
        {"name": "DY Patil Online", "location": "Pune", "naac": "A++", "nirf": "Rank 46", "fees": 120000, "program": "BBA General", "energy": "Distoversity Catalyst", "type": "Online Degree", "approvals": "UGC, AICTE", "placement": "90%", "avg_pkg": "4.2 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Dr._D._Y._Patil_Vidyapeeth_logo.png/220px-Dr._D._Y._Patil_Vidyapeeth_logo.png"}
    ])

df = load_data()

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'user_scores' not in st.session_state: st.session_state.user_scores = {}
if 'messages' not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Hi there! I'm Eduveer. I can help you find the perfect university based on your Genius Profile. What's on your mind?"}]

# --- 5. AI REPORT LOGIC (PERSUASIVE + ALISON) ---
def generate_report_text(profile, scores):
    core_type = profile.replace("Distoversity ", "")
    
    # Content Strategy: Validation -> Pain -> Roadmap
    if core_type == "Creator":
        pain = "You despise routine. Ambiguity is your playground, but execution is your prison."
        heel = "The 'Idea Junkie' Syndrome (Starting 50 projects, finishing 0)."
        skills = ["Systems Thinking", "Strategic Delegation", "Product Launch Systems"]
        alison = ["Diploma in Innovation Management", "Design Thinking - A Primer"]
    elif core_type == "Influencer":
        pain = "You hate isolation. Spreadsheets drain you; people energize you."
        heel = "The 'Surface Level' Trap (All talk, no action)."
        skills = ["Data Analytics", "Financial Literacy", "High-Ticket Negotiation"]
        alison = ["Diploma in Social Media Marketing", "Public Speaking & Communication"]
    elif core_type == "Catalyst":
        pain = "You hate chaos. You need a clear target and a finish line."
        heel = "The 'Cog in the Wheel' Risk (Getting stuck in middle management)."
        skills = ["Innovation Strategy", "Agile Leadership", "Process Automation"]
        alison = ["Diploma in Project Management", "Operations Management Supervision"]
    else: # Analyst
        pain = "You hate hype. You trust data, not emotions."
        heel = "Analysis Paralysis (Waiting for 100% certainty before moving)."
        skills = ["Persuasive Communication", "Risk Quantification", "Leadership Psychology"]
        alison = ["Data Science Fundamentals", "Advanced Excel Training"]

    return f"""
### 🚨 THE URGENT TRUTH ABOUT YOUR CAREER
**Your Profile: {profile}**

Most people guess their career path. You don't have to. You are a **{core_type}**, wired for specific high-value roles.

**Why you feel stuck:** {pain}

---
### ⚠️ THE RISK OF IGNORING THIS
**Your Achilles Heel: {heel}**
If you don't align your degree with your energy, you risk burning out in a job you hate within 3 years.

---
### 🚀 YOUR MILLION-RUPEE ROADMAP
To dominate your industry, master these exact skills:
1. **{skills[0]}**
2. **{skills[1]}**
3. **{skills[2]}**

---
### 🎓 FREE UPSKILLING (Powered by Alison)
As a Distoversity member, start these **FREE** courses today:
* **{alison[0]}**
* **{alison[1]}**

**Don't just get a degree. Build an unfair advantage.**
"""

@st.dialog("⚡ CHIEF GENIUS OFFICER REPORT")
def show_popup_report(profile, scores):
    # Clean Container for Markdown
    with st.container(border=True):
        st.markdown(generate_report_text(profile, scores))
        
    st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <div style="background: #E0F2FE; padding: 15px; border-radius: 15px; border: 1px solid #BAE6FD;">
            <h3 style="color:#0284C7; margin:0;">🚀 STOP GUESSING. START WINNING.</h3>
            <p style="color:#475569; font-size:0.9rem;">Expert Career Strategy Call (Usually ₹1999, FREE today).</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("📞 Claim My Free Career Strategy Call", type="primary", use_container_width=True):
        st.success("Request Received! Redirecting to booking...")
        time.sleep(2)
        st.rerun()

# --- 6. NAVIGATION ---
def navbar():
    with st.container():
        c1, c2, c3, c4, c5, c6, c7, c8 = st.columns([1.5, 0.8, 0.8, 0.8, 0.8, 0.8, 1, 1.5])
        with c1: st.markdown("<div class='nav-logo' style='font-family:Outfit; font-weight:800; font-size:1.8rem; color:#0284C7;'>Distoversity.</div>", unsafe_allow_html=True)
        
        # Horizontal Menu Logic
        nav_options = ["Home", "Explorer", "Eduveer AI", "Assessment", "FAQ", "Partners"]
        
        # Helper to match current page to index
        try: idx = nav_options.index(st.session_state.page)
        except: idx = 0
            
        selected = st.radio("Nav", nav_options, index=idx, horizontal=True, label_visibility="collapsed", key="nav_radio")
        
        if selected != st.session_state.page:
            st.session_state.page = selected
            st.rerun()

# --- 7. PAGES ---

def render_home():
    # Sky Blue Gradient Hero
    st.markdown("""
    <div class="hero-section" style="background: radial-gradient(circle at 50% 0%, #E0F2FE 0%, #FFFFFF 70%); border-radius: 0 0 50px 50px; padding: 5rem 1rem; text-align: center; margin-bottom: 3rem;">
        <span style="background:#FFFFFF; color:#0EA5E9; padding:6px 16px; border-radius:30px; font-size:0.85rem; font-weight:700; border:1px solid #BAE6FD; box-shadow:0 4px 10px rgba(14,165,233,0.1);">SCIENTIFIC CAREER CERTAINTY</span>
        <h1 style="color:#0F172A; margin-top: 20px; margin-bottom: 15px;">STOP GUESSING YOUR FUTURE.<br><span style="color:#0EA5E9;">START ENGINEERING IT.</span></h1>
        <p style="color:#475569; font-size: 1.2rem; max-width: 700px; margin: 0 auto 30px auto;">
            The Era of Subjective Career Advice is Obsolete.<br>
            We provide <b>Strategic Clarity</b> via <b>Computational Rigor</b> using our proprietary 4D Energy Model.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🚀 Start Strategic Profile Assessment", key="hero_cta", type="primary", use_container_width=True):
            st.session_state.page = 'Assessment'
            st.rerun()

    # Trust Signals
    st.markdown("<br><p style='text-align:center; font-weight:600; color:#94A3B8; letter-spacing:1.5px; font-size:0.9rem;'>TRUSTED BY INDIA'S TOP GRADE 'A' UNIVERSITIES</p>", unsafe_allow_html=True)
    cols = st.columns(5)
    for p in ["AMITY", "MANIPAL", "JAIN ONLINE", "NMIMS", "LPU"]:
        cols[list(["AMITY", "MANIPAL", "JAIN ONLINE", "NMIMS", "LPU"]).index(p)].markdown(f"<h4 style='text-align:center; color:#64748B; opacity:0.7;'>{p}</h4>", unsafe_allow_html=True)

    # Why Distoversity Section
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; margin-bottom:10px;'>Why Distoversity?</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748B; margin-bottom:40px;'>We don't just match you to a university. We match you to a future where you win.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("""<div class="d-card"><h3 style="color:#0EA5E9;">🧠 Scientific</h3><p style="color:#475569;">Traditional tests fail. We map your psychological infrastructure using Wealth Dynamics.</p></div>""", unsafe_allow_html=True)
    with c2: st.markdown("""<div class="d-card"><h3 style="color:#0EA5E9;">🤖 AI Powered</h3><p style="color:#475569;">Eduveer doesn't sleep. Get unbiased, data-driven advice on fees and placements 24/7.</p></div>""", unsafe_allow_html=True)
    with c3: st.markdown("""<div class="d-card"><h3 style="color:#0EA5E9;">🚀 Strategic</h3><p style="color:#475569;">We define specific roles where your energy distribution delivers maximum commercial value.</p></div>""", unsafe_allow_html=True)

def render_explorer():
    st.markdown("## 🏫 University Power Explorer")
    st.markdown("Use our advanced data engine to compare top online universities.")
    
    # Filter Bar
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1: max_fee = st.slider("Max Budget (₹)", 100000, 500000, 350000, step=10000)
        with c2: energy_filter = st.multiselect("Energy Fit", ["Distoversity Creator", "Distoversity Influencer", "Distoversity Catalyst", "Distoversity Analyst"], default=["Distoversity Creator", "Distoversity Analyst"])

    filtered_df = df[(df['fees'] <= max_fee) & (df['energy'].isin(energy_filter))]
    
    st.write(f"Showing **{len(filtered_df)}** universities based on your filters:")
    
    # Card Grid
    for idx, row in filtered_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="d-card" style="margin-bottom:15px; padding:1.5rem; border-left: 5px solid #0EA5E9;">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                    <div style="display:flex; align-items:center; gap:15px;">
                        <img src="{row['img']}" height="60" style="object-fit:contain; width:60px;">
                        <div>
                            <h3 style="margin:0; font-size:1.3rem; color:#0F172A;">{row['name']}</h3>
                            <span style="color:#64748B; font-size:0.9rem;">{row['program']}</span>
                        </div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-weight:700; color:#0EA5E9; font-size:1.4rem;">₹{row['fees']:,}</div>
                        <div style="margin-top:5px;">
                            <span class="match-tag">⚡ {row['energy'].replace('Distoversity ', '')}</span>
                        </div>
                    </div>
                </div>
                <div style="margin-top:15px; padding-top:15px; border-top:1px solid #F1F5F9; display:flex; gap:10px;">
                    <span class="feature-tag">📍 {row['location']}</span>
                    <span class="feature-tag">🏆 {row['naac']}</span>
                    <span class="feature-tag">💼 {row['placement']} Placement</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2 = st.columns([1, 1])
            c1.button("View Brochure", key=f"b_{idx}", use_container_width=True)
            c2.button("Apply Now", key=f"a_{idx}", type="primary", use_container_width=True)

def render_assessment():
    st.markdown("""<div style="text-align:center; margin-bottom:40px;"><h2 style="color:#0EA5E9;">Discover Your Core Genius</h2><p style="color:#64748B;">We map your success trajectory by answering 5 high-level questions.</p></div>""", unsafe_allow_html=True)
    
    # Centered Form
    c_main = st.container(border=True)
    with c_main:
        with st.form("assessment_form"):
            q1_ops = ["Generate multiple creative solutions (Creator)", "Discuss with others to find consensus (Influencer)", "Follow proven step-by-step methods (Catalyst)", "Analyze data and metrics first (Analyst)"]
            st.markdown('**1. When solving a problem, you naturally:**')
            q1 = st.radio("q1", q1_ops, label_visibility="collapsed", index=None)
            
            q2_ops = ["Freedom to experiment and innovate", "Collaborative team settings", "Structured processes and clear timelines", "Quiet space for deep analytical work"]
            st.markdown('**2. Your ideal work environment involves:**')
            q2 = st.radio("q2", q2_ops, label_visibility="collapsed", index=None)
            
            q3_ops = ["Creating something new from scratch", "Presenting ideas and influencing outcomes", "Completing tasks on schedule", "Perfecting systems and solving puzzles"]
            st.markdown('**3. You feel most energized when:**')
            q3 = st.radio("q3", q3_ops, label_visibility="collapsed", index=None)
            
            q4_ops = ["Intuitive and pattern-based", "People-focused and consensus-driven", "Experience-based and practical", "Data-driven and logical"]
            st.markdown('**4. Your decision-making style is:**')
            q4 = st.radio("q4", q4_ops, label_visibility="collapsed", index=None)
            
            q5_ops = ["Share innovative concepts and possibilities", "Build relationships and network actively", "Organize action items and ensure follow-through", "Provide data-backed insights and analysis"]
            st.markdown('**5. In group settings, you naturally:**')
            q5 = st.radio("q5", q5_ops, label_visibility="collapsed", index=None)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.form_submit_button("Reveal My Spark ➤", type="primary", use_container_width=True):
                if None in [q1, q2, q3, q4, q5]:
                    st.warning("Please answer all 5 questions.")
                else:
                    with st.spinner("Calculating Multidimensional Regression..."):
                        time.sleep(1)
                        # Logic: Positional Index Mapping
                        scores = {"Distoversity Creator": 0, "Distoversity Influencer": 0, "Distoversity Catalyst": 0, "Distoversity Analyst": 0}
                        map_keys = list(scores.keys())
                        
                        # Add points based on index (0=Creator, 1=Influencer, etc.)
                        for q_val, ops in zip([q1, q2, q3, q4, q5], [q1_ops, q2_ops, q3_ops, q4_ops, q5_ops]):
                            idx = ops.index(q_val)
                            scores[map_keys[idx]] += 1
                            
                        st.session_state.user_profile = max(scores, key=scores.get)
                        st.session_state.user_scores = {k: (v/5)*100 for k,v in scores.items()}
                        st.session_state.page = 'Result'
                        st.rerun()

def render_result():
    profile = st.session_state.user_profile
    scores = st.session_state.user_scores
    if not profile: st.warning("Take assessment first!"); st.stop()
    
    st.balloons()
    st.markdown(f"""
    <div style="text-align:center; padding:3rem; background:#F0F9FF; border-radius:24px; margin-bottom:3rem; border:1px solid #BAE6FD;">
        <p style="color:#0EA5E9; font-weight:700; letter-spacing:1px;">YOUR CORE GENIUS IS</p>
        <h1 style="color:#0284C7; font-size:3.5rem; margin:10px 0;">{profile.replace('Distoversity ', '')}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Energy Breakdown
    st.subheader("📊 Energy Distribution")
    cols = st.columns(4)
    cols[0].metric("Creator", f"{int(scores['Distoversity Creator'])}%")
    cols[1].metric("Influencer", f"{int(scores['Distoversity Influencer'])}%")
    cols[2].metric("Catalyst", f"{int(scores['Distoversity Catalyst'])}%")
    cols[3].metric("Analyst", f"{int(scores['Distoversity Analyst'])}%")
    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🎯 Matched Universities")
        matches = df[df['energy'] == profile]
        for idx, row in matches.iterrows():
             st.markdown(f"""<div class="d-card" style="padding:1rem; margin-bottom:10px; border-left:4px solid #0EA5E9;"><h4>{row['name']}</h4><p style="color:#64748B; font-size:0.9rem;">✅ Perfect fit for {profile} learning style</p></div>""", unsafe_allow_html=True)
    with c2:
        st.subheader("🗺️ Strategic Roadmap")
        st.info("Unlock your 15-Page Strategy Report to see your specific career path.")
        email = st.text_input("Enter Email to Unlock Report", key="email_input")
        if st.button("Generate AI Report Now", type="primary", use_container_width=True):
            if email:
                with st.spinner("Connecting to AI..."):
                    time.sleep(2)
                    show_popup_report(profile, scores)

def render_about():
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("## The Distoversity Story")
        st.markdown("""
        <div style="border-left:3px solid #0EA5E9; padding-left:20px; margin-bottom:20px;">
            <h4 style="margin:0;">2019: The Struggle</h4>
            <p style="color:#64748B;">Arrived in Delhi. Middle-class background. Zero guidance. I was the person with no opportunity.</p>
        </div>
        <div style="border-left:3px solid #0EA5E9; padding-left:20px; margin-bottom:20px;">
            <h4 style="margin:0;">The Realization</h4>
            <p style="color:#64748B;">Worked in SMT/Electrical departments at companies like Yazaki and Oppo. Recognized that 'Sales' drives education, not 'Need'.</p>
        </div>
        <div style="border-left:3px solid #0EA5E9; padding-left:20px;">
            <h4 style="margin:0;">The Solution</h4>
            <p style="color:#64748B;">Founded Distoversity to combine Wealth Dynamics + AI. We believe Education is a Right. Our aim is Empowering India.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")

def render_faq():
    st.title("❓ Frequently Asked Questions")
    tab1, tab2, tab3 = st.tabs(["🌟 Career", "💻 Online Ed", "🎓 Universities"])
    with tab1:
        with st.expander("I'm confused about my career path."): st.write("We use AI to discover your Genius Profile.")
        with st.expander("Is this a psychological test?"): st.write("No, it's a success trajectory tool based on Wealth Dynamics.")
    with tab2:
        with st.expander("Is online education valid?"): st.write("Yes, all our partners are UGC/NAAC accredited.")
    with tab3:
        with st.expander("How do I apply?"): st.write("Book a session and we handle the rest.")

def render_institutions():
    st.markdown("""
    <div class="hero-section" style="padding:3rem 1rem; background:#F8FAFC; border-radius:30px;">
        <h1 style="text-align:center;">Recruit Students Aligned With Your <span style="color:#0EA5E9;">Institutional DNA</span></h1>
        <p style="text-align:center; max-width:700px; margin:0 auto; color:#64748B;">
            Stop sorting résumés; start welcoming students who fit. Distoversity uses proprietary AI to match students' Genius Profiles to institutions where they'll thrive.
        </p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")
    with c2:
        st.markdown("### Why Partner With Us?")
        st.markdown("- **🎯 Targeted Recruitment:** Matched candidates based on personality.")
        st.markdown("- **📉 Lower Attrition:** Students are 40% less likely to drop out.")
        st.markdown("- **🧠 AI-Powered Screening:** Pre-qualified for academic intent.")
        st.button("Request Partnership Demo", type="primary")

# --- WHATSAPP STYLE CHAT (FIXED) ---
def render_eduveer():
    st.markdown("""<div style="text-align:center; margin-bottom:20px;"><h1>Chat with <span style="color:#0EA5E9;">Eduveer AI</span></h1><p style="color:#64748B;">Your 24/7 Career Architect.</p></div>""", unsafe_allow_html=True)
    
    # Fixed height container creates the "WhatsApp Web" scroll effect
    with st.container(height=500, border=True):
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
    
    # Input stays at bottom natively
    if prompt := st.chat_input("Ask Eduveer about fees, syllabus, or your profile..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun() # Instant refresh to show message
        
    # Handle response after rerun to prevent lag
    if st.session_state.messages[-1]["role"] == "user":
        with st.spinner("Eduveer is thinking..."):
            time.sleep(1)
            response = "I recommend looking at our Explorer tab for detailed fees."
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

# --- STICKY MOBILE BUTTON ---
st.markdown("""<div class="sticky-cta"><a href="#" class="sticky-btn">🚀 Book Career Advice</a></div>""", unsafe_allow_html=True)

# --- MAIN ROUTER ---
navbar()

if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'FAQ': render_faq()
elif st.session_state.page == 'Institutions': render_institutions()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
elif st.session_state.page == 'Eduveer': render_eduveer()
