import streamlit as st
import time
import random

# --- 1. WORLD-CLASS CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Identity-First Career Architecture",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. VETERAN UI SYSTEM (Custom CSS) ---
st.markdown("""
    <style>
    /* IMPORT PREMIUM FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

    /* RESET & VARIABLES */
    :root {
        --primary: #0F172A;      /* Navy Black */
        --accent: #2563EB;       /* Electric Blue */
        --success: #10B981;      /* Emerald */
        --bg: #F8FAFC;           /* Slate 50 */
        --card-bg: #FFFFFF;
        --text-main: #1E293B;
        --text-sub: #64748B;
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-main);
        background-color: var(--bg);
    }

    /* HIDE STREAMLIT CHROME */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* TYPOGRAPHY SYSTEM */
    h1 {
        font-weight: 800 !important;
        letter-spacing: -0.03em !important;
        font-size: 3.5rem !important;
        background: linear-gradient(135deg, #0F172A 0%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1 !important;
    }
    
    h2 {
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
        font-size: 2.2rem !important;
        color: var(--primary);
    }

    .subtitle {
        font-size: 1.25rem;
        color: var(--text-sub);
        line-height: 1.6;
        max-width: 600px;
    }

    /* COMPONENT: PREMIUM CARD */
    .d-card {
        background: var(--card-bg);
        border: 1px solid #E2E8F0;
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .d-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.01);
        border-color: var(--accent);
    }

    /* COMPONENT: ACTION BUTTON */
    .d-btn-primary {
        display: inline-block;
        background: var(--accent);
        color: white;
        padding: 1rem 2.5rem;
        border-radius: 100px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.2s;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
        border: none;
        cursor: pointer;
        text-align: center;
    }
    .d-btn-primary:hover {
        background: #1D4ED8;
        transform: scale(1.02);
    }
    
    /* COMPONENT: LOCKED CONTENT BLUR */
    .locked-overlay {
        position: relative;
        overflow: hidden;
    }
    .blur-layer {
        filter: blur(12px);
        opacity: 0.4;
        user-select: none;
        pointer-events: none;
    }
    .lock-badge {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
        text-align: center;
        z-index: 10;
        width: 80%;
    }

    /* CUSTOM NAV BAR */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem 0;
        margin-bottom: 3rem;
        border-bottom: 1px solid #F1F5F9;
    }
    .brand-logo {
        font-weight: 800;
        font-size: 1.5rem;
        color: var(--primary);
        letter-spacing: -0.05em;
    }
    .brand-logo span { color: var(--accent); }

    /* FORM STYLING */
    .stRadio > div { gap: 1rem; }
    .stRadio label {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        width: 100%;
        transition: 0.2s;
    }
    .stRadio label:hover { border-color: var(--accent); background: #F8FAFC; }
    
    </style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# --- 4. UI COMPONENTS ---

def navbar():
    st.markdown("""
    <div class="nav-container">
        <div class="brand-logo">Distover<span>sity</span>.</div>
        <div style="color: #64748B; font-size: 0.9rem; font-weight: 500;">
            Science over Sales.
        </div>
    </div>
    """, unsafe_allow_html=True)

def footer():
    st.markdown("""
    <div style="margin-top: 5rem; padding-top: 2rem; border-top: 1px solid #E2E8F0; text-align: center; color: #94A3B8; font-size: 0.85rem;">
        <p>© 2025 Distoversity Inc. | Empowering India.</p>
        <p>Proprietary Framework adapted for Indian Education Context. Not a clinical diagnostic tool.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 5. PAGE LOGIC ---

def page_home():
    navbar()
    
    # HERO SECTION
    col1, col2 = st.columns([1.4, 1])
    
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background: #EFF6FF; color: #2563EB; font-weight: 700; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; display: inline-block; padding: 0.5rem 1rem; border-radius: 100px; margin-bottom: 1rem;">
            🚀 90% of Degrees are Mismatched
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h1>Stop Guessing Your Future.<br>Start Engineering It.</h1>", unsafe_allow_html=True)
        
        st.markdown("""
        <p class="subtitle">
            The era of subjective career advice is obsolete. We use <b>Computational Rigor</b> to match your psychological DNA to the top 1% of University Programs (Amity, Manipal, LPU).
        </p>
        <br>
        """, unsafe_allow_html=True)
        
        if st.button("Discover Your Core Genius (Free) ➤", type="primary"):
            st.session_state['page'] = 'assessment'
            st.rerun()
            
        st.markdown("""
        <div style="margin-top: 2rem; display: flex; gap: 2rem; opacity: 0.6; filter: grayscale(100%);">
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/Indian_Institute_of_Technology_Delhi_Logo.svg/1200px-Indian_Institute_of_Technology_Delhi_Logo.svg.png" height="40">
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png" height="40">
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png" height="40">
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Abstract 3D Illustration
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/business-decision-making-illustration-download-in-svg-png-gif-file-formats--strategy-choice-direction-path-startup-pack-people-illustrations-3972826.png?f=webp", use_column_width=True)

    # VALUE PROP SECTION
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Scientific Certainty. No Opinions.</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; margin-bottom: 3rem;'>We moved beyond 'Interest' to 'Energy'. See the difference.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="d-card">
            <div style="font-size: 2rem; margin-bottom: 1rem;">🧠</div>
            <h3>Your Genius</h3>
            <p style="color: #64748B;">Identify if you are a Creator, Influencer, Catalyst, or Analyst using our AI Engine.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="d-card">
            <div style="font-size: 2rem; margin-bottom: 1rem;">🏫</div>
            <h3>University Match</h3>
            <p style="color: #64748B;">We filter 500+ universities to find the curriculum that fits your cognitive style.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="d-card">
            <div style="font-size: 2rem; margin-bottom: 1rem;">🗺️</div>
            <h3>Strategic Roadmap</h3>
            <p style="color: #64748B;">Don't just study. Build a 4-year portfolio that makes you unemployable-proof.</p>
        </div>
        """, unsafe_allow_html=True)
    
    footer()

def page_assessment():
    st.markdown("""
    <div style="text-align: center; max-width: 700px; margin: 0 auto 3rem auto;">
        <div style="color: #2563EB; font-weight: 700; margin-bottom: 1rem;">STEP 1 OF 3</div>
        <h2>Decode Your Professional Identity</h2>
        <p style="color: #64748B;">This is not a test. It is a diagnosis. Answer based on who you <i>are</i>, not who you want to be.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # ASSESSMENT CONTAINER
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.form("distoversity_engine"):
                st.markdown("### 1. The Group Dynamic Protocol")
                st.markdown("In a high-pressure team project, which role do you naturally default to?")
                q1 = st.radio("Select one:", [
                    "💡 The Spark: I generate the core idea but hate the logistics. (Creator)",
                    "🗣️ The Voice: I pitch the idea and keep the team morale high. (Influencer)",
                    "⚡ The Engine: I ensure we hit the deadline and coordinate everyone. (Catalyst)",
                    "📊 The Anchor: I research the data and ensure accuracy. (Analyst)"
                ], label_visibility="collapsed")
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                st.markdown("### 2. The 'Ambiguity' Stress Test")
                st.markdown("What drains your energy the fastest?")
                q2 = st.radio("Select one:", [
                    "Routine, repetition, and details.",
                    "Working alone in a room for hours.",
                    "Chaos, lack of instructions, and changing plans.",
                    "High-pressure sales and emotional conflict."
                ], label_visibility="collapsed")
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                submitted = st.form_submit_button("Reveal My Core Genius ➤", type="primary")
                
                if submitted:
                    with st.spinner("Running Multidimensional Regression..."):
                        time.sleep(1.5)
                    with st.spinner("Mapping to Latent Career Space..."):
                        time.sleep(1.0)
                    
                    # LOGIC MAPPING
                    if "Spark" in q1: st.session_state['profile'] = "CREATOR"
                    elif "Voice" in q1: st.session_state['profile'] = "INFLUENCER"
                    elif "Engine" in q1: st.session_state['profile'] = "CATALYST"
                    else: st.session_state['profile'] = "ANALYST"
                    
                    st.session_state['page'] = 'result'
                    st.rerun()

def page_result():
    profile = st.session_state.get('profile', 'CATALYST')
    
    # DYNAMIC CONTENT (Based on your 'Rhythm Master' input)
    if profile == "CATALYST" or profile == "ANALYST":
        archetype = "THE RHYTHM MASTER"
        tagline = "The Operational Architect"
        pain_point = "Ambiguity & Inefficiency"
        solution = "Lead Through Data"
    else:
        archetype = "THE VISIONARY BUILDER"
        tagline = "The Innovation Architect"
        pain_point = "Stagnation & Routine"
        solution = "Rapid Prototyping"

    st.balloons()
    
    # RESULT HERO
    st.markdown(f"""
    <div class="d-card" style="background: linear-gradient(135deg, #EFF6FF 0%, #FFFFFF 100%); border-color: #BFDBFE; text-align: center; margin-bottom: 2rem;">
        <div style="color: #2563EB; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 1rem;">CORE GENIUS REVEALED</div>
        <h1 style="font-size: 4rem !important; margin-bottom: 0.5rem;">{profile}</h1>
        <h3 style="color: #1E40AF !important;">Archetype: {archetype}</h3>
        <p style="max-width: 600px; margin: 1rem auto; color: #475569;">
            You are the {tagline}. Your biggest professional pain point is <b>{pain_point}</b>. 
            You need certainty, process, and measurable finish lines.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    # 1. THE UNIVERSITY MATCH (VISIBLE TEASER)
    with col1:
        st.markdown("### 🎯 Your University Matches")
        st.markdown("""
        <div class="d-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
                <div style="font-weight:700; font-size:1.1rem;">Manipal University Jaipur</div>
                <div style="background:#DCFCE7; color:#15803D; padding:4px 8px; border-radius:4px; font-size:0.8rem; font-weight:700;">96% MATCH</div>
            </div>
            <p style="font-size:0.9rem; color:#64748B; margin-bottom:0.5rem;"><b>Recommended Program:</b> B.Tech (Data Science) or BBA (Analytics)</p>
            <p style="font-size:0.9rem;">✅ <b>Why:</b> Matches your need for {solution}. Their curriculum is structured, not chaotic.</p>
        </div>
        <div class="d-card" style="margin-top: 1rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
                <div style="font-weight:700; font-size:1.1rem;">Amity University Online</div>
                <div style="background:#DCFCE7; color:#15803D; padding:4px 8px; border-radius:4px; font-size:0.8rem; font-weight:700;">92% MATCH</div>
            </div>
            <p style="font-size:0.9rem; color:#64748B; margin-bottom:0.5rem;"><b>Recommended Program:</b> BCA (Cloud Security)</p>
            <p style="font-size:0.9rem;">✅ <b>Why:</b> Offers the verifiable precision you crave.</p>
        </div>
        """, unsafe_allow_html=True)

    # 2. THE "LOCKED" STRATEGIC DEEP DIVE (LEAD MAGNET)
    with col2:
        st.markdown("### 🗺️ Your Strategic Roadmap")
        
        st.markdown(f"""
        <div class="locked-overlay">
            <div class="blur-layer">
                <div class="d-card">
                    <h4>🚨 Critical Weak Point: The Efficiency Trap</h4>
                    <p>Your drive for analysis risks paralyzing your speed. If you fail to inject Creator energy, you will just be an Auditor...</p>
                    <br>
                    <h4>⚡ Phase 1: Rapid Prototyping</h4>
                    <p>Master structured experimentation. Launch, test, and discard concepts using Agile...</p>
                    <br>
                    <h4>🗣️ Phase 2: High-Leverage Articulation</h4>
                    <p>Move beyond data to selling the vision. Convert complex insights into narratives...</p>
                    <br>
                    <h4>💰 Salary Projection 2029</h4>
                    <p>Based on this trajectory, your estimated market value will be...</p>
                </div>
            </div>
            
            <div class="lock-badge">
                <div style="font-size: 2rem; margin-bottom: 1rem;">🔒</div>
                <h3>Unlock Your Full Strategy</h3>
                <p style="color: #64748B; font-size: 0.9rem; margin-bottom: 1.5rem;">
                    Get the full <b>"Rhythm Master" Report</b>, the "Efficiency Trap" warning, and the 4-Year Execution Plan.
                </p>
                
                <div style="text-align: left;">
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # ACTUAL STREAMLIT FORM FOR INTERACTION
        with st.form("lead_gen"):
            email = st.text_input("Enter your email to unlock the full PDF:", placeholder="student@gmail.com")
            st.caption("🔒 We respect your data privacy. No spam.")
            unlock_btn = st.form_submit_button("Send My Full Report & Roadmap ➤", type="primary")
            
            if unlock_btn and email:
                st.success(f"Success! The 'Rhythm Master' Protocol has been sent to {email}.")
                st.info("Please check your inbox in 3 minutes.")

# --- 6. MAIN ROUTING ---

if st.session_state['page'] == 'home':
    page_home()
elif st.session_state['page'] == 'assessment':
    page_assessment()
elif st.session_state['page'] == 'result':
    page_result()
