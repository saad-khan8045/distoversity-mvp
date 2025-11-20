import streamlit as st
import pandas as pd
import time
import plotly.express as px
import plotly.graph_objects as go

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Identity-First Career Architecture",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. THE "SKY BLUE" DESIGN SYSTEM (CSS) ---
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
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-dark);
        background-color: #FFFFFF;
        scroll-behavior: smooth;
    }

    /* HEADERS */
    h1, h2, h3 { font-family: 'Outfit', sans-serif; color: var(--primary); font-weight: 700; }
    h1 { font-size: 3.5rem !important; letter-spacing: -1px; line-height: 1.1; }
    
    /* COMPONENT: PREMIUM CARD */
    .d-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
        height: 100%;
    }
    .d-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 119, 182, 0.1);
        border-color: var(--accent);
    }

    /* COMPONENT: STICKY NAVIGATION (FIXED) */
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
        /* Margin top ensures content doesn't hide behind sticky header */
        margin-top: 1rem; 
    }

    /* TIMELINE */
    .timeline-item {
        border-left: 4px solid var(--primary);
        padding-left: 1.5rem;
        padding-bottom: 2rem;
        position: relative;
    }
    .timeline-item::before {
        content: ''; width: 16px; height: 16px; background: var(--primary);
        border-radius: 50%; position: absolute; left: -10px; top: 0;
    }

    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA ENGINE ---
