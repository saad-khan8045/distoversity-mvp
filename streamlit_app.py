import streamlit as st
import pandas as pd
import time

# --- 1. PAGE SEO & CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity: Empowering India’s Careers | AI Career Counseling, University Comparison, Alison Upskilling",
    page_icon="🇮🇳",
    layout="wide"
)

st.markdown("""
    <meta name="description" content="Distoversity: Discover your unique genius, compare top online universities with data, and get personalized AI career guidance. Upskill FREE with Alison. Ethical, science-based counseling. Empowering India.">
""", unsafe_allow_html=True)

# --- 2. UNIVERSAL CSS (VISIBILITY & GRAPHICS) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@800&family=Plus+Jakarta+Sans:wght@400;700&display=swap');
html,body,[class*='css']{
    font-family:'Plus Jakarta Sans',sans-serif!important;background-color:#f8fbff!important;color:#232d36;}
h1,h2,h3{font-family:'Outfit',sans-serif!important;color:#003366;font-weight:800;}
.nav-logo{font-family:'Outfit',sans-serif;font-size:2rem;font-weight:800;}
.stButton>button{
    background:linear-gradient(90deg,#0077B6,#00B4D8);color:#fff;font-weight:700;
    border:none;border-radius:30px;padding:0.6rem 1.6rem;}
.d-card{background:#fff;border:1px solid #E2E8F0;border-radius:24px;padding:1.4rem;box-shadow:0 4px 20px -6px #b7e1fa1a;}
.badge {border-radius:18px;padding:5px 16px;font-size:1rem;font-weight:600;display:inline-block;}
.feat{background:#d1fae580;color:#066c32;}
.seo{background:#ffeacf;color:#ae7600;}
.cta-sticky{
    position:fixed;bottom:13px;right:13px;z-index:9999;
    background:#0077B6;padding:12px 27px;border-radius:40px;
    color:white;font-weight:700;font-size:1.18rem;
    border:none;box-shadow:0 5px 16px #0077B633;
    display:flex;align-items:center;gap:12px;}
.flag {font-size:2.2rem;display:inline-block;vertical-align:middle;margin-left:2px;}
</style>
""", unsafe_allow_html=True)

# --- 3. DATA: UNIVERSITIES, ALISON ---
UNIS = [
    {"name":"Jain (Online)","type":"Private","city":"Bengaluru","profile":"Creator","fee":210000,"naac":"A++","pkg":"32LPA","alison":"Innovation Management"},
    {"name":"Manipal Online","type":"Private","city":"Jaipur","profile":"Analyst","fee":175000,"naac":"A+","pkg":"18LPA","alison":"Data Science Fundamentals"},
    {"name":"Amity University Online","type":"Private","city":"Global","profile":"Creator","fee":345000,"naac":"A+","pkg":"15LPA","alison":"Design Thinking: Primer"},
    {"name":"LPU Online","type":"Private","city":"Global","profile":"Catalyst","fee":160000,"naac":"A++","pkg":"21LPA","alison":"Agile Leadership"},
    {"name":"Chandigarh University Online","type":"Private","city":"Online","profile":"Influencer","fee":180000,"naac":"A+","pkg":"28LPA","alison":"Social Media Marketing"},
    {"name":"NMIMS Global","type":"Private","city":"Online","profile":"Influencer","fee":400000,"naac":"A+","pkg":"45LPA","alison":"Public Speaking"},
    {"name":"DY Patil Online","type":"Private","city":"Pune","profile":"Catalyst","fee":120000,"naac":"A++","pkg":"12LPA","alison":"Project Management"}
]
alison_courses = {
    "Creator":["Innovation Management","Design Thinking: A Primer"],
    "Influencer":["Social Media Marketing","Public Speaking & Communication"],
    "Catalyst":["Agile Leadership","Project Management Essentials"],
    "Analyst":["Data Science Fundamentals","Advanced Excel Strategies"]
}

# --- 4. SESSION STATE ---
if "page" not in st.session_state: st.session_state.page = "Home"
if "profile" not in st.session_state: st.session_state.profile = None
if "scores" not in st.session_state: st.session_state.scores = None

# --- 5. NAVBAR ---
def navbar():
    cols = st.columns([2,1,1.2,1.2,1,1.6])
    with cols[0]:
        st.markdown("""<span class='nav-logo'>Distoversity <span style="color:#00B4D8;">Empowering INDIA</span>
        <span class='flag'>🇮🇳</span></span>""",unsafe_allow_html=True)
    if cols[1].button("Home"): st.session_state.page="Home";st.rerun()
    if cols[2].button("Assessment"): st.session_state.page="Assessment";st.rerun()
    if cols[3].button("Universities"): st.session_state.page="Universities";st.rerun()
    if cols[4].button("FAQ"): st.session_state.page="FAQ";st.rerun()
    if cols[5].button("About"): st.session_state.page="About";st.rerun()
    st.markdown("---")

# --- 6. PAGES ---
def home_page():
    st.markdown("""
    <div style="background:linear-gradient(89deg,#e0f7fa, #fff 50%);border-radius:28px;padding:3.3rem 1.2rem 2rem;">
        <h1 style="margin-bottom:14px;">Redefine Your Career Destiny 
        <span class='flag'>🇮🇳</span></h1>
        <p style="font-size:1.26rem;">India's smart students and professionals trust Distoversity for AI-powered, ethical career guidance + university selection.<br>
        <span class="badge feat">No Sales | Pure Science | 100% Confidential</span></p>
        <ul>
            <li>Quiz for your unique <b>Creator, Influencer, Catalyst, Analyst</b> profile</li>
            <li>Side-by-side university comparison (fees, placement, NAAC, city, Alison courses)</li>
            <li>Instant upskilling—free Alison courses for your profile</li>
            <li>Clear call-to-action: Book a strategy or apply</li>
        </ul>
    </div>
    """,unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/India_Flag_300.png/150px-India_Flag_300.png",width=120)
    st.markdown("")
    st.button("🚀 Unlock My Career Genius (Assessment)",type="primary",on_click=lambda: nav("Assessment")) 

def assessment_page():
    st.markdown("<h2 style='text-align:center;'>Start Your Genius Assessment</h2>",unsafe_allow_html=True)
    st.info("Answer 5 questions to discover your core genius & best-matched universities.")
    with st.form("dist_assess"):
        q1 = st.radio("Q1. Work makes you happiest when?",["You're inventing new things","You're motivating or leading people","You're finishing & executing a big task","You're discovering patterns in data"],index=None)
        q2 = st.radio("Q2. Your friends see you as…",["The idea generator","The connector/leader","The action finisher","The deep thinker"],index=None)
        q3 = st.radio("Q3. You get bored by…",["Repetition & same-same","Isolation/no people","Waiting/no targets","Hype, not facts"],index=None)
        q4 = st.radio("Q4. If given one day, you would…",["Sketch 3 startup ideas","Organize an event/network","Complete a pending project","Analyze stocks & trends"],index=None)
        q5 = st.radio("Q5. Life goal?",["Invent world's best product","Inspire a million hearts","Become CEO of ops","Solve million-dollar data problem"],index=None)
        if st.form_submit_button("Submit My Profile"):
            map_prof = {"Creator":0,"Influencer":0,"Catalyst":0,"Analyst":0}
            answers = [q1,q2,q3,q4,q5]
            for a in answers:
                if "idea" in a or "invent" in a or "Sketch" in a or "product" in a: map_prof["Creator"]+=1
                elif "people" in a or "leading" in a or "Inspire" in a or "event" in a or "connector" in a or "hearts" in a: map_prof["Influencer"]+=1
                elif "finish" in a or "CEO" in a or "Complete" in a or "execute" in a or "pending" in a or "project" in a: map_prof["Catalyst"]+=1
                else: map_prof["Analyst"]+=1
            winner = max(map_prof, key=map_prof.get)
            st.session_state.profile = winner
            st.session_state.scores = map_prof
            nav("Result")

def result_page():
    profile = st.session_state.get("profile")
    scores = st.session_state.get("scores")
    if not profile:
        st.warning("Assessment complete karein!"); return
    st.success(f"Your Genius: {profile}")
    st.markdown(f"""<h3 style='color:#00B4D8;'>Congratulations! You are a <span style="text-transform:uppercase;">{profile}</span> type.</h3>""",unsafe_allow_html=True)
    st.markdown(f"""<div class="badge seo">Top Skills: {', '.join(alison_courses[profile])}</div>""",unsafe_allow_html=True)
    st.markdown("""
    <div class='d-card' style='margin:1rem 0 2rem 0;'>
        <b>Your Leadership Traits:</b>
        <ul>
            <li>Creator: Idea champion, visionary, builder</li>
            <li>Influencer: Connector, motivator, communicator</li>
            <li>Catalyst: Go-getter, action-driver, integrator</li>
            <li>Analyst: Proof expert, data Sherlock, detail master</li>
        </ul>
    </div>
    """,unsafe_allow_html=True)
    st.markdown(f"<h4>Recommended Alison Upskilling Courses:</h4>",unsafe_allow_html=True)
    for course in alison_courses[profile]:
        st.write(f"• {course} (Free | [See on Alison](https://alison.com/courses))")
    st.markdown("<hr>",unsafe_allow_html=True)
    st.markdown("<b>Top University Matches:</b>",unsafe_allow_html=True)
    matches = [u for u in UNIS if u['profile']==profile]
    for u in matches:
        st.markdown(f"""
        <div class="d-card"><h3>{u['name']}</h3>
        <span class="badge feat">{u['city']}</span> | <span class="badge seo">NAAC: {u['naac']}</span> | <b>Fee:</b> ₹{u['fee']:,}<br>
        <b>Alison Course:</b> {u['alison']} || <b>Placements:</b> {u['pkg']}
        </div>
        """,unsafe_allow_html=True)
    st.button("Compare All Universities",on_click=lambda: nav("Universities"))

def universities_page():
    st.markdown("<h2>Compare Top Indian Online Universities</h2>",unsafe_allow_html=True)
    st.caption("Sort, filter, and compare universities on fee, NAAC, placement, program & your best fit.")
    df = pd.DataFrame(UNIS)
    cols = st.columns(4)
    sel_profile = cols[0].selectbox("Your Profile",["All"]+list(alison_courses.keys()))
    sel_sort = cols[1].selectbox("Sort By",["Fee (Lowest)","Fee (Highest)","Placements (Highest)"])
    budget = cols[2].slider("Max Fee (Lakhs)",1,6,3)
    naac_only = cols[3].checkbox("Only NAAC A++",False)
    temp = df[df['fee']<=budget*100000]
    if naac_only: temp=temp[temp.naac=="A++"]
    if sel_profile!="All": temp = temp[temp.profile==sel_profile]
    if sel_sort=="Fee (Lowest)": temp=temp.sort_values("fee")
    elif sel_sort=="Fee (Highest)": temp=temp.sort_values("fee",ascending=False)
    else: temp=temp.sort_values("pkg",ascending=False)
    st.dataframe(temp[["name","profile","fee","naac","city","pkg"]].reset_index(drop=True),use_container_width=True)
    if st.button("Go to Assessment",type="primary"): nav("Assessment")

def faq_page():
    st.title("FAQ - Distoversity")
    faq = [
        ("What makes Distoversity different from others?",
         "Zero commission, zero fake leads. Our process is science+AI. Every result is private. No bias, no pressure. We NEVER sell your data."),
        ("I am a professional. Is this for me or just for students?",
         "Both! Our platform matches school grads, college-goers, and working pros to their best-fit university and skill track."),
        ("How do you select universities?",
         "UGC-AICTE-NAAC approvals ONLY. We show all data (fee/placement/NAAC) for honest comparison."),
        ("What is Alison?",
         "Alison is the world's biggest free upskilling platform. For every Distoversity profile, we give you matching Alison links for skill growth."),
        ("Is my data safe?",
         "Absolutely. Your data is **never sold or tracked**. We believe careers are sacred, not sales data."),
        ("How can I book a TFI/counselor call?",
         "Direct WhatsApp or Email from every result page, and use sticky CTA at bottom right. We respond in hours—not days!")
    ]
    for q,a in faq:
        with st.expander(q):
            st.write(a)

def about_page():
    st.markdown("""
    <h1>About Distoversity <span class='flag'>🇮🇳</span></h1>
    <p style="font-size:1.16rem;">
    <b>From the Founder:</b><br>
    My journey began not in a college—but on the assembly lines of India. I witnessed thousands chasing random degrees, ending frustrated, because nobody mapped their true genius to their education.<br>
    <br>
    <b>What We Do:</b><br>
    We are a mission-driven ed-tech platform that<br>
        • Puts student identity first—using AI, psychology, and real data.<br>
        • Gives honest, detailed, **side-by-side university comparison**: fee, placements, NAAC rank, city, upskilling, and fit.<br>
        • Partners ONLY with top, legitimate institutions.<br>
        • Guides you to free, world-class upskilling after your degree (with Alison references).<br>
        • Fights 'sales' in counseling—with only science and empathy.<br>
    <br>
    <b>Why TFI?</b><br>
    Because careers change families, and families change societies. We want Teach For India fellows, alumni & students to get the platform, tools, and mentorship they deserve—without sales, bias or hidden fee.<br>
    <br>
    <b>Contact or Collaborate:</b><br>
    distoversity@gmail.com | [LinkedIn](https://linkedin.com) | WhatsApp Request: +91-9111111111
    </p>
    """,unsafe_allow_html=True)

# --- 7. HELPER ---
def nav(p): st.session_state.page=p; st.rerun()


# --- 8. MAIN ROUTER ---
navbar()
page_map = {"Home":home_page,"Assessment":assessment_page,
            "Result":result_page,"Universities":universities_page,
            "FAQ":faq_page,"About":about_page}
if st.session_state.page=="Result":
    result_page()
else:
    page_map[st.session_state.page]()

# --- 9. STICKY CTA + FOOTER ---
st.markdown("""
<a href="mailto:distoversity@gmail.com?subject=Book Career Counseling (Distoversity)" target="_blank"
class="cta-sticky" style="text-decoration:none;">
<span class='flag'>🇮🇳</span> EMPOWERING INDIA — Book 1:1 Counseling 🚀
</a>
<div class="footer-note">
<b>EMPOWERING INDIA 🇮🇳</b> | Privacy: Data never shared. Alison Certified | Copyright &copy; 2025 Distoversity.
</div>
""",unsafe_allow_html=True)
