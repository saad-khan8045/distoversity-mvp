import streamlit as st
import time

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | The Career Architecture Platform",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. ULTRA-PREMIUM CSS (Glassmorphism & Gradients) ---
st.markdown("""
    <style>
    /* IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Plus+Jakarta+Sans:wght@400;500;700&display=swap');

    /* GLOBAL VARIABLES */
    :root {
        --primary-dark: #0B0F19;
        --primary-blue: #3B82F6;
        --accent-glow: #8B5CF6;
        --text-main: #1E293B;
        --glass-bg: rgba(255, 255, 255, 0.9);
        --glass-border: rgba(255, 255, 255, 0.6);
    }

    /* MODERN BACKGROUND (The "Catchy" Look) */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgba(59, 130, 246, 0.1) 0%, transparent 20%),
                    radial-gradient(circle at 90% 80%, rgba(139, 92, 246, 0.1) 0%, transparent 20%),
                    #F8FAFC;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* HIDE DEFAULT STREAMLIT ELEMENTS */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* TYPOGRAPHY */
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif;
        color: var(--primary-dark);
    }
    
    /* ANIMATED GRADIENT TEXT */
    .gradient-text {
        background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* GLASS CARDS */
    .glass-card {
        background: var(--glass-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid #E2E8F0;
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.04);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(37, 99, 235, 0.1);
        border-color: #BFDBFE;
    }

    /* HERO RESULT CARD (Gradient Border) */
    .hero-card {
        background: white;
        border-radius: 24px;
        padding: 3rem;
        text-align: center;
        position: relative;
        border: 2px solid transparent;
        background-image: linear-gradient(white, white), linear-gradient(135deg, #3B82F6, #8B5CF6);
        background-origin: border-box;
        background-clip: content-box, border-box;
        box-shadow: 0 20px 50px rgba(37, 99, 235, 0.15);
        margin-bottom: 3rem;
    }

    /* BUTTON STYLING */
    .stButton>button {
        background: linear-gradient(90deg, #2563EB 0%, #4F46E5 100%);
        color: white;
        border-radius: 12px;
        padding: 16px 32px;
        font-weight: 600;
        border: none;
        width: 100%;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.5);
    }

    /* LOCK & BLUR SECTION (Fixed the bug) */
    .blur-container {
        position: relative;
        overflow: hidden;
        border-radius: 16px;
    }
    .blur-content {
        filter: blur(8px);
        opacity: 0.6;
        pointer-events: none;
        user-select: none;
    }
    .lock-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,1) 60%);
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
        padding-bottom: 2rem;
        z-index: 10;
    }
    .lock-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        background: #EFF6FF;
        width: 80px;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }

    /* NAVBAR */
    .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem 0;
        margin-bottom: 2rem;
    }
    .logo { font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.8rem; color: #0F172A; }
    .logo span { color: #2563EB; }
    </style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# --- 4. UI COMPONENTS ---

def render_navbar():
    st.markdown("""
    <div class="nav">
        <div class="logo">Distover<span>sity</span>.</div>
        <div style="font-weight: 500; color: #64748B; background: white; padding: 8px 16px; border-radius: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            Science > Sales
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_hero():
    render_navbar()
    
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="display:inline-block; background:#EEF2FF; color:#4F46E5; font-weight:700; font-size:0.8rem; padding:6px 12px; border-radius:30px; margin-bottom:1rem;">
            🚀 THE NEW STANDARD IN CAREER GUIDANCE
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h1 style='font-size: 4rem; line-height: 1.1;'>Stop Guessing.<br><span class='gradient-text'>Start Engineering.</span></h1>", unsafe_allow_html=True)
        
        st.markdown("""
        <p style="font-size: 1.2rem; color: #475569; line-height: 1.6; margin-top: 1rem; max-width: 90%;">
            We don't ask what you <i>like</i>. We analyze who you <i>are</i>. 
            Join 50,000+ students using AI to match their psychological DNA to Top Tier Universities.
        </p>
        <br>
        """, unsafe_allow_html=True)
        
        if st.button("⚡ Discover Your Core Genius (Free)"):
            st.session_state['page'] = 'assessment'
            st.rerun()
            
        st.markdown("""
        <div style="margin-top: 2rem; display: flex; gap: 1rem; align-items: center; opacity: 0.7;">
            <div style="font-size: 0.9rem; font-weight: 600; color: #64748B;">TRUSTED BY:</div>
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/Indian_Institute_of_Technology_Delhi_Logo.svg/1200px-Indian_Institute_of_Technology_Delhi_Logo.svg.png" height="30" style="filter: grayscale(100%);">
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png" height="30" style="filter: grayscale(100%);">
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png" height="30" style="filter: grayscale(100%);">
        </div>
        """, unsafe_allow_html=True)

    with c2:
        # A cleaner, more abstract 3D visual
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/startup-launch-illustration-download-in-svg-png-gif-file-formats--rocket-business-project-management-boost-pack-illustrations-3689409.png?f=webp", use_column_width=True)

def render_assessment():
    st.progress(33, "Analyzing Cognitive Patterns...")
    
    st.markdown("""
    <div style="text-align:center; margin-bottom: 3rem;">
        <h2 style="font-size: 2.5rem;">Decode Your Identity</h2>
        <p style="color:#64748B;">Select the option that feels most natural to you.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            with st.form("quiz_form"):
                st.markdown("#### 1. In a team, what is your superpower?")
                q1 = st.radio("Select one:", [
                    "💡 Creating the Vision (I hate details)",
                    "🗣️ Leading the People (I love talking)",
                    "⚡ Managing the Timeline (I love stability)",
                    "📊 Analyzing the Data (I love facts)"
                ], label_visibility="collapsed")
                
                st.markdown("<br>#### 2. What is your biggest stressor?", unsafe_allow_html=True)
                q2 = st.radio("Select one:", [
                    "Boredom & Routine",
                    "Isolation / Working Alone",
                    "Chaos / Last minute changes",
                    "Being Wrong / Inaccuracy"
                ], label_visibility="collapsed")
                
                st.markdown("<br>", unsafe_allow_html=True)
                submit = st.form_submit_button("Analyze My Profile ➤")
                
                if submit:
                    with st.spinner("Mapping Neural Pathways..."):
                        time.sleep(1.5)
                    
                    if "Creating" in q1: st.session_state['profile'] = "CREATOR"
                    elif "Leading" in q1: st.session_state['profile'] = "INFLUENCER"
                    elif "Managing" in q1: st.session_state['profile'] = "CATALYST"
                    else: st.session_state['profile'] = "ANALYST"
                    
                    st.session_state['page'] = 'result'
                    st.rerun()

def render_result():
    profile = st.session_state.get('profile', 'CREATOR')
    
    # Dynamic Text Logic
    if profile == "CREATOR":
        archetype = "THE VISIONARY BUILDER"
        pain = "Stagnation & Routine"
    elif profile == "INFLUENCER":
        archetype = "THE CHARISMATIC LEADER"
        pain = "Isolation & Details"
    elif profile == "CATALYST":
        archetype = "THE RHYTHM MASTER"
        pain = "Ambiguity & Inefficiency"
    else:
        archetype = "THE SYSTEM ARCHITECT"
        pain = "Chaos & Inaccuracy"

    st.balloons()
    
    # 1. HERO CARD (The Big Reveal)
    st.markdown(f"""
    <div class="hero-card">
        <div style="color: #64748B; font-weight: 600; letter-spacing: 2px; font-size: 0.9rem; margin-bottom: 1rem;">CORE GENIUS REVEALED</div>
        <h1 class="gradient-text" style="font-size: 5rem !important; margin: 0;">{profile}</h1>
        <h3 style="margin-top: 1rem;">Archetype: {archetype}</h3>
        <p style="color: #475569; max-width: 600px; margin: 1rem auto;">
            You are not just a student. You are an Architect of {profile.lower()}s. 
            Your biggest professional pain point is <b>{pain}</b>. 
            You need certainty, process, and measurable finish lines.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1])
    
    # 2. UNIVERSITY MATCHES (Glass Cards)
    with c1:
        st.markdown("### 🎯 University Matches")
        st.markdown("""
        <div class="glass-card" style="margin-bottom: 1.5rem;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-weight:700; font-size:1.2rem;">Manipal University Jaipur</div>
                <div style="background:#DCFCE7; color:#15803D; padding:4px 10px; border-radius:6px; font-weight:700; font-size:0.8rem;">96% MATCH</div>
            </div>
            <p style="color:#64748B; margin-top:0.5rem; font-size:0.95rem;"><b>Program:</b> B.Tech (Data Science) / BBA</p>
            <p style="font-size:0.9rem; margin-top:0.5rem;">✅ <b>Why:</b> Matches your need for structure. Their curriculum is precise, not chaotic.</p>
        </div>
        
        <div class="glass-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-weight:700; font-size:1.2rem;">Amity University Online</div>
                <div style="background:#DCFCE7; color:#15803D; padding:4px 10px; border-radius:6px; font-weight:700; font-size:0.8rem;">92% MATCH</div>
            </div>
            <p style="color:#64748B; margin-top:0.5rem; font-size:0.95rem;"><b>Program:</b> BCA (Cloud Security)</p>
            <p style="font-size:0.9rem; margin-top:0.5rem;">✅ <b>Why:</b> Offers the verifiable precision you crave.</p>
        </div>
        """, unsafe_allow_html=True)

    # 3. THE LOCKED SECTION (Fixed the bug by using absolute positioning within HTML)
    with c2:
        st.markdown("### 🗺️ Your Strategic Roadmap")
        
        # This entire block is HTML to ensure the blur works perfectly
        st.markdown("""
        <div class="glass-card blur-container">
            <div class="blur-content">
                <h4 style="color: #1E293B;">🚨 Critical Weak Point: The Efficiency Trap</h4>
                <p style="color: #64748B;">Your inherent drive for process risks paralyzing your speed. You will become an Auditor instead of an Architect if you don't...</p>
                <br>
                <h4 style="color: #1E293B;">⚡ Phase 1: Rapid Prototyping</h4>
                <p style="color: #64748B;">Master structured experimentation. Launch, test, and discard concepts using Agile methodologies...</p>
                <br>
                <h4 style="color: #1E293B;">🗣️ Phase 2: High-Leverage Articulation</h4>
                <p style="color: #64748B;">Move beyond data to selling the vision. Convert complex insights into narratives...</p>
                <br>
                <h4 style="color: #1E293B;">💰 Salary Projection 2029</h4>
                <p style="color: #64748B;">Based on current market trends for {profile}s, your estimated starting package...</p>
            </div>

            <div class="lock-overlay">
                <div class="lock-icon">🔒</div>
                <h3 style="margin:0;">Unlock Full Report</h3>
                <p style="color:#64748B; margin-bottom:1.5rem; font-size:0.9rem;">Get the 15-Page "Rhythm Master" Protocol</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # The Functional Form (Outside the HTML block so Streamlit handles the logic)
        with st.form("lead_gen"):
            email = st.text_input("Enter email to unlock PDF:", placeholder="student@gmail.com")
            unlock = st.form_submit_button("Send My Roadmap Now")
            
            if unlock:
                if "@" in email:
                    st.success(f"Success! Report sent to {email}")
                else:
                    st.error("Please enter a valid email.")

# --- 5. ROUTER ---
if st.session_state['page'] == 'home':
    render_hero()
elif st.session_state['page'] == 'assessment':
    render_navbar()
    render_assessment()
elif st.session_state['page'] == 'result':
    render_navbar()
    render_result()
