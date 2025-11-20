import streamlit as st
import pandas as pd
import time
import plotly.express as px
import random

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Discover Your Spark",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# --- 2. ULTRA-PREMIUM DESIGN SYSTEM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    :root {
        --primary: #0077B6;       /* Deep Sky Blue */
        --primary-dark: #023E8A;
        --primary-light: #ADE8F4;
        --accent: #00B4D8;        /* Bright Blue */
        --text-main: #0F172A;
        --text-sub: #475569;
        --white: #FFFFFF;
        --hero-gradient: radial-gradient(circle at 50% 0%, #E0F2FE 0%, #FFFFFF 70%); 
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-main);
        background-color: #FFFFFF;
        scroll-behavior: smooth;
    }

    /* HEADERS */
    h1, h2, h3 { font-family: 'Outfit', sans-serif; color: var(--primary-dark); font-weight: 800; }
    h1 { font-size: 4rem !important; letter-spacing: -2px; line-height: 1.1; }
    
    /* COMPONENT: PREMIUM GLASS CARD */
    .d-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    .d-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 50px -10px rgba(0, 119, 182, 0.15);
        border-color: var(--accent);
    }

    /* COMPONENT: AI REPORT CARD (Updated Font) */
    .ai-report-box {
        background: #F8FAFC;
        border-left: 5px solid #0EA5E9;
        padding: 25px;
        margin-bottom: 20px;
        font-family: 'Plus Jakarta Sans', sans-serif; /* FIXED: Matches site font now */
        font-size: 1rem;
        line-height: 1.6;
        color: #334155;
        border-radius: 8px;
    }
    
    /* COMPONENT: CTA BOX */
    .cta-box {
        background: linear-gradient(135deg, #0077B6 0%, #023E8A 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 25px rgba(0, 119, 182, 0.3);
    }
    .cta-box h3 { color: white !important; margin-bottom: 10px; }

    /* COMPONENT: TAGS */
    .feature-tag {
        background: #F1F5F9; color: #475569; padding: 4px 12px; 
        border-radius: 20px; font-size: 0.8rem; font-weight: 600; 
        display: inline-block; margin-right: 5px; margin-bottom: 5px;
    }
    .match-tag {
        background: #DCFCE7; color: #166534; padding: 4px 12px; 
        border-radius: 20px; font-size: 0.8rem; font-weight: 700;
    }

    /* COMPONENT: ASSESSMENT QUESTION TEXT */
    .question-text {
        font-size: 1.2rem;
        font-weight: 600;
        color: #0F172A;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }

    /* COMPONENT: STICKY NAV */
    div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stHorizontalBlock"]) {
        position: sticky;
        top: 0;
        background-color: rgba(255, 255, 255, 0.98);
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
        padding: 0.6rem 2rem;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 119, 182, 0.2);
        transition: 0.2s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 8px 25px rgba(0, 119, 182, 0.3); }
    
    /* HERO */
    .hero-section {
        background: var(--hero-gradient);
        padding: 6rem 2rem 5rem 2rem;
        text-align: center;
        border-radius: 0 0 60px 60px;
        margin-bottom: 4rem;
        border-bottom: 1px solid #E0F2FE;
    }

    /* ALISON */
    .alison-section {
        background: linear-gradient(135deg, #FFF7ED 0%, #FFFFFF 100%);
        border: 1px solid #FFEDD5;
        border-radius: 24px;
        padding: 3rem;
        text-align: center;
        margin-top: 5rem;
    }
    
    /* UTILS */
    .icon-circle {
        width: 60px; height: 60px; background: #F0F9FF; border-radius: 50%; 
        display: flex; align-items: center; justify-content: center; 
        font-size: 1.8rem; margin: 0 auto 1rem auto; color: var(--primary);
    }

    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. ENRICHED PARTNER DATA ---
UNIVERSITY_DATA = [
    {
        "name": "Jain Online", 
        "location": "Bangalore", 
        "naac": "A++", 
        "nirf": "Top 100",
        "fees": 210000, 
        "program": "MBA Marketing", 
        "energy": "Distoversity Influencer", 
        "type": "Online Degree", 
        "approvals": "UGC-DEB, AICTE", 
        "placement": "98%",
        "avg_pkg": "6.2 LPA",
        "highest_pkg": "32 LPA",
        "highlights": "Strong Alumni, Live Classes",
        "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Jain_University_logo.png"
    },
    {
        "name": "Manipal University Online", 
        "location": "Jaipur", 
        "naac": "A+", 
        "nirf": "Rank 76",
        "fees": 175000, 
        "program": "MCA Data Science", 
        "energy": "Distoversity Analyst", 
        "type": "Online Degree", 
        "approvals": "UGC, NAAC", 
        "placement": "94%",
        "avg_pkg": "5.5 LPA",
        "highest_pkg": "18 LPA",
        "highlights": "Global Access, Coursera Free",
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png"
    },
    {
        "name": "Amity University Online", 
        "location": "Global", 
        "naac": "A+", 
        "nirf": "Top 50",
        "fees": 345000, 
        "program": "BCA Cloud Security", 
        "energy": "Distoversity Creator", 
        "type": "Online Degree", 
        "approvals": "UGC-DEB, WES", 
        "placement": "92%",
        "avg_pkg": "4.8 LPA",
        "highest_pkg": "15 LPA",
        "highlights": "Virtual Job Fairs, Portfolio Building",
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png"
    },
    {
        "name": "LPU Online", 
        "location": "Global", 
        "naac": "A++", 
        "nirf": "Rank 47",
        "fees": 160000, 
        "program": "MBA Operations", 
        "energy": "Distoversity Catalyst", 
        "type": "Online Degree", 
        "approvals": "UGC, AICTE", 
        "placement": "91%",
        "avg_pkg": "5.0 LPA",
        "highest_pkg": "21 LPA",
        "highlights": "Affordable, Mentor Support",
        "img": "https://upload.wikimedia.org/wikipedia/en/d/d4/Lovely_Professional_University_logo.png"
    },
    {
        "name": "Chandigarh University", 
        "location": "Online", 
        "naac": "A+", 
        "nirf": "Rank 29",
        "fees": 180000, 
        "program": "MBA General", 
        "energy": "Distoversity Influencer", 
        "type": "Online Degree", 
        "approvals": "UGC-DEB", 
        "placement": "89%",
        "avg_pkg": "5.2 LPA",
        "highest_pkg": "28 LPA",
        "highlights": "Flexible Exams, Case Studies",
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Chandigarh_University_logo.png/220px-Chandigarh_University_logo.png"
    },
    {
        "name": "NMIMS CDOL", 
        "location": "Online", 
        "naac": "A+", 
        "nirf": "Top 20 B-School",
        "fees": 400000, 
        "program": "MBA Finance", 
        "energy": "Distoversity Analyst", 
        "type": "Online Degree", 
        "approvals": "UGC-DEB, AICTE", 
        "placement": "93%",
        "avg_pkg": "7.0 LPA",
        "highest_pkg": "45 LPA",
        "highlights": "Premium Brand, Leadership Focus",
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/NMIMS_University_logo.png/220px-NMIMS_University_logo.png"
    },
    {
        "name": "DY Patil Online", 
        "location": "Pune", 
        "naac": "A++", 
        "nirf": "Rank 46",
        "fees": 120000, 
        "program": "BBA General", 
        "energy": "Distoversity Catalyst", 
        "type": "Online Degree", 
        "approvals": "UGC, AICTE", 
        "placement": "90%",
        "avg_pkg": "4.2 LPA",
        "highest_pkg": "12 LPA",
        "highlights": "Flexible Exams, Mentor Support",
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Dr._D._Y._Patil_Vidyapeeth_logo.png/220px-Dr._D._Y._Patil_Vidyapeeth_logo.png"
    }
]
df = pd.DataFrame(UNIVERSITY_DATA)

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'user_scores' not in st.session_state: st.session_state.user_scores = {}

# Init Chat History for Eduveer
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I'm Eduveer, your AI career guide. Ask me anything about online degrees, university comparisons, or finding your genius profile!"}]

# --- 5. AI GENERATION LOGIC & POPUP ---
def generate_report_text(profile, scores):
    """Generates the text for the report based on the specific profile."""
    
    # Mapping Short Logic to Full Logic
    pain_point = ""
    achilles_heel = ""
    skills = []
    
    # Extract just the type for logic (Creator, Influencer, etc.)
    core_type = profile.replace("Distoversity ", "")

    if core_type == "Creator":
        pain_point = "You despise routine, bureaucracy, and being told 'that's how we've always done it.' Ambiguity is your playground, but execution is your prison."
        achilles_heel = "The 'Idea Junkie' Syndrome. You start 50 projects and finish zero. Without structure, you risk becoming a dreamer who never ships."
        skills = ["Systems Thinking (to ground your ideas)", "Project Management (to finish what you start)", "Strategic Leadership"]
    elif core_type == "Influencer":
        pain_point = "You hate isolation and spreadsheets. You thrive on energy, yet you feel drained when forced to work in a silo without human connection."
        achilles_heel = "The 'Surface Level' Trap. You can sell anything, but if you lack depth, you risk being seen as 'all talk, no action'."
        skills = ["Data Analytics (to back your pitch)", "Financial Literacy", "Operational Execution"]
    elif core_type == "Catalyst":
        pain_point = "You hate chaos and vague instructions. You want a clear target, but you feel undervalued when 'creative types' get all the glory."
        achilles_heel = "The 'Cog in the Wheel' Risk. You are so good at execution you risk getting stuck in middle management forever."
        skills = ["Innovation Strategy (to see the big picture)", "Public Speaking", "Agile Leadership"]
    elif core_type == "Analyst":
        pain_point = "You hate hype and emotional decision making. You want the data, but you feel frustrated when others ignore the facts for a 'good story'."
        achilles_heel = "Analysis Paralysis. You risk waiting for 100% certainty before moving, missing every major opportunity."
        skills = ["Persuasive Communication (to sell your data)", "Team Management", "Creative Problem Solving"]

    # The Report Text
    report = f"""
    ### SECTION 1: YOUR CORE GENIUS REVEAL (The Instant Validation)
    **Archetype: {profile} ({int(scores.get(profile, 0))}% Match)**
    
    Listen closely: Your brain is wired differently. {pain_point}
    
    You don't need 'fixing'. You need alignment. The world tries to force you into a box, but your energy spectrum proves you were built for something else.

    ---
    
    ### SECTION 2: YOUR CRITICAL WEAK POINT (The Urgency)
    **The Danger Zone: {achilles_heel}**
    
    Here is the hard truth: Talent without leverage is just a hobby. If you do not develop the specific counter-skills to balance your energy, you will hit a ceiling. You risk watching less talented people overtake you simply because they mastered the things you ignore.
    
    Don't let your greatest strength become your single point of failure.

    ---

    ### SECTION 3: YOUR STRATEGIC ROADMAP (The High Value Path)
    **The Solution: Your Next Move**
    
    To unlock your full potential, you don't need 'more education'. You need *strategic* upskilling. Based on your profile, you must master these three high-impact skills immediately:
    
    1. **{skills[0]}**
    2. **{skills[1]}**
    3. **{skills[2]}**
    
    This is not about changing who you are. It's about arming yourself with the weapons you lack.
    """
    return report

@st.dialog("⚡ CHIEF GENIUS OFFICER REPORT")
def show_popup_report(profile, scores):
    report_content = generate_report_text(profile, scores)
    
    st.markdown(f"""
    <div class="ai-report-box">
        {report_content}
    </div>
    """, unsafe_allow_html=True)
    
    # SECTION 4: THE CLOSING PITCH (The Irresistible Offer)
    st.markdown("""
    <div class="cta-box">
        <h3>🚀 The Final Decision</h3>
        <p>You are standing at a crossroads. You can go back to ambiguity, or you can step into clarity.</p>
        <p style="font-size:0.9rem; opacity:0.9;">We have curated a specific roadmap that bridges your gap.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("📞 Book My Career Advice Call Now", type="primary", use_container_width=True):
        st.success("Request Received! Our Chief Genius Officer will contact you within 2 hours.")
        time.sleep(2)
        st.rerun()

# --- 6. NAVIGATION SYSTEM ---
def navbar():
    with st.container():
        c1, c2, c3, c4, c5, c6, c7 = st.columns([2, 1, 1, 1, 1, 1, 1.5])
        with c1:
            st.markdown("<div class='nav-logo'>Distoversity<span style='color:#0EA5E9'>.</span></div>", unsafe_allow_html=True)
        
        if c2.button("Home", use_container_width=True): st.session_state.page = 'Home'; st.rerun()
        if c3.button("About", use_container_width=True): st.session_state.page = 'About'; st.rerun()
        if c4.button("Explorer", use_container_width=True): st.session_state.page = 'Explorer'; st.rerun()
        if c5.button("FAQ", use_container_width=True): st.session_state.page = 'FAQ'; st.rerun()
        if c6.button("Partners", use_container_width=True): st.session_state.page = 'Institutions'; st.rerun()
        if c7.button("Take Assessment", type="primary", use_container_width=True): st.session_state.page = 'Assessment'; st.rerun()

# --- 7. EDUVEER SIDEBAR CHAT ---
def render_eduveer_sidebar():
    with st.sidebar:
        st.markdown("### 🤖 Eduveer AI Assistant")
        st.markdown("Got questions? Chat with our AI guide live!")
        
        # Container for chat history
        chat_container = st.container(height=400)
        with chat_container:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        # Chat Input
        if prompt := st.chat_input("Ask Eduveer..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_container:
                with st.chat_message("user"):
                    st.markdown(prompt)
            
            # Simulate AI Response (Mock Logic)
            with chat_container:
                with st.chat_message("assistant"):
                    response_text = ""
                    if "fees" in prompt.lower():
                        response_text = "Most online MBA programs range from ₹1.5L to ₹4L. Jain Online is around ₹2.1L, while NMIMS is ₹4L. Which one fits your budget?"
                    elif "placement" in prompt.lower():
                        response_text = "Our partner universities like Jain and Amity have placement support with 85%+ placement rates. Top packages go up to 32 LPA."
                    elif "creator" in prompt.lower() or "profile" in prompt.lower():
                        response_text = "If you're a Creator, look for programs that allow project work, like BCA or Digital Marketing. Avoid rigid, purely theoretical courses."
                    else:
                        response_text = "That's a great question! Based on your profile, I'd recommend booking a free counseling call to discuss this in detail."
                    
                    # Typing effect
                    message_placeholder = st.empty()
                    full_response = ""
                    for chunk in response_text.split():
                        full_response += chunk + " "
                        time.sleep(0.05)
                        message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- 8. PAGES ---

def render_home():
    st.markdown("""
    <div class="hero-section">
        <div class="hero-badge" style="background:rgba(0,119,182,0.1); color:#0077B6; padding:8px 20px; border-radius:30px; display:inline-block; font-weight:700; font-size:0.9rem; margin-bottom:20px;">CAREER ARCHITECTURE FOR PROFESSIONALS</div>
        <h1 style="margin-bottom:20px; font-size:4.5rem; background:-webkit-linear-gradient(45deg, #0077B6, #00B4D8); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Don't Just Upgrade Your Degree.<br>Upgrade Your Identity.</h1>
        <p style="max-width:800px; margin:0 auto 40px auto; font-size:1.3rem; color:#475569;">
            Whether you are a student or a working professional, alignment is everything.<br>
            We match your <b>Core Professional Identity</b> to India's Top Online Universities.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🚀 Discover Your Spark (Free)", key="home_cta", use_container_width=True):
            st.session_state.page = 'Assessment'
            st.rerun()

    st.markdown("<br><p style='text-align:center; font-weight:700; color:#94A3B8; letter-spacing:1px;'>TRUSTED BY STUDENTS OF TOP UNIVERSITIES</p>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, p in enumerate(["AMITY ONLINE", "MANIPAL", "JAIN ONLINE", "NMIMS CDOL", "LPU ONLINE"]):
        cols[i].markdown(f"<h3 style='text-align:center; color:#0F172A; opacity:0.8; font-size:1.1rem;'>{p}</h3>", unsafe_allow_html=True)

    # Features
    st.markdown("<br><br><h2 style='text-align:center;'>Why Professionals Choose Us</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="d-card"><div class="icon-circle">🧠</div><h3 style="text-align:center; font-size:1.5rem;">Identity Analysis</h3><p style="text-align:center; color:#64748B;">Stop forcing yourself into roles you hate. Find your natural flow.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="d-card"><div class="icon-circle">🏫</div><h3 style="text-align:center; font-size:1.5rem;">Online Degrees</h3><p style="text-align:center; color:#64748B;">Valid degrees from UGC-approved universities like Amity & Manipal.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="d-card"><div class="icon-circle">🚀</div><h3 style="text-align:center; font-size:1.5rem;">Career Roadmap</h3><p style="text-align:center; color:#64748B;">Integrate your degree with <b>ALISON</b> certifications for maximum impact.</p></div>""", unsafe_allow_html=True)

def render_explorer():
    st.markdown("## 🏫 University Power Explorer")
    st.markdown("Use our advanced data engine to compare top online universities. **All listed are UGC/AICTE Approved.**")
    
    # 1. COMPARISON WIDGET
    st.markdown("### ⚖️ Compare Universities")
    compare_list = st.multiselect("Select up to 3 universities to compare side-by-side:", df['name'].tolist(), max_selections=3)
    
    if compare_list:
        st.markdown("<br>", unsafe_allow_html=True)
        comp_df = df[df['name'].isin(compare_list)].set_index('name')
        display_cols = ['fees', 'placement', 'avg_pkg', 'highest_pkg', 'naac', 'approvals', 'highlights']
        st.dataframe(comp_df[display_cols].style.format(thousands=","), use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # 2. ADVANCED FILTERS
    st.markdown("### 🔍 Find Your Match")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        max_fee = st.slider("Max Budget (₹)", 50000, 500000, 350000, 50000)
    with c2:
        energy_filter = st.multiselect("Energy Fit", ["Distoversity Creator", "Distoversity Influencer", "Distoversity Catalyst", "Distoversity Analyst"], default=["Distoversity Creator", "Distoversity Analyst", "Distoversity Influencer", "Distoversity Catalyst"])
    with c3:
        sort_by = st.selectbox("Sort By", ["Lowest Fees", "Highest Placement %", "Highest Avg Package"])
    with c4:
        min_placement = st.slider("Min Placement %", 50, 100, 80)

    # 3. FILTERING LOGIC
    filtered_df = df[
        (df['fees'] <= max_fee) & 
        (df['energy'].isin(energy_filter)) &
        (df['placement'].str.replace('%','').astype(int) >= min_placement)
    ]
    
    if sort_by == "Lowest Fees":
        filtered_df = filtered_df.sort_values(by='fees')
    elif sort_by == "Highest Placement %":
        filtered_df = filtered_df.sort_values(by='placement', ascending=False)
    
    st.write(f"Showing **{len(filtered_df)}** universities based on your filters:")
    
    # 4. DISPLAY CARDS
    for idx, row in filtered_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="d-card" style="margin-bottom:20px; border-left: 5px solid #0077B6; padding: 1.5rem;">
                <div style="display:flex; justify-content:space-between; align-items:start; flex-wrap: wrap; gap: 15px;">
                    <div style="display:flex; align-items:center; gap:20px; flex: 2;">
                        <img src="{row['img']}" height="70" style="object-fit:contain; max-width:100px;">
                        <div>
                            <h3 style="margin:0; font-size:1.4rem; color:#023E8A;">{row['name']}</h3>
                            <div style="margin-top:5px;">
                                <span class="feature-tag">📍 {row['location']}</span>
                                <span class="feature-tag">🏆 NAAC {row['naac']}</span>
                                <span class="feature-tag">📜 {row['approvals']}</span>
                            </div>
                            <p style="margin-top:8px; font-size:0.9rem; color:#64748B;"><b>Highlights:</b> {row['highlights']}</p>
                        </div>
                    </div>
                    <div style="text-align:right; flex: 1; border-left:1px solid #E2E8F0; padding-left:20px;">
                        <div style="font-weight:800; color:#0077B6; font-size:1.5rem;">₹{row['fees']:,}</div>
                        <p style="margin:0; font-size:0.9rem; color:#475569;">Total Fees</p>
                        <div style="margin-top:10px;">
                            <span style="color:#16A34A; font-weight:700;">{row['placement']} Placement</span><br>
                            <span style="font-size:0.85rem; color:#64748B;">Avg Pkg: {row['avg_pkg']}</span>
                        </div>
                        <div style="margin-top:10px;">
                            <span class="match-tag">⚡ {row['energy']}</span>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            c_btn1, c_btn2, c_space = st.columns([1, 1, 4])
            with c_btn1:
                 st.button(f"View Brochure", key=f"broch_{idx}")
            with c_btn2:
                 st.button(f"Apply Now", key=f"apply_{idx}", type="primary")

def render_assessment():
    st.markdown("""
    <div style="text-align:center; margin-bottom:40px;">
        <h2 style="font-size:2.5rem; color:#0077B6; margin-bottom:10px;">Discover Your Spark</h2>
        <p style="color:#64748B; font-size:1.1rem;">Answer these 5 questions to find your core energy type.</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        with st.form("assessment_form"):
            # Q1
            st.markdown('<p class="question-text">1. When solving a problem, you naturally:</p>', unsafe_allow_html=True)
            q1 = st.radio("q1_select", [
                "Generate multiple creative solutions (Creator)",
                "Discuss with others to find consensus (Influencer)",
                "Follow proven step-by-step methods (Catalyst)",
                "Analyze data and metrics first (Analyst)"
            ], label_visibility="collapsed")
            
            # Q2
            st.markdown('<p class="question-text">2. Your ideal work environment involves:</p>', unsafe_allow_html=True)
            q2 = st.radio("q2_select", [
                "Freedom to experiment and innovate",
                "Collaborative team settings",
                "Structured processes and clear timelines",
                "Quiet space for deep analytical work"
            ], label_visibility="collapsed")
            
            # Q3
            st.markdown('<p class="question-text">3. You feel most energized when:</p>',
