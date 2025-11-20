import streamlit as st
import pandas as pd
import time
import plotly.express as px

# --- 1. ENTERPRISE CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Identity-First Career Guidance",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. DESIGN SYSTEM (SKY BLUE PREMIUM) ---
st.markdown("""
    <style>
    /* FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    :root {
        --primary: #0077B6;       /* Deep Sky Blue */
        --secondary: #90E0EF;     /* Soft Sky Blue */
        --accent: #00B4D8;        /* Bright Blue */
        --background: #F8FAFC;    /* Very Light Grey */
        --text-main: #0F172A;     /* Navy Black */
        --text-sub: #475569;      /* Slate Grey */
    }

    /* GLOBAL OVERRIDES */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-main);
        background-color: var(--background);
    }

    /* TYPOGRAPHY */
    h1, h2, h3, h4 {
        font-family: 'Outfit', sans-serif;
        color: var(--primary);
        font-weight: 700;
    }
    h1 { font-size: 3.5rem !important; line-height: 1.1; letter-spacing: -1px; }
    h2 { font-size: 2.2rem !important; }
    p { font-size: 1.1rem; line-height: 1.6; color: var(--text-sub); }

    /* CARDS & CONTAINERS */
    .glass-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        border: 1px solid #E2E8F0;
        transition: transform 0.2s;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 119, 182, 0.1);
        border-color: var(--accent);
    }

    /* BUTTONS */
    .stButton>button {
        background: linear-gradient(90deg, #0077B6 0%, #0096C7 100%);
        color: white;
        border-radius: 50px;
        padding: 0.75rem 2.5rem;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 12px rgba(0, 119, 182, 0.3);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 20px rgba(0, 119, 182, 0.4);
        color: white;
    }

    /* HERO SECTION */
    .hero-wrapper {
        background: linear-gradient(180deg, #E0F2FE 0%, #FFFFFF 100%);
        padding: 6rem 2rem 4rem 2rem;
        text-align: center;
        border-radius: 0 0 50px 50px;
        margin-bottom: 3rem;
        border-bottom: 1px solid #E2E8F0;
    }

    /* LOCK & BLUR */
    .blur-content { filter: blur(8px); opacity: 0.5; pointer-events: none; user-select: none; }
    .lock-badge {
        position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        background: white; padding: 2rem; border-radius: 20px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.1); text-align: center; width: 90%; max-width: 400px;
        border: 1px solid #BAE6FD;
    }

    /* HIDE STREAMLIT BRANDING */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. DATABASE (HARDCODED FROM YOUR IMAGES) ---
# This replaces the CSV loading to ensure 100% uptime without file errors.
UNIVERSITY_DATA = [
    {
        "name": "Manipal University Jaipur",
        "location": "Jaipur",
        "naac": "A+",
        "program": "B.Tech Data Science",
        "fees": "₹1.75 Lakh",
        "energy": "Analyst",
        "match": 96,
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png"
    },
    {
        "name": "Amity University Online",
        "location": "Noida (Online)",
        "naac": "A+",
        "program": "BCA (Cloud Security)",
        "fees": "₹3.45 Lakh",
        "energy": "Creator",
        "match": 94,
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png"
    },
    {
        "name": "LPU Online",
        "location": "Punjab (Online)",
        "naac": "A++",
        "program": "MBA (Operations)",
        "fees": "₹1.60 Lakh",
        "energy": "Catalyst",
        "match": 91,
        "logo": "https://upload.wikimedia.org/wikipedia/en/d/d4/Lovely_Professional_University_logo.png"
    },
    {
        "name": "Jain University",
        "location": "Bangalore",
        "naac": "A++",
        "program": "MBA (Marketing)",
        "fees": "₹2.10 Lakh",
        "energy": "Influencer",
        "match": 93,
        "logo": "https://upload.wikimedia.org/wikipedia/en/8/86/Jain_University_logo.png"
    },
    {
        "name": "Chandigarh University",
        "location": "Punjab",
        "naac": "A+",
        "program": "B.Des (UX/UI)",
        "fees": "₹1.80 Lakh",
        "energy": "Creator",
        "match": 89,
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Chandigarh_University_logo.png/220px-Chandigarh_University_logo.png"
    },
    {
        "name": "UPES Online",
        "location": "Dehradun",
        "naac": "A",
        "program": "BBA (Analytics)",
        "fees": "₹1.50 Lakh",
        "energy": "Analyst",
        "match": 95,
        "logo": "https://www.upes.ac.in/media/1003/upes-logo.png"
    }
]

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None

# --- 5. NAVIGATION SYSTEM ---
def sidebar_nav():
    with st.sidebar:
        st.markdown("### 🔷 Distoversity")
        st.caption("Identity-First Career Architecture")
        
        st.markdown("---")
        
        if st.button("🏠 Home", use_container_width=True): st.session_state.page = 'Home'; st.rerun()
        if st.button("ℹ️ About Us", use_container_width=True): st.session_state.page = 'About'; st.rerun()
        if st.button("🛠️ Services", use_container_width=True): st.session_state.page = 'Services'; st.rerun()
        if st.button("🏫 University Explorer", use_container_width=True): st.session_state.page = 'Explorer'; st.rerun()
        
        st.markdown("---")
        
        if st.button("⚡ Take Assessment", type="primary", use_container_width=True): st.session_state.page = 'Assessment'; st.rerun()
        
        st.markdown("---")
        st.info("© 2025 Distoversity\nDelhi, India")

# --- 6. PAGE: HOME ---
def page_home():
    # HERO SECTION
    st.markdown("""
    <div class="hero-wrapper">
        <div style="color:#0077B6; font-weight:700; letter-spacing:2px; margin-bottom:10px;">INDIA'S #1 CAREER ARCHITECTURE PLATFORM</div>
        <h1>Stop Guessing Your Future.<br>Start Engineering It.</h1>
        <p style="max-width:700px; margin:20px auto;">
            We don't ask "What are your marks?". We ask <b>"What is your flow?"</b>.<br>
            Join 50,000+ students using AI to match their psychological DNA to the top 1% of Universities.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("🚀 Discover Your Core Genius (Free)", use_container_width=True):
            st.session_state.page = 'Assessment'
            st.rerun()

    # TRUST SIGNALS
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:600; color:#94A3B8; letter-spacing:1px;'>TRUSTED BY PARTNERS FROM</p>", unsafe_allow_html=True)
    
    cols = st.columns(5)
    partners = ["IIT DELHI", "AMITY", "MANIPAL", "NMIMS", "LPU"]
    for i, p in enumerate(partners):
        cols[i].markdown(f"<h3 style='text-align:center; color:#CBD5E1; font-size:1.5rem;'>{p}</h3>", unsafe_allow_html=True)

    # WHY US (Content from your prompt)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Scientific Certainty. No Opinions.</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="glass-card">
            <div style="font-size:2.5rem; margin-bottom:10px;">🧠</div>
            <h3>Identity Analysis</h3>
            <p>Our AI Engine segregates learners into 4 Archetypes: Creator, Influencer, Catalyst, and Analyst.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="glass-card">
            <div style="font-size:2.5rem; margin-bottom:10px;">🏫</div>
            <h3>University Match</h3>
            <p>We don't sell admissions. We match you to curriculums (Amity, Manipal, LPU) that fit your brain.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="glass-card">
            <div style="font-size:2.5rem; margin-bottom:10px;">🗺️</div>
            <h3>Career Roadmap</h3>
            <p>A 4-year strategic plan including internships, skills (Alison/LinkedIn), and personal branding.</p>
        </div>
        """, unsafe_allow_html=True)

# --- 7. PAGE: ABOUT US ---
def page_about():
    st.markdown("## Our Mission")
    st.write("To democratize career certainty for every Indian student.")
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("### The Founder's Story")
        st.write("""
        I came to Delhi in 2019 from a middle-class background with limited opportunities. 
        Like many, I searched for a career path and worked in industries like Engineering (SMT Department) 
        at companies like **Yazaki** and **Oppo**.
        
        While working on the factory floor, I realized a critical flaw: 
        *Brilliant people were failing because they were in roles that fought against their natural nature.*
        
        Distoversity was born to fix this. We combine the **Wealth Dynamics** framework with AI to ensure 
        no student ever climbs the wrong ladder again.
        """)
        
        st.info("💡 **Our Philosophy:** Education is a right. Alignment is a necessity.")
    
    with col2:
        st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Building the Future of India")

# --- 8. PAGE: UNIVERSITY EXPLORER ---
def page_explorer():
    st.markdown("## 🏫 University Explorer")
    st.write("Browse our database of NAAC A+ Accredited Partners.")
    
    # Search Bar
    search = st.text_input("Search by Name or Program", placeholder="e.g., Manipal, MBA...")
    
    # Filters
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        energy_filter = st.selectbox("Filter by Energy Type", ["All", "Creator", "Influencer", "Catalyst", "Analyst"])
    
    # Display Data
    for uni in UNIVERSITY_DATA:
        if search.lower() in uni['name'].lower() or search.lower() in uni['program'].lower():
            if energy_filter == "All" or energy_filter == uni['energy']:
                with st.container():
                    st.markdown(f"""
                    <div class="glass-card" style="margin-bottom:1rem;">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div>
                                <h3 style="margin:0;">{uni['name']}</h3>
                                <p style="margin:0; color:#64748B;">📍 {uni['location']} | 🏆 NAAC {uni['naac']}</p>
                            </div>
                            <div style="text-align:right;">
                                <div style="background:#E0F2FE; color:#0077B6; padding:5px 10px; border-radius:8px; font-weight:bold;">{uni['fees']}</div>
                            </div>
                        </div>
                        <hr style="margin:10px 0; opacity:0.2;">
                        <div style="display:flex; justify-content:space-between;">
                            <p><b>Best For:</b> {uni['energy']}</p>
                            <p><b>Program:</b> {uni['program']}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

# --- 9. PAGE: ASSESSMENT (LOGIC) ---
def page_assessment():
    st.markdown("## ⚡ Decode Your Professional DNA")
    st.write("Select the option that feels most natural to you.")
    
    with st.form("quiz_form"):
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
        
        st.markdown("<br>#### 3. How do you prefer to be rewarded?", unsafe_allow_html=True)
        q3 = st.radio("Select one:", [
            "Freedom to create new things",
            "Recognition and applause",
            "A sense of belonging and stability",
            "Certainty and accuracy"
        ], label_visibility="collapsed", key="q3")
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Analyze My Profile ➤", type="primary")
        
        if submitted:
            with st.spinner("Mapping Neural Pathways..."):
                time.sleep(1.5)
            
            # LOGIC
            if "Idea" in q1: st.session_state.user_profile = "Creator"
            elif "Presenter" in q1: st.session_state.user_profile = "Influencer"
            elif "Organizer" in q1: st.session_state.user_profile = "Catalyst"
            else: st.session_state.user_profile = "Analyst"
            
            st.session_state.page = 'Result'
            st.rerun()

# --- 10. PAGE: RESULT (GATED) ---
def page_result():
    profile = st.session_state.user_profile
    if not profile:
        st.warning("Please take the assessment first.")
        if st.button("Go to Assessment"): st.session_state.page = 'Assessment'; st.rerun()
        return

    st.balloons()
    
    # HEADER
    st.markdown(f"""
    <div style="text-align:center; padding:3rem; background:#F0F9FF; border-radius:20px; border:1px solid #BAE6FD; margin-bottom:3rem;">
        <div style="color:#0077B6; font-weight:700; letter-spacing:2px;">PRIMARY ARCHETYPE DETECTED</div>
        <h1 style="font-size:5rem !important; color:#0077B6; margin:10px 0;">{profile}</h1>
        <p style="font-size:1.2rem;">Your psychological DNA maps to specific high-growth careers.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    # LEFT: MATCHES
    with c1:
        st.markdown("### 🎯 Top University Matches")
        matches = [u for u in UNIVERSITY_DATA if u['energy'] == profile]
        
        if matches:
            for u in matches:
                st.markdown(f"""
                <div class="glass-card" style="margin-bottom:1rem;">
                    <div style="display:flex; justify-content:space-between;">
                        <h4 style="margin:0;">{u['name']}</h4>
                        <span style="background:#E0F2FE; color:#0077B6; padding:4px 8px; border-radius:6px; font-weight:bold;">{u['match']}% Match</span>
                    </div>
                    <p style="font-size:0.9rem; margin-top:5px;"><b>Program:</b> {u['program']}</p>
                    <p style="font-size:0.9rem; color:green;">✅ High Alignment with {profile} Energy</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("We are finding custom matches for you. Book a call.")

    # RIGHT: ROADMAP (LOCKED)
    with c2:
        st.markdown("### 🗺️ Strategic Career Roadmap")
        
        st.markdown("""
        <div class="blur-container">
            <div class="blur-content">
                <div class="glass-card" style="margin-bottom:1rem;">
                    <h4>Year 1: Foundation Strategy</h4>
                    <p>Focus on the core skills of innovation. Avoid rigid structures...</p>
                </div>
                <div class="glass-card">
                    <h4>The "Efficiency Trap" Warning</h4>
                    <p>Your biggest weakness is detailed execution. To fix this...</p>
                </div>
            </div>
            
            <div class="lock-badge">
                <div style="font-size:3rem; margin-bottom:10px;">🔒</div>
                <h3>Unlock Full Report</h3>
                <p>Get your 15-Page Strategy + 1:1 Session</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.form("lead_gen"):
            st.text_input("Full Name")
            email = st.text_input("Email Address", placeholder="student@gmail.com")
            
            st.markdown("""
            <div style="background:#F0F9FF; padding:15px; border-radius:8px; border:1px solid #0077B6; margin-bottom:15px; font-size:0.9rem;">
                💎 <b>Strategic Session (₹499)</b><br>
                Includes: Full Report, University List, Mentorship Call.
            </div>
            """, unsafe_allow_html=True)
            
            if st.form_submit_button("Unlock Now - Pay ₹499", use_container_width=True):
                if "@" in email:
                    st.success("Redirecting to Payment Gateway...")
                else:
                    st.error("Please enter a valid email.")

# --- 11. MAIN ROUTER ---
sidebar_nav()

if st.session_state.page == 'Home':
    page_home()
elif st.session_state.page == 'About':
    page_about()
elif st.session_state.page == 'Services':
    page_services()
elif st.session_state.page == 'Explorer':
    page_explorer()
elif st.session_state.page == 'Assessment':
    page_assessment()
elif st.session_state.page == 'Result':
    page_result()
