import streamlit as st
import pandas as pd
import time

# --- SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Discover Your Spark",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ULTRA-PREMIUM DESIGN/CSS + VISIBILITY FIX ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;800&family=Plus+Jakarta+Sans:wght@400;800&display=swap');
    :root {
        --primary: #0077B6;
        --primary-dark: #023E8A;
        --accent: #00B4D8;
        --text-main: #0F172A; --white:#fff;
    }
    html,body,[class*="css"]{font-family:'Plus Jakarta Sans',sans-serif;color:var(--text-main);
        background:#fff;scroll-behavior:smooth;}
    h1,h2,h3{font-family:'Outfit',sans-serif;color:var(--primary-dark);font-weight:800;}
    h1{font-size:3.2rem!important;}
    .d-card{background:#fff;border:1px solid #E2E8F0;border-radius:18px;padding:2rem;
        box-shadow:0 6px 24px -10px rgba(0,0,0,0.09);}
    .nav-logo{font-family:'Outfit';font-weight:800;font-size:2rem;color:var(--primary-dark);}
    .stButton>button{background:linear-gradient(90deg,#0077B6 0%,#00B4D8 100%);
        color:#fff;border-radius:30px;font-weight:700;border:none;}
    input,textarea,select,div[data-baseweb="select"]{
        background:#fff!important;color:#000!important;-webkit-text-fill-color:#000!important;
        border:1px solid #CBD5E1!important;}
    .feature-tag{background:#F1F5F9;color:#475569;padding:4px 12px;border-radius:20px;
        font-size:0.8rem;font-weight:600;display:inline-block;margin-right:5px;margin-bottom:5px;}
    .match-tag{background:#DCFCE7;color:#166534;padding:4px 12px;border-radius:20px;
        font-size:0.8rem;font-weight:700;}
    .footer-note {font-size:0.92rem;color:#64748B !important;text-align:center;margin-top:2rem;}
    #MainMenu,footer,header{visibility:hidden;}
    </style>
""", unsafe_allow_html=True)

# --- DATA: Universities & Assessment Logic ---
UNIVERSITY_DATA = [
    {"name":"Jain Online","energy":"Distoversity Influencer","fees":210000,"location":"Bangalore","program":"MBA Marketing","placement":"98%"},
    {"name":"Manipal University Online","energy":"Distoversity Analyst","fees":175000,"location":"Jaipur","program":"MCA Data Science","placement":"94%"},
    {"name":"Amity University Online","energy":"Distoversity Creator","fees":345000,"location":"Global","program":"BCA Cloud Security","placement":"92%"},
    {"name":"LPU Online","energy":"Distoversity Catalyst","fees":160000,"location":"Global","program":"MBA Operations","placement":"91%"},
    {"name":"Chandigarh University","energy":"Distoversity Influencer","fees":180000,"location":"Online","program":"MBA General","placement":"89%"},
    {"name":"NMIMS CDOL","energy":"Distoversity Analyst","fees":400000,"location":"Online","program":"MBA Finance","placement":"93%"},
    {"name":"DY Patil Online","energy":"Distoversity Catalyst","fees":120000,"location":"Pune","program":"BBA General","placement":"90%"}
]
df = pd.DataFrame(UNIVERSITY_DATA)
PROFILES = ["Distoversity Creator","Distoversity Influencer","Distoversity Catalyst","Distoversity Analyst"]

# --- STATE ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'user_scores' not in st.session_state: st.session_state.user_scores = {}

# --- NAVBAR ---
def navbar():
    cols = st.columns([2,1,1,1,1,1])
    with cols[0]: st.markdown("<div class='nav-logo'>Distoversity <span style='color:#00B4D8'>Empowering INDIA</span></div>",unsafe_allow_html=True)
    if cols[1].button("Home"): st.session_state.page='Home'; st.rerun()
    if cols[2].button("Assessment"): st.session_state.page='Assessment'; st.rerun()
    if cols[3].button("Universities"): st.session_state.page='Explorer'; st.rerun()
    if cols[4].button("FAQ"): st.session_state.page='FAQ'; st.rerun()
    if cols[5].button("About"): st.session_state.page='About'; st.rerun()
    st.markdown("---")

# --- PAGES ---
def render_home():
    st.markdown("""
    <div class="hero-section" style="padding:3rem 1rem;background:linear-gradient(60deg,#e0f7fa,#fff);border-radius:24px;">
        <div style="color:#0077B6;font-weight:700;">EMPOWERING INDIA 🇮🇳</div>
        <h1>Stop Guessing. <span style="color:#00B4D8;">Engineer</span> Your Career.</h1>
        <p style="font-size:1.2rem;max-width: 650px;margin:0 auto 20px;">We match your <b>natural genius</b> to leading online universities. One assessment. Lifelong clarity.</p>
        <a href="#" style="color: #0077B6;">UGC-AICTE-NAAC Recognized | Confidential | No Spam</a>
    </div>
    """,unsafe_allow_html=True)
    if st.button("✨ Take My Genius Assessment", type="primary"):
        st.session_state.page='Assessment'; st.rerun()
    st.markdown("<br>",unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/India_Flag_300.png/150px-India_Flag_300.png","Empowering India")

def render_assessment():
    st.markdown("<h2 style='text-align:center;'>Distoversity Genius Assessment</h2>",unsafe_allow_html=True)
    st.write("Answer honestly. Your results are private & personalized.")
    with st.form("form_quiz"):
        q1 = st.radio("Your favourite work style?",["Create new things","Inspire/lead people","Organize & execute plans","Research/analyze data"])
        q2 = st.radio("People trust you for...",["Ideas/Innovation","Motivation/Networking","Execution/Getting results","Data Logic/Clarity"])
        q3 = st.radio("You avoid...",["Routine","Being unheard","Chaos","Unproven hype"])
        q4 = st.radio("Energy comes from...",["Fresh Projects","Meeting People","Fixing Problems","Solving Puzzles"])
        q5 = st.radio("You'd rather...",["Invent","Convince","Finish","Evaluate"])
        if st.form_submit_button("Finish ➔",type="primary"):
            counts = {"Distoversity Creator":0,"Distoversity Influencer":0,"Distoversity Catalyst":0,"Distoversity Analyst":0}
            mapping = {0:"Creator",1:"Influencer",2:"Catalyst",3:"Analyst"}
            for i,ans in enumerate([q1,q2,q3,q4,q5]):
                if "Create" in ans or "Ideas" in ans or "Invent" in ans: counts["Distoversity Creator"] += 1
                elif "Inspire" in ans or "lead" in ans or "Motivation" in ans or "Networking" in ans or "People" in ans or "Convince" in ans: counts["Distoversity Influencer"] += 1
                elif "Organize" in ans or "Execution" in ans or "Finish" in ans or "results" in ans or "Fix" in ans: counts["Distoversity Catalyst"] += 1
                else: counts["Distoversity Analyst"] += 1
            winner = max(counts,key=counts.get)
            st.session_state.user_profile=winner
            st.session_state.user_scores=counts
            st.session_state.page='Result'; st.rerun()

def render_result():
    profile = st.session_state.user_profile
    scores = st.session_state.user_scores
    if not profile: st.warning("Assessment complete karein."); return
    st.balloons()
    st.markdown(f"<h2 style='color:#0077B6;text-align:center;'>Congratulations!<br>Your Genius: {profile.replace('Distoversity ','')}</h2>",unsafe_allow_html=True)
    st.write(f"Score breakdown: {scores}")
    st.markdown("<h4>Best Matching Universities:</h4>",unsafe_allow_html=True)
    matches = df[df.energy==profile]
    for _,row in matches.iterrows():
        st.markdown(f"""
        <div class="d-card">
        <h3>{row['name']}</h3>
        <p>{row['program']} | {row['location']} | {row['placement']} Placement</p>
        <b>Fees:</b> ₹{row['fees']:,}
        </div>
        """,unsafe_allow_html=True)
    st.success("Want a personalized PDF report or roadmap? Contact [distoversity@gmail.com](mailto:distoversity@gmail.com)")

def render_explorer():
    st.title("University Explorer")
    energy = st.selectbox("Choose your energy:", PROFILES)
    st.write(f"Showing all universities best for {energy}:")
    info = df[df.energy==energy]
    st.dataframe(info.reset_index(drop=True))

def render_faq():
    st.title("Frequently Asked Questions")
    st.markdown("""
- **How is my result calculated?**  
  Algorithm checks your 5 answers for energy alignment—it's not random!
- **Data security?**  
  Results are **private**; we neither share nor sell data.
- **Is it for working professionals too?**  
  Yes—our quiz & roadmap both for students and working pros!
    """)

def render_about():
    st.title("Distoversity Story")
    st.info("From factory floor to career architect. Our mission: Empowering India with logic + empathy. No sales, just science. No bias—just career clarity.")

navbar()

if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'Result': render_result()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'FAQ': render_faq()
elif st.session_state.page == 'About': render_about()

# --- FOOTER ---
st.markdown("""
<div class="footer-note">
<b>EMPOWERING INDIA 🇮🇳 | Privacy Policy: 100% secure. We never share your data.<br>
Copyright © 2025 Distoversity.</b>
</div>
""",unsafe_allow_html=True)
