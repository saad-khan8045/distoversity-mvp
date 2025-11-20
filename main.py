import streamlit as st
import pandas as pd
import time
import plotly.express as px

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Career Architecture for Professionals",
    page_icon="🚀",
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

    /* COMPONENT: COMPARISON TABLE */
    .stDataFrame { border-radius: 16px; overflow: hidden; border: 1px solid #E2E8F0; }

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
    }
]
df = pd.DataFrame(UNIVERSITY_DATA)

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'compare_list' not in st.session_state: st.session_state.compare_list = []

# --- 5. NAVIGATION ---
def navbar():
    with st.container():
        c1, c2, c3, c4, c5, c6 = st.columns([2, 1, 1, 1, 1, 1.5])
        with c1:
            st.markdown("<div class='nav-logo'>Distoversity<span style='color:#0EA5E9'>.</span></div>", unsafe_allow_html=True)
        
        if c2.button("Home", use_container_width=True): st.session_state.page = 'Home'; st.rerun()
        if c3.button("About", use_container_width=True): st.session_state.page = 'About'; st.rerun()
        if c4.button("Explorer", use_container_width=True): st.session_state.page = 'Explorer'; st.rerun()
        if c5.button("FAQ", use_container_width=True): st.session_state.page = 'FAQ'; st.rerun()
        if c6.button("Take Assessment", type="primary", use_container_width=True): st.session_state.page = 'Assessment'; st.rerun()

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
        if st.button("🚀 Discover Your Career Energy (Free)", key="home_cta", use_container_width=True):
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

# --- 7. PAGE: POWER EXPLORER (ENHANCED) ---
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