UNIVERSITY_DATA = [
    {"name": "Jain University", "location": "Bangalore", "naac": "A++", "placement": "98%", "fees": 210000, "program": "MBA Marketing", "energy": "Influencer", "type": "Online", "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Jain_University_logo.png"},
    {"name": "Manipal University Jaipur", "location": "Jaipur", "naac": "A+", "placement": "94%", "fees": 175000, "program": "B.Tech Data Science", "energy": "Analyst", "type": "Campus", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png"},
    {"name": "Amity University Online", "location": "Noida", "naac": "A+", "placement": "92%", "fees": 345000, "program": "BCA Cloud Security", "energy": "Creator", "type": "Online", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png"},
    {"name": "LPU Online", "location": "Punjab", "naac": "A++", "placement": "91%", "fees": 160000, "program": "MBA Operations", "energy": "Catalyst", "type": "Online", "img": "https://upload.wikimedia.org/wikipedia/en/d/d4/Lovely_Professional_University_logo.png"},
    {"name": "Chandigarh University", "location": "Punjab", "naac": "A+", "placement": "89%", "fees": 180000, "program": "B.Des UX/UI", "energy": "Creator", "type": "Campus", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Chandigarh_University_logo.png/220px-Chandigarh_University_logo.png"},
    {"name": "UPES Online", "location": "Dehradun", "naac": "A", "placement": "95%", "fees": 150000, "program": "BBA Analytics", "energy": "Analyst", "type": "Online", "img": "https://www.upes.ac.in/media/1003/upes-logo.png"},
    {"name": "NMIMS Global", "location": "Mumbai", "naac": "A+", "placement": "93%", "fees": 400000, "program": "MBA Finance", "energy": "Analyst", "type": "Online", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/NMIMS_University_logo.png/220px-NMIMS_University_logo.png"},
    {"name": "DY Patil University", "location": "Pune", "naac": "A++", "placement": "90%", "fees": 120000, "program": "BBA General", "energy": "Catalyst", "type": "Online", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Dr._D._Y._Patil_Vidyapeeth_logo.png/220px-Dr._D._Y._Patil_Vidyapeeth_logo.png"}
]
df = pd.DataFrame(UNIVERSITY_DATA)

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None

# --- 5. NAVIGATION SYSTEM (STICKY HEADER) ---
def navbar():
    # The CSS 'position: sticky' above applies to this container
    with st.container():
        c1, c2, c3, c4, c5, c6 = st.columns([2, 1, 1, 1, 1, 1.5])
        with c1:
            st.markdown("<div class='nav-logo'>Distoversity<span style='color:#0EA5E9'>.</span></div>", unsafe_allow_html=True)
        
        # Navigation Logic
        if c2.button("Home", use_container_width=True): st.session_state.page = 'Home'; st.rerun()
        if c3.button("About", use_container_width=True): st.session_state.page = 'About'; st.rerun()
        if c4.button("Explorer", use_container_width=True): st.session_state.page = 'Explorer'; st.rerun()
        if c5.button("FAQ", use_container_width=True): st.session_state.page = 'FAQ'; st.rerun()
        if c6.button("Take Assessment", type="primary", use_container_width=True): st.session_state.page = 'Assessment'; st.rerun()

# --- 6. PAGE: HOME ---
def render_home():
    # Hero
    st.markdown("""
    <div class="hero-section">
        <div style="color:#0077B6; font-weight:700; letter-spacing:2px; margin-bottom:15px;">INDIA'S IDENTITY-FIRST CAREER PLATFORM</div>
        <h1>Stop Guessing Your Future.<br>Start Engineering It.</h1>
        <p style="max-width:700px; margin:20px auto;">
            We don't ask "What are your marks?". We ask <b>"What is your flow?"</b>.<br>
            Match your psychological DNA to the top 1% of Universities like Amity, Manipal, and LPU.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("🚀 Discover Your Energy Type (Free)", key="home_cta"):
            st.session_state.page = 'Assessment'
            st.rerun()

    # Social Proof
    st.markdown("<br><p style='text-align:center; font-weight:600; color:#94A3B8;'>TRUSTED BY STUDENTS FROM</p>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, p in enumerate(["IIT DELHI", "AMITY", "MANIPAL", "NMIMS", "LPU"]):
        cols[i].markdown(f"<h3 style='text-align:center; color:#CBD5E1; font-size:1.4rem;'>{p}</h3>", unsafe_allow_html=True)

    # Value Prop Grid
    st.markdown("<br><br><h2 style='text-align:center;'>Scientific Certainty. No Opinions.</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="d-card"><h3>🧠 Identity Analysis</h3><p>Segregates learners into 4 Archetypes: Creator, Influencer, Catalyst, Analyst.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="d-card"><h3>🏫 University Match</h3><p>Filter 500+ universities to find curriculums that fit your cognitive style.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="d-card"><h3>🗺️ Career Roadmap</h3><p>A 4-year strategic plan including internships, skills, and branding.</p></div>""", unsafe_allow_html=True)

# --- 7. PAGE: UNIVERSITY EXPLORER ---
def render_explorer():
    st.markdown("## 🏫 University Explorer")
    st.write("Compare 500+ universities scientifically matched to your Genius Profile.")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        max_fee = st.slider("Max Budget (₹)", 50000, 500000, 250000, 50000)
    with col2:
        energy_filter = st.multiselect("Energy Fit", ["Creator", "Influencer", "Catalyst", "Analyst"], default=["Creator", "Analyst"])
    with col3:
        prog_type = st.multiselect("Program", ["MBA", "B.Tech", "BCA", "BBA", "B.Des"], default=["MBA", "BCA"])

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
                    <img src="{row['img']}" height="50">
                    <div>
                        <h3 style="margin:0; font-size:1.4rem;">{row['name']}</h3>
                        <p style="margin:0; font-size:0.9rem;">📍 {row['location']} | 🏆 {row['naac']}</p>
                    </div>
                </div>
                <div style="text-align:right;">
                    <div style="font-weight:700; color:#0077B6; font-size:1.2rem;">₹{row['fees']:,}</div>
                    <div style="font-size:0.8rem; background:#E0F2FE; padding:4px 8px; border-radius:4px; color:#0077B6; display:inline-block;">{row['energy']} Fit</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"View Details for {row['name']}", key=f"btn_{idx}"):
                st.toast("Redirecting to Detailed Profile...")

# --- 8. PAGE: ASSESSMENT ---
def render_assessment():
    st.markdown("## ⚡ Decode Your Professional DNA")
    st.write("Select the option that feels most natural to you.")
    
    with st.form("assessment"):
        st.markdown("#### 1. In a team project, what role do you naturally take?")
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
    if not profile:
        st.warning("Take assessment first!"); st.stop()

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
        <div style="position:relative; filter:blur(8px); opacity:0.5;">
            <div class="d-card"><h4>Year 1: Foundation</h4><p>Focus on core skills...</p></div>
            <div class="d-card"><h4>The Efficiency Trap</h4><p>Your weakness is details...</p></div>
        </div>
        <div style="position:absolute; top:60%; left:75%; transform:translate(-50%, -50%); background:white; padding:2rem; border-radius:16px; box-shadow:0 20px 40px rgba(0,0,0,0.1); text-align:center; width:300px;">
            <div style="font-size:3rem;">🔒</div>
            <h3>Unlock Full Report</h3>
            <p>Get your 15-Page Strategy + 1:1 Session</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("lead"):
            email = st.text_input("Enter Email to Unlock")
            if st.form_submit_button("Unlock Now - ₹499", use_container_width=True):
                st.success("Redirecting to Payment...")

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
    st.markdown("Everything you need to know about Distoversity and online education.")
    
    tab1, tab2, tab3 = st.tabs(["🌟 Career Guidance", "💻 Online Education", "🎓 Universities"])
    
    with tab1:
        st.header("General Guidance")
        with st.expander("❓ I'm confused about my career path. How can Distoversity help?"):
            st.write("We help you discover your 'Genius Profile' via AI, guiding you to academic fields and careers that truly fit you.")
        with st.expander("❓ Is the Distoversity Profile a psychological test?"):
            st.write("It's a self-discovery tool based on Wealth Dynamics, not a clinical diagnosis.")
        with st.expander("❓ How accurate are the recommendations?"):
            st.write("Our AI matches your profile to suitable institutions with high relevance, backed by a 92% student satisfaction rate.")
        with st.expander("❓ How does personalized matching work?"):
            st.write("We analyze your Energy Type (Dynamo, Blaze, Tempo, Steel) to find the curriculum style that fits your brain.")

    with tab2:
        st.header("Online Education")
        with st.expander("❓ Is online education a good option for me?"):
            st.write("If you are a Creator or Analyst type, online education offers the flexibility you crave. We help you validate this.")
        with st.expander("❓ How can I ensure quality?"):
            st.write("We only partner with NAAC A+ and A++ accredited universities like Amity and Manipal.")
        with st.expander("❓ Are these degrees recognized?"):
            st.write("Yes, all our partner universities are UGC-DEB approved, making your degree valid for government jobs and corporate hiring.")
        with st.expander("❓ Is it affordable?"):
            st.write("Online degrees cost 60-80% less than on-campus degrees while providing the same qualification.")

    with tab3:
        st.header("Universities & Programs")
        with st.expander("❓ Which universities partner with Distoversity?"):
            st.write("We partner with 16+ top universities including Jain, LPU, Amrita, IGNOU, and DY Patil.")
        with st.expander("❓ How do I apply?"):
            st.write("After your assessment, book a Strategic Session, and our counselors will handle the entire application process for you.")
        with st.expander("❓ Do you help with placement?"):
            st.write("Our partner universities have robust placement cells, and we provide career roadmaps to maximize your hirability.")

# --- 11. MAIN ROUTER ---
navbar()

if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'About': render_about()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'FAQ': render_faq()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
