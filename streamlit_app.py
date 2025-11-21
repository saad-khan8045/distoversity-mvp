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

# --- ENHANCED DESIGN SYSTEM ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Inter:wght@400;500;600;700&display=swap');

/* Base styles */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background: #f8fafc !important;
    color: #1e293b;
    line-height: 1.7;
}

/* Typography hierarchy */
h1 {
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 900 !important;
    font-size: 2.75rem !important;
    line-height: 1.2 !important;
    letter-spacing: -0.03em !important;
    color: #0f172a !important;
    margin-bottom: 1.25rem !important;
}

h2 {
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 800 !important;
    font-size: 2rem !important;
    line-height: 1.3 !important;
    letter-spacing: -0.02em !important;
    color: #1e293b !important;
    margin-bottom: 1rem !important;
}

h3 {
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.5rem !important;
    line-height: 1.4 !important;
    color: #334155 !important;
    margin-bottom: 0.75rem !important;
}

h4 {
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.25rem !important;
    color: #475569 !important;
}

p, li, span {
    font-size: 1.0625rem !important;
    line-height: 1.75 !important;
    color: #475569 !important;
}

/* Navigation */
.nav-logo {
    font-family: 'Montserrat', sans-serif;
    font-size: 2rem;
    font-weight: 900 !important;
    color: #0f172a !important;
    display: inline;
    margin-right: 0.5rem;
    letter-spacing: -0.02em;
}

.empower-small {
    font-family: 'Montserrat', sans-serif !important;
    font-size: 0.9rem;
    color: #0ea5e9 !important;
    font-weight: 700 !important;
    display: inline-block;
    margin-left: 0.25rem;
}

.nav-flag {
    font-size: 1.25rem;
    display: inline;
    vertical-align: middle;
    margin-left: 0.25rem;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%) !important;
    color: #ffffff !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.0625rem !important;
    border: none !important;
    border-radius: 0.75rem !important;
    padding: 0.875rem 2rem !important;
    box-shadow: 0 4px 14px rgba(14, 165, 233, 0.25) !important;
    transition: all 0.3s ease !important;
    cursor: pointer !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(14, 165, 233, 0.35) !important;
}

/* Cards */
.d-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 1rem;
    padding: 1.75rem 1.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;
}

.d-card:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    border-color: #cbd5e1;
}

.hero-section, .about-box {
    background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
    border-radius: 1.25rem;
    margin-bottom: 2.5rem;
    padding: 3rem 2.5rem;
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

/* Labels and form elements */
label, .question-text {
    color: #1e293b !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1.0625rem !important;
    margin-bottom: 0.5rem !important;
}

/* Badges */
.badge {
    background: #e0f2fe;
    color: #0369a1;
    font-family: 'Montserrat', sans-serif !important;
    padding: 0.5rem 1rem;
    font-weight: 700;
    border-radius: 0.5rem;
    font-size: 0.9375rem;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    display: inline-block;
}

.alison-tag {
    background: #d1fae5;
    color: #065f46;
    border-radius: 0.5rem;
    font-size: 0.9375rem;
    font-weight: 700;
    display: inline-block;
    padding: 0.375rem 0.75rem;
    margin-bottom: 0.5rem;
    margin-left: 0.25rem;
}

/* CTA Sticky */
.cta-sticky {
    position: fixed;
    bottom: 1.5rem;
    right: 1.5rem;
    z-index: 9999;
    background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%) !important;
    color: white;
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 1rem;
    padding: 1rem 2rem;
    border-radius: 3rem;
    box-shadow: 0 4px 20px rgba(14, 165, 233, 0.35);
    border: none;
    transition: all 0.3s ease;
}

.cta-sticky:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 24px rgba(14, 165, 233, 0.45);
}

/* Lists */
ul, ol {
    font-size: 1.0625rem;
    line-height: 1.85;
    color: #475569;
    margin-left: 1.25rem;
}

ul li, ol li {
    margin-bottom: 0.75rem;
}

/* Horizontal rule */
hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 2rem 0;
}

/* Footer */
.footer-note {
    font-size: 0.9375rem;
    text-align: center;
    margin: 2.5rem 0 1rem;
    color: #64748b;
    line-height: 1.6;
}

/* Info boxes */
.stAlert {
    border-radius: 0.75rem !important;
    border-left: 4px solid #0ea5e9 !important;
}