# --- 8. PAGE: ASSESSMENT (REFINED) ---
def render_assessment():
    # Centered Header
    st.markdown("""
    <div style="text-align:center; margin-bottom:40px;">
        <h2 style="font-size:2.5rem; color:#0077B6; margin-bottom:10px;">Decode Your Professional DNA</h2>
        <p style="color:#64748B; font-size:1.1rem;">This isn't a test. It's a diagnostic tool for your career.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Centered Form Container (Visual trick using columns)
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        with st.form("assessment_form"):
            # Question 1: Clean HTML styling
            st.markdown('<p class="question-text">1. In a high-pressure project, what role do you naturally take?</p>', unsafe_allow_html=True)
            q1 = st.radio("q1_select", [
                "💡 The Idea Generator (I hate details)",
                "🗣️ The Presenter (I love talking)",
                "⚡ The Organizer (I keep things on time)",
                "📊 The Analyst (I check the data)"
            ], label_visibility="collapsed")
            
            # Question 2: Clean HTML styling
            st.markdown('<p class="question-text">2. What drains your energy the most?</p>', unsafe_allow_html=True)
            q2 = st.radio("q2_select", [
                "Routine and repetitive data entry",
                "Working alone in a quiet room",
                "Chaos and unclear instructions",
                "Emotional conflict and sales"
            ], label_visibility="collapsed")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Submit Button
            if st.form_submit_button("Analyze My Profile ➤", type="primary", use_container_width=True):
                with st.spinner("Mapping Neural Pathways..."):
                    time.sleep(1.5)
                
                # Logic
                if "Idea" in q1: st.session_state.user_profile = "Creator"
                elif "Presenter" in q1: st.session_state.user_profile = "Influencer"
                elif "Organizer" in q1: st.session_state.user_profile = "Catalyst"
                else: st.session_state.user_profile = "Analyst"
                
                st.session_state.page = 'Result'
                st.rerun()

# --- 9. PAGE: RESULT ---
def render_result():
    profile = st.session_state.user_profile
    if not profile: st.warning("Take assessment first!"); st.stop()

    st.balloons()
    st.markdown(f"""
    <div style="text-align:center; padding:3rem; background:#F0F9FF; border-radius:20px; border:1px solid #BAE6FD; margin-bottom:3rem;">
        <div style="color:#0077B6; font-weight:700; letter-spacing:2px;">PRIMARY ARCHETYPE DETECTED</div>
        <h1 style="font-size:5rem !important; color:#0077B6; margin:10px 0;">{profile}</h1>
        <p style="font-size:1.2rem;">Your core professional identity maps to specific high-growth careers.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🎯 Top University Matches")
        matches = df[df['energy'] == profile]
        for idx, row in matches.iterrows():
             st.markdown(f"""
            <div class="d-card" style="margin-bottom:1rem; padding:1.5rem;">
                <div style="display:flex; justify-content:space-between;">
                    <h4 style="margin:0;">{row['name']}</h4>
                    <span class="match-tag">94% Match</span>
                </div>
                <p style="margin-top:10px;">✅ High Alignment with {profile} Energy</p>
            </div>
            """, unsafe_allow_html=True)
            
    with c2:
        st.markdown("### 🗺️ Your Strategic Roadmap")
        st.markdown("""
        <div class="d-card alison-card" style="margin-bottom:1rem;">
            <h4>Recommended ALISON Courses</h4>
            <p>To complement your degree, we recommend these free certifications:</p>
            <ul>
                <li>Diploma in Project Management</li>
                <li>Operations Management</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="position:relative; filter:blur(8px); opacity:0.5;">
            <div class="d-card"><h4>Year 1: Foundation</h4><p>Focus on core skills...</p></div>
        </div>
        <div style="position:absolute; top:80%; left:75%; transform:translate(-50%, -50%); background:white; padding:2rem; border-radius:16px; box-shadow:0 20px 40px rgba(0,0,0,0.1); text-align:center; width:300px;">
            <div style="font-size:3rem;">🔒</div>
            <h3>Unlock Full Report</h3>
            <p>Get your 15-Page Strategy + 1:1 Session</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("lead"):
            email = st.text_input("Enter Email to Unlock")
            if st.form_submit_button("Unlock Now - ₹499", use_container_width=True):
                st.success("Redirecting to Payment...")

# --- 10. PAGE: ABOUT & FAQ ---
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
        st.header("General Guidance")
        with st.expander("❓ I'm confused about my career path. How can Distoversity help?"):
            st.write("We help you discover your 'Genius Profile' (natural strengths) via AI, guiding you to academic fields and careers that truly fit you.")
        with st.expander("❓ Is the Distoversity 'Genius Profile' a psychological test?"):
            st.write("It's a self-discovery and guidance tool based on Wealth Dynamics, not a psychological diagnostic test or guarantee.")
        with st.expander("❓ How accurate are Distoversity's recommendations?"):
            st.write("Our AI matches your Genius Profile to suitable institutions for informed guidance and a high relevance score.")
        with st.expander("❓ What is the 'Genius Profile' and what do Dynamo, Blaze, Tempo, and Steel mean?"):
            st.write("It's your natural strength: Dynamo (Ideas), Blaze (People), Tempo (Timing), Steel (Systems/Details).")
            
    with tab2:
        st.header("Online Education")
        with st.expander("❓ Is online education a good option for me?"):
            st.write("Your Genius Profile reveals if your learning style thrives in online environments. We help you find matching programs.")
        with st.expander("❓ How can I ensure the quality of an online degree program?"):
            st.write("Look for accredited universities, clear curricula, and strong student support. We recommend reputable institutions.")
        with st.expander("❓ Will an online degree be recognized by employers in India?"):
            st.write("Yes, valid degrees from UGC-approved universities are recognized by employers.")
        with st.expander("❓ Does technology make quality education more affordable?"):
            st.write("Yes, online programs often have lower fees compared to traditional campus programs.")
            
    with tab3:
        st.header("Universities & Programs")
        with st.expander("❓ Which universities partner with Distoversity?"):
            st.write("We partner with top-tier private universities known for their online programs.")
        with st.expander("❓ How do I apply for an online degree program through Distoversity?"):
            st.write("We guide you through the application process after your assessment and counseling session.")

# --- 11. MAIN ROUTER ---
navbar()

if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'FAQ': render_faq()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
