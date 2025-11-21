import streamlit as st
import pandas as pd

# --- PAGE CONFIG & SEO ---
st.set_page_config(
    page_title="Distoversity | Free Career Assessment & Expert University Counseling - Find Your Perfect Career Path",
    page_icon="🎓",
    layout="wide"
)
st.markdown("""
    <meta name="description" content="Discover your ideal career with Distoversity's free 4D Assessment. Get personalized university recommendations, expert counseling, and skill-building resources. Your data is 100% private - we never sell it!">
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
    {"name":"DY Patil Online","type":"Private","city":"Pune","profile":"Catalyst","fee":120000,"naac":"A++","pkg":"12LPA","alison":"Project Management"}
]
alison_courses = {
    "Creator":["Innovation Management", "Design Thinking (Alison)"],
    "Influencer":["Social Media Marketing (Alison)", "Public Speaking"],
    "Catalyst":["Agile Leadership (Alison)", "Project Management"],
    "Analyst":["Data Science Fundamentals (Alison)", "Excel Strategies"]
}

# --- STATE ---
if "page" not in st.session_state: st.session_state.page = "Home"
if "profile" not in st.session_state: st.session_state.profile = None
if "scores" not in st.session_state: st.session_state.scores = None

# --- NAVBAR ---
def navbar():
    cols = st.columns([2.4,1,1.25,1.23,1,1.46])
    with cols[0]:
        st.markdown("<span class='nav-logo'>Distoversity</span>",unsafe_allow_html=True)
        st.markdown("<span class='empower-small'>Your Career Success Partner <span class='nav-flag'>🎓</span></span>",unsafe_allow_html=True)
    if cols[1].button("Home"): st.session_state.page="Home";st.rerun()
    if cols[2].button("4D Assessment"): st.session_state.page="Assessment";st.rerun()
    if cols[3].button("Universities"): st.session_state.page="Universities";st.rerun()
    if cols[4].button("FAQ"): st.session_state.page="FAQ";st.rerun()
    if cols[5].button("About"): st.session_state.page="About";st.rerun()
    st.markdown("---")

# --- PAGE ROUTES ---
def home_page():
    st.markdown("""
    <div class="hero-section">
        <h1>Unlock Your Dream Career – Start Your Free Assessment Today! <span class='nav-flag'>🎯</span></h1>
        <p style="font-size:1.17rem;">Discover your perfect career path with expert guidance you can trust.<br>
        <span class="badge">Free 4D Assessment | Expert Counseling | Top University Matches</span></p>
        <ul>
        <li>🎯 Take our <b>Free 4D Career Assessment</b> – Find out if you're a Creator, Influencer, Catalyst, or Analyst!</li>
        <li>🎓 Compare India's best UGC & NAAC approved universities with complete transparency</li>
        <li>📚 Get access to <span class="alison-tag">Free Skill Courses</span> perfectly matched to your career type</li>
        <li>💡 Receive honest guidance from real mentors + AI – we help you decide, never push sales</li>
        <li>🔒 <b>We are NOT selling your data</b> – Your privacy is 100% protected, always!</li>
        </ul>
        <p style="font-size:1.1rem;margin-top:1rem;"><b>Ready to discover your true potential? Your dream career starts here!</b></p>
    </div>
    """,unsafe_allow_html=True)
    st.button("🚀 Start Your Free Assessment Now",type="primary",on_click=lambda: nav("Assessment"))
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/India_Flag_300.png/80px-India_Flag_300.png",width=64)

def assessment_page():
    st.markdown("<h2 style='text-align:center;'>Discover Your Career DNA – Free 4D Assessment</h2>",unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;'>
      <span class='badge'>100% Free | Takes Only 2 Minutes | Instant Results</span>
      <br>
      <span style="font-size:1.07rem; color:#1376d4;"><b>Find your natural career strengths: Creator, Influencer, Catalyst, or Analyst.<br>Get your personalized career roadmap based on your unique energy!</b></span>
    </div>
    """,unsafe_allow_html=True)
    st.info("✅ Just 5 simple questions • No right or wrong answers • Discover what makes you unique")
    with st.form("dist_assess"):
        q1 = st.radio("Q1. When do you feel most excited and motivated at work?",["Creating something new and innovative","Leading and inspiring others","Completing projects and achieving goals","Analyzing data and solving problems"],index=None)
        q2 = st.radio("Q2. How would your friends describe you?",["The creative idea person","The natural leader who motivates","The reliable one who gets things done","The smart problem-solver"],index=None)
        q3 = st.radio("Q3. What frustrates you the most?",["Boring, repetitive tasks","Working alone without interaction","Unclear goals and delays","Making decisions without facts"],index=None)
        q4 = st.radio("Q4. If you had a completely free day, what would you choose to do?",["Brainstorm 3 new business ideas","Organize an event with friends","Complete all your pending tasks","Learn about new trends and data"],index=None)
        q5 = st.radio("Q5. What's your ultimate career dream?",["Build something world-changing","Inspire thousands of people","Lead operations at a top company","Solve complex challenges with data"],index=None)
        if st.form_submit_button("✨ Get My Free Career Profile →"):
            tally = {"Creator":0,"Influencer":0,"Catalyst":0,"Analyst":0}
            for a in [q1,q2,q3,q4,q5]:
                if "idea" in a or "Creating" in a or "creative" in a or "Brainstorm" in a or "Build" in a: tally["Creator"]+=1
                elif "inspiring" in a or "Leader" in a or "Inspire" in a or "Leading" in a or "event" in a or "motivates" in a: tally["Influencer"]+=1
                elif "Completing" in a or "achieving" in a or "gets things done" in a or "operations" in a or "pending" in a: tally["Catalyst"]+=1
                else: tally["Analyst"]+=1
            winner = max(tally, key=tally.get)
            st.session_state.profile = winner
            st.session_state.scores = tally
            nav("Result")

