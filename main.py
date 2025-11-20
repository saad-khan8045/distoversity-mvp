import streamlit as st
import time

# --- PAGE CONFIGURATION (Must be first) ---
st.set_page_config(
    page_title="Distoversity | Premium Career Architecture",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- PREMIUM CSS OVERHAUL ---
st.markdown("""
    <style>
    /* 1. IMPORT GOOGLE FONTS (Poppins for Headings, Inter for Body) */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@300;400;600&display=swap');

    /* 2. GLOBAL RESET */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1E293B; /* Slate 800 */
    }
    
    /* 3. HEADINGS */
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #0F172A; /* Slate 900 */
    }
    h1 { font-size: 3rem !important; line-height: 1.2 !important; }
    h2 { font-size: 2rem !important; }
    h3 { color: #0077B6 !important; } /* Distoversity Blue */

    /* 4. CUSTOM CARDS (Glassmorphism) */
    .premium-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid #F1F5F9;
        transition: transform 0.3s ease;
    }
    .premium-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,71,255,0.1);
        border-color: #0077B6;
    }

    /* 5. BUTTON STYLING */
    .stButton>button {
        background: linear-gradient(135deg, #0077B6 0%, #0056b3 100%);
        color: white;
        border-radius: 50px; /* Pill shape */
        padding: 12px 35px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 119, 182, 0.3);
        font-family: 'Poppins', sans-serif;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(0, 119, 182, 0.4);
    }

    /* 6. HERO SECTION GRADIENT */
    .hero-bg {
        background: linear-gradient(180deg, #F0F9FF 0%, #FFFFFF 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    /* 7. HIDE STREAMLIT DEFAULT ELEMENTS */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 8. BLUR EFFECT FOR UPSELL */
    .blur-text {
        color: transparent;
        text-shadow: 0 0 8px rgba(0,0,0,0.5);
        user-select: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state['step'] = 'landing'

# --- ASSETS (Use Unsplash URLs so it works on cloud) ---
IMG_HERO = "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1171&q=80"
IMG_DYNAMO = "https://cdn-icons-png.flaticon.com/512/2921/2921222.png" # Lightbulb
IMG_STEEL = "https://cdn-icons-png.flaticon.com/512/2103/2103650.png" # Chart

# --- PAGES ---

def render_navbar():
    # A custom simple navbar using columns
    c1, c2, c3 = st.columns([1, 3, 1])
    with c1:
        st.markdown("### 🔹 Distoversity")
    with c3:
        if st.button("Login / Sign Up"):
            st.toast("Portal coming soon!")

def render_hero():
    st.markdown('<div class="hero-bg">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("# Stop Guessing.\n# Start Engineering.")
        st.markdown("""
        <p style='font-size: 1.2rem; color: #475569; margin-top: 1rem;'>
        The Indian education system sells you degrees. We give you an <b>Identity</b>.
        Join 50,000+ students using AI to match their psychological DNA to the perfect university.
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🚀 Discover Your Spark (Free Analysis)"):
            st.session_state['step'] = 'assessment'
            st.rerun()
            
        st.markdown("<small>✨ Backed by Wealth Dynamics | 🏆 Partnered with Amity & Manipal</small>", unsafe_allow_html=True)

    with col2:
        st.image(IMG_HERO, use_column_width=True, output_format="PNG")
        
    st.markdown('</div>', unsafe_allow_html=True)

def render_features():
    st.markdown("<h2 style='text-align: center;'>How Distoversity Works</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B;'>Three steps to absolute career certainty.</p><br>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="premium-card">
            <h3>1. The Spark Test</h3>
            <p>Forget long exams. Our 2-minute AI assessment identifies your core energy frequency (Dynamo, Blaze, Tempo, Steel).</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="premium-card">
            <h3>2. The Alignment</h3>
            <p>We don't just suggest jobs. We match you to specific University Programs (BCA/MBA) that fit your psychological makeup.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="premium-card">
            <h3>3. The Roadmap</h3>
            <p>Get a 4-Year Strategic Plan, including internships and skills, not just a degree certificate.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

def render_assessment():
    st.markdown("<br>", unsafe_allow_html=True)
    # Using a container to center the form and make it look like a paper
    with st.container():
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.markdown("""
            <div class="premium-card" style="border-top: 5px solid #0077B6;">
                <h2 style="text-align:center;">⚡ Energy Profile Assessment</h2>
                <p style="text-align:center; color:#64748B;">Answer honestly to unlock your University Matches.</p>
            </div>
            <br>
            """, unsafe_allow_html=True)
            
            with st.form("assessment_form"):
                st.markdown("#### Q1. In a team, what is your superpower?")
                q1 = st.radio("Select one:", [
                    "Creating the Vision (I hate details)",
                    "Leading the People (I love talking)",
                    "Managing the Timeline (I love stability)",
                    "Analyzing the Data (I love facts)"
                ])
                
                st.markdown("<br>#### Q2. What is your biggest fear?", unsafe_allow_html=True)
                q2 = st.radio("Select one:", [
                    "Boredom & Routine",
                    "Being Ignored / Isolation",
                    "Sudden Changes / Chaos",
                    "Being Wrong / Criticism"
                ])
                
                st.markdown("<br>", unsafe_allow_html=True)
                submit = st.form_submit_button("Analyze My DNA 🧬")
                
                if submit:
                    with st.spinner("Connecting to Neural Engine..."):
                        time.sleep(1.5)
                    
                    # Simple Logic
                    if "Creating" in q1: st.session_state['result'] = "DYNAMO (Creator)"
                    elif "Leading" in q1: st.session_state['result'] = "BLAZE (Influencer)"
                    elif "Managing" in q1: st.session_state['result'] = "TEMPO (Catalyst)"
                    else: st.session_state['result'] = "STEEL (Analyst)"
                    
                    st.session_state['step'] = 'result'
                    st.rerun()

def render_result():
    profile = st.session_state.get('result', 'DYNAMO')
    
    st.balloons()
    st.markdown(f"""
    <div class="hero-bg" style="background: #F0FDF4; border: 1px solid #22C55E;">
        <h2 style="color: #15803D;">🎉 Analysis Complete</h2>
        <h1>You are a {profile}</h1>
        <p>You possess the rare ability to see what others cannot.</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("### 🔓 Your University Matches")
        st.markdown("""
        <div class="premium-card">
            <div style="display:flex; align-items:center; gap:10px;">
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png" width="50">
                <h4>Amity University Online</h4>
            </div>
            <p><b>Match Score: 98%</b></p>
            <p style="color:green; font-size:0.9rem;">Recommended for your profile</p>
        </div>
        <br>
        <div class="premium-card">
            <div style="display:flex; align-items:center; gap:10px;">
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png" width="50">
                <h4>Manipal University Jaipur</h4>
            </div>
            <p><b>Match Score: 92%</b></p>
            <p style="color:green; font-size:0.9rem;">High Alignment</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("### 🔒 The Why & The Roadmap")
        st.markdown("""
        <div class="premium-card" style="position:relative; overflow:hidden;">
            <h4>Why Amity Fits You:</h4>
            <p class="blur-text">Based on your profile, the curriculum structure allows for maximum creativity...</p>
            <br>
            <h4>Your 4-Year Plan:</h4>
            <p class="blur-text">Year 1: Focus on Ideation. Year 2: Intern at...</p>
            
            <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(255,255,255,0.7); display:flex; flex-direction:column; align-items:center; justify-content:center;">
                <h3>🔒 LOCKED</h3>
                <p>Enter email to unlock full report</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("lead_gen"):
            email = st.text_input("Email Address", placeholder="name@gmail.com")
            btn = st.form_submit_button("Unlock Full Report")
            if btn and email:
                st.success(f"Report sent to {email}!")

# --- MAIN ROUTING ---

render_navbar()

if st.session_state['step'] == 'landing':
    render_hero()
    render_features()
    
    # Footer / Social Proof
    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown("**Trusted by:**")
    c2.markdown("**IIT Delhi Alumni**")
    c3.markdown("**NID Design Heads**")
    c4.markdown("**500+ Schools**")

elif st.session_state['step'] == 'assessment':
    if st.button("← Back to Home"):
        st.session_state['step'] = 'landing'
        st.rerun()
    render_assessment()

elif st.session_state['step'] == 'result':
    if st.button("← Start Over"):
        st.session_state['step'] = 'landing'
        st.rerun()
    render_result()
