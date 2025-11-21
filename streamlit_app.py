import streamlit as st
import pandas as pd

# --- PAGE CONFIG & SEO ---
st.set_page_config(
    page_title="Distoversity | Empowering India – 4D Assessment, Ethical Career & University Guidance",
    page_icon="🇮🇳",
    layout="wide"
)
st.markdown("""
    <meta name="description" content="Distoversity – Take the 4D Assessment to discover your four career energies, compare top Indian universities, join Alison's global community, and get ethical, mentor-led career advice.">
""", unsafe_allow_html=True)

# --- MODERN DESIGN / COLOR / FONT ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Inter:wght@400;700&display=swap');
html,body,[class*="css"]{
    font-family:'Inter',sans-serif!important;
    background:#f4f9fd!important;
    color:#19315B;
}
h1,h2,h3{
    font-family:'Montserrat',sans-serif!important;
    font-weight:900!important;letter-spacing:-1.1px;
    color:#003366!important;
}
.nav-logo{
    font-family:'Montserrat',sans-serif;font-size:2.18rem;font-weight:900!important;
    color:#003366!important;display:inline;margin-right:7px;letter-spacing:-2px;
}
.empower-small{
    font-family:'Montserrat',sans-serif!important;
    font-size:1rem;
    color:#1376d4!important;
    font-weight:700!important;display:inline-block;margin-top:2px;margin-left:2px;
}
.nav-flag{
    font-size:1.3rem;display:inline;vertical-align:middle;margin-left:3px;
}
.stButton>button{
    background:#1376d4!important;
    color:#fff!important;
    font-family:'Montserrat',sans-serif!important;
    font-weight:800;
    font-size:1.09rem;
    border:none;
    border-radius:32px;
    padding:0.60rem 1.6rem;
    box-shadow:0 2px 14px #1ab6ed21;
}
.d-card{
    background:linear-gradient(95deg,#fff 88%,#e6f3fe 100%);
    border:1.3px solid #daecfa;
    border-radius:18px;
    padding:1.25rem 1.3rem 1.1rem;
    margin:1.1rem 0;
    box-shadow:0 3px 11px #98d4fb22;
}
.hero-section,.about-box{
    background:linear-gradient(97deg,#e7f1fb 85%,#fff 100%);
    border-radius:24px;
    margin-bottom:33px;
    padding:2.15rem 2.0rem 1.35rem;
    border:1px solid #dbe5ee;}
label,.question-text{
    color:#0d2e42!important;font-weight:700!important;
    font-family:'Montserrat',sans-serif!important;
    font-size:1.13rem;}
.badge{
    background:#e6f3fe;
    color:#0077B6;
    font-family:'Montserrat',sans-serif!important;
    padding:7px 17px;
    font-weight:700;border-radius:15px;
    font-size:0.96rem;margin-right:6px;margin-bottom:4px;}
.cta-sticky{
    position:fixed;bottom:17px;right:17px;z-index:9188;
    background:#0077B6!important;
    color:white;font-family:'Montserrat',sans-serif;
    font-weight:900;font-size:1.09rem;
    padding:0.92rem 2.09rem;
    border-radius:39px;
    box-shadow:0 3px 18px #1376d41a;
    border:none;}
.footer-note{
    font-size:1.01rem;text-align:center;margin:1.9rem 0 0;color:#476;}
hr {border:none;border-top:1.6px solid #e2eaf7;margin:21px 0;}
ul,ol{font-size:1.07rem;color:#26334c;}
.alison-tag{
    background:#e7f7e7;color:#38953b;
    border-radius:9px;
    font-size:0.94rem;
    font-weight:700;
    display:inline-block;
    padding:3px 9px;
    margin-bottom:7px;
    margin-left:2px;
}
</style>
""", unsafe_allow_html=True)

# --- DATA ---
UNIS = [
    {"name":"Jain (Online)","type":"Private","city":"Bengaluru","profile":"Creator","fee":210000,"naac":"A++","pkg":"32LPA","alison":"Innovation Management"},
    {"name":"Manipal Online","type":"Private","city":"Jaipur","profile":"Analyst","fee":175000,"naac":"A+","pkg":"18LPA","alison":"Data Science Fundamentals"},
    {"name":"Amity University Online","type":"Private","city":"Global","profile":"Creator","fee":345000,"naac":"A+","pkg":"15LPA","alison":"Design Thinking (Alison)"},
    {"name":"LPU Online","type":"Private","city":"Global","profile":"Catalyst","fee":160000,"naac":"A++","pkg":"21LPA","alison":"Agile Leadership (Alison)"},
    {"name":"Chandigarh University Online","type":"Private","city":"Online","profile":"Influencer","fee":180000,"naac":"A+","pkg":"28LPA","alison":"Social Media Marketing (Alison)"},
    {"name":"NMIMS Global","type":"Private","city":"Online","profile":"Influencer","fee":400000,"naac":"A+","pkg":"45LPA","alison":"Public Speaking"},
    {"name":"DY Patil Online","type":"Private","city":"Pune","profile":"Catalyst","fee":120000,"naac":"A++","pkg":"12LPA","alison":"Project Management"},
]
alison_courses = {
    "Creator":["Innovation Management", "Design Thinking (Alison)"],
    "Influencer":["Social Media Marketing (Alison)", "Public Speaking"],
    "Catalyst":["Agile Leadership (Alison)", "Project Management"],
    "Analyst":["Data Science Fundamentals (Alison)", "Excel Strategies"]
}

# --- SESSION STATE ---
if "page" not in st.session_state: st.session_state.page = "Home"
if "profile" not in st.session_state: st.session_state.profile = None
if "scores" not in st.session_state: st.session_state.scores = None

# --- FOUNDER MODAL ---
if "founder_modal" not in st.session_state:
    st.session_state.founder_modal = True

def founder_modal():
    import streamlit.components.v1 as components
    modal_code = """
    <div id="founder-modal" style="position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(30,77,136,0.10);z-index:99999;display:flex;align-items:center;justify-content:center;">
      <div style="background:white;max-width:330px;border-radius:15px;box-shadow:0 6px 24px #00336624;padding:19px 13px 10px;text-align:center;position:relative;font-family:Montserrat;">
        <button onclick="document.getElementById('founder-modal').style.display='none';document.body.style.overflow='';"
        style='position:absolute;top:7px;right:7px;background:#e6f3fe;font-size:1.3rem;color:#1376d4;border:none;border-radius:8px;font-weight:700;width:26px;height:26px;cursor:pointer;'>×</button>
        <img src='https://avatars.githubusercontent.com/u/7087942?s=400' width='52' style='border-radius:14px;box-shadow:0 2px 12px #00336626;'>
        <h4 style='margin:11px 0 6px 0;font-family:Montserrat;color:#003366;font-size:1.03rem;'>Mohd Saad</h4>
        <div style="font-size:0.97rem;color:#1376d4;font-weight:700;">Senior Career Advisor & Founder</div>
        <div style="font-size:0.91rem;color:#124;background:#e6f3fe;border-radius:6px;padding:5px 3px;margin:8px 0 5px;">
            <b>Guiding you with ethics, not sales.</b><br>
            Every student is seen, heard, and supported.<br>
        </div>
        <a href="https://linkedin.com/" target="_blank" style="text-decoration:none;">
            <button style="background:#1376d4;color:#fff;font-family:Montserrat;font-weight:700;font-size:0.97rem;padding:6px 14px;border:none;border-radius:10px;margin-bottom:5px;cursor:pointer;">LinkedIn</button>
        </a>
        <br>
        <button onclick="document.getElementById('founder-modal').style.display='none';document.body.style.overflow='';"
         style="margin-top:7px;background:#ececec;color:#003366;font-family:Inter;font-weight:700;border:none;border-radius:10px;padding:6px 13px;">OK, Explore</button>
      </div>
    </div>
    <script>
    document.body.style.overflow = 'hidden';
    document.getElementById('founder-modal').addEventListener('click', function(e) {
      if(e.target === this) { this.style.display='none';document.body.style.overflow = ''; }
    });
    </script>
    """
    components.html(modal_code, height=310)

# --- NAVBAR ---
def navbar():
    cols = st.columns([2.4,1,1.25,1.23,1,1.46])
    with cols[0]:
        st.markdown("<span class='nav-logo'>Distoversity</span>",unsafe_allow_html=True)
        st.markdown("<span class='empower-small'>Empowering India <span class='nav-flag'>🇮🇳</span></span>",unsafe_allow_html=True)
    if cols[1].button("Home"): st.session_state.page="Home";st.rerun()
    if cols[2].button("4D Assessment"): st.session_state.page="Assessment";st.rerun()
    if cols[3].button("Universities"): st.session_state.page="Universities";st.rerun()
    if cols[4].button("FAQ"): st.session_state.page="FAQ";st.rerun()
    if cols[5].button("About"): st.session_state.page="About";st.rerun()
    st.markdown("---")

def home_page():
    if st.session_state.page == "Home" and st.session_state.founder_modal:
        founder_modal()
        st.session_state.founder_modal = False
    st.markdown("""
    <div class="hero-section">
        <h1>Engineer Your Career Destiny <span class='nav-flag'>🇮🇳</span></h1>
        <p style="font-size:1.17rem;">Experience India's most ethical consultative career science.<br>
        <span class="badge">4D Assessment | Mentor + AI Guidance | Trusted University Match</span></p>
        <ul>
        <li>Take the <b>Distoversity 4D Assessment</b> (Discover your Creator, Influencer, Catalyst, Analyst energies!)</li>
        <li>Compare NAAC/UGC universities—transparent, unbiased data only</li>
        <li>Join <span class="alison-tag">Alison Community</span> upskilling courses matched for every energy profile</li>
        <li>All counseling and advice are consultative, not transactional—mentor + AI, never pushy selling</li>
        </ul>
    </div>
    """,unsafe_allow_html=True)
    st.button("✨ Start Your 4D Assessment",type="primary",on_click=lambda: nav("Assessment"))
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/India_Flag_300.png/80px-India_Flag_300.png",width=64)

def assessment_page():
    st.markdown("<h2 style='text-align:center;'>4D Assessment – Discover Your 4 Energies</h2>",unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;'>
      <span class='badge'>AI Supported | Mentor Validated | Career Science for India</span>
      <br>
      <span style="font-size:1.07rem; color:#1376d4;"><b>Our original test reveals your 4 energies: Creator, Influencer, Catalyst, Analyst.<br>This is your unique blueprint for success—no random results, only clarity.</b></span>
    </div>
    """,unsafe_allow_html=True)
    st.info("Answer 5 short questions. No right/wrong answers—just your energy flow.")
    with st.form("dist_assess"):
        q1 = st.radio("Q1. Work makes you happiest when?",["Inventing new things","Inspiring/leading people","Finishing/executing big projects","Solving complex puzzles"],index=None)
        q2 = st.radio("Q2. Friends see you as…",["The innovator","The motivator","The finisher","The analyst"],index=None)
        q3 = st.radio("Q3. You get bored by…",["Repeating/routine work","Isolation/lack of people","Waiting/unclear targets","Hype, not facts"],index=None)
        q4 = st.radio("Q4. If given a whole free day, you would…",["Draw 3 startup ideas","Host an event","Clear all pending tasks","Decode new trends in stocks/news"],index=None)
        q5 = st.radio("Q5. Life goal?",["Invent something world-class","Inspire lakhs","Become Operations CEO","Crack million-dollar data puzzle"],index=None)
        if st.form_submit_button("See My 4D Profile →"):
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
        st.warning("Complete your 4D Assessment first!"); return
    st.markdown(f"<h2 style='color:#1376d4;text-align:center;'>You're a <span style='text-transform:uppercase;'>{prof}</span> Genius.</h2>",unsafe_allow_html=True)
    st.markdown(f"""<div class="badge" style="margin-bottom:10px;">AI + Mentor Verified | 4D Career DNA</div>""",unsafe_allow_html=True)
    st.markdown("""
    <div class='d-card' style='margin-bottom:1.2rem;'>
        <b>Your Growth Story (per Energy):</b>
        <ul>
        <li>Creator: Visionary, original, high-impact—but finish what you start.</li>
        <li>Influencer: Leader, motivator, connector—avoid the all-talk trap.</li>
        <li>Catalyst: Results-getter, ops expert—keep upskilling, avoid burnout!</li>
        <li>Analyst: Data solver, reliable—don’t let perfection block action.</li>
        </ul>
    </div>
    """,unsafe_allow_html=True)
    st.markdown(f"<h4>Recommended Alison Upskilling</h4>",unsafe_allow_html=True)
    st.markdown("<span class='alison-tag'>Alison Community Member | Free Skill Courses</span>",unsafe_allow_html=True)
    for course in alison_courses[prof]:
        st.write(f"• {course} ([See on Alison](https://alison.com/courses))")
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
    st.markdown("<h2>Compare India's Top Universities</h2>",unsafe_allow_html=True)
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
    st.markdown("Click any university row for advice—or return to [4D Assessment](#) for your unique fit.")

def faq_page():
    st.title("Distoversity FAQ")
    faq = [
        ("What is the 4D Assessment?",
         "Distoversity's 4D Assessment is India's original test for discovering your four career energies (Creator, Influencer, Catalyst, Analyst). Each energy leads to unique careers, skills, and university matches."),
        ("How is advice given?",
         "Every match is AI supported, reviewed by real career mentors. We guide, never push sales or random leads."),
        ("How does Alison help?",
         "Founder is an Alison global community member. All learners get free, profile-based upskilling links."),
        ("How is selling consultative?",
         "We never rush decisions. Our counselors serve as architects, not 'closers'. Every step is science + empathy."),
        ("How do you select universities?",
         "UGC/NAAC/AICTE verified only. Stats and fit are shown with transparent filters."),
        ("How can I contact you?",
         "Sticky bottom button, email: distoversity@gmail.com, WhatsApp: +91-9111111111.")
    ]
    for q,a in faq:
        with st.expander(q):
            st.write(a)

def about_page():
    st.markdown("""
    <div class='about-box'>
    <h1 style="margin-bottom:6px;">Distoversity – Ethical Career Science <span class='nav-flag'>🇮🇳</span></h1>
    <span class='empower-small'>Empowering India</span>
    <hr>
    <p>
    <b>Consultative selling—not closing leads.</b> Distoversity is India's impact-driven career company. We are counselors + AI, never just bots; we advise, not advertise.<br>
    <br>
    <b>Founder:</b> <br>
    <img src='https://avatars.githubusercontent.com/u/7087942?s=400' width='42' style='border-radius:8px;vertical-align:middle;margin-right:6px;'><b>Mohd Saad, Senior Career Advisor & Founder</b> <br>
    Guiding you with ethics, not sales. Every student is seen, heard, and supported. <br>
    <a href="https://linkedin.com/" target="_blank"><button style='background:#1376d4;color:#fff;font-family:Montserrat;font-weight:700;font-size:0.89rem;padding:4px 10px;border:none;border-radius:8px;margin-top:5px;'>LinkedIn</button></a>
    <br>
    <span class='alison-tag'>Alison Community Member</span>: Bringing global skill learning free for Indians.<br>
    <br>
    <b>For partners & TFI:</b> We aspire to work with every impact-focused educator, fellow, and org. Careers change lives—let's architect India's future, together.<br>
    <b>Contact:</b> distoversity@gmail.com | <a href="https://linkedin.com/">LinkedIn</a>
    </p>
    </div>
    """,unsafe_allow_html=True)

def nav(p): st.session_state.page=p; st.rerun()

navbar()
page_map = {
    "Home": home_page,
    "Assessment": assessment_page,
    "Result": result_page,
    "Universities": universities_page,
    "FAQ": faq_page,
    "About": about_page,
}
if st.session_state.page == "Result":
    result_page()
else:
    page_map[st.session_state.page]()

st.markdown("""
<a href="mailto:distoversity@gmail.com?subject=Book%20Distoversity%20Counseling"
class="cta-sticky" target="_blank" style="text-decoration:none;">
<span class='nav-flag'>🇮🇳</span> Book Consultative Career Call 🚀
</a>
<div class="footer-note">
Distoversity <span class='empower-small'>Empowering India <span class='nav-flag'>🇮🇳</span></span>
<br>
Privacy: Data always private. Alison Community | Copyright © 2025 Distoversity.
</div>
""", unsafe_allow_html=True)
