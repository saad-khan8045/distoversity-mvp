import streamlit as st
import pandas as pd
import time

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Distoversity | Scientific Career Guidance",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS & THEMING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&family=Plus+Jakarta+Sans:wght@400;700&display=swap');
    :root { --primary: #0077B6; --primary-dark: #023E8A; --bg-light: #F4F9FD; }
    html, body, [class*="css"] { font-family:'Plus Jakarta Sans',sans-serif; background:var(--bg-light);}
    h1,h2,h3 {font-family:'Outfit',sans-serif;color:#003366 !important;}
    .stButton>button {background:linear-gradient(90deg,#0077B6 0%,#00B4D8 100%);color:#fff;border-radius:30px;font-weight:600;border:none;}
    .d-card {background:#fff;border:1px solid #E2E8F0;border-radius:16px;padding:1.2rem;box-shadow:0 4px 12px rgba(0,0,0,0.04);}
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATA ---
@st.cache_data
def load_data():
    return pd.DataFrame([
        {"name": "Amity Online", "fees": 350000, "type": "Distoversity Analyst", "badge": "Top Ranked"},
        {"name": "Manipal Jaipur", "fees": 175000, "type": "Distoversity Creator", "badge": "NAAC A+"},
        {"name": "LPU Online", "fees": 160000, "type": "Distoversity Catalyst", "badge": "Affordable"},
        {"name": "NMIMS", "fees": 400000, "type": "Distoversity Influencer", "badge": "Premium"},
        {"name": "Jain University", "fees": 210000, "type": "Distoversity Influencer", "badge": "Placement Focus"}
    ])
df = load_data()

# --- 4. APP STATE ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'lead_captured' not in st.session_state: st.session_state.lead_captured = False
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'messages' not in st.session_state: st.session_state.messages = [{"role":"assistant","content":"Hi! I am Eduveer. I can guide your career path."}]

# --- 5. UTILITIES ---
def get_superpower(prof):
    if "Creator" in prof: return "Innovation & Starting New Things"
    if "Influencer" in prof: return "People & Communication"
    if "Catalyst" in prof: return "Execution & Timing"
    return "Data & Systems"

def get_bot_response(user_query):
    q = user_query.lower()
    if "fee" in q or "cost" in q: return "Our listed universities have fees ranging ₹98,000–₹400,000. Check Explorer for budget fit."
    if "placement" in q or "job" in q: return "NMIMS recorded a highest package of ₹24 LPA. Placement stats are in Explorer!"
    if "valid" in q or "ugc" in q: return "100% valid: All universities listed are UGC-DEB/NAAC accredited."
    return "Great question! Use Explorer for a quick comparison or book a Premium Session for deep advice."

# --- 6. NAVIGATION ---
def navbar():
    cols = st.columns([2,1,1,1,1,1,1])
    with cols[0]: st.markdown("<h3>Distoversity<span style='color:#00B4D8'>.</span></h3>", unsafe_allow_html=True)
    if cols[1].button("Home"): st.session_state.page="Home";st.rerun()
    if cols[2].button("About"): st.session_state.page="About";st.rerun()
    if cols[3].button("4D Quiz"): st.session_state.page="Assessment";st.rerun()
    if cols[4].button("Courses"): st.session_state.page="Explorer";st.rerun()
    if cols[5].button("Bot"): st.session_state.page="Eduveer";st.rerun()
    if cols[6].button("FAQ"): st.session_state.page="FAQ";st.rerun()
    st.markdown("---")

# --- 7. PAGE LOGIC ---
def render_home():
    st.markdown("""
    <div style="text-align:center;padding:2rem 0;">
        <span style="background:#E0F2FE;color:#0077B6;padding:6px 16px;border-radius:20px;font-size:0.85rem;font-weight:700;">🚫 DON'T BE SOLD. BE GUIDED.</span>
        <h1 style="margin:20px 0;font-weight:800;">Is Your Career Designed by <span style="color:#0077B6">Science</span> or a <span style="color:#F97316">Sales Agent?</span></h1>
        <p style="color:#475569;font-size:1.2rem;">93% choose wrong courses by trusting 'Free Counselors.' We use the <b>4-Genius Framework</b> to match your DNA to the degree.</p>
    </div>""", unsafe_allow_html=True)
    if st.button("🧬 Decode My Career DNA (Free)",type="primary"): st.session_state.page='Assessment';st.rerun()
    if st.button("Meet the Founder ➔"): st.session_state.page='About';st.rerun()

def render_about():
    st.markdown("<h2 style='text-align:center;'>The Man Who Rejected the 'System'</h2>",unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#64748B;'>From factory floor to fixing education.</p>",unsafe_allow_html=True)
    for headline, desc, color in [
        ("🏭 2019: The Factory Floor","Career began at Oppo & Yazaki, 12-hour shifts, saw thousands lacking guidance.","#F97316"),
        ("📞 2021: The Sales Trap & Integrity","2,000+ students helped at Amity, realized 'Education is being sold, not served.' Chose integrity, built a better system.", "#0077B6"),
        ("🧬 2024: Birth of Distoversity","Built platform using Data & Psychology, not sales. Mission: 1,000K students grow together.","#10B981")]:
        st.markdown(f"""
        <div class="d-card" style="border-left:5px solid {color} !important;">
            <h3>{headline}</h3><p>{desc}</p>
        </div>""",unsafe_allow_html=True)
    if st.button("See My Logic ➔",type="primary"): st.session_state.page='Assessment';st.rerun()

def render_assessment():
    st.markdown("<h2 style='text-align:center;'>🧠 The 4-Genius Energy Analysis</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#64748B;'>Stop forcing yourself into careers that don't fit.</p>", unsafe_allow_html=True)
    with st.form("quiz"):
        q1=st.radio("1. Problem arises, FIRST instinct?",["💡 Create Ideas","🗣️ Talk to People","⚡ Start Acting","📊 Analyze Data"],label_visibility="collapsed")
        q2=st.radio("2. What drains your energy?",["Routine Tasks","Working Alone","Vague Plans","Sales Pressure"],label_visibility="collapsed")
        if st.form_submit_button("Analyze My Energy ➤",type="primary"):
            if "Create" in q1: st.session_state.user_profile="Distoversity Creator"
            elif "Talk" in q1: st.session_state.user_profile="Distoversity Influencer"
            elif "Act" in q1: st.session_state.user_profile="Distoversity Catalyst"
            else: st.session_state.user_profile="Distoversity Analyst"
            st.session_state.page='Result';st.rerun()

def render_result():
    profile=st.session_state.user_profile
    if not profile: st.warning("Complete assessment first.");return
    if not st.session_state.lead_captured:
        st.markdown(f"""
        <div class="d-card" style="text-align:center;padding:2rem;">
            <h2 style="color:#0077B6;">🎉 Profile Identified!</h2>
            <p style="font-size:1.2rem;">Your Core Energy Type is: <b>{profile.split()[1]}</b></p>
            <hr>
            <p>To unlock your <b>Career Roadmap</b>, <b>University Matches</b> & <b>Salary Prediction</b>, enter details:</p>
        </div>""",unsafe_allow_html=True)
        with st.form("lead_gen"):
            name=st.text_input("Name")
            phone=st.text_input("WhatsApp Number")
            if st.form_submit_button("🔓 Unlock My Full Report"):
                if name and len(phone)>9:
                    st.session_state.lead_captured=True;st.rerun()
                else: st.error("Enter valid details.");return
        return
    st.balloons()
    st.markdown(f"""
    <div class="d-card" style="background:#F0F9FF !important;text-align:center;">
        <span style="font-size:1rem;color:#0077B6;font-weight:700;">OFFICIAL DISTOVERSITY PROFILE</span>
        <h1 style="color:#0077B6 !important;">{profile.replace('Distoversity ','')}</h1>
        <p><b>Superpower:</b> {get_superpower(profile)}</p>
    </div>""",unsafe_allow_html=True)
    st.markdown("""
    <div class="gold-card">
        <h3 style="color:#D97706 !important;">👑 Premium Guidance</h3>
        <p>Don't risk your career—get a <b>1:1 Session</b> with Career Architect.</p>
        <h2 style="color:#D97706 !important;">₹999 <span style="font-size:1rem; text-decoration:line-through; color:gray;">₹2,499</span></h2>
        <a href="https://wa.me/919118231052?text=I want to book Premium Career Session." target="_blank" style="text-decoration:none;">
        <button style="background:#D97706;color:white;border:none;padding:10px 20px;border-radius:5px;font-weight:bold;cursor:pointer;">Book Now ➤</button></a>
    </div>
    """, unsafe_allow_html=True)
    if st.button("View Matched Universities ➔"):
        st.session_state.page="Explorer";st.rerun()

def render_explorer():
    st.title("University Explorer")
    budget=st.slider("Max Budget",50000,500000,200000)
    filtered=df[df.fees<=budget]
    for _,row in filtered.iterrows():
        wa_link=f"https://wa.me/919118231052?text=I am interested in {row['name']}."
        st.markdown(f"""
        <div class="d-card">
            <h4>{row['name']}</h4>
            <p>🏅 {row['badge']} | 💰 ₹{row['fees']:,}</p>
            <a href="{wa_link}" style="text-decoration:none;">
            <button style="background:#0077B6;color:white;width:100%;padding:10px;border:none;border-radius:5px;">👉 Apply on WhatsApp</button></a>
        </div>
        """,unsafe_allow_html=True)
    if st.button("Ask Eduveer Bot ➔"): st.session_state.page="Eduveer";st.rerun()

def render_eduveer():
    st.title("Chat with Eduveer 🤖")
    with st.container(height=400):
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        if prompt:=st.chat_input("Ask about fees, placements..."):
            st.session_state.messages.append({"role":"user","content":prompt})
            st.chat_message("user").write(prompt)
            resp=get_bot_response(prompt)
            st.session_state.messages.append({"role":"assistant","content":resp});st.rerun()

def render_faq():
    st.title("❓ Frequently Asked Questions")
    tab1, tab2 = st.tabs(["Career Guidance","Universities"])
    with tab1:
        st.header("General FAQs")
        st.write("Discover your 'Genius Profile' and get matched to fitting careers and degrees.")
        st.write("We use Wealth Dynamics for strengths mapping.")
    with tab2:
        st.header("Universities & Admissions")
        st.write("All partners NAAC A+/A++, UGC/DEB accredited.")
        st.write("Apply via WhatsApp or form, guided by our counselors.")

# --- 8. MAIN ROUTER ---
navbar()
if st.session_state.page=="Home": render_home()
elif st.session_state.page=="About": render_about()
elif st.session_state.page=="Assessment": render_assessment()
elif st.session_state.page=="Result": render_result()
elif st.session_state.page=="Explorer": render_explorer()
elif st.session_state.page=="Eduveer": render_eduveer()
elif st.session_state.page=="FAQ": render_faq()
