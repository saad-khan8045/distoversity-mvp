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

# --- CSS / FONT / DESIGN SYSTEM ---
# ...[your existing CSS block, unchanged]...

# --- DATA ---
UNIS = [...] # [insert your existing UNIS list here]
alison_courses = {...} # [your existing profile->course dict]

if "page" not in st.session_state: st.session_state.page = "Home"
if "profile" not in st.session_state: st.session_state.profile = None
if "scores" not in st.session_state: st.session_state.scores = None

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
    <div style='margin:20px 0 13px 0;font-size:1.12rem;color:#1376d4;background:#e6f3fe;padding:10px 15px;border-radius:13px;font-family:Montserrat'>
    Education is a business—but only ethical businesses truly succeed.<br>
    Distoversity puts honesty, empathy, and people first. Our advice is unbiased, our ethics are visible, and our goal is student impact—not forced sales.<br>
    <b>If your business builds lives, your success will build forever.</b>
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
      <span style="font-size:1.07rem; color:#1376d4;"><b>Our test reveals your 4 energies: Creator, Influencer, Catalyst, Analyst.<br>This is your unique blueprint for success—no random results, only clarity.</b></span>
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
    <b>Founder’s Insight:</b> From factories, real counseling, and learning with Alison, I built the 4D Assessment for every student—science, privacy, and empathy at the core.<br>
    <br>
    <span class='alison-tag'>Alison Community Member</span>: Bringing global skill learning free for Indians.<br>
    <br>
    <b>For partners & TFI:</b> We aspire to work with every impact-focused educator, fellow, and org. Careers change lives—let's architect India's future, together.<br>
    <b>Contact:</b> distoversity@gmail.com | <a href="https://linkedin.com">LinkedIn</a>
    </p>
    </div>
    """,unsafe_allow_html=True)

def nav(p): st.session_state.page=p; st.rerun()

navbar()
page_map = {"Home": home_page, "Assessment": assessment_page, "Result": result_page,
            "Universities": universities_page, "FAQ": faq_page, "About": about_page}
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
