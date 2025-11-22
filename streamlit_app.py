import streamlit as st

st.set_page_config(
    page_title="Distoversity | Empowering India",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FONTS AND UNIVERSAL CSS ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Inter:wght@400;700&display=swap" rel="stylesheet">
<style>
html, body, [data-testid="stAppViewContainer"], .stApp, .main {
    background-color: #f4f9fd !important;
    color: #19315B !important;
    font-family: "Inter", "Montserrat", Arial, sans-serif !important;
    font-size: 1.01em;
}
h1, h2, h3, h4, h5 {
    font-family: "Montserrat", Arial, sans-serif !important;
    color: #19376D !important;
    font-weight: 900 !important;
}
@media screen and (max-width: 650px) {
    html, body, [data-testid="stAppViewContainer"], .stApp, .main { font-size: 1.06em; }
}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: PROFESSIONAL ---
with st.sidebar:
    st.markdown("<span style='font-family:Montserrat,sans-serif;font-size:2em;font-weight:900;color:#003366;'>DISTOVERSITY</span> <span style='font-size:1.18em;'>| EMPOWERING INDIA</span>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("<div style='font-family:Montserrat,sans-serif;font-size:1.02em;color:#1264a1;font-weight:700;margin:0 0 8px 1px;'>Your Career Success Partner</div>",unsafe_allow_html=True)
    st.markdown("Founder | EdTech Entrepreneur<br>Early Childhood & EdTech Leader", unsafe_allow_html=True)
    st.caption("📍 New Delhi, India")
    st.markdown("<div style='background:#dbf4e5;padding:9px 10px 7px 11px;border-radius:9px;font-size:1em;margin-top:7px;margin-bottom:8px;'>🎯 <b>Mission:</b> Replace 'Sales' in education with 'Science', Ethics, and Empowerment.</div>", unsafe_allow_html=True)

    # SKILLS & DOMAIN EXPERTISE (PROFESSIONAL LAYOUT)
    st.markdown("""
    <div style='margin-bottom:13px; margin-top:2px;'>
      <b style='font-family:Montserrat,sans-serif;font-size:1.12em;display:block;margin-bottom:3px;'>🚀 Key Skills & Domain Expertise</b>
      <div style='margin-bottom:13px;'>
        <b style='font-family:Montserrat,sans-serif;font-size:1.06em;display:block;'>Teaching & Educational Mentorship</b>
        <span style='font-family:Inter,sans-serif;font-weight:500;font-size:1em;'>
          • 10+ years ground teaching & empowerment<br>
          • Pedagogy, curriculum development, mentorship
        </span>
      </div>
      <div style='margin-bottom:13px;'>
        <b style='font-family:Montserrat,sans-serif;font-size:1.06em;display:block;'>Domain Expertise</b>
        <span style='font-family:Inter,sans-serif;font-weight:500;font-size:1em;line-height:1.23em;'>
          • Leadership for Footprints franchise growth (all India)<br>
          • 2,000+ students personally counseled/advised<br>
          • Admissions, student guidance (Subharti, Himalayan Garhwal, Noida International, Amity, Manipal, DY Patil, NMIMS)<br>
          • Power BI, Python, Streamlit analytics for student & franchise insights<br>
          • Deep child psychology understanding (Footprints Early Ed)<br>
          • Team Leadership | Ed-Psychology | Business Strategy
        </span>
      </div>
      <div style='font-family:Inter,sans-serif;font-size:1em;margin-top:6px;margin-bottom:7px;'>
        <span style='font-weight:600;'>Our counselling is <span style='color:#008066;'>data-driven</span>, powered by assessment. <span style='color:#0077B6;'>Cost: ₹999/session.</span></span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # MOTIVATIONAL CTA
    st.markdown("""
    <div style="background:linear-gradient(110deg,#e0f2fe,#c5fdd6);border-radius:12px;padding:18px 14px 12px 14px;
        border:1.5px solid #bae6fd;margin-bottom:16px;box-shadow:0 3px 18px #c6f9f866; font-family: Inter, sans-serif;">
    <span style="font-size:1.11em;font-weight:700;color:#085f43;">🌟 Ready to discover your energy and direction?</span><br>
    Let's move beyond confusion and guesswork.<br>
    <b>Book a 4D Assessment—let’s plan your next step together.</b><br>
    <span style='color:#1f5d58;font-size:1em;'>No more random calls. Real futures, real results.<br>
    Sign up for your session now for just <b>₹999!</b></span><br>
    <a href='mailto:saad01489@gmail.com?subject=Book%20my%204D%20Assessment%20Session' target="_blank">
    <button style='margin-top:9px;background: #059669;color:#fff;border:none;border-radius:5px;padding:10px 27px;
    font-size:1.06em;font-weight:700;letter-spacing:0.02em;box-shadow:0 2px 8px #20715023;cursor:pointer;'>
    Book My Session
    </button></a>
    <span style='background:#e7f7e7;color:#308045;border-radius:7px;font-size:0.88em;font-weight:600;display:inline-block;padding:3px 9px;margin-top:8px;'>Proud Alison Community Member</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='font-family:Inter,sans-serif;font-size:1em;margin-bottom:5px;color:#126064;'>🔒 <b>We are NOT selling your data</b>. Your privacy is 100% protected.</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:Inter,sans-serif;color:#516984;font-size:0.97em;margin-bottom:2px;'>Copyright © 2025 Distoversity. All rights reserved.</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:Inter,sans-serif;font-size:0.96em;'><a href='https://linkedin.com' target='_blank'>LinkedIn</a> | <a href='mailto:saad01489@gmail.com'>Email</a></div>", unsafe_allow_html=True)
    st.markdown("<hr style='border:none;border-top:1.4px solid #e2eaf7;margin:10px 0;'>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:Montserrat,sans-serif;font-weight:700;font-size:1.01em;'>Try Our Career Guidance Platform</div>", unsafe_allow_html=True)
    st.markdown("<a href='https://distoversity-mvp-j4pmyhqdjr7v7ukpgwmyx6.streamlit.app/' target='_blank' style='background:#e0f2fe;padding:7px 16px;font-weight:600;color:#0077B6;border-radius:7px;font-size:0.98em;display:inline-block;text-decoration:none;margin-top:7px;'>👉 Distoversity Career Platform</a>", unsafe_allow_html=True)

# ---- Your existing TABS/BODY code below (from previous versions, unchanged) ----
# Just keep your main `tab1, tab2, tab3, tab4 = st.tabs([...])` and related logic

# ---- Footer (Optional, can use yours) ----
st.markdown("""
<div style='font-family:Inter,sans-serif;font-size:0.97em;color:#516984;text-align:center;margin-top:22px;'>
Distoversity | Your Career Success Partner 🎓<br>
<b>🔒 We are NOT selling your data</b> – Your privacy is always protected. <br>
Proud Alison Community Member | Copyright © 2025 Distoversity.
</div>
""",unsafe_allow_html=True)
