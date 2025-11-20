final version of website 


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

# --- 2. ULTRA-PREMIUM DESIGN SYSTEM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    :root {
        --primary: #0077B6;       /* Deep Sky Blue */
        --primary-dark: #023E8A;
        --primary-light: #ADE8F4;
        --accent: #00B4D8;        /* Bright Blue */
        --text-main: #0F172A;
        --text-sub: #475569;
        --white: #FFFFFF;
        --hero-gradient: radial-gradient(circle at 50% 0%, #E0F2FE 0%, #FFFFFF 70%); 
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-main);
        background-color: #FFFFFF;
        scroll-behavior: smooth;
    }

    /* HEADERS */
    h1, h2, h3 { font-family: 'Outfit', sans-serif; color: var(--primary-dark); font-weight: 800; }
    h1 { font-size: 4rem !important; letter-spacing: -2px; line-height: 1.1; }
    
    /* MOBILE ADJUSTMENT */
    @media (max-width: 768px) {
        h1 { font-size: 2.5rem !important; }
        .nav-logo { font-size: 1.5rem !important; }
        .hero-section { padding: 2rem 1rem !important; }
        
        /* Sticky Button Visibility */
        .sticky-cta { display: block !important; }
    }

    /* COMPONENT: PREMIUM GLASS CARD */
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

    /* COMPONENT: AI REPORT CARD */
    .ai-report-box {
        background: #F8FAFC;
        border-left: 5px solid #0EA5E9;
        padding: 20px;
        margin-bottom: 20px;
        font-family: 'Courier New', monospace;
        font-size: 0.95rem;
    }
    
    /* COMPONENT: CTA BOX */
    .cta-box {
        background: linear-gradient(135deg, #0077B6 0%, #023E8A 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 25px rgba(0, 119, 182, 0.3);
    }
    .cta-box h3 { color: white !important; margin-bottom: 10px; }

    /* COMPONENT: TAGS */
    .feature-tag {
        background: #F1F5F9; color: #475569; padding: 4px 12px; 
        border-radius: 20px; font-size: 0.8rem; font-weight: 600; 
        display: inline-block; margin-right: 5px; margin-bottom: 5px;
    }
    .match-tag {
        background: #DCFCE7; color: #166534; padding: 4px 12px; 
        border-radius: 20px; font-size: 0.8rem; font-weight: 700;
    }

    /* COMPONENT: ASSESSMENT QUESTION TEXT */
    .question-text {
        font-size: 1.2rem;
        font-weight: 600;
        color: #0F172A;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }

    /* --- NAVIGATION STYLING (HORIZONTAL SCROLL) --- */
    div[role="radiogroup"] {
        display: flex;
        flex-direction: row;
        overflow-x: auto;
        white-space: nowrap;
        padding-bottom: 10px;
        justify-content: center;
    }
    div[role="radiogroup"] label {
        background-color: #F8FAFC;
        padding: 10px 20px;
        border-radius: 30px;
        margin: 0 5px;
        border: 1px solid #E2E8F0;
        transition: all 0.3s;
    }
    div[role="radiogroup"] label:hover {
        border-color: #0077B6;
        color: #0077B6;
    }

    /* --- ASSESSMENT FORM FIX (VERTICAL ALIGNMENT) --- */
    /* Overrides horizontal nav style ONLY inside the form */
    [data-testid="stForm"] div[role="radiogroup"] {
        flex-direction: column !important; 
        background-color: transparent !important;
        padding: 0 !important;
        justify-content: flex-start !important;
        overflow: visible !important;
    }
    [data-testid="stForm"] div[role="radiogroup"] label {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        margin-bottom: 10px !important;
        width: 100% !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }
    [data-testid="stForm"] div[role="radiogroup"] label:hover {
        border-color: #0077B6 !important;
        background-color: #F0F9FF !important;
    }

    .nav-logo { font-family: 'Outfit'; font-weight: 800; font-size: 1.8rem; color: var(--primary-dark); }
    
    /* COMPONENT: BUTTONS */
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
    
    /* HERO */
    .hero-section {
        background: var(--hero-gradient);
        padding: 6rem 2rem 5rem 2rem;
        text-align: center;
        border-radius: 0 0 60px 60px;
        margin-bottom: 4rem;
        border-bottom: 1px solid #E0F2FE;
    }

    /* UTILS */
    .icon-circle {
        width: 60px; height: 60px; background: #F0F9FF; border-radius: 50%; 
        display: flex; align-items: center; justify-content: center; 
        font-size: 1.8rem; margin: 0 auto 1rem auto; color: var(--primary);
    }

    /* SCROLLABLE CHAT CONTAINER */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 20px;
    }

    /* STICKY MOBILE BUTTON (Hidden on Desktop) */
    .sticky-cta {
        display: none;
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 9999;
        width: 90%;
    }
    .sticky-btn {
        background: linear-gradient(90deg, #0077B6 0%, #00B4D8 100%);
        color: white;
        padding: 15px;
        border-radius: 50px;
        text-align: center;
        font-weight: bold;
        box-shadow: 0 10px 25px rgba(0, 119, 182, 0.4);
        display: block;
        text-decoration: none;
    }

    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA ENGINE (With Caching for Speed) ---
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

# --- 5. AI GENERATION LOGIC & POPUP (INCLUDES ALISON) ---
def generate_report_text(profile, scores):
    core_type = profile.replace("Distoversity ", "")
    pain_point = ""
    achilles_heel = ""
    skills = []
    alison_courses = []
    
    if core_type == "Creator":
        pain_point = "You despise routine. Ambiguity is your playground."
        achilles_heel = "The 'Idea Junkie' Syndrome."
        skills = ["Systems Thinking", "Project Management", "Strategic Leadership"]
        alison_courses = ["Diploma in Innovation Management", "Design Thinking - A Primer"]
    elif core_type == "Influencer":
        pain_point = "You hate isolation and spreadsheets."
        achilles_heel = "The 'Surface Level' Trap."
        skills = ["Data Analytics", "Financial Literacy", "Operational Execution"]
        alison_courses = ["Diploma in Social Media Marketing", "Public Speaking & Communication"]
    elif core_type == "Catalyst":
        pain_point = "You hate chaos and vague instructions."
        achilles_heel = "The 'Cog in the Wheel' Risk."
        skills = ["Innovation Strategy", "Public Speaking", "Agile Leadership"]
        alison_courses = ["Diploma in Project Management", "Operations Management Supervision"]
    elif core_type == "Analyst":
        pain_point = "You hate hype and emotional decision making."
        achilles_heel = "Analysis Paralysis."
        skills = ["Persuasive Communication", "Team Management", "Creative Problem Solving"]
        alison_courses = ["Data Science Fundamentals", "Advanced Excel Training"]

    return f"""
### 🚨 THE URGENT TRUTH ABOUT YOUR CAREER
**Your Profile: {profile}**

Most people guess their career path. You don't have to. 
You are a **{core_type}**, which means you are wired for specific high-value roles, not generic jobs.

**Why you feel stuck:**
{pain_point}

---
### ⚠️ THE RISK OF IGNORING THIS
**Your Achilles Heel: {achilles_heel}**
If you don't align your degree with your energy, you risk burning out in a job you hate within 3 years.

---
### 🚀 YOUR MILLION-RUPEE ROADMAP
To dominate your industry, you need these exact skills:
1. **{skills[0]}**
2. **{skills[1]}**
3. **{skills[2]}**

---
### 🎓 FREE UPSKILLING (Powered by Alison)
As a Distoversity member, we recommend these **FREE** courses to bridge your gap immediately:
* **{alison_courses[0]}**
* **{alison_courses[1]}**

**Don't just get a degree. Build an unfair advantage.**
"""

@st.dialog("⚡ CHIEF GENIUS OFFICER REPORT")
def show_popup_report(profile, scores):
    report_content = generate_report_text(profile, scores)
    
    # Using st.container to prevent HTML formatting issues
    with st.container(border=True):
        st.markdown(report_content)
        
    st.markdown("""<div class="cta-box"><h3>🚀 STOP GUESSING. START WINNING.</h3><p>Expert Career Strategy Call (Usually ₹1999, FREE for you today).</p></div>""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("📞 Claim My Free Career Strategy Call", type="primary", use_container_width=True):
        st.success("Request Received! Our Chief Genius Officer will contact you within 2 hours.")
        time.sleep(2)
        st.rerun()

# --- 6. NAVIGATION SYSTEM ---
def navbar():
    with st.container():
        c1, c2, c3, c4, c5, c6, c7, c8 = st.columns([1.5, 0.8, 0.8, 0.8, 0.8, 0.8, 1, 1.5])
        with c1:
            st.markdown("<div class='nav-logo'>Distoversity<span style='color:#0EA5E9'>.</span></div>", unsafe_allow_html=True)
        
        # Horizontal menu logic logic
        if c2.button("Home", use_container_width=True): st.session_state.page = 'Home'; st.rerun()
        if c3.button("About", use_container_width=True): st.session_state.page = 'About'; st.rerun()
        if c4.button("Explorer", use_container_width=True): st.session_state.page = 'Explorer'; st.rerun()
        if c5.button("FAQ", use_container_width=True): st.session_state.page = 'FAQ'; st.rerun()
        if c6.button("Partners", use_container_width=True): st.session_state.page = 'Institutions'; st.rerun()
        if c7.button("🤖 Eduveer", use_container_width=True): st.session_state.page = 'Eduveer'; st.rerun()
        if c8.button("Take Assessment", type="primary", use_container_width=True): st.session_state.page = 'Assessment'; st.rerun()

# --- 7. PAGES ---

def render_home():
    st.markdown("""
    <div class="hero-section">
        <div class="hero-badge" style="background:rgba(0,119,182,0.1); color:#0077B6; padding:8px 20px; border-radius:30px; display:inline-block; font-weight:700; font-size:0.9rem; margin-bottom:20px;">SCIENTIFIC CAREER CERTAINTY</div>
        <h1 style="margin-bottom:20px; font-size:4.5rem; background:-webkit-linear-gradient(45deg, #0077B6, #00B4D8); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">STOP GUESSING YOUR FUTURE.<br>START ENGINEERING IT.</h1>
        <p style="max-width:800px; margin:0 auto 40px auto; font-size:1.3rem; color:#475569;">
            The Era of Subjective Career Advice is Obsolete.<br>
            We provide <b>Strategic Clarity</b> via <b>Computational Rigor</b> using our proprietary 4D Energy Model.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🚀 Start Strategic Profile Assessment", key="home_cta", use_container_width=True):
            st.session_state.page = 'Assessment'
            st.rerun()

    st.markdown("<br><p style='text-align:center; font-weight:700; color:#94A3B8; letter-spacing:1px;'>TRUSTED BY INDIA'S TOP GRADE 'A' UNIVERSITIES</p>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, p in enumerate(["AMITY ONLINE", "MANIPAL", "JAIN ONLINE", "NMIMS CDOL", "LPU ONLINE"]):
        cols[i].markdown(f"<h3 style='text-align:center; color:#0F172A; opacity:0.8; font-size:1.1rem;'>{p}</h3>", unsafe_allow_html=True)

    # "Why Distoversity" Section
    st.markdown("<br><br><h2 style='text-align:center;'>Why Distoversity?</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748B; max-width:600px; margin:0 auto 30px auto;'>We don't just match you to a university. We match you to a future where you win.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("""<div class="d-card"><div class="icon-circle">🧠</div><h3 style="text-align:center; font-size:1.5rem;">Scientific Alignment</h3><p style="text-align:center; color:#64748B;">Traditional tests fail to quantify energy. We map your full psychological infrastructure using Wealth Dynamics.</p></div>""", unsafe_allow_html=True)
    with c2: st.markdown("""<div class="d-card"><div class="icon-circle">🤖</div><h3 style="text-align:center; font-size:1.5rem;">AI Powered</h3><p style="text-align:center; color:#64748B;">Eduveer doesn't sleep. Get unbiased, data-driven advice on fees, placements, and syllabus 24/7.</p></div>""", unsafe_allow_html=True)
    with c3: st.markdown("""<div class="d-card"><div class="icon-circle">🚀</div><h3 style="text-align:center; font-size:1.5rem;">Career Architecture</h3><p style="text-align:center; color:#64748B;">Defining specific roles where your energy distribution delivers maximum commercial value.</p></div>""", unsafe_allow_html=True)

def render_explorer():
    st.markdown("## 🏫 University Power Explorer")
    st.markdown("Use our advanced data engine to compare top online universities.")
    
    st.markdown("###⚖️ Compare Universities")
    compare_list = st.multiselect("Select up to 3 universities to compare side-by-side:", df['name'].tolist(), max_selections=3)
    
    if compare_list:
        st.markdown("<br>", unsafe_allow_html=True)
        comp_df = df[df['name'].isin(compare_list)].set_index('name')
        display_cols = ['fees', 'placement', 'avg_pkg', 'highest_pkg', 'naac', 'approvals', 'highlights']
        st.dataframe(comp_df[display_cols].style.format(thousands=","), use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 🔍 Find Your Match")
    c1, c2, c3, c4 = st.columns(4)
    with c1: max_fee = st.slider("Max Budget (₹)", 50000, 500000, 350000, 50000)
    with c2: energy_filter = st.multiselect("Energy Fit", ["Distoversity Creator", "Distoversity Influencer", "Distoversity Catalyst", "Distoversity Analyst"], default=["Distoversity Creator", "Distoversity Analyst", "Distoversity Influencer", "Distoversity Catalyst"])
    with c3: sort_by = st.selectbox("Sort By", ["Lowest Fees", "Highest Placement %", "Highest Avg Package"])
    with c4: min_placement = st.slider("Min Placement %", 50, 100, 80)

    filtered_df = df[(df['fees'] <= max_fee) & (df['energy'].isin(energy_filter)) & (df['placement'].str.replace('%','').astype(int) >= min_placement)]
    if sort_by == "Lowest Fees": filtered_df = filtered_df.sort_values(by='fees')
    elif sort_by == "Highest Placement %": filtered_df = filtered_df.sort_values(by='placement', ascending=False)
    
    st.write(f"Showing **{len(filtered_df)}** universities based on your filters:")
    
    for idx, row in filtered_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="d-card" style="margin-bottom:20px; border-left: 5px solid #0077B6; padding: 1.5rem;">
                <div style="display:flex; justify-content:space-between; align-items:start; flex-wrap: wrap; gap: 15px;">
                    <div style="display:flex; align-items:center; gap:20px; flex: 2;">
                        <img src="{row['img']}" height="70" style="object-fit:contain; max-width:100px;">
                        <div>
                            <h3 style="margin:0; font-size:1.4rem; color:#023E8A;">{row['name']}</h3>
                            <div style="margin-top:5px;">
                                <span class="feature-tag">📍 {row['location']}</span>
                                <span class="feature-tag">🏆 {row['naac']}</span>
                                <span class="feature-tag">📜 {row['approvals']}</span>
                            </div>
                            <p style="margin-top:8px; font-size:0.9rem; color:#64748B;"><b>Highlights:</b> {row['highlights']}</p>
                        </div>
                    </div>
                    <div style="text-align:right; flex: 1; border-left:1px solid #E2E8F0; padding-left:20px;">
                        <div style="font-weight:800; color:#0077B6; font-size:1.5rem;">₹{row['fees']:,}</div>
                        <p style="margin:0; font-size:0.9rem; color:#475569;">Total Fees</p>
                        <div style="margin-top:10px;">
                            <span style="color:#16A34A; font-weight:700;">{row['placement']} Placement</span><br>
                            <span style="font-size:0.85rem; color:#64748B;">Avg Pkg: {row['avg_pkg']}</span>
                        </div>
                        <div style="margin-top:10px;">
                            <span class="match-tag">⚡ {row['energy']}</span>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            c_btn1, c_btn2, c_space = st.columns([1, 1, 4])
            with c_btn1: st.button(f"View Brochure", key=f"broch_{idx}", use_container_width=True)
            with c_btn2: st.button(f"Apply Now", key=f"apply_{idx}", type="primary")

def render_assessment():
    st.markdown("""<div style="text-align:center; margin-bottom:40px;"><h2 style="font-size:2.5rem; color:#0077B6;">Discover Your Core Genius</h2><p style="color:#64748B;">We map your success trajectory by answering 5 high-level questions.</p></div>""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        with st.form("assessment_form"):
            q1_options = ["Generate multiple creative solutions (Creator)", "Discuss with others to find consensus (Influencer)", "Follow proven step-by-step methods (Catalyst)", "Analyze data and metrics first (Analyst)"]
            st.markdown('<p class="question-text">1. When solving a problem, you naturally:</p>', unsafe_allow_html=True)
            q1 = st.radio("q1_select", q1_options, label_visibility="collapsed", index=None)
            
            q2_options = ["Freedom to experiment and innovate", "Collaborative team settings", "Structured processes and clear timelines", "Quiet space for deep analytical work"]
            st.markdown('<p class="question-text">2. Your ideal work environment involves:</p>', unsafe_allow_html=True)
            q2 = st.radio("q2_select", q2_options, label_visibility="collapsed", index=None)
            
            q3_options = ["Creating something new from scratch", "Presenting ideas and influencing outcomes", "Completing tasks on schedule", "Perfecting systems and solving puzzles"]
            st.markdown('<p class="question-text">3. You feel most energized when:</p>', unsafe_allow_html=True)
            q3 = st.radio("q3_select", q3_options, label_visibility="collapsed", index=None)
            
            q4_options = ["Intuitive and pattern-based", "People-focused and consensus-driven", "Experience-based and practical", "Data-driven and logical"]
            st.markdown('<p class="question-text">4. Your decision-making style is:</p>', unsafe_allow_html=True)
            q4 = st.radio("q4_select", q4_options, label_visibility="collapsed", index=None)
            
            q5_options = ["Share innovative concepts and possibilities", "Build relationships and network actively", "Organize action items and ensure follow-through", "Provide data-backed insights and analysis"]
            st.markdown('<p class="question-text">5. In group settings, you naturally:</p>', unsafe_allow_html=True)
            q5 = st.radio("q5_select", q5_options, label_visibility="collapsed", index=None)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.form_submit_button("Reveal My Spark ➤", type="primary", use_container_width=True):
                if None in [q1, q2, q3, q4, q5]:
                    st.warning("Please answer all questions to reveal your profile.")
                else:
                    with st.spinner("Analyzing your Energy Profile with Multidimensional Regression..."):
                        time.sleep(1.5)
                        scores = {"Distoversity Creator": 0, "Distoversity Influencer": 0, "Distoversity Catalyst": 0, "Distoversity Analyst": 0}
                        profile_map = ["Distoversity Creator", "Distoversity Influencer", "Distoversity Catalyst", "Distoversity Analyst"]
                        answers_indices = [q1_options.index(q1), q2_options.index(q2), q3_options.index(q3), q4_options.index(q4), q5_options.index(q5)]
                        for idx in answers_indices:
                            scores[profile_map[idx]] += 1
                        final_scores = {k: (v/5)*100 for k,v in scores.items()}
                        st.session_state.user_profile = max(scores, key=scores.get)
                        st.session_state.user_scores = final_scores
                        st.session_state.page = 'Result'
                        st.rerun()

def render_result():
    profile = st.session_state.user_profile
    scores = st.session_state.user_scores
    if not profile: st.warning("Take assessment first!"); st.stop()
    st.balloons()
    st.markdown(f"""<div style="text-align:center; padding:3rem; background:#F0F9FF; border-radius:20px; border:1px solid #BAE6FD; margin-bottom:3rem;"><div style="color:#0077B6; font-weight:700;">YOUR CORE GENIUS IS</div><h1 style="color:#0077B6;">{profile}</h1></div>""", unsafe_allow_html=True)
    
    st.markdown("### 📊 Energy Breakdown")
    c_stats = st.columns(4)
    c_stats[0].metric("Creator", f"{int(scores['Distoversity Creator'])}%")
    c_stats[1].metric("Influencer", f"{int(scores['Distoversity Influencer'])}%")
    c_stats[2].metric("Catalyst", f"{int(scores['Distoversity Catalyst'])}%")
    c_stats[3].metric("Analyst", f"{int(scores['Distoversity Analyst'])}%")
    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🎯 Potential University Matches")
        matches = df[df['energy'] == profile]
        for idx, row in matches.iterrows():
             st.markdown(f"""<div class="d-card" style="margin-bottom:1rem; padding:1.5rem;"><h4>{row['name']}</h4><p>✅ Aligns with {profile} learning style</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("### 🗺️ Your Full Genius Profile")
        email = st.text_input("Enter Email to Unlock Full Results", key="email_input")
        if st.button("Generate My AI Report Now", use_container_width=True):
            if email:
                with st.spinner("Connecting to AI Neural Network..."):
                    time.sleep(2)
                    show_popup_report(profile, scores)

def render_about():
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("## The Distoversity Story")
        st.markdown("""<div class="timeline-item"><h4>2019: The Struggle</h4><p>Arrived in Delhi. Middle-class background. Zero guidance. I was the person from a middle-class family with no opportunity.</p></div><div class="timeline-item"><h4>The Realization</h4><p>Worked in SMT/Electrical departments at companies like Yazaki and Oppo. Recognized that 'Sales' drives education, not 'Need'.</p></div><div class="timeline-item"><h4>The Solution</h4><p>Founded Distoversity to combine Wealth Dynamics + AI. We believe Education is a Right. Our aim is Empowering India.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")

def render_faq():
    st.title("❓ Frequently Asked Questions")
    tab1, tab2, tab3 = st.tabs(["🌟 Career Guidance", "💻 Online Education", "🎓 Universities"])
    with tab1:
        st.header("General Education & Career")
        with st.expander("❓ I'm confused about my career path after high school. How can Distoversity help?"):
            st.write("We help you discover your 'Genius Profile' (natural strengths) via AI, guiding you to academic fields and careers that truly fit you.")
        with st.expander("❓ Is the Distoversity 'Genius Profile' a psychological test?"):
            st.write("No, it is a self-discovery and guidance tool based on Wealth Dynamics, not a psychological diagnostic test.")
        with st.expander("❓ How accurate are the recommendations?"):
            st.write("Our recommendations are based on data-driven matching of your profile with university strengths, leading to a 92% satisfaction rate.")
        with st.expander("❓ What do Dynamo, Blaze, Tempo, and Steel mean?"):
            st.write("Dynamo = Ideas (Creator), Blaze = People (Influencer), Tempo = Timing (Catalyst), Steel = Details (Analyst).")

    with tab2:
        st.header("Online Education & Learning Trends")
        with st.expander("❓ Is online education a good option?"):
            st.write("Yes! Your profile determines your online fit. We match you to programs that suit your learning style.")
        with st.expander("❓ Will my online degree be recognized?"):
            st.write("Absolutely. All our partner universities are UGC/NAAC accredited, making their degrees valid for jobs and higher education.")
        with st.expander("❓ Is tech making education affordable?"):
            st.write("Yes, technology reduces infrastructure costs, allowing top universities to offer degrees at a fraction of the campus cost.")

    with tab3:
        st.header("Universities & Admissions")
        with st.expander("❓ Which universities partner with Distoversity?"):
            st.write("We partner only with NAAC A+ and A++ accredited universities like Amity, Manipal, Jain, and NMIMS.")
        with st.expander("❓ How do I apply?"):
            st.write("Once you find your match, you can request a brochure or book a call. Our counselors will guide you through the application process.")

def render_institutions():
    st.markdown("""
    <div class="hero-section">
        <h1>Recruit Students Aligned With Your <span style="color:#00B4D8">Institutional DNA</span></h1>
        <p style="max-width:700px; margin:20px auto; font-size:1.3rem; color:#475569;">
            Stop sorting résumés; start welcoming students who fit. Distoversity uses proprietary AI to match students' Genius Profiles to institutions where they'll thrive.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")
    with c2:
        st.markdown("### Why Partner With Us?")
        st.markdown("""
        - **🎯 Targeted Recruitment:** We don't send you 'leads'; we send you matched candidates based on personality alignment.
        - **📉 Lower Attrition:** Students matched by 'Energy Fit' are 40% less likely to drop out.
        - **🧠 AI-Powered Screening:** Our pre-qualification process ensures you get serious, academic-intent students.
        - **🤝 Exclusive Access:** Get access to our 'Genius Profile' database of pre-assessed students.
        """)
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("Request Partnership Demo", type="primary")

def render_eduveer():
    st.markdown("""<div style="text-align:center; padding-bottom: 20px;"><h1>Chat with <span style="color:#00B4D8">Eduveer AI</span></h1></div>""", unsafe_allow_html=True)
    
    with st.container(height=600, border=True):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]): st.markdown(message["content"])

        if prompt := st.chat_input("Ask Eduveer about fees, syllabus..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            response_text = "I recommend looking at our Explorer tab for detailed fees."
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            with st.chat_message("assistant"): st.markdown(response_text)

# --- STICKY BUTTON (Shows only on Mobile) ---
st.markdown("""<div class="sticky-cta"><a href="#" class="sticky-btn">🚀 Book Career Advice</a></div>""", unsafe_allow_html=True)

# --- 12. MAIN ROUTER ---
navbar()

if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'FAQ': render_faq()
elif st.session_state.page == 'Institutions': render_institutions()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
elif st.session_state.page == 'Eduveer': render_eduveer()