/* Dataframes */
.dataframe {
    border-radius: 0.75rem !important;
    overflow: hidden !important;
}

/* Radio buttons and inputs */
.stRadio > label {
    font-size: 1rem !important;
    color: #334155 !important;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    h1 {
        font-size: 2rem !important;
    }
    h2 {
        font-size: 1.5rem !important;
    }
    .hero-section, .about-box {
        padding: 2rem 1.5rem;
    }
    .cta-sticky {
        font-size: 0.875rem;
        padding: 0.75rem 1.5rem;
    }
}
</style>
""", unsafe_allow_html=True)

# --- DATA ---
UNIS = [
    {"name":"Jain (Online)","type":"Private","city":"Bengaluru","profile":"Creator","fee":210000,"naac":"A++","pkg":"32LPA","alison":"Innovation Management"},
    {"name":"Manipal Online","type":"Private","city":"Jaipur","profile":"Analyst","fee":175000,"naac":"A+","pkg":"18LPA","alison":"Data Science Fundamentals"},
    {"name":"Amity University Online","type":"Private","city":"Global","profile":"Creator","fee":345000,"naac":"A+","pkg":"15LPA","alison":"Design Thinking"},
    {"name":"LPU Online","type":"Private","city":"Global","profile":"Catalyst","fee":160000,"naac":"A++","pkg":"21LPA","alison":"Agile Leadership"},
    {"name":"Chandigarh University Online","type":"Private","city":"Online","profile":"Influencer","fee":180000,"naac":"A+","pkg":"28LPA","alison":"Social Media Marketing"},
    {"name":"NMIMS Global","type":"Private","city":"Online","profile":"Influencer","fee":400000,"naac":"A+","pkg":"45LPA","alison":"Public Speaking"},
    {"name":"DY Patil Online","type":"Private","city":"Pune","profile":"Catalyst","fee":120000,"naac":"A++","pkg":"12LPA","alison":"Project Management"},
]
alison_courses = {
    "Creator":["Innovation Management", "Design Thinking"],
    "Influencer":["Social Media Marketing", "Public Speaking"],
    "Catalyst":["Agile Leadership", "Project Management"],
    "Analyst":["Data Science Fundamentals", "Excel Strategies"]
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
    <div id="founder-modal" style="position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(15,23,42,0.15);z-index:99999;display:flex;align-items:center;justify-content:center;backdrop-filter:blur(2px);">
      <div style="background:white;max-width:360px;border-radius:1.25rem;box-shadow:0 20px 60px rgba(0,0,0,0.15);padding:2rem 1.5rem 1.25rem;text-align:center;position:relative;font-family:Montserrat;animation:slideUp 0.4s ease;">
        <button onclick="document.getElementById('founder-modal').style.display='none';document.body.style.overflow='';"
        style='position:absolute;top:0.75rem;right:0.75rem;background:#f1f5f9;font-size:1.5rem;color:#64748b;border:none;border-radius:0.5rem;font-weight:700;width:32px;height:32px;cursor:pointer;transition:all 0.2s;'>×</button>
        <img src='https://avatars.githubusercontent.com/u/7087942?s=400' width='64' style='border-radius:1rem;box-shadow:0 4px 16px rgba(0,0,0,0.12);margin-bottom:1rem;'>
        <h4 style='margin:0.5rem 0;font-family:Montserrat;color:#0f172a;font-size:1.25rem;font-weight:700;'>Mohd Saad</h4>
        <div style="font-size:0.9375rem;color:#0ea5e9;font-weight:600;margin-bottom:1rem;">Senior Career Advisor & Founder</div>
        <div style="font-size:0.9375rem;color:#475569;background:#f1f5f9;border-radius:0.75rem;padding:0.875rem;margin:1rem 0;line-height:1.6;text-align:left;">
            <strong style="color:#1e293b;">Guiding you with ethics, not sales.</strong><br>
            Every student is seen, heard, and supported.
        </div>
        <a href="https://linkedin.com/" target="_blank" style="text-decoration:none;">
            <button style="background:linear-gradient(135deg,#0ea5e9 0%,#0284c7 100%);color:#fff;font-family:Montserrat;font-weight:700;font-size:0.9375rem;padding:0.625rem 1.25rem;border:none;border-radius:0.625rem;margin-bottom:0.5rem;cursor:pointer;transition:all 0.3s;box-shadow:0 2px 8px rgba(14,165,233,0.25);">LinkedIn
