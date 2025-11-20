import streamlit as st
import pandas as pd
import time
import plotly.graph_objects as go

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Identity-First Career Guidance",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. UI/UX DESIGN SYSTEM (CSS) ---
# Implementing your specific Palette: Light Blue (#ADD8E6), White, Coral Accent (#FF6B35)
st.markdown("""
    <style>
    /* IMPORT FONTS: Poppins (Headers) & Inter (Body) */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Poppins:wght@400;600;700&display=swap');

    :root {
        --primary: #ADD8E6;
        --accent: #FF6B35;
        --text: #1A1A1A;
        --bg: #FFFFFF;
        --creator: #9B59B6;
        --influencer: #E67E22;
        --catalyst: #27AE60;
        --analyst: #3498DB;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--text);
        background-color: #F8FAFC;
    }

    h1, h2, h3, h4 {
        font-family: 'Poppins', sans-serif;
        color: #0F172A;
    }

    /* HERO SECTION STYLES */
    .hero-container {
        background: linear-gradient(180deg, #F0F9FF 0%, #FFFFFF 100%);
        padding: 4rem 2rem;
        text-align: center;
        border-radius: 0 0 40px 40px;
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #0F172A 0%, #2563EB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
        margin-bottom: 1rem;
    }

    /* BUTTONS */
    .stButton>button {
        background: linear-gradient(135deg, #FF6B35 0%, #FF8C42 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 32px;
        font-weight: 600;
        font-size: 18px;
        box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 107, 53, 0.4);
        color: white;
    }

    /* CARDS */
    .energy-card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        border-top: 5px solid #ccc;
        transition: transform 0.2s;
    }
    .energy-card:hover { transform: translateY(-5px); }

    /* PROGRESS BAR */
    .stProgress > div > div > div > div {
        background-color: #FF6B35;
    }

    /* HIDE DEFAULT ELEMENTS */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* BLUR LOCK */
    .blur-content { filter: blur(8px); opacity: 0.6; pointer-events: none; }
    .lock-overlay {
        position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        background: rgba(255,255,255,0.95); padding: 2rem; border-radius: 16px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1); text-align: center; width: 80%;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'home'
if 'scores' not in st.session_state: st.session_state.scores = {'Creator':0, 'Influencer':0, 'Catalyst':0, 'Analyst':0}
if 'q_index' not in st.session_state: st.session_state.q_index = 0

# --- 4. DATA LOADING ---
@st.cache_data
def load_data():
    try:
        uni_df = pd.read_csv('data/university_program_details.csv')
        return uni_df
    except:
        return pd.DataFrame() # Fallback if data gen didn't run

data = load_data()

# --- 5. COMPONENTS ---

def navbar():
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown("<div style='font-family:Poppins; font-weight:700; font-size:1.5rem; color:#0F172A;'>Distoversity<span style='color:#FF6B35;'>.</span></div>", unsafe_allow_html=True)
    with col2:
        if st.button("Login"): pass

def render_hero():
    st.markdown("""
        <div class="hero-container">
            <div style="color:#FF6B35; font-weight:700; letter-spacing:1px; margin-bottom:10px;">INDIA'S FIRST IDENTITY-FIRST PLATFORM</div>
            <div class="hero-title">STOP GUESSING YOUR FUTURE.<br>START ENGINEERING IT.</div>
            <p style="font-size:1.2rem; color:#64748B; max-width:700px; margin:0 auto 2rem auto;">
                We don't ask "What are your marks?". We ask <b>"What is your flow?"</b>.
                Join 4,000+ students finding their career DNA.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Discover Your Energy Type (Free) ➤", use_container_width=True):
            st.session_state.page = 'assessment'
            st.rerun()
    
    # Trust Signals
    st.markdown("<br><div style='text-align:center; color:#94A3B8; font-weight:600;'>TRUSTED BY PARTNERS FROM</div>", unsafe_allow_html=True)
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.markdown("<h4 style='text-align:center; color:#CBD5E1;'>AMITY</h4>", unsafe_allow_html=True)
    c2.markdown("<h4 style='text-align:center; color:#CBD5E1;'>MANIPAL</h4>", unsafe_allow_html=True)
    c3.markdown("<h4 style='text-align:center; color:#CBD5E1;'>NMIMS</h4>", unsafe_allow_html=True)
    c4.markdown("<h4 style='text-align:center; color:#CBD5E1;'>LPU</h4>", unsafe_allow_html=True)
    c5.markdown("<h4 style='text-align:center; color:#CBD5E1;'>JAIN</h4>", unsafe_allow_html=True)

def render_energy_cards():
    st.markdown("<h2 style='text-align:center; margin-top:4rem;'>The 4 Energy Archetypes</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown("""
        <div class="energy-card" style="border-color: #9B59B6;">
            <h3 style="color:#9B59B6;">CREATOR</h3>
            <p><b>The Innovator</b></p>
            <p style="font-size:0.9rem; color:#666;">Big Picture, Innovation, start-ups.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="energy-card" style="border-color: #E67E22;">
            <h3 style="color:#E67E22;">INFLUENCER</h3>
            <p><b>The Connector</b></p>
            <p style="font-size:0.9rem; color:#666;">People, Sales, Leadership.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="energy-card" style="border-color: #27AE60;">
            <h3 style="color:#27AE60;">CATALYST</h3>
            <p><b>The Grounded</b></p>
            <p style="font-size:0.9rem; color:#666;">Execution, Service, Timing.</p>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div class="energy-card" style="border-color: #3498DB;">
            <h3 style="color:#3498DB;">ANALYST</h3>
            <p><b>The Architect</b></p>
            <p style="font-size:0.9rem; color:#666;">Data, Systems, Details.</p>
        </div>
        """, unsafe_allow_html=True)

# --- 6. ASSESSMENT LOGIC ---
QUESTIONS = [
    {"q": "When solving a problem, you naturally:", "opts": [
        ("Generate multiple creative solutions", "Creator"),
        ("Discuss with others to find consensus", "Influencer"),
        ("Follow proven step-by-step methods", "Catalyst"),
        ("Analyze data and metrics first", "Analyst")
    ]},
    {"q": "You feel most energized when:", "opts": [
        ("Creating something new from scratch", "Creator"),
        ("Presenting ideas and influencing outcomes", "Influencer"),
        ("Completing tasks on schedule", "Catalyst"),
        ("Perfecting systems and solving puzzles", "Analyst")
    ]},
    {"q": "After a 3-hour party with strangers:", "opts": [
        ("Energized with new ideas but need alone time", "Creator"),
        ("Completely energized and want to continue", "Influencer"),
        ("Ready to wind down with close friends", "Catalyst"),
        ("Exhausted and need quiet time to recharge", "Analyst")
    ]},
    {"q": "Your decision-making style is:", "opts": [
        ("Intuitive and pattern-based", "Creator"),
        ("People-focused and consensus-driven", "Influencer"),
        ("Experience-based and practical", "Catalyst"),
        ("Data-driven and logical", "Analyst")
    ]}
]

def render_assessment():
    st.markdown("<br>", unsafe_allow_html=True)
    progress = (st.session_state.q_index + 1) / len(QUESTIONS)
    st.progress(progress, text=f"Question {st.session_state.q_index + 1} of {len(QUESTIONS)}")
    
    q_data = QUESTIONS[st.session_state.q_index]
    
    st.markdown(f"""
    <div style="background:white; padding:3rem; border-radius:16px; box-shadow:0 4px 20px rgba(0,0,0,0.05); max-width:800px; margin:0 auto;">
        <h2 style="margin-bottom:2rem;">{q_data['q']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Render Options as large clickable buttons
    # In Streamlit, we use columns to make them look like a grid
    c1, c2 = st.columns(2)
    
    def answer_callback(profile):
        st.session_state.scores[profile] += 1
        if st.session_state.q_index < len(QUESTIONS) - 1:
            st.session_state.q_index += 1
        else:
            st.session_state.page = 'result'
        # No rerunning inside callback, script reruns automatically on interaction
    
    opts = q_data['opts']
    
    with c1:
        if st.button(f"A) {opts[0][0]}", use_container_width=True): answer_callback(opts[0][1])
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(f"C) {opts[2][0]}", use_container_width=True): answer_callback(opts[2][1])

    with c2:
        if st.button(f"B) {opts[1][0]}", use_container_width=True): answer_callback(opts[1][1])
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(f"D) {opts[3][0]}", use_container_width=True): answer_callback(opts[3][1])

def render_result_gated():
    # Calculate Winner
    scores = st.session_state.scores
    winner = max(scores, key=scores.get)
    total = sum(scores.values())
    pct = int((scores[winner]/total)*100) if total > 0 else 0
    
    # Color Mapping
    colors = {'Creator': '#9B59B6', 'Influencer': '#E67E22', 'Catalyst': '#27AE60', 'Analyst': '#3498DB'}
    primary_color = colors[winner]

    st.balloons()
    
    # VISIBLE HEADER
    st.markdown(f"""
    <div style="text-align:center; padding:2rem;">
        <div style="background:{primary_color}; color:white; padding:8px 16px; border-radius:30px; display:inline-block; font-weight:700;">PRIMARY ARCHETYPE DETECTED</div>
        <h1 style="font-size:4rem; color:{primary_color}; margin-top:1rem;">{winner} ({pct}%)</h1>
        <p style="color:#64748B; font-size:1.2rem;">Your psychological DNA maps to specific career paths.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    
    # VISIBLE PART: TOP UNIVERSITIES (TEASER)
    with c1:
        st.markdown("### 🎓 Top University Matches")
        # Filter data based on energy (Simulated logic)
        matches = data[data['Primary_Energy_Fit'] == winner]
        
        if not matches.empty:
            for idx, row in matches.iterrows():
                st.markdown(f"""
                <div style="background:white; padding:1.5rem; border-radius:12px; margin-bottom:1rem; border-left:5px solid {primary_color}; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
                    <h4>{row['University_Name']}</h4>
                    <div style="display:flex; gap:10px; font-size:0.9rem; color:#666;">
                        <span>NAAC {row['NAAC_Grade']}</span> • <span>pkg: {row['Average_Package']}</span>
                    </div>
                    <div style="margin-top:10px; color:{primary_color}; font-weight:600; font-size:0.9rem;">
                        ✅ 94% Match for {winner}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Data loading... showing sample matches.")

    # BLURRED PART: THE ROADMAP (LEAD MAGNET)
    with c2:
        st.markdown("### 🗺️ Strategic Career Roadmap")
        
        st.markdown("""
        <div style="position:relative;">
            <div class="blur-content">
                <div style="background:white; padding:2rem; border-radius:12px; margin-bottom:1rem;">
                    <h4>Year 1: Foundation Strategy</h4>
                    <p>Focus on the core skills of innovation. Avoid rigid structures...</p>
                </div>
                 <div style="background:white; padding:2rem; border-radius:12px;">
                    <h4>The "Efficiency Trap" Warning</h4>
                    <p>Your biggest weakness is detailed execution. To fix this...</p>
                </div>
            </div>
            
            <div class="lock-overlay">
                <div style="font-size:3rem;">🔒</div>
                <h3>Unlock Full Report</h3>
                <p>Get your 15-Page Career Roadmap + Session</p>
                <div style="text-align:left; margin-top:1rem;">
                    <form>
                    </form>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("lead_gen"):
            col_a, col_b = st.columns(2)
            with col_a: st.text_input("Name")
            with col_b: st.text_input("Phone")
            email = st.text_input("Email Address", placeholder="student@gmail.com")
            
            st.markdown(f"""
            <div style="background:#FFF4E5; padding:15px; border-radius:8px; border:1px solid #FF6B35; margin-bottom:15px;">
                <strong>💎 STRATEGIC POWER SESSION (₹499)</strong><br>
                <span style="font-size:0.9rem;">Includes: Full Report, University List, 1:1 Session, Community Access.</span>
            </div>
            """, unsafe_allow_html=True)
            
            submitted = st.form_submit_button(f"Unlock Now - Pay ₹499", use_container_width=True)
            if submitted:
                st.success("Redirecting to Razorpay Secure Gateway...")
                time.sleep(2)
                st.info("(Razorpay Integration would trigger here in live mode)")

# --- 7. ROUTER ---
navbar()
if st.session_state.page == 'home':
    render_hero()
    render_energy_cards()
elif st.session_state.page == 'assessment':
    render_assessment()
elif st.session_state.page == 'result':
    render_result_gated()