def result_page():
    prof = st.session_state.get("profile")
    scores = st.session_state.get("scores")
    if not prof:
        st.warning("⚠️ Please complete your free assessment first to see your personalized results!"); return
    st.markdown(f"<h2 style='color:#1376d4;text-align:center;'>🎉 Congratulations! You're a <span style='text-transform:uppercase;'>{prof}</span></h2>",unsafe_allow_html=True)
    st.markdown(f"""<div class="badge" style="margin-bottom:10px;">Expert Verified | Your Personalized Career DNA</div>""",unsafe_allow_html=True)
    st.markdown("""
    <div class='d-card' style='margin-bottom:1.2rem;'>
        <b>📊 Understanding Each Career Type (Your Strengths & Growth Tips):</b>
        <ul>
        <li><b>Creator:</b> You're innovative and visionary! Focus on finishing what you start to maximize your impact.</li>
        <li><b>Influencer:</b> You naturally inspire and lead people! Build genuine connections and turn your words into action.</li>
        <li><b>Catalyst:</b> You're a results-driven achiever! Keep learning new skills and remember to maintain work-life balance.</li>
        <li><b>Analyst:</b> You excel at solving complex problems with data! Don't let perfectionism stop you from taking action.</li>
        </ul>
    </div>
    """,unsafe_allow_html=True)
    st.markdown(f"<h4>🎓 Recommended Free Skill Courses for {prof}s</h4>",unsafe_allow_html=True)
    st.markdown("<span class='alison-tag'>100% Free Learning | Build Career-Ready Skills</span>",unsafe_allow_html=True)
    for course in alison_courses[prof]:
        st.write(f"✅ {course} ([Start Free Course Now](https://alison.com/courses))")
    st.markdown("<hr>",unsafe_allow_html=True)
    st.markdown("<b>🎯 Perfect University Matches for Your Career Profile:</b>",unsafe_allow_html=True)
    matches = [u for u in UNIS if u['profile'] == prof]
    for u in matches:
        st.markdown(f"""
        <div class="d-card"><h3>🏆 {u['name']}</h3>
        <span class="badge">{u['city']}</span> | <span class="badge">NAAC:
