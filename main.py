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
    initial_sidebar_state="collapsed" # Keeps app clean on mobile
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
    
    /* MOBILE ADJUSTMENT FOR HEADERS */
    @media only screen and (max-width: 600px) {
        h1 { font-size: 2.5rem !important; }
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

    /* COMPONENT: AI REPORT CARD (Inside Modal) */
    .ai-report-box {
        background: #F8FAFC;
        border-left: 5px solid #0EA5E9;
        padding: 20px;
        margin-bottom: 20px;
        font-family: 'Courier New', monospace; /* Tech/AI feel */
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

    /* SIDEBAR STYLING (Replaces Top Nav) */
    [data-testid="stSidebar"] {
        background-color: #F8FAFC;
        border-right: 1px solid #E2E8F0;
    }
    .nav-logo { font-family: 'Outfit'; font-weight: 800; font-size: 1.8rem; color: var(--primary-dark); margin-bottom: 20px;}
    
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

    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. ENRICHED PARTNER DATA ---
UNIVERSITY_DATA = [
    {
        "name": "Jain Online", 
        "location": "Bangalore", 
        "naac": "A++", 
        "nirf": "Top 100",
        "fees": 210000, 
        "program": "MBA Marketing", 
        "energy": "Distoversity Influencer", 
        "type": "Online Degree", 
        "approvals": "UGC-DEB, AICTE", 
        "placement": "98%",
        "avg_pkg": "6.2 LPA",
        "highest_pkg": "32 LPA",
        "highlights": "Strong Alumni, Live Classes",
        "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Jain_University_logo.png"
    },
    {
        "name": "Manipal University Online", 
        "location": "Jaipur", 
        "naac": "A+", 
        "nirf": "Rank 76",
        "fees": 175000, 
        "program": "MCA Data Science", 
        "energy": "Distoversity Analyst", 
        "type": "Online Degree", 
        "approvals": "UGC, NAAC", 
        "placement": "94%",
        "avg_pkg": "5.5 LPA",
        "highest_pkg": "18 LPA",
        "highlights": "Global Access, Coursera Free",
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png"
    },
    {
        "name": "Amity University Online", 
        "location": "Global", 
        "naac": "A+", 
        "nirf": "Top 50",
        "fees": 345000, 
        "program": "BCA Cloud Security", 
        "energy": "Distoversity Creator", 
        "type": "Online Degree", 
        "approvals": "UGC-DEB, WES", 
        "placement": "92%",
        "avg_pkg": "4.8 LPA",
        "highest_pkg": "15 LPA",
        "highlights": "Virtual Job Fairs, Portfolio Building",
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png"
    },
    {
        "name": "LPU Online", 
        "location": "Global", 
        "naac": "A++", 
        "nirf": "Rank 47",
        "fees": 160000, 
        "program": "MBA Operations", 
        "energy": "Distoversity Catalyst", 
        "type": "Online Degree", 
        "approvals": "UGC, AICTE", 
        "placement": "91%",
        "avg_pkg": "5.0 LPA",
        "highest_pkg": "21 LPA",
        "highlights": "Affordable, Mentor Support",
        "img": "https://upload.wikimedia.org/wikipedia/en/d/d4/Lovely_Professional_University_logo.png"
    },
    {
        "name": "Chandigarh University", 
        "location": "Online", 
        "naac": "A+", 
        "nirf": "Rank 29", 
        "fees": 180000, 
        "program": "MBA General", 
        "energy": "Distoversity Influencer", 
        "type": "Online Degree", 
        "approvals": "UGC-DEB", 
        "placement": "89%", 
        "avg_pkg": "5.2 LPA", 
        "highest_pkg": "28 LPA", 
        "highlights": "Flexible Exams, Case Studies", 
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Chandigarh_University_logo.png/220px-Chandigarh_University_logo.png"
    },
    {
        "name": "NMIMS CDOL", 
        "location": "Online", 
        "naac": "A+", 
        "nirf": "Top 20 B-School", 
        "fees": 400000, 
        "program": "MBA Finance", 
        "energy": "Distoversity Analyst", 
        "type": "Online Degree", 
        "approvals": "UGC-DEB, AICTE", 
        "placement": "93%", 
        "avg_pkg": "7.0 LPA", 
        "highest_pkg": "45 LPA", 
        "highlights": "Premium Brand, Leadership Focus", 
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/NMIMS_University_logo.png/220px-NMIMS_University_logo.png"
    },
    {
        "name": "DY Patil Online", 
        "location": "Pune", 
        "naac": "A++", 
        "nirf": "Rank 46", 
        "fees": 120000, 
        "program": "BBA General", 
        "energy": "Distoversity Catalyst", 
        "type": "Online Degree", 
        "approvals": "UGC, AICTE", 
        "placement": "90%", 
        "avg_pkg": "4.2 LPA", 
        "highest_pkg": "12 LPA", 
        "highlights": "Flexible Exams, Mentor Support", 
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Dr._D._Y._Patil_Vidyapeeth_logo.png/220px-Dr._D._Y._Patil_Vidyapeeth_logo.png"
    }
]
df = pd.DataFrame(UNIVERSITY_DATA)

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'user_scores' not in st.session_state: st.session_state.user_scores = {}
if 'messages' not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Hello! I am Eduveer. I can help you find the perfect university based on your Genius Profile. What's on your mind?"}]

# --- 5. MOBILE-FRIENDLY NAVIGATION (SIDEBAR) ---
# Replaces the crashing columns layout
with st.sidebar:
    st.markdown("<div class='nav-logo'>Distoversity<span style='color:#0EA5E9'>.</span></div>", unsafe_allow_html=True)
    
    # Sidebar Navigation Menu
    selected = st.radio(
        "Menu",
        ["Home", "Explorer", "Eduveer AI", "FAQ", "Partners", "About", "Take Assessment"],
        index=0 if st.session_state.page == "Home" else 0,
        label_visibility="collapsed"
    )
    
    # Logic to update page
    if selected == "Home": st.session_state.page = 'Home'
    elif selected == "Explorer": st.session_state.page = 'Explorer'
    elif selected == "Eduveer AI": st.session_state.page = 'Eduveer'
    elif selected == "FAQ": st.session_state.page = 'FAQ'
    elif selected == "Partners": st.session_state.page = 'Institutions'
    elif selected == "About": st.session_state.page = 'About'
    elif selected == "Take Assessment": st.session_state.page = 'Assessment'

    st.divider()
    st.info("Discover Your Spark Today.")

# --- 6. AI GENERATION LOGIC ---
def generate_report_text(profile, scores):
    core_type = profile.replace("Distoversity ", "")
    pain_point = ""
    achilles_heel = ""
    skills = []
    
    if core_type == "Creator":
        pain_point = "You despise routine. Ambiguity is your playground, but execution is your prison."
        achilles_heel = "The 'Idea Junkie' Syndrome."
        skills = ["Systems Thinking", "Project Management", "Strategic Leadership"]
    elif core_type == "Influencer":
        pain_point = "You hate isolation. You thrive on energy, but struggle in silos."
        achilles_heel = "The 'Surface Level' Trap."
        skills = ["Data Analytics", "Financial Literacy", "Operational Execution"]
    elif core_type == "Catalyst":
        pain_point = "You hate chaos. You want a clear target and feel undervalued when 'creatives' get glory."
        achilles_heel = "The 'Cog in the Wheel' Risk."
        skills = ["Innovation Strategy", "Public Speaking", "Agile Leadership"]
    elif core_type == "Analyst":
        pain_point = "You hate hype. You want the data, not a good story."
        achilles_heel = "Analysis Paralysis."
        skills = ["Persuasive Communication", "Team Management", "Creative Problem Solving"]

    report = f"""
    ### SECTION 1: YOUR CORE GENIUS REVEAL
    **Archetype: {profile} ({int(scores.get(profile, 0))}% Match)**
    
    Listen closely: Your brain is wired differently. {pain_point}
    
    ---
    ### SECTION 2: YOUR CRITICAL WEAK POINT
    **The Danger Zone: {achilles_heel}**
    
    ---
    ### SECTION 3: YOUR STRATEGIC ROADMAP
    **The Solution: Your Next Move**
    1. **{skills[0]}**
    2. **{skills[1]}**
    3. **{skills[2]}**
    """
    return report

@st.dialog("⚡ CHIEF GENIUS OFFICER REPORT")
def show_popup_report(profile, scores):
    report_content = generate_report_text(profile, scores)
    st.markdown(f"""<div class="ai-report-box">{report_content}</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="cta-box"><h3>🚀 The Final Decision</h3><p>You are standing at a crossroads. Step into clarity.</p></div>""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("📞 Book My Career Advice Call Now", type="primary", use_container_width=True):
        st.success("Request Received!")
        time.sleep(2)
        st.rerun()

# --- 7. PAGE RENDERERS ---

def render_home():
    st.markdown("""
    <div class="hero-section">
        <div class="hero-badge" style="background:rgba(0,119,182,0.1); color:#0077B6; padding:8px 20px; border-radius:30px; display:inline-block; font-weight:700; font-size:0.9rem; margin-bottom:20px;">CAREER ARCHITECTURE FOR PROFESSIONALS</div>
        <h1 style="margin-bottom:20px; font-size:4.5rem; background:-webkit-linear-gradient(45deg, #0077B6, #00B4D8); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Don't Just Upgrade Your Degree.<br>Upgrade Your Identity.</h1>
        <p style="max-width:800px; margin:0 auto 40px auto; font-size:1.3rem; color:#475569;">
            Whether you are a student or a working professional, alignment is everything.<br>
            We match your <b>Core Professional Identity</b> to India's Top Online Universities.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🚀 Discover Your Spark (Free)", key="home_cta", use_container_width=True):
            st.session_state.page = 'Assessment'
            st.rerun()

    st.markdown("<br><p style='text-align:center; font-weight:700; color:#94A3B8; letter-spacing:1px;'>TRUSTED BY STUDENTS OF TOP UNIVERSITIES</p>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, p in enumerate(["AMITY ONLINE", "MANIPAL", "JAIN ONLINE", "NMIMS CDOL", "LPU ONLINE"]):
        cols[i].markdown(f"<h3 style='text-align:center; color:#0F172A; opacity:0.8; font-size:1.1rem;'>{p}</h3>", unsafe_allow_html=True)

    st.markdown("<br><br><h2 style='text-align:center;'>Why Professionals Choose Us</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="d-card"><div class="icon-circle">🧠</div><h3 style="text-align:center; font-size:1.5rem;">Identity Analysis</h3><p style="text-align:center; color:#64748B;">Stop forcing yourself into roles you hate. Find your natural flow.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="d-card"><div class="icon-circle">🏫</div><h3 style="text-align:center; font-size:1.5rem;">Online Degrees</h3><p style="text-align:center; color:#64748B;">Valid degrees from UGC-approved universities like Amity & Manipal.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="d-card"><div class="icon-circle">🚀</div><h3 style="text-align:center; font-size:1.5rem;">Career Roadmap</h3><p style="text-align:center; color:#64748B;">Integrate your degree with <b>ALISON</b> certifications for maximum impact.</p></div>""", unsafe_allow_html=True)

def render_explorer():
    st.markdown("## 🏫 University Power Explorer")
    st.markdown("Use our advanced data engine to compare top online universities. **All listed are UGC/AICTE Approved.**")
    
    # 1. COMPARISON WIDGET
    st.markdown("###⚖️ Compare Universities")
    compare_list = st.multiselect("Select up to 3 universities to compare side-by-side:", df['name'].tolist(), max_selections=3)
    
    if compare_list:
        st.markdown("<br>", unsafe_allow_html=True)
        comp_df = df[df['name'].isin(compare_list)].set_index('name')
        display_cols = ['fees', 'placement', 'avg_pkg', 'highest_pkg', 'naac', 'approvals', 'highlights']
        st.dataframe(comp_df[display_cols].style.format(thousands=","), use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # 2. ADVANCED FILTERS
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
            with c_btn1: st.button(f"View Brochure", key=f"broch_{idx}")
            with c_btn2: st.button(f"Apply Now", key=f"apply_{idx}", type="primary")

def render_assessment():
    st.markdown("""<div style="text-align:center; margin-bottom:40px;"><h2 style="font-size:2.5rem; color:#0077B6;">Discover Your Spark</h2><p style="color:#64748B;">Answer these 5 questions to find your core energy type.</p></div>""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        with st.form("assessment_form"):
            st.markdown('<p class="question-text">1. When solving a problem, you naturally:</p>', unsafe_allow_html=True)
            q1 = st.radio("q1_select", ["Generate multiple creative solutions (Creator)", "Discuss with others to find consensus (Influencer)", "Follow proven step-by-step methods (Catalyst)", "Analyze data and metrics first (Analyst)"], label_visibility="collapsed")
            st.markdown('<p class="question-text">2. Your ideal work environment involves:</p>', unsafe_allow_html=True)
            q2 = st.radio("q2_select", ["Freedom to experiment and innovate", "Collaborative team settings", "Structured processes and clear timelines", "Quiet space for deep analytical work"], label_visibility="collapsed")
            st.markdown('<p class="question-text">3. You feel most energized when:</p>', unsafe_allow_html=True)
            q3 = st.radio("q3_select", ["Creating something new from scratch", "Presenting ideas and influencing outcomes", "Completing tasks on schedule", "Perfecting systems and solving puzzles"], label_visibility="collapsed")
            st.markdown('<p class="question-text">4. Your decision-making style is:</p>', unsafe_allow_html=True)
            q4 = st.radio("q4_select", ["Intuitive and pattern-based", "People-focused and consensus-driven", "Experience-based and practical", "Data-driven and logical"], label_visibility="collapsed")
            st.markdown('<p class="question-text">5. In group settings, you naturally:</p>', unsafe_allow_html=True)
            q5 = st.radio("q5_select", ["Share innovative concepts and possibilities", "Build relationships and network actively", "Organize action items and ensure follow-through", "Provide data-backed insights and analysis"], label_visibility="collapsed")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.form_submit_button("Reveal My Spark ➤", type="primary", use_container_width=True):
                with st.spinner("Analyzing your Energy Profile..."):
                    time.sleep(1.5)
                    answers = [q1, q2, q3, q4, q5]
                    counts = {"Distoversity Creator": 0, "Distoversity Influencer": 0, "Distoversity Catalyst": 0, "Distoversity Analyst": 0}
                    for a in answers:
                        if "Creator" in a or "innovate" in a or "scratch" in a or "Intuitive" in a: counts["Distoversity Creator"] += 1
                        elif "Influencer" in a or "Collaborative" in a or "Presenting" in a or "People" in a: counts["Distoversity Influencer"] += 1
                        elif "Catalyst" in a or "Structured" in a or "schedule" in a or "Experience" in a: counts["Distoversity Catalyst"] += 1
                        else: counts["Distoversity Analyst"] += 1
                    scores = {k: (v/5)*100 for k,v in counts.items()}
                    st.session_state.user_profile = max(counts, key=counts.get)
                    st.session_state.user_scores = scores
                    st.session_state.page = 'Result'
                    st.rerun()

def render_result():
    profile = st.session_state.user_profile
    scores = st.session_state.user_scores
    if not profile: st.warning("Take assessment first!"); st.stop()

    st.balloons()
    st.markdown(f"""
    <div style="text-align:center; padding:3rem; background:#F0F9FF; border-radius:20px; border:1px solid #BAE6FD; margin-bottom:3rem;">
        <div style="color:#0077B6; font-weight:700; letter-spacing:2px;">YOUR CORE ENERGY IS</div>
        <h1 style="font-size:5rem !important; color:#0077B6; margin:10px 0;">{profile}</h1>
        <p style="font-size:1.2rem;">Your Spark profile aligns with specific high-growth environments.</p>
        <div style="display:flex; justify-content:center; gap:20px; margin-top:20px; flex-wrap:wrap;">
            <span class="feature-tag">Creator: {int(scores['Distoversity Creator'])}%</span>
            <span class="feature-tag">Influencer: {int(scores['Distoversity Influencer'])}%</span>
            <span class="feature-tag">Catalyst: {int(scores['Distoversity Catalyst'])}%</span>
            <span class="feature-tag">Analyst: {int(scores['Distoversity Analyst'])}%</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🎯 Potential University Matches")
        matches = df[df['energy'] == profile]
        for idx, row in matches.iterrows():
             st.markdown(f"""<div class="d-card" style="margin-bottom:1rem; padding:1.5rem;"><h4>{row['name']}</h4><p style="margin-top:10px;">✅ Aligns with {profile} learning style</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("### 🗺️ Your Full Genius Profile")
        st.markdown("""<div class="d-card"><h4>4-Year Strategic Roadmap</h4><p class="blur-content">Year 1: Foundation...</p></div><br>""", unsafe_allow_html=True)
        email = st.text_input("Enter Email to Unlock Full Results", key="email_input")
        if st.button("Generate My AI Report Now", use_container_width=True):
            if email:
                with st.spinner("Connecting to AI Neural Network..."):
                    time.sleep(2)
                    show_popup_report(profile, scores)

def render_eduveer():
    st.markdown("""
    <div class="hero-section" style="padding-bottom: 2rem; margin-bottom: 2rem;">
        <h1>Chat with <span style="color:#00B4D8">Eduveer AI</span></h1>
        <p style="color:#475569;">Your 24/7 Academic Counselor.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="d-card" style="min-height: 500px; display: flex; flex-direction: column;">', unsafe_allow_html=True)
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Ask Eduveer about MBA fees, courses..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Simulated Response
            response_text = "I can help with that! Based on your request, I recommend looking at our Explorer tab for detailed fees."
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            with st.chat_message("assistant"):
                st.markdown(response_text)
        
        st.markdown('</div>', unsafe_allow_html=True)

def render_about():
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("## The Distoversity Story")
        st.markdown("""<div class="timeline-item"><h4>2019: The Struggle</h4><p>Arrived in Delhi. Middle-class background. Zero guidance.</p></div><div class="timeline-item"><h4>The Factory Floor (Yazaki & Oppo)</h4><p>Worked in SMT/Electrical depts. Saw brilliant engineers failing because of misalignment.</p></div><div class="timeline-item"><h4>The Solution</h4><p>Founded Distoversity to combine Wealth Dynamics + AI to fix Career Misalignment.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")

def render_faq():
    st.title("❓ Frequently Asked Questions")
    with st.expander("❓ I'm confused about my career path."):
        st.write("We help you discover your 'Genius Profile' via AI.")

def render_institutions():
    st.markdown("""<div class="hero-section"><h1>Recruit Students Aligned With Your <span style="color:#00B4D8">Institutional DNA</span></h1></div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.image("https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")
    with c2: 
        st.markdown("### Why Partner With Us?")
        st.button("Request Partnership Demo")

# --- 8. MAIN ROUTER ---
if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'FAQ': render_faq()
elif st.session_state.page == 'Institutions': render_institutions()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
elif st.session_state.page == 'Eduveer': render_eduveer()
