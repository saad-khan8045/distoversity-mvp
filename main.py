import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Empowering India",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM PROFESSIONAL THEME (CSS) ---
st.markdown("""
    <style>
    /* IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    /* GLOBAL STYLES */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #FFFFFF;
        color: #1A202C;
    }

    /* HEADERS */
    h1, h2, h3 {
        color: #000080; /* Navy Blue */
        font-weight: 700;
    }
    
    h4, h5 {
        color: #0077B6; /* Distoversity Blue */
    }

    /* BUTTON STYLING (Premium Gradient) */
    .stButton>button {
        background: linear-gradient(90deg, #0077B6 0%, #005f8b 100%);
        color: white;
        border-radius: 8px;
        padding: 12px 30px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

    /* THE 'BLUR' EFFECT (For Lead Magnet) */
    .blur-content {
        filter: blur(8px);
        -webkit-filter: blur(8px);
        user-select: none;
        opacity: 0.6;
        pointer-events: none;
    }
    
    /* LOCKED BOX OVERLAY */
    .locked-overlay {
        background-color: rgba(240, 248, 255, 0.9);
        border: 2px solid #000080;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        position: relative;
        margin-top: -100px;
        z-index: 10;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    /* TRUST BOX (Disclaimer) */
    .trust-disclaimer {
        background-color: #F7FAFC;
        border-left: 4px solid #000080;
        padding: 15px;
        font-size: 0.85rem;
        color: #4A5568;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* CARD STYLING */
    .uni-card {
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        background-color: white;
        transition: 0.3s;
    }
    .uni-card:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border-color: #BEE3F8;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state['step'] = 'home'
if 'profile' not in st.session_state:
    st.session_state['profile'] = "Not Assessed"

# --- CONTENT VARIABLES (From Spreadsheets) ---
DISCLAIMER = """
**Core Guidance Disclaimer:** Distoversity's Genius Profile is a tool for career guidance based on personal preferences. 
It is not a substitute for professional psychological counseling or a guarantee of job placement.
"""

PRIVACY_POLICY = """
🔒 **Your Privacy is Key:** We collect your email to send you your results and personalized recommendations. 
We will never sell your data. Your information is stored securely per Indian data protection regulations.
"""

# --- PAGES ---

def page_home():
    # Hero Section
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown("### 🇮🇳 Empowering India's Students")
        st.title("Stop Guessing Your Future.\nStart Engineering It.")
        st.write(
            "90% of students choose the wrong degree based on marks, not mindset. "
            "Our AI-Psychometric Engine matches your unique 'Spark' to Top Universities like **Manipal, Amity, and LPU**."
        )
        
        st.markdown(f'<div class="trust-disclaimer">{DISCLAIMER}</div>', unsafe_allow_html=True)
        
        if st.button("Discover Your Spark (Free 2-Min Test) ➤"):
            st.session_state['step'] = 'assessment'
            st.rerun()
            
        st.caption("Trusted by 50,000+ Students | Methodology inspired by Wealth Dynamics")

    with col2:
        # Placeholder for a high-quality student image
        st.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Find your flow.")

    st.divider()
    
    # Social Proof / University Logos Strip
    st.markdown("<h5 style='text-align: center; color:#718096;'>PARTNERING WITH INDIA'S BEST ONLINE & CAMPUS PROGRAMS</h5>", unsafe_allow_html=True)
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1: st.markdown("**IIT Delhi**")
    with c2: st.markdown("**Manipal Online**")
    with c3: st.markdown("**Amity Online**")
    with c4: st.markdown("**LPU Online**")
    with c5: st.markdown("**DY Patil**")

def page_assessment():
    st.progress(25, text="Step 1 of 4: Identifying Core Energy...")
    st.subheader("⚡ Discover Your Spark")
    
    with st.form("spark_form"):
        st.write("**1. When working on a major project, what is your natural role?**")
        q1 = st.radio("Select the option that feels most like 'you':", [
            "A) Generating new ideas and starting things (Dynamo)",
            "B) Connecting with people and presenting (Blaze)",
            "C) Ensuring the timing and service is perfect (Tempo)",
            "D) Analyzing the data and building systems (Steel)"
        ], label_visibility="collapsed")
        
        st.write("")
        st.write("**2. What environment makes you feel most exhausted?**")
        st.radio("Select one:", [
            "A) Routine data entry and silence",
            "B) Being isolated in a room alone",
            "C) Chaos and lack of clear instructions",
            "D) Emotional drama and selling to strangers"
        ])
        
        st.write("")
        st.info("💡 *There are no wrong answers. Be honest to get the best University Match.*")
        
        submit = st.form_submit_button("Analyze My Profile")
        
        if submit:
            # SIMULATED ANALYSIS (Loading Screen)
            with st.spinner("🧠 Analyzing Neural Pathways..."):
                time.sleep(1)
            with st.spinner("🏛️ Scanning Database: Manipal, Amity, LPU, DY Patil..."):
                time.sleep(1.5)
            with st.spinner("⚙️ Calculating Career Risk Factors..."):
                time.sleep(1)
            
            # Simple Logic for MVP
            if "Dynamo" in q1: st.session_state['profile'] = "Dynamo (Creator)"
            elif "Blaze" in q1: st.session_state['profile'] = "Blaze (Influencer)"
            elif "Tempo" in q1: st.session_state['profile'] = "Tempo (Catalyst)"
            else: st.session_state['profile'] = "Steel (Analyst)"
            
            st.session_state['step'] = 'upsell'
            st.rerun()

def page_upsell():
    # THE RESULT (Visible)
    st.success(f"🎉 Analysis Complete: You are a **{st.session_state['profile']}**!")
    
    st.markdown("### 🔓 Your Profile Snapshot")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info(f"**Strength:** As a {st.session_state['profile']}, you thrive when you can focus on your natural flow. Traditional education often fails you because it ignores this.")
    with col_b:
        st.write("We have identified **3 University Programs** where your specific personality type is statistically more likely to succeed.")

    st.divider()

    # THE GATED CONTENT (Blurred)
    st.subheader("🏛️ Your Personalized University Matches")
    st.caption("Based on: Affordability, Accreditation, and Personality Fit.")

    c1, c2 = st.columns(2)
    
    # LEFT: VISIBLE LOGOS (The Tease)
    with c1:
        st.markdown("""
        <div class="uni-card">
            <h4>1. Amity University Online</h4>
            <p><b>Program:</b> BCA / MCA (AI Specialization)</p>
            <p>✅ <b>Match Score: 94%</b></p>
        </div>
        <div class="uni-card">
            <h4>2. Manipal University Jaipur</h4>
            <p><b>Program:</b> BBA (Digital Marketing)</p>
            <p>✅ <b>Match Score: 89%</b></p>
        </div>
         <div class="uni-card">
            <h4>3. Lovely Professional Uni (LPU)</h4>
            <p><b>Program:</b> MBA (Business Analytics)</p>
            <p>✅ <b>Match Score: 87%</b></p>
        </div>
        """, unsafe_allow_html=True)

    # RIGHT: BLURRED REASONING (The Value)
    with c2:
        st.markdown("""
        <div class="blur-content">
            <h4>Why Amity fits your DNA:</h4>
            <p>Based on your Dynamo profile, Amity's flexible module allows you to innovate without getting stuck in rigid attendance structures. The curriculum focuses on...</p>
            <br>
            <h4>Why Manipal fits your DNA:</h4>
            <p>Manipal offers the specific analytical rigor that a Steel profile needs. Their alumni network in Data Science is...</p>
            <br>
            <h4>Career Roadmap 2025-2029:</h4>
            <p>Year 1: Focus on Foundation. Year 2: Internship at...</p>
        </div>
        """, unsafe_allow_html=True)
        
        # THE LOCK OVERLAY
        st.markdown("""
        <div class="locked-overlay">
            <h3>🔒 UNLOCK YOUR REPORT</h3>
            <p>See exactly <b>WHY</b> these universities match your personality and get your 4-Year Roadmap.</p>
        </div>
        """, unsafe_allow_html=True)

    # LEAD CAPTURE FORM
    st.markdown("### 📩 Where should we send your Full Report?")
    with st.form("lead_capture"):
        email = st.text_input("Enter your email address", placeholder="student@gmail.com")
        st.markdown(f"<small>{PRIVACY_POLICY}</small>", unsafe_allow_html=True)
        
        unlock = st.form_submit_button("Send My Full Profile & Roadmap Now ➤")
        
        if unlock:
            if "@" in email:
                st.balloons()
                st.success(f"Success! The Full Report for {st.session_state['profile']} has been emailed to {email}.")
                st.info("Check your inbox (and spam folder) in 2 minutes.")
            else:
                st.error("Please enter a valid email address.")

def page_institutions():
    st.title("For Institutions: Recruit Precision, Not Just Volume.")
    st.markdown("### Transform Your Student Recruitment with AI")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("**The Problem:** High dropout rates and disengaged students happen when you recruit based on marks alone.")
        st.write("**The Distoversity Solution:** We don't just send you leads. We send you students whose **Genius Profile** aligns with your institutional DNA.")
        
        st.markdown("#### Partnership Benefits")
        st.markdown("""
        - ✅ **Targeted Recruitment:** Move beyond academics to recruit based on personality alignment.
        - ✅ **Lower Attrition:** Students matched by 'Energy' stay longer and perform better.
        - ✅ **Data-Driven:** Access our proprietary AI-matching algorithm.
        """)
        
        st.info('"Distoversity empowers us to recruit not just brilliant minds, but aligned personalities." — Dean, Top Partner University')

    with col2:
        with st.form("b2b_form"):
            st.write("**Request Institutional Demo**")
            st.text_input("Institution Name")
            st.text_input("Contact Person")
            st.text_input("Official Email")
            st.form_submit_button("Request Demo")

def page_faq():
    st.title("Frequently Asked Questions")
    
    with st.expander("Q: I'm confused about my career. How can Distoversity help?"):
        st.write("A: We help you discover your 'Genius Profile' via AI, guiding you to academic fields and universities (like Amity, Manipal, etc.) that truly fit your natural strengths.")
        
    with st.expander("Q: Is this a psychological test?"):
        st.write("A: No. It is a self-discovery tool based on Wealth Dynamics and Energy Profiling. It is designed for guidance, not clinical diagnosis.")
        
    with st.expander("Q: Is the University recommendation guaranteed admission?"):
        st.write("A: No. We identify 'Potential Matches' where you may thrive based on your profile. Admission depends on your academic performance and the university's criteria.")

    with st.expander("Q: Do you cover Online Degrees?"):
        st.write("A: Yes! We specialize in matching students to high-quality Online Degrees (Amity Online, Manipal Online, etc.) which are perfect for self-driven 'Dynamo' profiles.")

# --- MAIN NAVIGATION ---
def main():
    # Sidebar Navigation
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4729/4729351.png", width=50) # Placeholder Logo
    st.sidebar.title("Distoversity")
    menu = st.sidebar.radio("Navigation", ["Home", "Discover Your Spark", "For Universities (B2B)", "FAQ"])
    
    st.sidebar.markdown("---")
    st.sidebar.info("© 2025 Distoversity\nEmpowering India.")

    if menu == "Home":
        if st.session_state['step'] == 'home':
            page_home()
        elif st.session_state['step'] == 'assessment':
            page_assessment()
        elif st.session_state['step'] == 'upsell':
            page_upsell()
    
    elif menu == "Discover Your Spark":
        if st.session_state['step'] == 'upsell':
            page_upsell()
        else:
            page_assessment()
            
    elif menu == "For Universities (B2B)":
        page_institutions()
        
    elif menu == "FAQ":
        page_faq()

if __name__ == "__main__":
    main()
