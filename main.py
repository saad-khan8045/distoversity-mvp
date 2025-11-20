import streamlit as st
import pandas as pd
import time
import random

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Empowering India",
    page_icon="🎓",
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

    /* COMPONENT: AI REPORT CARD (HTML VERSION) */
    .ai-report-box {
        background: #F8FAFC;
        border-left: 5px solid #0EA5E9;
        padding: 25px;
        margin-bottom: 20px;
        font-family: 'Plus Jakarta Sans', sans-serif;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .ai-title { color: #023E8A; font-weight: 800; font-size: 1.2rem; margin-bottom: 15px; display: flex; align-items: center; gap: 8px; }
    .ai-section { margin-bottom: 20px; background: white; padding: 15px; border-radius: 8px; border: 1px solid #E2E8F0; }
    .ai-label { font-size: 0.8rem; text-transform: uppercase; color: #64748B; font-weight: 700; letter-spacing: 0.05em; margin-bottom: 5px; display: block; }
    .ai-text { font-size: 1rem; color: #1E293B; line-height: 1.6; }
    .ai-highlight { color: #D97706; font-weight: 600; }
    
    /* COMPONENT: CTA BOX */
    .cta-box {
        background: linear-gradient(135deg, #0077B6 0%, #023E8A 100%);
        color: white;
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 20px 25px -5px rgba(0, 119, 182, 0.25);
    }
    .cta-box h3 { color: white !important; margin-bottom: 10px; font-size: 1.5rem; }

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
    
    /* EDUVEER CHAT STYLES */
    .stChatMessage { background: transparent; border: none; margin-bottom: 10px; }
    .stChatMessage.assistant .stMarkdown { background: #F0F9FF; border: 1px solid #BAE6FD; border-radius: 4px 16px 16px 16px; padding: 12px; font-size: 0.9rem; color: #0F172A; }
    .stChatMessage.user .stMarkdown { background: #F1F5F9; border: 1px solid #E2E8F0; color: #334155; border-radius: 16px 4px 16px 16px; padding: 12px; text-align: left; font-size: 0.9rem; }

    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. DATASETS ---

# A. SITE DATA (For Explorer Page - Visuals)
SITE_DATA = [
    {"name": "Jain Online", "location": "Bangalore", "naac": "A++", "fees": 210000, "energy": "Distoversity Influencer", "placement": "98%", "avg_pkg": "6.2 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Jain_University_logo.png", "approvals": "UGC-DEB", "highlights": "Strong Alumni"},
    {"name": "Manipal Online", "location": "Jaipur", "naac": "A+", "fees": 175000, "energy": "Distoversity Analyst", "placement": "94%", "avg_pkg": "5.5 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Manipal_University_logo.svg/1200px-Manipal_University_logo.svg.png", "approvals": "UGC, NAAC", "highlights": "Global Access"},
    {"name": "Amity Online", "location": "Global", "naac": "A+", "fees": 345000, "energy": "Distoversity Creator", "placement": "92%", "avg_pkg": "4.8 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Amity_University_logo.png/220px-Amity_University_logo.png", "approvals": "UGC-DEB", "highlights": "Job Fairs"},
    {"name": "LPU Online", "location": "Global", "naac": "A++", "fees": 160000, "energy": "Distoversity Catalyst", "placement": "91%", "avg_pkg": "5.0 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/d/d4/Lovely_Professional_University_logo.png", "approvals": "AICTE", "highlights": "Affordable"},
    {"name": "NMIMS CDOL", "location": "Online", "naac": "A+", "fees": 400000, "energy": "Distoversity Analyst", "placement": "93%", "avg_pkg": "7.0 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/NMIMS_University_logo.png/220px-NMIMS_University_logo.png", "approvals": "UGC-DEB", "highlights": "Premium Brand"},
    {"name": "Chandigarh Uni", "location": "Online", "naac": "A+", "fees": 180000, "energy": "Distoversity Influencer", "placement": "89%", "avg_pkg": "5.2 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Chandigarh_University_logo.png/220px-Chandigarh_University_logo.png", "approvals": "UGC-DEB", "highlights": "Flexible Exams"},
    {"name": "DY Patil", "location": "Pune", "naac": "A++", "fees": 120000, "energy": "Distoversity Catalyst", "placement": "90%", "avg_pkg": "4.2 LPA", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Dr._D._Y._Patil_Vidyapeeth_logo.png/220px-Dr._D._Y._Patil_Vidyapeeth_logo.png", "approvals": "UGC", "highlights": "Mentor Support"}
]
df = pd.DataFrame(SITE_DATA)

# B. EDUVEER BRAIN DATA (For Chat Recommendations)
EDUVEER_UNIVERSITIES = [
    {"name": "Amity Online", "programs": ["MBA", "MCA", "BBA"], "max_fee": 350000, "fee": "₹1.75L", "logo": "🅰️", "best_for": ["Analyst"], "avg_pkg": "₹6-8 LPA"},
    {"name": "Manipal Jaipur", "programs": ["MBA", "BCA"], "max_fee": 300000, "fee": "₹1.50L", "logo": "Ⓜ️", "best_for": ["Creator"], "avg_pkg": "₹5-7 LPA"},
    {"name": "LPU Online", "programs": ["M.Sc CS", "MBA"], "max_fee": 180000, "fee": "₹98k", "logo": "🏫", "best_for": ["Catalyst"], "avg_pkg": "₹4-6 LPA"},
    {"name": "NMIMS Global", "programs": ["MBA (Ex)"], "max_fee": 400000, "fee": "₹4.0L", "logo": "📈", "best_for": ["Influencer"], "avg_pkg": "₹10-12 LPA"},
    {"name": "Chandigarh Uni", "programs": ["MCA", "MBA"], "max_fee": 150000, "fee": "₹1.10L", "logo": "🏛️", "best_for": ["Creator"], "avg_pkg": "₹5-6 LPA"},
    {"name": "DY Patil", "programs": ["BBA", "MBA"], "max_fee": 220000, "fee": "₹1.30L", "logo": "🏥", "best_for": ["Catalyst"], "avg_pkg": "₹4.5-6.5 LPA"}
]

QUESTIONS = [
    {"q": "When solving problems, you prefer:", "options": [("💡 Innovation", "Creator"), ("🗣️ Discussion", "Influencer"), ("📊 Data", "Analyst"), ("⚡ Action", "Catalyst")]},
    {"q": "Your ideal workspace is:", "options": [("🎨 Studio", "Creator"), ("📢 Boardroom", "Influencer"), ("💻 Lab", "Analyst"), ("🏗️ Field", "Catalyst")]},
    {"q": "How do friends describe you?", "options": [("✨ Visionary", "Creator"), ("🎤 Leader", "Influencer"), ("🧠 Logical", "Analyst"), ("🛡️ Reliable", "Catalyst")]},
    {"q": "What motivates you?", "options": [("🚀 Creating", "Creator"), ("🤝 Connecting", "Influencer"), ("🔍 Analyzing", "Analyst"), ("✅ Doing", "Catalyst")]},
    {"q": "Role in a movie crew:", "options": [("🎬 Director", "Creator"), ("🌟 Actor", "Influencer"), ("🎞️ Editor", "Analyst"), ("📋 Producer", "Catalyst")]}
]

HOOK_CATEGORIES = {
    "Financial": ["💸 EMI Plans?", "💰 Hidden Costs?", "📉 ROI Analysis?"],
    "Academic": ["🏫 Faculty Quality?", "📚 Syllabus?", "📝 Exam Mode?"],
    "Outcome": ["💼 Placements?", "📈 Salary Hike?", "🌍 Global Valid?"]
}

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'user_scores' not in st.session_state: st.session_state.user_scores = {}

# EDUVEER STATE
if "ev_messages" not in st.session_state: st.session_state.ev_messages = []
if "ev_step" not in st.session_state: st.session_state.ev_step = 0
if "ev_q_index" not in st.session_state: st.session_state.ev_q_index = 0
if "ev_scores" not in st.session_state: st.session_state.ev_scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}
if "ev_user" not in st.session_state: st.session_state.ev_user = {}
if "ev_filter" not in st.session_state: st.session_state.ev_filter = {"budget": 1000000, "course": "All"}
if "ev_hooks" not in st.session_state: st.session_state.ev_hooks = ["💰 Check Fees", "💼 Placements"]

# --- 5. CORE FUNCTIONS ---

# 5a. SITE: AI REPORT POPUP (HTML Generation)
def get_report_content(profile, scores):
    """Returns structured data for the HTML report to avoid formatting errors."""
    core_type = profile.replace("Distoversity ", "")
    
    if core_type == "Creator":
        pain_point = "You despise routine. Ambiguity is your playground, but execution can feel like a prison."
        achilles_heel = "The 'Idea Junkie' Syndrome. You risk starting 50 projects and finishing zero."
        skills = ["Systems Thinking", "Project Management", "Strategic Leadership"]
    elif core_type == "Influencer":
        pain_point = "You hate isolation. You thrive on energy, but feel drained in silos."
        achilles_heel = "The 'Surface Level' Trap. Being seen as all talk, no action."
        skills = ["Data Analytics", "Financial Literacy", "Operational Execution"]
    elif core_type == "Catalyst":
        pain_point = "You hate chaos. You want clear targets, but feel undervalued."
        achilles_heel = "The 'Cog in the Wheel' Risk. Getting stuck in middle management."
        skills = ["Innovation Strategy", "Public Speaking", "Agile Leadership"]
    else: # Analyst
        pain_point = "You hate hype. You want data, but feel frustrated by emotional decisions."
        achilles_heel = "Analysis Paralysis. Waiting for 100% certainty before moving."
        skills = ["Persuasive Communication", "Team Management", "Creative Problem Solving"]
        
    return {
        "profile": profile,
        "match": int(scores.get(profile, 0)),
        "pain_point": pain_point,
        "achilles_heel": achilles_heel,
        "skills": skills
    }

@st.dialog("🤖 EDUVEER AI COUNSELLOR REPORT")
def show_popup_report(profile, scores):
    data = get_report_content(profile, scores)
    
    # Pure HTML Structure for Perfect Rendering
    html_structure = f"""
    <div class="ai-report-box">
        <div class="ai-title">⚡ YOUR EDUVEER ANALYSIS</div>
        <div class="ai-section" style="border-left: 4px solid #0EA5E9;">
            <span class="ai-label">Archetype</span>
            <div class="ai-text" style="font-size: 1.2rem; font-weight: 700; color: #023E8A;">
                {data['profile']} <span style="font-weight:400; font-size:0.9rem; color:#64748B;">({data['match']}% Match)</span>
            </div>
            <p style="margin-top:10px; font-style: italic;">"{data['pain_point']}"</p>
        </div>
        
        <div class="ai-section" style="border-left: 4px solid #F59E0B;">
            <span class="ai-label">⚠️ CRITICAL WEAK POINT</span>
            <div class="ai-text">
                <span class="ai-highlight">{data['achilles_heel']}</span><br>
                Talent without leverage is just a hobby. Don't let your greatest strength become your failure.
            </div>
        </div>
        
        <div class="ai-section" style="border-left: 4px solid #10B981;">
            <span class="ai-label">🚀 STRATEGIC ROADMAP</span>
            <div class="ai-text">
                Master these 3 high-impact skills immediately:
                <ul style="margin-top:5px; padding-left:20px;">
                    <li><b>{data['skills'][0]}</b></li>
                    <li><b>{data['skills'][1]}</b></li>
                    <li><b>{data['skills'][2]}</b></li>
                </ul>
            </div>
        </div>
    </div>
    """
    
    st.markdown(html_structure, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cta-box">
        <h3>🚀 The Final Decision</h3>
        <p style="opacity:0.9">Step into clarity. We have curated a roadmap specifically for you.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📞 Book My Career Advice Call Now", type="primary", use_container_width=True):
        st.success("Request Received! Eduveer will contact you within 2 hours.")
        time.sleep(2)
        st.rerun()

# 5b. EDUVEER LOGIC
def get_bot_response(query, budget):
    q = query.lower()
    if "fee" in q or "cost" in q:
        low = next((u for u in EDUVEER_UNIVERSITIES if u['max_fee'] < 200000), None)
        return f"Let's talk numbers 💰. **{low['name']}** is a budget-friendly option at {low['fee']}. What is your range?" if low else "Fees vary from 1L to 4L."
    if "place" in q or "job" in q:
        top = max(EDUVEER_UNIVERSITIES, key=lambda x: int(x['avg_pkg'].split('-')[0].replace('₹','').strip()))
        return f"ROI is key 📈. **{top['name']}** sees packages up to **{top['avg_pkg']}**. Placements depend on skills too."
    if "valid" in q or "ugc" in q:
        return "✅ **100% Valid.** All our partners are UGC-DEB approved. Safe for Govt jobs."
    return "That's a great question. I focus on **ROI, Validity, and Curriculum**. Want to compare fees?"

def update_hooks():
    cat1, cat2 = random.sample(list(HOOK_CATEGORIES.keys()), 2)
    st.session_state.ev_hooks = [random.choice(HOOK_CATEGORIES[cat1]), random.choice(HOOK_CATEGORIES[cat2])]

def ev_msg(role, text):
    st.session_state.ev_messages.append({"role": role, "content": text})

# --- 6. EDUVEER SIDEBAR COMPONENT ---
def render_eduveer():
    with st.sidebar:
        st.markdown("### 🤖 Eduveer AI Receptionist")
        
        # MINIMIZABLE WINDOW (EXPANDER)
        with st.expander("💬 Chat Window", expanded=True):
            
            # INIT CHAT
            if st.session_state.ev_step == 0 and not st.session_state.ev_messages:
                ev_msg("assistant", "Namaste! 🙏 I am **Eduveer**. I can help you find the perfect university. Shall we start with a quick check?")
                st.session_state.ev_step = 1
                st.rerun()

            # DISPLAY CHAT
            chat_box = st.container(height=350)
            with chat_box:
                for m in st.session_state.ev_messages:
                    with st.chat_message(m["role"]):
                        st.markdown(m["content"])
            
            # STEP 1: ASSESSMENT
            if st.session_state.ev_step == 1:
                curr = QUESTIONS[st.session_state.ev_q_index]
                cols = st.columns(2)
                for i, (txt, en) in enumerate(curr["options"]):
                    if cols[i%2].button(txt, key=f"ev_q_{st.session_state.ev_q_index}_{i}", use_container_width=True):
                        st.session_state.ev_scores[en] += 1
                        ev_msg("user", txt)
                        if st.session_state.ev_q_index < 4:
                            st.session_state.ev_q_index += 1
                        else:
                            st.session_state.ev_step = 2
                        st.rerun()

            # STEP 2: LEAD GEN
            elif st.session_state.ev_step == 2:
                if "ev_name_ask" not in [m.get("id","") for m in st.session_state.ev_messages]:
                    st.session_state.ev_messages.append({"role": "assistant", "content": "Great! I have a profile for you. What should I call you?", "id": "ev_name_ask"})
                    st.rerun()
                
                name = st.chat_input("Type your name...")
                if name:
                    st.session_state.ev_user["name"] = name
                    ev_msg("user", name)
                    st.session_state.ev_step = 3
                    st.rerun()

            # STEP 3: BUDGET
            elif st.session_state.ev_step == 3:
                if "ev_bud_ask" not in [m.get("id","") for m in st.session_state.ev_messages]:
                    st.session_state.ev_messages.append({"role": "assistant", "content": f"Hi **{st.session_state.ev_user['name']}**! What's your max budget?", "id": "ev_bud_ask"})
                    st.rerun()
                
                b_cols = st.columns(2)
                if b_cols[0].button("Under 2L", use_container_width=True):
                     st.session_state.ev_filter["budget"] = 200000
                     ev_msg("user", "Under 2L")
                     st.session_state.ev_step = 4
                     st.rerun()
                if b_cols[1].button("No Limit", use_container_width=True):
                     st.session_state.ev_filter["budget"] = 1000000
                     ev_msg("user", "No Limit")
                     st.session_state.ev_step = 4
                     st.rerun()

            # STEP 4: RESULTS & CHAT
            elif st.session_state.ev_step == 4:
                if "ev_res" not in [m.get("id","") for m in st.session_state.ev_messages]:
                    primary = max(st.session_state.ev_scores, key=st.session_state.ev_scores.get)
                    matches = [u for u in EDUVEER_UNIVERSITIES if u["max_fee"] <= st.session_state.ev_filter["budget"]]
                    if not matches: matches = EDUVEER_UNIVERSITIES[:2]
                    
                    res_msg = f"🎯 You are a **{primary}**. Based on your budget, I recommend **{matches[0]['name']}** ({matches[0]['fee']}) or **{matches[1]['name']}**."
                    st.session_state.ev_messages.append({"role": "assistant", "content": res_msg, "id": "ev_res"})
                    st.rerun()

                # Dynamic Hooks
                h_cols = st.columns(2)
                for i, h in enumerate(st.session_state.ev_hooks):
                    if h_cols[i].button(h, key=f"hook_{i}", use_container_width=True):
                        ev_msg("user", h)
                        resp = get_bot_response(h, st.session_state.ev_filter["budget"])
                        ev_msg("assistant", resp)
                        update_hooks()
                        st.rerun()

                # Free Chat
                if prompt := st.chat_input("Ask Eduveer..."):
                    ev_msg("user", prompt)
                    resp = get_bot_response(prompt, st.session_state.ev_filter["budget"])
                    ev_msg("assistant", resp)
                    update_hooks()
                    st.rerun()

# --- 7. NAVIGATION ---
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

# --- 8. PAGE FUNCTIONS (DEFINED BEFORE USE) ---

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

    st.markdown("<br><br><h2 style='text-align:center;'>Why Professionals Choose Us</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="d-card"><div class="icon-circle">🧠</div><h3 style="text-align:center; font-size:1.5rem;">Identity Analysis</h3><p style="text-align:center; color:#64748B;">Stop forcing yourself into roles you hate. Find your natural flow.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="d-card"><div class="icon-circle">🏫</div><h3 style="text-align:center; font-size:1.5rem;">Online Degrees</h3><p style="text-align:center; color:#64748B;">Valid degrees from UGC-approved universities.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="d-card"><div class="icon-circle">🚀</div><h3 style="text-align:center; font-size:1.5rem;">Career Roadmap</h3><p style="text-align:center; color:#64748B;">Integrate your degree with <b>ALISON</b> certifications.</p></div>""", unsafe_allow_html=True)

def render_explorer():
    st.markdown("## 🏫 University Power Explorer")
    st.markdown("Compare top online universities. **All listed are UGC/AICTE Approved.**")
    
    # 1. COMPARISON WIDGET
    st.markdown("### ⚖️ Compare Universities")
    compare_list = st.multiselect("Select up to 3 universities to compare:", df['name'].tolist(), max_selections=3)
    
    if compare_list:
        st.markdown("<br>", unsafe_allow_html=True)
        comp_df = df[df['name'].isin(compare_list)].set_index('name')
        display_cols = ['fees', 'placement', 'avg_pkg', 'naac', 'approvals', 'highlights']
        st.dataframe(comp_df[display_cols].style.format(thousands=","), use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # 2. ADVANCED FILTERS
    st.markdown("### 🔍 Find Your Match")
    c1, c2, c3, c4 = st.columns(4)
    with c1: max_fee = st.slider("Max Budget (₹)", 50000, 500000, 350000, 50000)
    with c2: energy_filter = st.multiselect("Energy Fit", ["Distoversity Creator", "Distoversity Influencer", "Distoversity Catalyst", "Distoversity Analyst"], default=["Distoversity Creator", "Distoversity Analyst", "Distoversity Influencer", "Distoversity Catalyst"])
    with c3: sort_by = st.selectbox("Sort By", ["Lowest Fees", "Highest Placement %"])
    with c4: min_placement = st.slider("Min Placement %", 50, 100, 80)

    # 3. FILTERING LOGIC
    filtered_df = df[
        (df['fees'] <= max_fee) & 
        (df['energy'].isin(energy_filter)) &
        (df['placement'].str.replace('%','').astype(int) >= min_placement)
    ]
    
    if sort_by == "Lowest Fees": filtered_df = filtered_df.sort_values(by='fees')
    else: filtered_df = filtered_df.sort_values(by='placement', ascending=False)
    
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
            with c_btn1: st.button(f"View Brochure", key=f"broch_{idx}")
            with c_btn2: st.button(f"Apply Now", key=f"apply_{idx}", type="primary")

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
            st.markdown('<p class="question-text">1. When solving a problem, you naturally:</p>', unsafe_allow_html=True)
            q1 = st.radio("q1_select", ["Generate multiple creative solutions (Creator)", "Discuss with others to find consensus (Influencer)", "Follow proven step-by-step methods (Catalyst)", "Analyze data and metrics first (Analyst)"], label_visibility="collapsed")
            
            st.markdown('<p class="question-text">2. Your ideal work environment involves:</p>', unsafe_allow_html=True)
            q2 = st.radio("q2_select", ["Freedom to experiment and innovate", "Collaborative team settings", "Structured processes and clear timelines", "Quiet space for deep analytical work"], label_visibility="collapsed")
            
            st.markdown('<p class="question-text">3. You feel most energized when:</p>', unsafe_allow_html=True)
            q3 = st.radio("q3_select", ["Creating something new from scratch", "Presenting ideas and influencing outcomes", "Completing tasks on schedule", "Perfecting systems and solving puzzles"], label_visibility="collapsed")

            st.markdown('<p class="question-text">4. Your decision-making style is:</p>', unsafe_allow_html=True)
            q4 = st.radio("q4_select", ["Intuitive and pattern-based", "People-focused and consensus-driven", "Experience-based and practical", "Data-driven and logical"], label_visibility="collapsed")

            st.markdown('<p class="question-text">5. In group settings, you naturally:</p>', unsafe_allow_html=True)
            q5 = st.radio("q5_select", ["Share innovative concepts and possibilities", "Build relationships and network actively", "Organize action items and ensure follow-through", "Provide data-backed insights and analysis"], label_visibility="collapsed")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.form_submit_button("Reveal My Spark ➤", type="primary", use_container_width=True):
                with st.spinner("Analyzing your Energy Profile..."):
                    time.sleep(1.5)
                
                answers = [q1, q2, q3, q4, q5]
                counts = {"Distoversity Creator": 0, "Distoversity Influencer": 0, "Distoversity Catalyst": 0, "Distoversity Analyst": 0}
                for a in answers:
                    if "Creator" in a or "innovate" in a or "scratch" in a or "Intuitive" in a or "concepts" in a: counts["Distoversity Creator"] += 1
                    elif "Influencer" in a or "Collaborative" in a or "Presenting" in a or "People" in a or "relationships" in a: counts["Distoversity Influencer"] += 1
                    elif "Catalyst" in a or "Structured" in a or "schedule" in a or "Experience" in a or "Organize" in a: counts["Distoversity Catalyst"] += 1
                    else: counts["Distoversity Analyst"] += 1
                
                total = 5
                scores = {k: (v/total)*100 for k,v in counts.items()}
                winner = max(counts, key=counts.get)
                st.session_state.user_profile = winner
                st.session_state.user_scores = scores
                st.session_state.page = 'Result'
                st.rerun()

def render_result():
    profile = st.session_state.user_profile
    scores = st.session_state.user_scores
    if not profile: st.warning("Take assessment first!"); st.stop()

    st.balloons()
    st.markdown(f"""
    <div style="text-align:center; padding:3rem; background:#F0F9FF; border-radius:20px; border:1px solid #BAE6FD; margin-bottom:3rem;">
        <div style="color:#0077B6; font-weight:700; letter-spacing:2px;">YOUR CORE ENERGY IS</div>
        <h1 style="font-size:5rem !important; color:#0077B6; margin:10px 0;">{profile}</h1>
        <p style="font-size:1.2rem;">Your Spark profile aligns with specific high-growth environments.</p>
        <div style="display:flex; justify-content:center; gap:20px; margin-top:20px; flex-wrap:wrap;">
            <span class="feature-tag">Creator: {int(scores['Distoversity Creator'])}%</span>
            <span class="feature-tag">Influencer: {int(scores['Distoversity Influencer'])}%</span>
            <span class="feature-tag">Catalyst: {int(scores['Distoversity Catalyst'])}%</span>
            <span class="feature-tag">Analyst: {int(scores['Distoversity Analyst'])}%</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🎯 Potential University Matches")
        matches = df[df['energy'] == profile]
        for idx, row in matches.iterrows():
             st.markdown(f"""
            <div class="d-card" style="margin-bottom:1rem; padding:1.5rem;">
                <div style="display:flex; justify-content:space-between;">
                    <h4 style="margin:0;">{row['name']}</h4>
                    <span class="match-tag">Potential Fit</span>
                </div>
                <p style="margin-top:10px;">✅ Aligns with {profile} learning style</p>
            </div>
            """, unsafe_allow_html=True)
            
    with c2:
        st.markdown("### 🗺️ Your Full Genius Profile")
        st.markdown("""
        <div class="d-card" style="margin-bottom:1rem;">
                <h4>Your Superpowers</h4>
                <p class="blur-content">Innovation, Big Picture Thinking...</p>
                <h4>Your Blind Spots</h4>
                <p class="blur-content">Routine tasks, detailed follow-through...</p>
        </div>
        <div style="position:relative;">
            <div class="d-card"><h4>4-Year Strategic Roadmap</h4><p class="blur-content">Year 1: Foundation...</p></div>
            <div class="lock-badge">
                <div style="font-size:3rem;">🔒</div>
                <h3>Unlock Full Genius Profile</h3>
                <p>Enter your email to generate your 15-Page Report via Llama AI</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        email = st.text_input("Enter Email to Unlock Full Results", key="email_input")
        if st.button("Generate My AI Report Now", use_container_width=True):
            if email:
                with st.spinner("Connecting to AI Neural Network... analyzing 5 data points..."):
                    time.sleep(2)
                    show_popup_report(profile, scores)
            else:
                st.error("Please enter a valid email.")

def render_about():
    c1, c2 = st.columns(2)
    with c1: st.markdown("## The Distoversity Story\nWe combine Wealth Dynamics + AI to fix Career Misalignment."); 
    with c2: st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")

def render_faq():
    st.title("❓ Frequently Asked Questions")
    st.markdown("Check the Eduveer chat for instant answers!");

def render_institutions():
    st.markdown("## Partner with Us"); st.button("Request Partnership Demo")

# --- 9. MAIN EXECUTION ROUTER (MUST BE LAST) ---

# 1. Render Eduveer Sidebar (Global)
render_eduveer()

# 2. Render Navbar (Global)
navbar()

# 3. Render Pages (Using the functions defined above)
if st.session_state.page == 'Home': 
    render_home()
elif st.session_state.page == 'Explorer': 
    render_explorer()
elif st.session_state.page == 'Assessment': 
    render_assessment()
elif st.session_state.page == 'Result': 
    render_result()
elif st.session_state.page == 'About': 
    render_about()
elif st.session_state.page == 'FAQ': 
    render_faq()
elif st.session_state.page == 'Institutions': 
    render_institutions()
