import streamlit as st
import pandas as pd
import time
import plotly.graph_objects as go

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | India's Premier Career Architecture",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. PREMIUM "SKY BLUE" CSS ---
st.markdown("""
    <style>
    /* IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Plus+Jakarta+Sans:wght@400;500;700&display=swap');

    :root {
        --primary: #0077B6;      /* Deep Sky Blue */
        --primary-light: #CAF0F8; /* Pale Sky Blue */
        --accent: #00B4D8;       /* Bright Sky Blue */
        --text-dark: #0F172A;    /* Navy Black */
        --text-grey: #475569;
        --bg-white: #FFFFFF;
        --bg-soft: #F0F9FF;      /* Very Light Blue BG */
    }

    /* GLOBAL STYLES */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-dark);
        background-color: var(--bg-white);
    }

    /* HEADINGS */
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif;
        color: var(--primary);
        font-weight: 700;
    }
    
    h1 { font-size: 3.5rem !important; letter-spacing: -1px; }
    h2 { font-size: 2.5rem !important; }

    /* CUSTOM CARDS */
    .info-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 119, 182, 0.08);
        border: 1px solid #E0F2FE;
        transition: transform 0.3s ease;
    }
    .info-card:hover {
        transform: translateY(-5px);
        border-color: var(--accent);
    }

    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(180deg, #E0F2FE 0%, #FFFFFF 100%);
        padding: 6rem 2rem 4rem 2rem;
        text-align: center;
        border-radius: 0 0 50px 50px;
        margin-bottom: 3rem;
    }

    /* BUTTONS */
    .stButton>button {
        background: linear-gradient(90deg, #0077B6 0%, #0096C7 100%);
        color: white;
        border-radius: 50px;
        padding: 16px 40px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 118, 182, 0.3);
        transition: all 0.3s;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(0, 118, 182, 0.4);
        color: white;
    }

    /* LOCK SECTION */
    .blur-box {
        filter: blur(8px);
        opacity: 0.5;
        pointer-events: none;
    }
    .lock-overlay {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: white;
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid #BAE6FD;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.1);
        text-align: center;
        width: 90%;
        max-width: 500px;
    }

    /* REMOVE STREAMLIT BRANDING */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. EMBEDDED DATA (FIXES KEY ERROR) ---
# We create the dataframe manually here so it never fails
data_dict = {
    'University_Name': [
        'Manipal University Jaipur', 'Amity University Online', 'LPU Online', 
        'Jain University', 'Chandigarh University', 'UPES Online'
    ],
    'Primary_Energy_Fit': [
        'Analyst', 'Creator', 'Catalyst', 
        'Influencer', 'Creator', 'Analyst'
    ],
    'Match_Score': [96, 94, 91, 93, 89, 95],
    'Program': [
        'B.Tech Data Science', 'BCA Cloud Security', 'MBA Operations',
        'MBA Marketing', 'B.Des UX/UI', 'BBA Analytics'
    ],
    'Why': [
        'Perfect structure for Analyst types.', 'Flexible modules for Creators.',
        'Process-driven curriculum for Catalysts.', 'Networking focus for Influencers.',
        'Innovation labs for Creators.', 'Data-heavy curriculum for Analysts.'
    ]
}
df = pd.DataFrame(data_dict)

# --- 4. SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = 'home'
if 'scores' not in st.session_state: st.session_state.scores = {'Creator':0, 'Influencer':0, 'Catalyst':0, 'Analyst':0}

# --- 5. PAGES ---

def page_home():
    # HERO SECTION
    st.markdown("""
    <div class="hero-section">
        <div style="color:#0077B6; font-weight:700; letter-spacing:2px; margin-bottom:10px;">INDIA'S IDENTITY-FIRST CAREER PLATFORM</div>
        <h1 style="margin-bottom: 20px;">Don't Just Get a Degree.<br>Get an <span style="color:#00B4D8;">Identity.</span></h1>
        <p style="font-size:1.3rem; color:#475569; max-width:700px; margin:0 auto 3rem auto; line-height:1.6;">
            We bridge the gap between <b>who you are</b> and <b>what you do</b>. 
            Using AI & Psychometrics to match students to the top 1% of Universities.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_cta1, col_cta2, col_cta3 = st.columns([1, 1, 1])
    with col_cta2:
        if st.button("⚡ Start Free Career Assessment", use_container_width=True):
            st.session_state.page = 'assessment'
            st.rerun()

    # COMPANY INFO SECTION (New!)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.markdown("## Who We Are")
        st.markdown("""
        <p style="font-size:1.1rem; color:#475569; line-height:1.8;">
        Founded in 2019 in Delhi, <b>Distoversity</b> was born from a simple realization: 
        <i>"Most students fail not because they lack talent, but because they lack alignment."</i>
        <br><br>
        We moved beyond generic phone calls. We use the <b>Wealth Dynamics</b> framework 
        to mathematically calculate your professional DNA and match it to university curriculums 
        that fit your cognitive style.
        </p>
        """, unsafe_allow_html=True)
    
    with c2:
        # Professional abstract image
        st.image("https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", 
                 caption="Empowering 50,000+ Students across India")

    # SERVICES GRID
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Our Core Services</h2>", unsafe_allow_html=True)
    
    sc1, sc2, sc3 = st.columns(3)
    with sc1:
        st.markdown("""
        <div class="info-card">
            <h3>🧠 Identity Analysis</h3>
            <p style="color:#64748B;">Our AI Engine segregates learners into 4 Archetypes: Creator, Influencer, Catalyst, and Analyst.</p>
        </div>
        """, unsafe_allow_html=True)
    with sc2:
        st.markdown("""
        <div class="info-card">
            <h3>🏫 University Match</h3>
            <p style="color:#64748B;">We don't sell admissions. We match you to curriculums (Amity, Manipal, LPU) that fit your brain.</p>
        </div>
        """, unsafe_allow_html=True)
    with sc3:
        st.markdown("""
        <div class="info-card">
            <h3>🚀 Career Roadmap</h3>
            <p style="color:#64748B;">A 4-year strategic plan including internships, skills (Alison/LinkedIn), and personal branding.</p>
        </div>
        """, unsafe_allow_html=True)

def page_assessment():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; margin-bottom:3rem;">
        <div style="color:#0077B6; font-weight:700;">STEP 1 OF 3</div>
        <h2>Decode Your Professional DNA</h2>
        <p style="color:#64748B;">Select the option that feels most natural to you.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.container():
        c_main = st.columns([1, 2, 1])[1]
        with c_main:
            with st.form("quiz"):
                st.markdown("#### 1. In a team project, what is your natural role?")
                q1 = st.radio("Select one:", [
                    "💡 The Idea Generator (I hate details)",
                    "🗣️ The Presenter (I love talking)",
                    "⚡ The Organizer (I keep things on time)",
                    "📊 The Analyst (I check the data)"
                ], label_visibility="collapsed")
                
                st.markdown("<br>#### 2. What drains your energy fast?", unsafe_allow_html=True)
                q2 = st.radio("Select one:", [
                    "Routine and repetitive tasks",
                    "Working alone in a quiet room",
                    "Chaos and unclear instructions",
                    "Emotional conflict and sales"
                ], label_visibility="collapsed")
                
                st.markdown("<br>", unsafe_allow_html=True)
                submit = st.form_submit_button("Reveal My Archetype ➤", use_container_width=True)
                
                if submit:
                    with st.spinner("Analyzing Cognitive Patterns..."):
                        time.sleep(1.5)
                    # Logic
                    if "Idea" in q1: st.session_state.scores['Creator'] += 1
                    elif "Presenter" in q1: st.session_state.scores['Influencer'] += 1
                    elif "Organizer" in q1: st.session_state.scores['Catalyst'] += 1
                    else: st.session_state.scores['Analyst'] += 1
                    
                    st.session_state.page = 'result'
                    st.rerun()

def page_result():
    # Determine Winner
    scores = st.session_state.scores
    winner = max(scores, key=scores.get) if sum(scores.values()) > 0 else "Creator"
    
    st.balloons()
    
    # RESULT HEADER
    st.markdown(f"""
    <div style="text-align:center; padding:3rem; background:#F0F9FF; border-radius:20px; border:1px solid #BAE6FD; margin-bottom:3rem;">
        <div style="color:#0077B6; font-weight:700; letter-spacing:2px;">PRIMARY ARCHETYPE DETECTED</div>
        <h1 style="font-size:5rem !important; color:#0077B6; margin:10px 0;">{winner}</h1>
        <p style="font-size:1.2rem; color:#475569;">Your psychological DNA maps to specific high-growth careers.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    
    # LEFT: UNIVERSITY MATCHES
    with c1:
        st.markdown("### 🎯 Top University Matches")
        # Filter the embedded dataframe
        matches = df[df['Primary_Energy_Fit'] == winner]
        
        if not matches.empty:
            for idx, row in matches.iterrows():
                st.markdown(f"""
                <div class="info-card" style="margin-bottom:1rem; padding:1.5rem;">
                    <div style="display:flex; justify-content:space-between;">
                        <h4 style="margin:0;">{row['University_Name']}</h4>
                        <span style="background:#E0F2FE; color:#0077B6; padding:4px 8px; border-radius:6px; font-weight:bold;">{row['Match_Score']}% Match</span>
                    </div>
                    <p style="color:#64748B; font-size:0.9rem; margin-top:5px;"><b>Program:</b> {row['Program']}</p>
                    <p style="font-size:0.9rem; margin-top:10px;">✅ {row['Why']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No direct matches found. Book a call for custom analysis.")

    # RIGHT: GATED CONTENT (The Fix for 'KeyError')
    with c2:
        st.markdown("### 🗺️ Your 4-Year Roadmap")
        
        # Container for visual blurring
        st.markdown("""
        <div style="position:relative;">
            <div class="blur-box">
                <div class="info-card" style="margin-bottom:1rem;">
                    <h4>Year 1: Foundation</h4>
                    <p>Focus on core skills. Avoid rigid structures...</p>
                </div>
                <div class="info-card">
                    <h4>The Efficiency Trap</h4>
                    <p>Your weakness is detail. Fix it by...</p>
                </div>
            </div>
            
            <div class="lock-overlay">
                <div style="font-size:3rem; margin-bottom:10px;">🔒</div>
                <h3>Unlock Full Report</h3>
                <p style="color:#64748B; margin-bottom:1.5rem;">Get your 15-Page Strategy + Session</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # The actual form
        with st.form("lead_capture"):
            st.text_input("Full Name")
            email = st.text_input("Email Address", placeholder="student@gmail.com")
            
            st.markdown("""
            <div style="background:#F0F9FF; padding:15px; border-radius:8px; border:1px solid #0077B6; margin-bottom:15px; font-size:0.9rem;">
                💎 <b>Strategic Session (₹499)</b><br>
                Includes: Full Report, University List, 1:1 Mentorship.
            </div>
            """, unsafe_allow_html=True)
            
            if st.form_submit_button("Unlock Now - Pay ₹499", use_container_width=True):
                st.success("Redirecting to Payment Gateway...")

# --- 6. ROUTER ---
if st.session_state.page == 'home':
    page_home()
elif st.session_state.page == 'assessment':
    page_assessment()
elif st.session_state.page == 'result':
    page_result()
