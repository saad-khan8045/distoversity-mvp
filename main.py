
FINAL WEBSITE 



import streamlit as st
import pandas as pd
import time
import plotly.express as px

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

    /* COMPONENT: ASSESSMENT QUESTION TEXT (FIXED) */
    .question-text {
        font-size: 1.2rem;
        font-weight: 600;
        color: #0F172A;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }

    /* COMPONENT: STICKY NAV */
    div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stHorizontalBlock"]) {
        position: sticky;
        top: 0;
        background-color: rgba(255, 255, 255, 0.98);
        z-index: 999;
        padding-top: 1rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #F1F5F9;
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

    /* ALISON */
    .alison-section {
        background: linear-gradient(135deg, #FFF7ED 0%, #FFFFFF 100%);
        border: 1px solid #FFEDD5;
        border-radius: 24px;
        padding: 3rem;
        text-align: center;
        margin-top: 5rem;
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
        "energy": "Influencer", 
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
        "energy": "Analyst", 
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
        "energy": "Creator", 
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
        "energy": "Catalyst", 
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
        "energy": "Influencer", 
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
        "energy": "Analyst", 
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
        "energy": "Catalyst", 
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

# --- 5. NAVIGATION SYSTEM (UPDATED WITH INSTITUTIONS) ---
def navbar():
    with st.container():
        c1, c2, c3, c4, c5, c6, c7 = st.columns([2, 1, 1, 1, 1, 1, 1.5])
        with c1:
            st.markdown("<div class='nav-logo'>Distoversity<span style='color:#0EA5E9'>.</span></div>", unsafe_allow_html=True)
        
        if c2.button("Home", use_container_width=True): st.session_state.page = 'Home'; st.rerun()
        if c3.button("About", use_container_width=True): st.session_state.page = 'About'; st.rerun()
        if c4.button("Explorer", use_container_width=True): st.session_state.page = 'Explorer'; st.rerun()
        if c5.button("FAQ", use_container_width=True): st.session_state.page = 'FAQ'; st.rerun()
        # New Button: For Institutions
        if c6.button("Partners", use_container_width=True): st.session_state.page = 'Institutions'; st.rerun()
        
        if c7.button("Take Assessment", type="primary", use_container_width=True): st.session_state.page = 'Assessment'; st.rerun()

# --- 6. PAGE: HOME ---
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

    # Features
    st.markdown("<br><br><h2 style='text-align:center;'>Why Professionals Choose Us</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="d-card"><div class="icon-circle">🧠</div><h3 style="text-align:center; font-size:1.5rem;">Identity Analysis</h3><p style="text-align:center; color:#64748B;">Stop forcing yourself into roles you hate. Find your natural flow.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="d-card"><div class="icon-circle">🏫</div><h3 style="text-align:center; font-size:1.5rem;">Online Degrees</h3><p style="text-align:center; color:#64748B;">Valid degrees from UGC-approved universities like Amity & Manipal.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="d-card"><div class="icon-circle">🚀</div><h3 style="text-align:center; font-size:1.5rem;">Career Roadmap</h3><p style="text-align:center; color:#64748B;">Integrate your degree with <b>ALISON</b> certifications for maximum impact.</p></div>""", unsafe_allow_html=True)

    # ALISON
    st.markdown("""
    <div class="alison-section">
        <h3 style="color:#D97706; font-size:2rem; margin-bottom:1rem;">🎓 Upskill with ALISON</h3>
        <p style="color:#92400E; font-size:1.1rem; max-width:700px; margin:0 auto 2rem auto;">
            We have partnered with <b>ALISON</b> to provide free certification courses.
        </p>
        <div style="display:flex; gap:15px; justify-content:center; flex-wrap:wrap;">
            <span style="background:white; padding:10px 20px; border-radius:30px; border:1px solid #FED7AA; color:#D97706; font-weight:600;">📜 Project Management</span>
            <span style="background:white; padding:10px 20px; border-radius:30px; border:1px solid #FED7AA; color:#D97706; font-weight:600;">💻 IT Support</span>
            <span style="background:white; padding:10px 20px; border-radius:30px; border:1px solid #FED7AA; color:#D97706; font-weight:600;">🗣️ Communication</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 7. PAGE: POWER EXPLORER ---
def render_explorer():
    st.markdown("## 🏫 University Power Explorer")
    st.markdown("Use our advanced data engine to compare top online universities. **All listed are UGC/AICTE Approved.**")
    
    # 1. COMPARISON WIDGET
    st.markdown("### ⚖️ Compare Universities")
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
    with c1:
        max_fee = st.slider("Max Budget (₹)", 50000, 500000, 350000, 50000)
    with c2:
        energy_filter = st.multiselect("Energy Fit", ["Creator", "Influencer", "Catalyst", "Analyst"], default=["Creator", "Analyst", "Influencer", "Catalyst"])
    with c3:
        sort_by = st.selectbox("Sort By", ["Lowest Fees", "Highest Placement %", "Highest Avg Package"])
    with c4:
        min_placement = st.slider("Min Placement %", 50, 100, 80)

    # 3. FILTERING LOGIC
    filtered_df = df[
        (df['fees'] <= max_fee) & 
        (df['energy'].isin(energy_filter)) &
        (df['placement'].str.replace('%','').astype(int) >= min_placement)
    ]
    
    if sort_by == "Lowest Fees":
        filtered_df = filtered_df.sort_values(by='fees')
    elif sort_by == "Highest Placement %":
        filtered_df = filtered_df.sort_values(by='placement', ascending=False)
    
    st.write(f"Showing **{len(filtered_df)}** universities based on your filters:")
    
    # 4. DISPLAY CARDS
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
                                <span class="feature-tag">🏆 NAAC {row['naac']}</span>
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
                            <span class="match-tag">⚡ {row['energy']} Fit</span>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            c_btn1, c_btn2, c_space = st.columns([1, 1, 4])
            with c_btn1:
                 st.button(f"View Brochure", key=f"broch_{idx}")
            with c_btn2:
                 st.button(f"Apply Now", key=f"apply_{idx}", type="primary")

# --- 8. PAGE: ASSESSMENT (5 Questions - "Discover Your Spark") ---
def render_assessment():
    st.markdown("""
    <div style="text-align:center; margin-bottom:40px;">
        <h2 style="font-size:2.5rem; color:#0077B6; margin-bottom:10px;">Discover Your Spark</h2>
        <p style="color:#64748B; font-size:1.1rem;">Answer these 5 questions to find your core energy type.</p>
        <p style="font-size:0.85rem; color:#94A3B8;"><i>Distoversity's Genius Profile is a tool for career guidance based on personal preferences. It is not a substitute for professional psychological counseling or a guarantee of job placement.</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        with st.form("assessment_form"):
            # Q1
            st.markdown('<p class="question-text">1. When solving a problem, you naturally:</p>', unsafe_allow_html=True)
            q1 = st.radio("q1_select", [
                "Generate multiple creative solutions (Creator)",
                "Discuss with others to find consensus (Influencer)",
                "Follow proven step-by-step methods (Catalyst)",
                "Analyze data and metrics first (Analyst)"
            ], label_visibility="collapsed")
            
            # Q2
            st.markdown('<p class="question-text">2. Your ideal work environment involves:</p>', unsafe_allow_html=True)
            q2 = st.radio("q2_select", [
                "Freedom to experiment and innovate",
                "Collaborative team settings",
                "Structured processes and clear timelines",
                "Quiet space for deep analytical work"
            ], label_visibility="collapsed")
            
            # Q3
            st.markdown('<p class="question-text">3. You feel most energized when:</p>', unsafe_allow_html=True)
            q3 = st.radio("q3_select", [
                "Creating something new from scratch",
                "Presenting ideas and influencing outcomes",
                "Completing tasks on schedule",
                "Perfecting systems and solving puzzles"
            ], label_visibility="collapsed")

            # Q4
            st.markdown('<p class="question-text">4. Your decision-making style is:</p>', unsafe_allow_html=True)
            q4 = st.radio("q4_select", [
                "Intuitive and pattern-based",
                "People-focused and consensus-driven",
                "Experience-based and practical",
                "Data-driven and logical"
            ], label_visibility="collapsed")

            # Q5
            st.markdown('<p class="question-text">5. In group settings, you naturally:</p>', unsafe_allow_html=True)
            q5 = st.radio("q5_select", [
                "Share innovative concepts and possibilities",
                "Build relationships and network actively",
                "Organize action items and ensure follow-through",
                "Provide data-backed insights and analysis"
            ], label_visibility="collapsed")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.form_submit_button("Reveal My Spark ➤", type="primary", use_container_width=True):
                with st.spinner("Analyzing your Energy Profile..."):
                    time.sleep(1.5)
                
                # Logic: Simple Majority
                answers = [q1, q2, q3, q4, q5]
                counts = {"Creator": 0, "Influencer": 0, "Catalyst": 0, "Analyst": 0}
                
                for a in answers:
                    if "Creator" in a or "innovate" in a or "scratch" in a or "Intuitive" in a or "concepts" in a: counts["Creator"] += 1
                    elif "Influencer" in a or "Collaborative" in a or "Presenting" in a or "People" in a or "relationships" in a: counts["Influencer"] += 1
                    elif "Catalyst" in a or "Structured" in a or "schedule" in a or "Experience" in a or "Organize" in a: counts["Catalyst"] += 1
                    else: counts["Analyst"] += 1
                
                winner = max(counts, key=counts.get)
                st.session_state.user_profile = winner
                st.session_state.page = 'Result'
                st.rerun()

# --- 9. PAGE: RESULT (GATED & COMPLIANT) ---
def render_result():
    profile = st.session_state.user_profile
    if not profile: st.warning("Take assessment first!"); st.stop()

    st.balloons()
    st.markdown(f"""
    <div style="text-align:center; padding:3rem; background:#F0F9FF; border-radius:20px; border:1px solid #BAE6FD; margin-bottom:3rem;">
        <div style="color:#0077B6; font-weight:700; letter-spacing:2px;">YOUR CORE ENERGY IS</div>
        <h1 style="font-size:5rem !important; color:#0077B6; margin:10px 0;">{profile}</h1>
        <p style="font-size:1.2rem;">Your Spark profile aligns with specific high-growth environments.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🎯 Potential University Matches")
        matches = df[df['energy'] == profile]
        for idx, row in matches.iterrows():
             st.markdown(f"""
            <div class="d-card" style="margin-bottom:1rem; padding:1.5rem;">
                <div style="display:flex; justify-content:space-between;">
                    <h4 style="margin:0;">{row['name']}</h4>
                    <span class="match-tag">Potential Fit</span>
                </div>
                <p style="margin-top:10px;">✅ Aligns with {profile} learning style</p>
            </div>
            """, unsafe_allow_html=True)
            
    with c2:
        st.markdown("### 🗺️ Your Full Genius Profile")
        st.markdown("""
        <div class="d-card" style="margin-bottom:1rem;">
             <h4>Your Superpowers</h4>
             <p class="blur-content">Innovation, Big Picture Thinking...</p>
             <h4>Your Blind Spots</h4>
             <p class="blur-content">Routine tasks, detailed follow-through...</p>
        </div>
        <div style="position:relative;">
            <div class="d-card"><h4>4-Year Strategic Roadmap</h4><p class="blur-content">Year 1: Foundation...</p></div>
            <div class="lock-badge">
                <div style="font-size:3rem;">🔒</div>
                <h3>Unlock Full Genius Profile</h3>
                <p>Get 15-Page Report + University List</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("lead"):
            email = st.text_input("Enter Email to Unlock Full Results")
            st.caption("🔒 We collect your email to send results and recommendations. We will never sell your data. Your information is stored securely per Indian and global data protection regulations.")
            
            if st.form_submit_button("Send My Full Profile & University Matches Now", use_container_width=True):
                st.success("Redirecting to Payment Gateway...")

# --- 10. PAGE: ABOUT & FAQ (FULL CONTENT) ---
def render_about():
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("## The Distoversity Story")
        st.markdown("""
        <div class="timeline-item">
            <h4>2019: The Struggle</h4>
            <p>Arrived in Delhi. Middle-class background. Zero guidance.</p>
        </div>
        <div class="timeline-item">
            <h4>The Factory Floor (Yazaki & Oppo)</h4>
            <p>Worked in SMT/Electrical depts. Saw brilliant engineers failing because of misalignment.</p>
        </div>
        <div class="timeline-item">
            <h4>The Solution</h4>
            <p>Founded Distoversity to combine Wealth Dynamics + AI to fix Career Misalignment.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")

def render_faq():
    st.title("❓ Frequently Asked Questions")
    
    tab1, tab2, tab3 = st.tabs(["🌟 Career Guidance", "💻 Online Education", "🎓 Universities"])
    
    with tab1:
        st.header("General Education & Career")
        with st.expander("❓ I'm confused about my career path after high school. How can Distoversity help?"):
            st.write("We help you discover your 'Genius Profile' (natural strengths) via AI, guiding you to academic fields and careers that truly fit you.")
        with st.expander("❓ Is the Distoversity 'Genius Profile' a psychological test or a definitive career predictor?"):
            st.write("It's a self-discovery and guidance tool based on Wealth Dynamics, not a psychological diagnostic test or guarantee.")
        with st.expander("❓ How accurate are Distoversity's recommendations?"):
            st.write("Our AI matches your Genius Profile to suitable institutions for informed guidance and a high relevance score.")
        with st.expander("❓ How does Distoversity personalize university recommendations?"):
            st.write("Our AI analyzes your Genius Profile (Dynamo, Blaze, Tempo, Steel) to match you with best-fit universities and programs.")
        with st.expander("❓ What is the 'Genius Profile' and what do Dynamo, Blaze, Tempo, and Steel mean?"):
            st.write("It's your natural strength: Dynamo (Ideas), Blaze (People), Tempo (Timing), Steel (Systems/Details).")
            
    with tab2:
        st.header("Online Education & Learning Trends")
        with st.expander("❓ Is online education a good option for me, and how can Distoversity help me explore it?"):
            st.write("Your Genius Profile reveals if your learning style thrives in online environments. We help you find matching programs.")
        with st.expander("❓ How can I ensure the quality of an online degree program?"):
            st.write("Look for accredited universities, clear curricula, and strong student support. We recommend reputable institutions.")
        with st.expander("❓ Will an online degree be recognized by employers in India?"):
            st.write("Yes, valid degrees from UGC-approved universities are recognized by employers.")
        with st.expander("❓ Does technology make quality education more affordable through Distoversity?"):
            st.write("Yes, online programs often have lower fees compared to traditional campus programs.")
            
    with tab3:
        st.header("University Programs")
        with st.expander("❓ Which universities partner with you?"):
            st.write("We partner with 16+ top universities including Jain, LPU, Amrita, IGNOU, and DY Patil.")
        with st.expander("❓ How do I apply through Distoversity?"):
            st.write("We guide you through the application process after your assessment and counseling session.")

# --- 11. PAGE: FOR INSTITUTIONS (NEW) ---
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
        st.markdown("- **Targeted Recruitment:** Recruit based on personality alignment.")
        st.markdown("- **Lower Attrition:** Students matched by 'Energy' stay longer.")
        st.markdown("- **Data-Driven:** Access our proprietary AI-matching algorithm.")
        st.button("Request Partnership Demo")

# --- 12. MAIN ROUTER ---
navbar()

if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'FAQ': render_faq()
elif st.session_state.page == 'Institutions': render_institutions()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
