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
    /* IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    :root {
        --primary: #0077B6;       /* Deep Sky Blue */
        --primary-dark: #023E8A;  /* Darker Blue for text */
        --primary-light: #ADE8F4; /* Glow Color */
        --accent: #00B4D8;        /* Bright Blue */
        --text-main: #0F172A;
        --text-sub: #475569;
        --white: #FFFFFF;
        --gradient-bg: radial-gradient(circle at 50% 0%, #E0F2FE 0%, #FFFFFF 70%);
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-main);
        background-color: #FFFFFF;
        scroll-behavior: smooth;
    }

    /* HEADERS */
    h1, h2, h3 { font-family: 'Outfit', sans-serif; color: var(--primary-dark); font-weight: 800; }
    h1 { 
        font-size: 4.5rem !important; 
        letter-spacing: -2px; 
        line-height: 1.1; 
        background: -webkit-linear-gradient(45deg, #0077B6, #0096C7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    /* COMPONENT: HERO SECTION (The "Attractive Force") */
    .hero-section {
        background: var(--gradient-bg);
        padding: 6rem 2rem 5rem 2rem;
        text-align: center;
        border-radius: 0 0 60px 60px;
        margin-bottom: 4rem;
        margin-top: 0rem;
        border-bottom: 1px solid #E0F2FE;
    }
    
    .hero-badge {
        background: rgba(0, 119, 182, 0.1);
        color: #0077B6;
        padding: 8px 20px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 1.5px;
        display: inline-block;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(0, 119, 182, 0.2);
    }

    /* COMPONENT: PREMIUM GLASS CARD */
    .d-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid #E2E8F0;
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 10px 40px -10px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        height: 100%;
    }
    .d-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 50px -10px rgba(0, 119, 182, 0.15);
        border-color: var(--accent);
    }

    /* COMPONENT: FEATURE ICON */
    .icon-box {
        width: 70px;
        height: 70px;
        background: linear-gradient(135deg, #E0F2FE, #FFFFFF);
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 20px -5px rgba(0, 119, 182, 0.1);
    }

    /* COMPONENT: STICKY NAV */
    div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stHorizontalBlock"]) {
        position: sticky;
        top: 0;
        background-color: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
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
        padding: 0.8rem 3rem;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        box-shadow: 0 10px 25px rgba(0, 119, 182, 0.3);
        transition: all 0.3s;
    }
    .stButton>button:hover { 
        transform: scale(1.05); 
        box-shadow: 0 15px 35px rgba(0, 119, 182, 0.4); 
    }
    
    /* COMPONENT: ALISON PARTNER SECTION */
    .alison-section {
        background: linear-gradient(135deg, #FFF7ED 0%, #FFFFFF 100%);
        border: 1px solid #FFEDD5;
        border-radius: 24px;
        padding: 3rem;
        text-align: center;
        margin-top: 4rem;
    }
    .pill {
        background: white;
        padding: 8px 20px;
        border-radius: 50px;
        font-weight: 600;
        color: #D97706;
        border: 1px solid #FED7AA;
        margin: 0 10px;
        box-shadow: 0 4px 10px rgba(251, 146, 60, 0.1);
    }

    /* HIDE STREAMLIT UI */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. PARTNER DATA ENGINE ---
UNIVERSITY_DATA = [
    {"name": "Jain Online", "location": "Bangalore", "naac": "A++", "fees": 210000, "program": "MBA Marketing", "energy": "Influencer", "type": "Online Degree", "approvals": "UGC-DEB, AICTE", "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Jain_University_logo.png"},
    {"name": "Manipal University Online", "location": "Jaipur", "naac": "A+", "fees": 175000, "program": "MCA Data Science", "energy": "Analyst", "type": "Online Degree", "approvals": "UGC, NAAC", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png"},
    {"name": "Amity University Online", "location": "Global", "naac": "A+", "fees": 345000, "program": "BCA Cloud Security", "energy": "Creator", "type": "Online Degree", "approvals": "UGC-DEB, WES", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png"},
    {"name": "LPU Online", "location": "Global", "naac": "A++", "fees": 160000, "program": "MBA Operations", "energy": "Catalyst", "type": "Online Degree", "approvals": "UGC, AICTE", "img": "https://upload.wikimedia.org/wikipedia/en/d/d4/Lovely_Professional_University_logo.png"},
    {"name": "Chandigarh University", "location": "Online", "naac": "A+", "fees": 180000, "program": "MBA General", "energy": "Influencer", "type": "Online Degree", "approvals": "UGC-DEB", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Chandigarh_University_logo.png/220px-Chandigarh_University_logo.png"},
    {"name": "UPES Online", "location": "Global", "naac": "A", "fees": 150000, "program": "BBA Analytics", "energy": "Analyst", "type": "Online Degree", "approvals": "UGC, NAAC", "img": "https://www.upes.ac.in/media/1003/upes-logo.png"},
    {"name": "NMIMS CDOL", "location": "Online", "naac": "A+", "fees": 400000, "program": "MBA Finance", "energy": "Analyst", "type": "Online Degree", "approvals": "UGC-DEB, AICTE", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/NMIMS_University_logo.png/220px-NMIMS_University_logo.png"},
    {"name": "DY Patil Online", "location": "Pune", "naac": "A++", "fees": 120000, "program": "BBA General", "energy": "Catalyst", "type": "Online Degree", "approvals": "UGC, AICTE", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Dr._D._Y._Patil_Vidyapeeth_logo.png/220px-Dr._D._Y._Patil_Vidyapeeth_logo.png"}
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
    # ULTRA-PREMIUM HERO
    st.markdown("""
    <div class="hero-section">
        <div class="hero-badge">CAREER ARCHITECTURE FOR PROFESSIONALS</div>
        <h1>Don't Just Upgrade Your Degree.<br>Upgrade Your <span style="color:#00B4D8">Identity.</span></h1>
        <p style="max-width:800px; margin:25px auto; font-size:1.3rem; color:#475569; line-height:1.6;">
            Whether you are a student or a working professional, alignment is everything.<br>
            We match your <b>Psychological DNA</b> to India's Top Online Universities.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # CENTERED CTA (PERFECTLY ALIGNED)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🚀 Discover Your Career Energy (Free)", key="home_cta", use_container_width=True):
            st.session_state.page = 'Assessment'
            st.rerun()

    # PARTNER LOGOS (Bold & Black)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:700; color:#94A3B8; letter-spacing: 1px; font-size:0.9rem;'>TRUSTED BY STUDENTS OF TOP UNIVERSITIES</p>", unsafe_allow_html=True)
    
    partner_list = ["Amity University Online", "Manipal University Online", "Jain Online", "NMIMS CDOL", "LPU Online"]
    cols = st.columns(5)
    for i, p in enumerate(partner_list):
        cols[i].markdown(f"<h3 style='text-align:center; color:#0F172A; font-weight:800; font-size:1.2rem; opacity:0.9;'>{p}</h3>", unsafe_allow_html=True)

    # FEATURE CARDS (The "Attractive Force")
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; font-size:2.5rem; color:#023E8A;'>Why Professionals Choose Us</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748B; margin-bottom:4rem; font-size:1.1rem;'>Scientific alignment for maximum career impact.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="d-card">
            <div class="icon-box">🧠</div>
            <h3 style="font-size:1.5rem; margin-bottom:1rem;">Identity Analysis</h3>
            <p style="color:#475569;">Stop forcing yourself into roles you hate. Find your natural flow with our AI assessment.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="d-card">
            <div class="icon-box">🏫</div>
            <h3 style="font-size:1.5rem; margin-bottom:1rem;">Online Degrees</h3>
            <p style="color:#475569;">Work while you learn. Valid degrees from UGC-approved universities like Amity & Manipal.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="d-card">
            <div class="icon-box">🚀</div>
            <h3 style="font-size:1.5rem; margin-bottom:1rem;">Career Roadmap</h3>
            <p style="color:#475569;">Integrate your degree with <b>ALISON</b> certifications for maximum professional impact.</p>
        </div>
        """, unsafe_allow_html=True)

    # ALISON INTEGRATION (Visual & Attractive)
    st.markdown("""
    <div class="alison-section">
        <h3 style="color:#D97706; font-size:2rem; margin-bottom:1rem;">🎓 Upskill with ALISON</h3>
        <p style="color:#92400E; font-size:1.1rem; max-width:700px; margin:0 auto 2rem auto;">
            We have partnered with <b>ALISON</b> to provide free certification courses that complement your degree.
        </p>
        <div style="display:flex; gap:15px; justify-content:center; flex-wrap: wrap;">
            <div class="pill">📜 Project Management</div>
            <div class="pill">💻 IT Support</div>
            <div class="pill">🗣️ Business Communication</div>
            <div class="pill">📊 Data Analytics</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 7. PAGE: UNIVERSITY EXPLORER ---
def render_explorer():
    st.markdown("## 🏫 University Explorer")
    st.markdown("Compare top private online universities matched to your Genius Profile. **All universities listed are UGC/AICTE Approved.**")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        max_fee = st.slider("Max Budget (₹)", 50000, 500000, 250000, 50000)
    with col2:
        energy_filter = st.multiselect("Energy Fit", ["Creator", "Influencer", "Catalyst", "Analyst"], default=["Creator", "Analyst"])
    with col3:
        prog_type = st.multiselect("Program", ["MBA", "BCA", "BBA", "MCA"], default=["MBA", "BCA"])

    filtered_df = df[(df['fees'] <= max_fee) & (df['energy'].isin(energy_filter))]
    
    st.write(f"Found **{len(filtered_df)}** matches for you:")
    
    for idx, row in filtered_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="d-card" style="margin-bottom:20px; border-left: 5px solid #0077B6;">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap: wrap; gap: 10px;">
                    <div style="display:flex; align-items:center; gap:25px;">
                        <img src="{row['img']}" height="70" style="object-fit:contain; max-width: 120px;">
                        <div>
                            <h3 style="margin:0; font-size:1.5rem; color:#023E8A;">{row['name']}</h3>
                            <p style="margin:5px 0; font-size:1rem; color:#64748B;">📍 {row['location']} | 🏆 {row['naac']} | 🎓 {row['type']}</p>
                            <p style="margin:0; font-size:0.9rem; color:#00B4D8; font-weight:600;">✅ Approvals: {row['approvals']}</p>
                        </div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-weight:800; color:#0077B6; font-size:1.4rem;">₹{row['fees']:,}</div>
                        <div style="font-size:0.85rem; background:#E0F2FE; padding:6px 12px; border-radius:6px; color:#0077B6; display:inline-block; margin-top:8px; font-weight:600;">{row['energy']} Fit</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            c_btn1, c_btn2, c_void = st.columns([1, 1, 3])
            with c_btn1:
                 if st.button(f"View Details", key=f"btn_view_{idx}"):
                    st.toast(f"Viewing details for {row['name']}...")
            with c_btn2:
                 if st.button(f"Brochure", key=f"btn_brochure_{idx}"):
                     st.toast("Downloading Brochure...")

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
        <div style="border-left: 4px solid #0077B6; padding-left: 20px; margin-bottom: 30px;">
            <h4 style="color:#023E8A;">2019: The Struggle</h4>
            <p>Arrived in Delhi. Middle-class background. Zero guidance.</p>
        </div>
        <div style="border-left: 4px solid #0077B6; padding-left: 20px; margin-bottom: 30px;">
            <h4 style="color:#023E8A;">The Factory Floor (Yazaki & Oppo)</h4>
            <p>Worked in SMT/Electrical depts. Saw brilliant engineers failing because of misalignment.</p>
        </div>
        <div style="border-left: 4px solid #0077B6; padding-left: 20px; margin-bottom: 30px;">
            <h4 style="color:#023E8A;">The Solution</h4>
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
