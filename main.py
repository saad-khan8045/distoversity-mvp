import streamlit as st
import pandas as pd
import time

# --- 1. PREMIUM CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Identity-First Career Architecture",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. VETERAN DESIGN SYSTEM (CSS) ---
st.markdown("""
    <style>
    /* IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    :root {
        --primary: #0077B6;       /* Deep Sky Blue */
        --primary-light: #E0F2FE; /* Very Light Blue */
        --accent: #0EA5E9;        /* Bright Blue */
        --text-dark: #0F172A;     /* Navy Black */
        --text-gray: #475569;     /* Slate Grey */
        --bg-white: #FFFFFF;
        --shadow: 0 10px 30px -10px rgba(0, 119, 182, 0.15);
    }

    /* GLOBAL STYLES */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-dark);
        background-color: #FFFFFF;
    }

    /* TYPOGRAPHY */
    h1, h2, h3 { font-family: 'Outfit', sans-serif; color: var(--primary); font-weight: 700; }
    h1 { font-size: 3.5rem !important; line-height: 1.1 !important; letter-spacing: -1px; }
    h2 { font-size: 2.5rem !important; margin-bottom: 1.5rem !important; }
    p { font-size: 1.15rem; line-height: 1.7; color: var(--text-gray); margin-bottom: 1.5rem; }

    /* COMPONENT: NAVIGATION BAR */
    div[data-testid="stHorizontalBlock"] {
        align-items: center;
        padding-bottom: 1rem;
        border-bottom: 1px solid #F1F5F9;
        margin-bottom: 2rem;
    }

    /* COMPONENT: INFO CARDS */
    .veteran-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: var(--shadow);
        transition: transform 0.2s;
        height: 100%;
    }
    .veteran-card:hover {
        transform: translateY(-5px);
        border-color: var(--accent);
        box-shadow: 0 20px 40px -10px rgba(0, 119, 182, 0.2);
    }

    /* COMPONENT: TIMELINE CARD */
    .timeline-card {
        border-left: 4px solid var(--primary);
        padding-left: 1.5rem;
        margin-bottom: 2rem;
    }

    /* BUTTONS */
    .stButton>button {
        background: linear-gradient(135deg, #0077B6 0%, #0284C7 100%);
        color: white;
        border-radius: 50px;
        padding: 0.8rem 2.5rem;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
        transition: all 0.3s;
        font-size: 1rem;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 20px rgba(2, 132, 199, 0.35);
        color: white;
    }

    /* HERO SECTION */
    .hero-box {
        background: linear-gradient(180deg, #F0F9FF 0%, #FFFFFF 100%);
        padding: 6rem 2rem 4rem 2rem;
        text-align: center;
        border-radius: 0 0 50px 50px;
        margin-bottom: 4rem;
        margin-top: -2rem;
    }
    
    /* HIDE STREAMLIT ELEMENTS */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* BLUR MECHANIC */
    .blur-container { position: relative; }
    .blur-content { filter: blur(10px); opacity: 0.5; pointer-events: none; user-select: none; }
    .lock-badge {
        position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        background: white; padding: 2.5rem; border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.12); text-align: center; width: 90%; max-width: 450px;
        border: 1px solid #BAE6FD;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA ENGINE (Hardcoded for Stability) ---
UNIVERSITY_DB = [
    {"name": "Manipal University Jaipur", "type": "Analyst", "program": "B.Tech Data Science", "match": 96, "desc": "Structure & Rigor"},
    {"name": "Amity University Online", "type": "Creator", "program": "BCA (Cloud Security)", "match": 94, "desc": "Flexibility & Innovation"},
    {"name": "LPU Online", "type": "Catalyst", "program": "MBA (Operations)", "match": 91, "desc": "Process & Execution"},
    {"name": "Jain University", "type": "Influencer", "program": "MBA (Marketing)", "match": 93, "desc": "Network & Leadership"},
    {"name": "Chandigarh University", "type": "Creator", "program": "B.Des (UX/UI)", "match": 89, "desc": "Creative Freedom"},
    {"name": "UPES Online", "type": "Analyst", "program": "BBA (Analytics)", "match": 95, "desc": "Data-Driven Focus"}
]

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'scores' not in st.session_state: st.session_state.scores = {'Creator':0, 'Influencer':0, 'Catalyst':0, 'Analyst':0}

# --- 5. TOP NAVIGATION BAR ---
def navbar():
    # This creates a sticky top nav look
    c1, c2, c3, c4, c5 = st.columns([2, 1, 1, 1, 1.2])
    with c1:
        st.markdown("<h3 style='margin:0; padding:0; font-size:1.8rem;'>Distoversity<span style='color:#0EA5E9'>.</span></h3>", unsafe_allow_html=True)
    with c2:
        if st.button("🏠 Home", key="nav_home", use_container_width=True): 
            st.session_state.page = 'Home'
            st.rerun()
    with c3:
        if st.button("ℹ️ About", key="nav_about", use_container_width=True): 
            st.session_state.page = 'About'
            st.rerun()
    with c4:
        if st.button("🛠️ Services", key="nav_services", use_container_width=True): 
            st.session_state.page = 'Services'
            st.rerun()
    with c5:
        if st.button("⚡ Assessment", key="nav_test", type="primary", use_container_width=True): 
            st.session_state.page = 'Assessment'
            st.rerun()

# --- 6. PAGE DEFINITIONS ---

def page_home():
    # HERO
    st.markdown("""
    <div class="hero-box">
        <div style="color:#0EA5E9; font-weight:700; letter-spacing:2px; margin-bottom:15px; font-size:0.9rem;">INDIA'S PREMIER CAREER ARCHITECTURE PLATFORM</div>
        <h1>Stop Guessing Your Future.<br>Start Engineering It.</h1>
        <p style="max-width:750px; margin:25px auto; font-size:1.25rem;">
            We don't ask "What are your marks?". We ask <b>"What is your flow?"</b>.<br>
            We use <b>Wealth Dynamics</b> & AI to match your psychological DNA to the top 1% of Universities.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # CTA BUTTON
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("🚀 Start Free Career Assessment ➤", use_container_width=True):
            st.session_state.page = 'Assessment'
            st.rerun()

    # SOCIAL PROOF
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:700; color:#94A3B8; letter-spacing:1px; font-size:0.9rem;'>TRUSTED BY PARTNERS FROM</p>", unsafe_allow_html=True)
    cols = st.columns(5)
    partners = ["IIT DELHI", "AMITY", "MANIPAL", "NMIMS", "LPU"]
    for i, p in enumerate(partners):
        cols[i].markdown(f"<h3 style='text-align:center; color:#CBD5E1; font-size:1.4rem; margin:0;'>{p}</h3>", unsafe_allow_html=True)

    # VALUE PROPOSITION
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Scientific Certainty. No Opinions.</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="veteran-card">
            <div style="font-size:3rem; margin-bottom:1rem;">🧠</div>
            <h3>Identity Analysis</h3>
            <p>Our AI Engine segregates learners into 4 Archetypes: Creator, Influencer, Catalyst, and Analyst.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="veteran-card">
            <div style="font-size:3rem; margin-bottom:1rem;">🏫</div>
            <h3>University Match</h3>
            <p>We don't sell admissions. We match you to curriculums (Amity, Manipal, LPU) that fit your brain.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="veteran-card">
            <div style="font-size:3rem; margin-bottom:1rem;">🗺️</div>
            <h3>Career Roadmap</h3>
            <p>A 4-year strategic plan including internships, skills (Alison/LinkedIn), and personal branding.</p>
        </div>
        """, unsafe_allow_html=True)

def page_about():
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("## The Distoversity Story")
        st.markdown("### From Factory Floor to Education Architect")
        
        st.markdown("""
        <div class="timeline-card">
            <h4>2019: The Struggle</h4>
            <p>I arrived in Delhi with nothing but a middle-class background and a hunger for opportunity. I had no guidance, only pressure.</p>
        </div>
        
        <div class="timeline-card">
            <h4>The Realization (Yazaki & Oppo)</h4>
            <p>I worked in the <b>SMT and Electrical departments</b> of global giants like Yazaki and Oppo. 
            On the factory floor, I saw a painful truth: 
            <i>Brilliant engineers were failing, not because they lacked talent, but because they were misaligned with their roles.</i></p>
        </div>
        
        <div class="timeline-card">
            <h4>The Shift to Education</h4>
            <p>I moved into the education sector, hoping to fix this. Instead, I found a sales machine. 
            Counselors were just pushing universities to meet targets. 
            <b>"Why is a phone call the only filter for a student's future?"</b> I asked. No one had an answer.</p>
        </div>
        
        <div class="timeline-card">
            <h4>The Birth of Distoversity</h4>
            <p>I combined my 6 years of experience with the <b>Wealth Dynamics</b> framework (Roger Hamilton) and AI. 
            We built a system that doesn't just admit students—it aligns them.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Building the Future")
        st.markdown("""
        <div class="veteran-card" style="background:#F0F9FF; border:none;">
            <h4>Our Mission</h4>
            <p><b>Education is a Right. Alignment is a Necessity.</b></p>
            <p>We are here to ensure that no Indian student ever climbs the wrong ladder again.</p>
        </div>
        """, unsafe_allow_html=True)

def page_services():
    st.markdown("## Our Premium Services")
    st.write("A complete ecosystem for your career growth.")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="veteran-card">
            <h3>🧠 Energy Assessment</h3>
            <p>Our proprietary 15-question engine identifies your core archetype: Creator, Influencer, Catalyst, or Analyst.</p>
            <div style="margin-top:20px; font-weight:700; color:#0077B6;">Price: FREE</div>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown("""
        <div class="veteran-card">
            <h3>🏫 University Matching</h3>
            <p>We filter 500+ universities to find the exact program curriculum that fits your brain.</p>
            <div style="margin-top:20px; font-weight:700; color:#0077B6;">Price: Included in Report</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="veteran-card" style="border-color:#0EA5E9; background:#F0F9FF;">
            <h3>💎 Strategic Session</h3>
            <p>A 30-minute 1:1 mentorship call, a 15-page PDF roadmap, and access to our Growth Community.</p>
            <div style="margin-top:20px; font-weight:700; color:#0077B6;">Price: ₹499</div>
        </div>
        """, unsafe_allow_html=True)

def page_assessment():
    st.markdown("## ⚡ Decode Your Professional DNA")
    st.write("Select the option that feels most natural to you (not what you *think* you should be).")
    
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
        matches = [u for u in UNIVERSITY_DB if u['type'] == profile]
        
        if matches:
            for u in matches:
                st.markdown(f"""
                <div class="veteran-card" style="margin-bottom:1rem; padding:1.5rem;">
                    <div style="display:flex; justify-content:space-between;">
                        <h4 style="margin:0;">{u['name']}</h4>
                        <span style="background:#E0F2FE; color:#0077B6; padding:4px 8px; border-radius:6px; font-weight:bold;">{u['match']}% Match</span>
                    </div>
                    <p style="font-size:0.9rem; margin-top:5px;"><b>Program:</b> {u['program']}</p>
                    <p style="font-size:0.9rem; color:green;">✅ {u['desc']}</p>
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
                <div class="veteran-card" style="margin-bottom:1rem;">
                    <h4>Year 1: Foundation Strategy</h4>
                    <p>Focus on the core skills of innovation. Avoid rigid structures...</p>
                </div>
                <div class="veteran-card">
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

# --- 7. MAIN ROUTER (CRITICAL FIX: Defined AFTER functions) ---
navbar()

if st.session_state.page == 'Home':
    page_home()
elif st.session_state.page == 'About':
    page_about()
elif st.session_state.page == 'Services':
    page_services()
elif st.session_state.page == 'Assessment':
    page_assessment()
elif st.session_state.page == 'Result':
    page_result()
