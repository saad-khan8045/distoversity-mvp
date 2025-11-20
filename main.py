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

# --- 2. PROFESSIONAL DESIGN SYSTEM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    :root {
        --primary: #0077B6;       /* Deep Sky Blue */
        --primary-light: #E0F2FE; /* Light Blue BG */
        --accent: #0EA5E9;        /* Bright Blue */
        --text-dark: #0F172A;
        --text-gray: #475569;
        --white: #FFFFFF;
        --gold: #F59E0B;
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-dark);
        background-color: #FFFFFF;
        scroll-behavior: smooth;
    }

    /* HEADERS */
    h1, h2, h3 { font-family: 'Outfit', sans-serif; color: var(--primary); font-weight: 700; }
    h1 { font-size: 3.8rem !important; letter-spacing: -1px; line-height: 1.1; }
    
    /* COMPONENT: PREMIUM CARD */
    .d-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    .d-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 119, 182, 0.1);
        border-color: var(--accent);
    }

    /* COMPONENT: ALISON CARD (Special) */
    .alison-card {
        background: linear-gradient(135deg, #FFF7ED 0%, #FFFFFF 100%);
        border: 1px solid #FED7AA;
    }

    /* COMPONENT: STICKY NAVIGATION */
    div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stHorizontalBlock"]) {
        position: sticky;
        top: 0;
        background-color: white;
        z-index: 999;
        padding-top: 1rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #F1F5F9;
        box-shadow: 0 4px 20px -10px rgba(0,0,0,0.1);
    }
    .nav-logo { font-family: 'Outfit'; font-weight: 800; font-size: 1.8rem; color: var(--primary); }
    
    /* COMPONENT: BUTTONS */
    .stButton>button {
        background: linear-gradient(135deg, #0077B6 0%, #0284C7 100%);
        color: white;
        border-radius: 50px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 10px rgba(0, 119, 182, 0.2);
        transition: 0.2s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 8px 20px rgba(0, 119, 182, 0.3); }
    
    /* COMPONENT: HERO */
    .hero-section {
        background: linear-gradient(180deg, #F0F9FF 0%, #FFFFFF 100%);
        padding: 5rem 2rem 3rem 2rem;
        text-align: center;
        border-radius: 0 0 50px 50px;
        margin-bottom: 3rem;
        margin-top: 1rem; 
    }

    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. PARTNER DATA ENGINE (ONLY PRIVATE UNIVERSITIES) ---
UNIVERSITY_DATA = [
    {"name": "Jain University Online", "location": "Bangalore", "naac": "A++", "fees": 210000, "program": "MBA Marketing", "energy": "Influencer", "type": "Online Degree", "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Jain_University_logo.png"},
    {"name": "Manipal University Jaipur", "location": "Online", "naac": "A+", "fees": 175000, "program": "MCA Data Science", "energy": "Analyst", "type": "Online Degree", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png"},
    {"name": "Amity University Online", "location": "Global", "naac": "A+", "fees": 345000, "program": "BCA Cloud Security", "energy": "Creator", "type": "Online Degree", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png"},
    {"name": "LPU Online", "location": "Global", "naac": "A++", "fees": 160000, "program": "MBA Operations", "energy": "Catalyst", "type": "Online Degree", "img": "https://upload.wikimedia.org/wikipedia/en/d/d4/Lovely_Professional_University_logo.png"},
    {"name": "Chandigarh University", "location": "Online", "naac": "A+", "fees": 180000, "program": "MBA General", "energy": "Influencer", "type": "Online Degree", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Chandigarh_University_logo.png/220px-Chandigarh_University_logo.png"},
    {"name": "UPES Online", "location": "Global", "naac": "A", "fees": 150000, "program": "BBA Analytics", "energy": "Analyst", "type": "Online Degree", "img": "https://www.upes.ac.in/media/1003/upes-logo.png"},
    {"name": "NMIMS Global", "location": "Online", "naac": "A+", "fees": 400000, "program": "MBA Finance", "energy": "Analyst", "type": "Online Degree", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/NMIMS_University_logo.png/220px-NMIMS_University_logo.png"},
    {"name": "DY Patil Online", "location": "Pune", "naac": "A++", "fees": 120000, "program": "BBA General", "energy": "Catalyst", "type": "Online Degree", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Dr._D._Y._Patil_Vidyapeeth_logo.png/220px-Dr._D._Y._Patil_Vidyapeeth_logo.png"}
]
df = pd.DataFrame(UNIVERSITY_DATA)

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None

# --- 5. NAVIGATION SYSTEM ---
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
    # Hero - Tailored for Professionals
    st.markdown("""
    <div class="hero-section">
        <div style="color:#0077B6; font-weight:700; letter-spacing:2px; margin-bottom:15px;">CAREER ARCHITECTURE FOR PROFESSIONALS & STUDENTS</div>
        <h1>Don't Just Upgrade Your Degree.<br>Upgrade Your <span style="color:#0EA5E9">Identity.</span></h1>
        <p style="max-width:700px; margin:20px auto;">
            Whether you are a student or a working professional, alignment is everything.<br>
            We match your <b>Psychological DNA</b> to India's Top Online Universities.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("🚀 Discover Your Career Energy (Free)", key="home_cta"):
            st.session_state.page = 'Assessment'
            st.rerun()

    # Partners (Private Universities Only)
    st.markdown("<br><p style='text-align:center; font-weight:600; color:#94A3B8;'>OFFICIAL PARTNERS</p>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, p in enumerate(["AMITY ONLINE", "MANIPAL", "JAIN ONLINE", "NMIMS", "LPU ONLINE"]):
        cols[i].markdown(f"<h3 style='text-align:center; color:#CBD5E1; font-size:1.4rem;'>{p}</h3>", unsafe_allow_html=True)

    # ALISON Integration (New!)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#FFF7ED; border:1px solid #FED7AA; border-radius:16px; padding:40px; text-align:center;">
        <h3 style="color:#D97706;">🎓 Upskill with ALISON</h3>
        <p style="color:#92400E;">We have partnered with <b>ALISON</b> to provide free certification courses that complement your degree.</p>
        <div style="display:flex; gap:20px; justify-content:center; margin-top:20px;">
            <span style="background:white; padding:10px 20px; border-radius:30px; border:1px solid #FED7AA;">📜 Project Management</span>
            <span style="background:white; padding:10px 20px; border-radius:30px; border:1px solid #FED7AA;">💻 IT Support</span>
            <span style="background:white; padding:10px 20px; border-radius:30px; border:1px solid #FED7AA;">🗣️ Communication</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Value Prop
    st.markdown("<br><br><h2 style='text-align:center;'>Why Professionals Choose Us</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="d-card"><h3>🧠 Identity Analysis</h3><p>Stop forcing yourself into roles you hate. Find your natural flow.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="d-card"><h3>🏫 Online Degrees</h3><p>Work while you learn. Valid degrees from UGC-approved universities.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="d-card"><h3>🚀 Career Roadmap</h3><p>Integrate your degree with ALISON certifications for maximum impact.</p></div>""", unsafe_allow_html=True)

# --- 7. PAGE: UNIVERSITY EXPLORER ---
def render_explorer():
    st.markdown("## 🏫 University Explorer")
    st.write("Compare top private online universities matched to your Genius Profile.")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        max_fee = st.slider("Max Budget (₹)", 50000, 500000, 250000, 50000)
    with col2:
        energy_filter = st.multiselect("Energy Fit", ["Creator", "Influencer", "Catalyst", "Analyst"], default=["Creator", "Analyst"])
    with col3:
        prog_type = st.multiselect("Program", ["MBA", "BCA", "BBA", "MCA"], default=["MBA", "BCA"])

    # Filtering Logic
    filtered_df = df[
        (df['fees'] <= max_fee) & 
        (df['energy'].isin(energy_filter))
    ]
    
    st.write(f"Found **{len(filtered_df)}** matches for you:")
    
    # Display Cards
    for idx, row in filtered_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="d-card" style="margin-bottom:15px; display:flex; justify-content:space-between; align-items:center;">
                <div style="display:flex; align-items:center; gap:20px;">
                    <img src="{row['img']}" height="60" style="object-fit:contain;">
                    <div>
                        <h3 style="margin:0; font-size:1.4rem;">{row['name']}</h3>
                        <p style="margin:0; font-size:0.9rem; color:#64748B;">📍 {row['location']} | 🏆 {row['naac']} | 🎓 {row['type']}</p>
                    </div>
                </div>
                <div style="text-align:right;">
                    <div style="font-weight:700; color:#0077B6; font-size:1.2rem;">₹{row['fees']:,}</div>
                    <div style="font-size:0.8rem; background:#E0F2FE; padding:4px 8px; border-radius:4px; color:#0077B6; display:inline-block; margin-top:5px;">{row['energy']} Fit</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"View Details for {row['name']}", key=f"btn_{idx}"):
                st.toast("Redirecting to Detailed Profile...")

# --- 8. PAGE: ASSESSMENT ---
def render_assessment():
    st.markdown("## ⚡ Decode Your Professional DNA")
    st.write("This isn't a test. It's a diagnostic tool for your career.")
    
    with st.form("assessment"):
        st.markdown("#### 1. In a high-pressure project, what role do you naturally take?")
        q1 = st.radio("Select one:", [
            "💡 The Idea Generator (I hate details)",
            "🗣️ The Presenter (I love talking)",
            "⚡ The Organizer (I keep things on time)",
            "📊 The Analyst (I check the data)"
        ], label_visibility="collapsed")
        
        st.markdown("<br>#### 2. What drains your energy the most?", unsafe_allow_html=True)
        q2 = st.radio("Select one:", [
            "Routine and repetitive data entry",
            "Working alone in a quiet room",
            "Chaos and unclear instructions",
            "Emotional conflict and sales"
        ], label_visibility="collapsed", key="q2")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.form_submit_button("Analyze My Profile ➤", type="primary"):
            with st.spinner("Mapping Neural Pathways..."):
                time.sleep(1.5)
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
        <p style="font-size:1.2rem;">Your psychological DNA maps to specific high-growth careers.</p>
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
                    <span style="background:#E0F2FE; color:#0077B6; padding:4px 8px; border-radius:6px;">94% Match</span>
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
    with st.expander("❓ How is this different from regular counseling?"):
        st.write("We use Energy Profiling, not just marks. We align you with your nature.")
    with st.expander("❓ Are these online degrees valid?"):
        st.write("Yes, all our partner universities (Amity, Manipal, Jain) are UGC-DEB approved and valid for government jobs.")
    with st.expander("❓ Do you guarantee jobs?"):
        st.write("We guarantee alignment. When you are in flow, success is inevitable.")

# --- 11. MAIN ROUTER ---
navbar()

if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'FAQ': render_faq()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
