import streamlit as st
import pandas as pd

# --- PAGE CONFIG & SEO ---
st.set_page_config(
    page_title="Distoversity | Free Career Assessment & University Counseling - Find Your Dream Career",
    page_icon="🎓",
    layout="wide"
)
st.markdown("""
    <meta name="description" content="Discover your ideal career with Distoversity's free 4D Assessment. Get personalized university recommendations and expert counseling. 100% data privacy - we never sell your information!">
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
    # Empowering India Vision Banner
    st.markdown("""
    <div style="background: linear-gradient(90deg, #E0F2FE 20%, #d1fae5 90%);
                border-radius:18px; border:2px solid #00AEEF;
                padding:24px 22px 18px 22px; margin-bottom:22px; box-shadow: 0 2px 14px #1ab6ed21;">
        <h2 style="text-align:center; color:#003366; margin-bottom:7px;">🚀 Our Vision: Empowering India</h2>
        <p style="font-size:1.17rem; color:#045; text-align:center;">
        <b>Distoversity</b> is on a mission to help every student—and every working professional—discover their purpose, build global skills, and achieve career dreams with ethics and transparency.<br>
        <span style="color:#1bbc87; font-weight:700;">Together, we are empowering India—one future at a time.</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    # ...rest of your home hero content unchanged...
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

# --- ENHANCED RESULT PAGE for Color & Engagement ---
def result_page():
    prof = st.session_state.get("profile")
    scores = st.session_state.get("scores")
    if not prof:
        st.warning("⚠️ Please complete your free assessment first to see your personalized results!"); return
    st.markdown(f"<h2 style='color:#1376d4;text-align:center;'>🎉 Congratulations! You're a <span style='text-transform:uppercase;'>{prof}</span></h2>",unsafe_allow_html=True)
    st.markdown(f"""<div class="badge" style="margin-bottom:10px;">Expert Verified | Your Personalized Career DNA</div>""",unsafe_allow_html=True)

    # Engaging color panels for Students & Professionals
    st.markdown("""
    <div style="background: linear-gradient(90deg, #eaf6ff 0%, #defcf9 100%);
                border-radius:16px; border:2px solid #b2ddff; padding:22px; margin:16px 0;">
        <h4 style="color:#1376d4; margin-bottom:6px;">🎓 For Students</h4>
        <ul style="color:#045;">
          <li>🔥 Build your skills and network—college is the launch pad to your dreams.</li>
          <li>🌟 Take leadership in clubs, events, projects—every step counts for growth!</li>
          <li>💎 Remember: Your career DNA matters more than just marks.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: linear-gradient(90deg, #f0fff4 0%, #e6fbf4 100%);
                border-radius:16px; border:2px solid #b6f0d4; padding:22px; margin:16px 0;">
        <h4 style="color:#1bbc87; margin-bottom:6px;">💼 For Working Professionals</h4>
        <ul style="color:#085;">
          <li>🚀 Upgrade your skills with flexible online courses—it's never too late.</li>
          <li>🤝 Mentor juniors—your experience is valuable and multiplies your growth.</li>
          <li>🔄 Experience + new skills = career transformation. It's time to pivot upwards!</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

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
        st.write(f"✅ {course} (Start Free Course Now)")
    st.markdown("<hr>",unsafe_allow_html=True)
    st.markdown("<b>🎯 Perfect University Matches for Your Career Profile:</b>",unsafe_allow_html=True)
    matches = [u for u in UNIS if u['profile'] == prof]
    for u in matches:
        st.markdown(f"""
        <div class="d-card"><h3>🏆 {u['name']}</h3>
        <span class="badge">{u['city']}</span> | <span class="badge">NAAC: {u['naac']}</span> | <b>Annual Fee:</b> ₹{u['fee']:,}<br>
        <b>💼 Avg Placement:</b> {u['pkg']} |
        <b>📚 Skill Course:</b> {u['alison']}
        </div>
        """,unsafe_allow_html=True)
    st.button("📚 Compare All Universities →",on_click=lambda: nav("Universities"))

def universities_page():
    st.markdown("<h2>Compare India's Top Universities</h2>",unsafe_allow_html=True)
    st.caption("Sort and filter by fees, NAAC rating, placement packages, career profile match, and city – all data completely transparent.")
    df = pd.DataFrame(UNIS)
    cols = st.columns(4)
    sel_prof = cols[0].selectbox("Filter by Career Profile",["All"]+list(alison_courses.keys()))
    sel_sort = cols[1].selectbox("Sort by",["Fee (Lowest)","Fee (Highest)","Placement (Highest)"])
    budget = cols[2].slider("Maximum Annual Fee (Lakh ₹)",1,6,3)
    naac_plus = cols[3].checkbox("Show only NAAC A++ universities",False)
    temp = df[df['fee']<=budget*100000]
    if naac_plus: temp=temp[temp.naac=="A++"]
    if sel_prof!="All": temp=temp[temp.profile==sel_prof]
    temp = temp.sort_values("fee" if "Fee" in sel_sort else "pkg", ascending="Lowest" in sel_sort)
    st.dataframe(temp[["name","profile","fee","naac","city","pkg"]].reset_index(drop=True),use_container_width=True)
    st.markdown("💡 Need help choosing? Take our Free 4D Assessment to find your perfect university match!")

def faq_page():
    st.title("Frequently Asked Questions")
    faq = [
        ("What is the 4D Assessment?",
         "Our 4D Assessment is a free career discovery tool that reveals your natural strengths across four career energies: Creator, Influencer, Catalyst, and Analyst. Each type has unique career paths, skills, and university recommendations perfectly matched to your personality."),
        ("How do you provide career guidance?",
         "We combine AI technology with real human mentors to give you personalized advice. We guide you to make the best decision for your future – we never push sales or force you into anything. Your success is our priority!"),
        ("What are the free skill courses from Alison?",
         "We're proud members of the Alison global learning community. Based on your career profile, we recommend free, high-quality courses that help you build job-ready skills. No cost, just value!"),
        ("Is my data safe with you?",
         "Absolutely! We are NOT selling your data. Your privacy is 100% protected. We use your information only to provide you with personalized career guidance. Your trust matters to us."),
        ("How do you select which universities to recommend?",
         "We only feature UGC, NAAC, and AICTE approved universities. All data (fees, placements, ratings) is verified and transparent. You get honest information to make informed decisions."),
        ("How can I contact you for counseling?",
         "Easy! Click the floating button on your screen, or email us at distoversity@gmail.com, or WhatsApp: +91-9111111111. We're here to help!")
    ]
    for q,a in faq:
        with st.expander(q):
            st.write(a)

def about_page():
    st.markdown("""
    <div class='about-box'>
    <h1 style="margin-bottom:6px;">Distoversity – Honest Career Guidance You Can Trust <span class='nav-flag'>🎓</span></h1>
    <span class='empower-small'>Your Career Success Partner</span>
    <hr>
    <p>
    <b>We guide, we don't sell.</b> Distoversity is India's most trusted career guidance platform. We combine expert counselors with AI technology to help you discover your true potential and find the perfect university match.<br>
    <br>
    <b>Our Mission:</b> Built with real counseling experience and powered by data science, our 4D Assessment helps every student discover their unique career DNA. We believe in transparency, privacy, and putting your success first.<br>
    <br>
    <span class='alison-tag'>Proud Alison Community Member</span>: We bring world-class free skill courses to Indian students.<br>
    <br>
    <b>For educational partners:</b> We work with impact-focused educators and organizations who believe careers change lives. Let's build India's future together!<br>
    <br>
    <b>🔒 Privacy Promise:</b> We are NOT selling your data. Your information is 100% private and secure.<br>
    <br>
    <b>Contact Us:</b> distoversity@gmail.com | <a href="https://linkedin.com">LinkedIn</a>
    </p>
    </div>
    """,unsafe_allow_html=True)

def nav(p): st.session_state.page=p; st.rerun()

# --- MAIN ROUTER ---
navbar()
page_map={"Home":home_page,"Assessment":assessment_page,"Result":result_page,
          "Universities":universities_page,"FAQ":faq_page,"About":about_page}
if st.session_state.page=="Result":
    result_page()
else:
    page_map[st.session_state.page]()

st.markdown("""
<a href="mailto:distoversity@gmail.com?subject=Book%20Career%20Counseling%20Call"
class="cta-sticky" target="_blank" style="text-decoration:none;">
<span class='nav-flag'>🎓</span> Book Free Career Counseling Call 🚀
</a>
<div class="footer-note">
Distoversity <span class='empower-small'>Your Career Success Partner <span class='nav-flag'>🎓</span></span>
<br>
🔒 <b>We are NOT selling your data</b> – Your privacy is always protected. Alison Community Member | Copyright © 2025 Distoversity.
</div>
""",unsafe_allow_html=True)
