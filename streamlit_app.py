import streamlit as st
import pandas as pd

# --- PAGE CONFIG & SEO ---
st.set_page_config(
    page_title="Distoversity | Empowering India – 4D Assessment, Ethical Career & University Guidance",
    page_icon="🇮🇳",
    layout="wide"
)
st.markdown("""
<meta name="description" content="Distoversity – Know your counsellor, get ethical career advice and take the 4D Assessment. Senior advisor Mohd Saad gives students consultative onboarding and post-admission success. Join Distoversity's transparent community—every career, every student, impact-first.">
""", unsafe_allow_html=True)

# --- MODERN DESIGN / COLOR / FONT ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Inter:wght@400;700&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif!important;background:#f4f9fd!important;color:#19315B;}
h1,h2,h3{font-family:'Montserrat',sans-serif!important;font-weight:900!important;letter-spacing:-1.1px;color:#003366!important;}
.nav-logo{font-family:'Montserrat',sans-serif;font-size:2.18rem;font-weight:900!important;color:#003366!important;display:inline;margin-right:7px;letter-spacing:-2px;}
.empower-small{font-family:'Montserrat',sans-serif!important;font-size:1rem;color:#1376d4!important;font-weight:700!important;display:inline-block;margin-top:2px;margin-left:2px;}
.nav-flag{font-size:1.3rem;display:inline;vertical-align:middle;margin-left:3px;}
.stButton>button{background:#1376d4!important;color:#fff!important;font-family:'Montserrat',sans-serif!important;font-weight:800;font-size:1.09rem;border:none;border-radius:32px;padding:0.60rem 1.6rem;box-shadow:0 2px 14px #1ab6ed21;}
.d-card{background:linear-gradient(95deg,#fff 88%,#e6f3fe 100%);border:1.3px solid #daecfa;border-radius:18px;padding:1.25rem 1.3rem 1.1rem;margin:1.1rem 0;box-shadow:0 3px 11px #98d4fb22;}
.hero-section,.about-box{background:linear-gradient(97deg,#e7f1fb 85%,#fff 100%);border-radius:24px;margin-bottom:33px;padding:2.15rem 2.0rem 1.35rem;border:1px solid #dbe5ee;}
label,.question-text{color:#0d2e42!important;font-weight:700!important;font-family:'Montserrat',sans-serif!important;font-size:1.13rem;}
.badge{background:#e6f3fe;color:#0077B6;font-family:'Montserrat',sans-serif!important;padding:7px 17px;font-weight:700;border-radius:15px;font-size:0.96rem;margin-right:6px;margin-bottom:4px;}
.cta-sticky{position:fixed;bottom:17px;right:17px;z-index:9188;background:#0077B6!important;color:white;font-family:'Montserrat',sans-serif;font-weight:900;font-size:1.09rem;padding:0.92rem 2.09rem;border-radius:39px;box-shadow:0 3px 18px #1376d41a;border:none;}
.footer-note{font-size:1.01rem;text-align:center;margin:1.9rem 0 0;color:#476;}
hr {border:none;border-top:1.6px solid #e2eaf7;margin:21px 0;}
ul,ol{font-size:1.07rem;color:#26334c;}
.alison-tag{background:#e7f7e7;color:#38953b;border-radius:9px;font-size:0.94rem;font-weight:700;display:inline-block;padding:3px 9px;margin-bottom:7px;margin-left:2px;}
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
    {"name":"DY Patil Online","type":"Private","city":"Pune","profile":"Catalyst","fee":120000,"naac":"A++","pkg":"12LPA","alison":"Project Management"}
]
alison_courses = {
    "Creator":["Innovation Management", "Design Thinking (Alison)"],
    "Influencer":["Social Media Marketing (Alison)", "Public Speaking"],
    "Catalyst":["Agile Leadership (Alison)", "Project Management"],
    "Analyst":["Data Science Fundamentals (Alison)", "Excel Strategies"]
}

if "page" not in st.session_state: st.session_state.page = "Home"
if "profile" not in st.session_state: st.session_state.profile = None
if "scores" not in st.session_state: st.session_state.scores = None

# --- FOUNDER MODAL POPUP ("Know Your Counsellor") ---
if "founder_modal" not in st.session_state:
    st.session_state.founder_modal = True

def founder_modal():
    import streamlit.components.v1 as components
    modal_code = """
    <div id="founder-modal" style="position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(44,72,116,0.19);z-index:99999;display:flex;align-items:center;justify-content:center;">
      <div style="background:#fff;max-width:440px;border-radius:24px;box-shadow:0 14px 44px #1376d434;padding:32px 29px 17px;text-align:center;position:relative;">
        <img src='https://avatars.githubusercontent.com/u/7087942?s=400&u=860ba9126b6e8ce3fe01a8b337b836ca95a2d165&v=4' width='86' style='border-radius:22px;box-shadow:0 5px 15px #255;'>
        <h3 style='margin:18px 0 3px 0;font-family:Montserrat, Inter;color:#003366;'>Know Your Counsellor</h3>
        <div style='font-size:1.11rem;color:#1576d7;font-family:Montserrat;'><b>Mohd Saad, Senior Career Advisor & Founder – Distoversity 🇮🇳</b></div>
        <div style="font-size:1.078rem;color:#124;border-radius:10px;background:#e6f3fe;padding:12px 7px;margin:19px 0 11px 0;">
        <b>Why trust matters?</b><br>
        My journey began on India's factory floors.<br>
        I've advised thousands—with real answers, not sales.<br>
        <span style="color:#1376d4;">Education is a business—but only ethics make it impactful.<br>
        Distoversity was built so every student is truly seen, heard, and guided—even post-admission.<br>
        Your dreams are not leads—they are lives to be built.</span>
        </div>
        <div style='font-size:1.06rem;color:#003366;margin:10px 0 17px 0;'><b>
        I am not from any university—I work only for you, and with you.<br>
        My mission is to reshape career guidance: one student, one ethical decision at a time.</b></div>
        <div style="margin-bottom:8px;">
            <span style="font-size:1.07rem;color:#167;text-shadow:0 1px 0 #cae;">Distoversity counseling charge: <b>₹999</b> | All admissions welcome</span>
        </div>
        <a href="mailto:distoversity@gmail.com?subject=Join%20Community" style="text-decoration:none;">
          <button style="background:#1376d4;color:#fff;font-family:Montserrat;font-weight:700;font-size:1.09rem;padding:10px 27px;border:none;border-radius:23px;margin-bottom:7px;">Connect with Me Now</button>
        </a>
        <br>
        <button onclick="document.getElementById('founder-modal').style.display='none';" style="margin-top:10px;background:#ececec;color:#003366;font-family:Inter;font-weight:700;border:none;border-radius:16px;padding:8px 22px;box-shadow:0 2px 8px #1376d412;">OK, Explore Distoversity</button>
        <div style="font-size:0.98rem;margin-top:12px;color:#476;">You are safe here – privacy and empathy first, career ethics always.</div>
      </div>
    </div>
    <script>
    document.body.style.overflow = 'hidden';
    document.getElementById('founder-modal').addEventListener('click', function(e) {
      if(e.target === this) { this.style.display='none';document.body.style.overflow = ''; }
    });
    </script>
    """
    components.html(modal_code, height=490)

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

# --- PAGE ROUTES ---
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
    <div style='margin:20px 0 13px 0;font-size:1.12rem;color:#1376d4;background:#e6f3fe;padding:10px 15px;border-radius:13px;font-family:Montserrat'>
    Education is a business—but only ethical businesses truly succeed.<br>
    Distoversity puts honesty, empathy, and people first. Our advice is unbiased, our ethics are visible, and our goal is student impact—not forced sales.<br>
    <b>If your business builds lives, your success will build forever.</b>
    </div>
    """,unsafe_allow_html=True)
    st.button("✨ Start Your 4D Assessment",type="primary",on_click=lambda: nav("Assessment"))
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/India_Flag_300.png/80px-India_Flag_300.png",width=64)

# --- (Other site logic remains as per your last code) ---
# Paste all your original assessment, university, FAQ, About, routing, footer, CTA code blocks BELOW this point, UNCHANGED.

# --- Example (paste rest as per your original code) ---
def assessment_page(): 
    # ... [YOUR ORIGINAL CODE CONTENT] ...

def result_page():
    # ... [YOUR ORIGINAL CODE CONTENT] ...

def universities_page():
    # ... [YOUR ORIGINAL CODE CONTENT] ...

def faq_page():
    # ... [YOUR ORIGINAL CODE CONTENT] ...

def about_page():
    # ... [YOUR ORIGINAL CODE CONTENT] ...

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
""",unsafe_allow_html=True)
