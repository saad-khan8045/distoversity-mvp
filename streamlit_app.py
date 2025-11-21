import streamlit as st
import pandas as pd
import time

# --- 1. PAGE CONFIGURATION & SEO ---
st.set_page_config(
    page_title="Distoversity | Empowering India - AI Career Counseling & University Match",
    page_icon="🇮🇳",
    layout="wide"
)
st.markdown("""
    <meta name="description" content="Distoversity — Discover your real career path with AI-powered assessment, honest university comparison, upskilling, and science-based guidance. Trusted by Indian students and professionals. Empowering India.">
""", unsafe_allow_html=True)

# --- 2. MODERN DESIGN SYSTEM, COLOR/FONT FIX ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;700;900&display=swap');
html,body,[class*='css']{
    font-family:'Inter',sans-serif!important;
    background:#f8fbff!important;
    color:#19202c;
}
h1,h2,h3{
    font-family:'Inter',sans-serif!important;
    color:#003366!important;
    font-weight:900!important;
}
.nav-logo{
    font-family:'Inter',sans-serif!important;
    font-size:2.25rem;font-weight:900!important;letter-spacing:-2px;
    color:#003366!important;display:inline;margin-left:5px;margin-right:10px;}
.nav-flag{font-size:2.1rem;display:inline;margin-left:6px;vertical-align:middle;}
.stButton>button{
    background:#1376d4!important;color:#fff!important;font-weight:700;
    border:none;border-radius:30px;padding:0.6rem 1.65rem;font-size:1.14rem;
    box-shadow:0 1.5px 7px #1ab6ed18;}
.d-card{
    background:#fff;
    border:1.1px solid #dae7f9;
    border-radius:19px;
    padding:1.38rem 1.2rem 1.15rem;
    margin-bottom:2rem;
}
.hero-section,.about-box{
    background:linear-gradient(98deg,#f2f7fc 80%,#fff 100%);
    border-radius:24px;
    box-shadow:0 8px 27px -10px #0077b614;
    margin-bottom:36px;padding:2.2rem 2rem 1.65rem;
    border:1px solid #e6ecf4;
}
label,.question-text{color:#1a304b!important;font-weight:700!important;font-size:1.16rem;}
.badge{
    background:#e6f3fe;
    color:#1376d4;
    padding:7px 20px;font-weight:700;
    border-radius:15px;font-size:1.05rem;margin-right:5px;box-shadow:0 1px 3px #b1ceec22;
    display:inline-block;}
.cta-sticky{
    position:fixed;bottom:22px;right:22px;z-index:9166;
    background:#1376d4!important;color:white;font-weight:800;
    font-size:1.15rem;padding:15px 37px;border-radius:45px;box-shadow:0 2px 16px #1376d418;border:none;}
.footer-note{font-size:1.08rem;text-align:center;margin:2.4rem 0 0;color:#375657!important;}
hr{border:none;border-top:1.7px solid #e2eaf7;margin:20px 0;}
ul,ol{font-size:1.10rem;color:#345;}
</style>
""", unsafe_allow_html=True)

# --- 3. DATA ---
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

# --- 4. STATE ---
if "page" not in st.session_state: st.session_state.page = "Home"
if "profile" not in st.session_state: st.session_state.profile = None
if "scores" not in st.session_state: st.session_state.scores = None

# --- 5. NAVBAR ---
def navbar():
    cols = st.columns([2,1,1.25,1.23,1,1.48])
    with cols[0]:
        st.markdown("""<span class='nav-logo'>Distoversity | Empowering India <span class='nav-flag'>🇮🇳</span></span>""",unsafe_allow_html=True)
    if cols[1].button("Home"): st.session_state.page="Home";st.rerun()
    if cols[2].button("Assessment"): st.session_state.page="Assessment";st.rerun()
    if cols[3].button("Universities"): st.session_state.page="Universities";st.rerun()
    if cols[4].button("FAQ"): st.session_state.page="FAQ";st.rerun()
    if cols[5].button("About"): st.session_state.page="About";st.rerun()
    st.markdown("---")

# --- 6. PAGE ROUTES ---
def home_page():
    st.markdown("""
    <div class="hero-section">
        <h1>Engineer Your Career Destiny <span class='nav-flag'>🇮🇳</span></h1>
        <p style="font-size:1.22rem;">India's smart students and professionals trust Distoversity for AI-powered, ethical career guidance and honest university comparison.<br>
        <span class="badge">No Sales | Pure Science | 100% Confidential</span></p>
        <ul>
        <li>Take our genius assessment (Creator, Influencer, Catalyst, Analyst profiles)</li>
        <li>Compare top NAAC/UGC-approved universities—real data, no hidden ads</li>
        <li>Get free upskilling (Alison) matched to your strengths</li>
        <li>Book a real, ethical career call—with TFI/Distoversity</li>
        </ul>
    </div>
    """,unsafe_allow_html=True)
    st.button("🚀 Start My Assessment",type="primary",on_click=lambda: nav("Assessment"))
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/India_Flag_300.png/150px-India_Flag_300.png",width=120)

def assessment_page():
    st.markdown("<h2 style='text-align:center;'>Start Your Genius Assessment</h2>",unsafe_allow_html=True)
    st.info("Answer 5 questions—get your best fit, upskilling pathway & top Indian university match!")
    with st.form("dist_assess"):
        q1 = st.radio("Q1. Work makes you happiest when?",["Inventing new things","Inspiring/leading people","Finishing/executing big projects","Solving complex puzzles"],index=None)
        q2 = st.radio("Q2. Friends see you as…",["The innovator","The motivator","The finisher","The analyst"],index=None)
        q3 = st.radio("Q3. You get bored by…",["Repeating/routine work","Isolation/lack of people","Waiting/unclear targets","Hype, not facts"],index=None)
        q4 = st.radio("Q4. If given a whole free day, you would…",["Draw 3 startup ideas","Host an event","Clear all pending tasks","Decode new trends in stocks/news"],index=None)
        q5 = st.radio("Q5. Life goal?",["Invent something world-class","Inspire lakhs","Become Operations CEO","Crack million-dollar data puzzle"],index=None)
        if st.form_submit_button("Reveal Genius →"):
            tally = {"Creator":0,"Influencer":0,"Catalyst":0,"Analyst":0}
            for a in [q1,q2,q3,q4,q5]:
                if "idea" in a or "Invent" in a or "innovator" in a or "draw" in a: tally["Creator"]+=1
                elif "Inspire" in a or "people" in a or "event" in a or "motivator" in a or "lakhs" in a: tally["Influencer"]+=1
                elif "Finish" in a or "Operations" in a or "clear" in a or "tasks" in a or "finisher" in a: tally["Catalyst"]+=1
                else: tally["Analyst"]+=1
            winner = max(tally, key=tally.get)
            st.session_state.profile = winner
            st.session_state.scores = tally
            nav("Result")

def result_page():
    prof = st.session_state.get("profile")
    scores = st.session_state.get("scores")
    if not prof:
        st.warning("Please complete the assessment first!"); return
    st.markdown(f"<h2 style='color:#1376d4;text-align:center;'>Congratulations! You're a <span style='text-transform:uppercase;'>{prof}</span> Genius.</h2>",unsafe_allow_html=True)
    st.markdown(f"""<div class="badge" style="margin-bottom:10px;">AI-Verified Profile</div>""",unsafe_allow_html=True)
    st.markdown("""
    <div class='d-card' style='margin-bottom:1.6rem;'>
        <b>Key Strengths & Pitfalls:</b>
        <ul>
        <li>Creator: Visionary, original, high-impact—but must finish what you start.</li>
        <li>Influencer: Leader, motivator, connector—avoid the 'all talk, no results' trap.</li>
        <li>Catalyst: Results-getter, executor, ops expert—watch for burnout, stay strategic!</li>
        <li>Analyst: Detail hawk, data solver, reliable—don't let perfection freeze your action.</li>
        </ul>
    </div>
    """,unsafe_allow_html=True)
    st.markdown(f"<h4>Skill Launchpad: Alison Upskilling Free Courses</h4>",unsafe_allow_html=True)
    for course in alison_courses[prof]:
        st.write(f"• {course} ([See Alison](https://alison.com/courses))")
    st.markdown("<hr>",unsafe_allow_html=True)
    st.markdown("<b>Top University Matches:</b>",unsafe_allow_html=True)
    matches = [u for u in UNIS if u['profile'] == prof]
    for u in matches:
        st.markdown(f"""
        <div class="d-card"><h3>{u['name']}</h3>
        <span class="badge">{u['city']}</span> | <span class="badge">NAAC: {u['naac']}</span> | <b>Fee:</b> ₹{u['fee']:,}<br>
        <b>Alison:</b> {u['alison']} | <b>Placement:</b> {u['pkg']}
        </div>
        """,unsafe_allow_html=True)
    st.button("Compare All Universities",on_click=lambda: nav("Universities"))

def universities_page():
    st.markdown("<h2>Compare India's Top Online Universities</h2>",unsafe_allow_html=True)
    st.caption("Sort/filter by fee, NAAC, placement, profile fit, and city—all data transparent.")
    df = pd.DataFrame(UNIS)
    cols = st.columns(4)
    sel_prof = cols[0].selectbox("Profile Filter",["All"]+list(alison_courses.keys()))
    sel_sort = cols[1].selectbox("Sort by",["Fee (Lowest)","Fee (Highest)","Placement (Highest)"])
    budget = cols[2].slider("Max Fee (Lakh ₹)",1,6,3)
    naac_plus = cols[3].checkbox("NAAC A++ only",False)
    temp = df[df['fee']<=budget*100000]
    if naac_plus: temp=temp[temp.naac=="A++"]
    if sel_prof!="All": temp=temp[temp.profile==sel_prof]
    temp = temp.sort_values("fee" if "Fee" in sel_sort else "pkg", ascending="Lowest" in sel_sort)
    st.dataframe(temp[["name","profile","fee","naac","city","pkg"]].reset_index(drop=True),use_container_width=True)
    st.markdown("Click any university row for personalized advice—or go back to [Assessment](#) for your unique fit!")

def faq_page():
    st.title("Distoversity FAQ")
    faq = [
        ("What makes Distoversity different?",
         "Science, empathy, and AI. We never sell your data, push spam, or show only top-paying partners. We care for every aspirant, not 'leads'."),
        ("Who can use Distoversity?",
         "Anyone—from 12th graders to working professionals to re-starters. We believe in true second chances!"),
        ("How do you select universities?",
         "UGC/AICTE/NAAC only. No fake sponsors. Only transparent info and honest statistics."),
        ("What's Alison upskilling?",
         "'Alison' is the world's best free upskilling site. Every profile here gets a custom skill launchpad—free, always."),
        ("How can I book a call?",
         "Sticky blue button (right bottom), Email: distoversity@gmail.com, or WhatsApp: +91-9111111111. Rapid response!")
    ]
    for q,a in faq:
        with st.expander(q):
            st.write(a)

def about_page():
    st.markdown("""
    <div class='about-box'>
    <h1>Distoversity: Story & Vision <span class='nav-flag'>🇮🇳</span></h1>
    <p>
    <b>💡 Founder’s Mission:</b> From assembly lines to founder—my journey is about replacing 'sales' with science. I saw how talent is wasted because schools matched marks—not minds.<br>
    <b>How we work:</b> We use AI, psychometrics, and live data to match everyone to their unique career flow zone. We only work with the most honest institutions. Distoversity is 100% commission-free.<br>
    <b>TFI fit:</b> Our platform empowers TFI’s alumni, students, staff to take better decisions, upskill for free, and spread the word. For every career changed, a family is transformed.<br>
    Email: <b>distoversity@gmail.com</b> &nbsp; | &nbsp; <a href="https://linkedin.com">LinkedIn</a>
    </p>
    </div>
    """,unsafe_allow_html=True)

# --- 7. NAV HELPER ---
def nav(p): st.session_state.page=p; st.rerun()

# --- 8. MAIN ROUTER ---
navbar()
page_map={"Home":home_page,"Assessment":assessment_page,"Result":result_page,
          "Universities":universities_page,"FAQ":faq_page,"About":about_page}
if st.session_state.page=="Result":
    result_page()
else:
    page_map[st.session_state.page]()

# --- 9. STICKY CTA + FOOTER ---
st.markdown("""
<a href="mailto:distoversity@gmail.com?subject=Book%20Distoversity%20Counseling"
class="cta-sticky" target="_blank" style="text-decoration:none;">
<span class='nav-flag'>🇮🇳</span> Book 1:1 Counseling 🚀
</a>
<div class="footer-note">
<b>EMPOWERING INDIA 🇮🇳</b> | Privacy: Data never shared. Alison Certified | Copyright &copy; 2025 Distoversity.
</div>
""",unsafe_allow_html=True)
