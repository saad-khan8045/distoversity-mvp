import streamlit as st
import pandas as pd
import time
import plotly.express as px

# --- 1. SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed" # Keeps sidebar hidden on mobile until clicked
)

# --- 2. RESPONSIVE CSS (Fixes Mobile Issues) ---
st.markdown("""
    <style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    :root { --primary: #0077B6; --text-main: #0F172A; }
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-main);
        background-color: #F8FAFC;
    }

    /* Fix for the header overlap on mobile */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* Card Styling */
    .d-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }

    /* Make radio buttons larger for mobile tapping */
    .stRadio label {
        font-size: 16px !important;
        padding: 10px 0;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA ---
# (Keeping your data structure)
UNIVERSITY_DATA = [
    {"name": "Manipal Online", "location": "Jaipur", "program": "MCA Data Science", "energy": "Steel (Analyst)", "fees": 175000, "emi": 4500, "placement": 94, "avg_pkg": 5.5, "naac": "A+", "approvals": "UGC, AICTE", "recruiters": ["Google", "Deloitte"], "logo": "https://via.placeholder.com/50"},
    {"name": "Jain Online", "location": "Bangalore", "program": "MBA Marketing", "energy": "Blaze (Influencer)", "fees": 210000, "emi": 5200, "placement": 98, "avg_pkg": 6.2, "naac": "A++", "approvals": "UGC-DEB", "recruiters": ["HDFC", "Amazon"], "logo": "https://via.placeholder.com/50"},
    {"name": "Amity Online", "location": "Global", "program": "BCA Cloud Security", "energy": "Creator (Dynamo)", "fees": 345000, "emi": 6500, "placement": 92, "avg_pkg": 4.8, "naac": "A+", "approvals": "UGC, WES", "recruiters": ["Microsoft", "TCS"], "logo": "https://via.placeholder.com/50"},
    {"name": "LPU Online", "location": "Punjab", "program": "MBA Operations", "energy": "Tempo (Catalyst)", "fees": 160000, "emi": 3500, "placement": 91, "avg_pkg": 5.0, "naac": "A++", "approvals": "UGC, AICTE", "recruiters": ["Capgemini", "Wipro"], "logo": "https://via.placeholder.com/50"}
]
df = pd.DataFrame(UNIVERSITY_DATA)

# --- 4. STATE MANAGEMENT ---
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'user_profile' not in st.session_state: st.session_state.user_profile = None
if 'messages' not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Hello! I am Eduveer. Ask me about your Genius Profile or any University."}]

# --- 5. RESPONSIVE NAVIGATION (THE FIX) ---
# Instead of columns at the top, we use the sidebar for navigation.
# This works perfectly on mobile (hamburger menu) and desktop (sidebar).

with st.sidebar:
    st.title("Distoversity.")
    st.write("Discover Your Spark.")
    st.write("---")
    
    # Navigation Menu
    selected = st.radio(
        "Navigate to:",
        ["Home", "University Explorer", "Eduveer AI", "Take Assessment", "FAQ"],
        index=0 if st.session_state.page == 'Home' else 1
    )
    
    # Update session state based on sidebar selection
    if selected == "Home": st.session_state.page = 'Home'
    elif selected == "University Explorer": st.session_state.page = 'Explorer'
    elif selected == "Eduveer AI": st.session_state.page = 'Eduveer'
    elif selected == "Take Assessment": st.session_state.page = 'Assessment'
    elif selected == "FAQ": st.session_state.page = 'FAQ'

    st.divider()
    st.info("Need help? Chat with Eduveer!")

# --- 6. PAGE CONTENT ---

def render_home():
    # Hero Section optimized for mobile (no fixed height)
    st.markdown("""
    <div style="text-align:center; padding: 3rem 1rem; background: radial-gradient(circle at 50% 0%, #E0F2FE 0%, #FFFFFF 70%); border-radius: 0 0 30px 30px;">
        <h1 style="font-size: 2.5rem; color:#023E8A; margin-bottom: 1rem;">Start Engineering Your Future.</h1>
        <p style="font-size: 1.1rem; color: #475569; margin-bottom: 2rem;">
            We match your natural <b>Genius Profile</b> to India's Top Online Universities using AI.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # CTA Button
    if st.button("⚡ Start Assessment (Free)", type="primary", use_container_width=True):
        st.session_state.page = 'Assessment'
        st.rerun()

    st.divider()
    st.subheader("Why Distoversity?")
    
    # Cards that stack on mobile automatically
    st.markdown("""
    <div class="d-card"><h3>🧠 Identity First</h3><p>We look at your Mind, not just your marks.</p></div>
    <div class="d-card"><h3>🤖 AI Powered</h3><p>Chat with Eduveer 24/7 for unbiased advice.</p></div>
    <div class="d-card"><h3>💼 Career Roadmap</h3><p>Don't just get a degree. Get a Strategy.</p></div>
    """, unsafe_allow_html=True)

def render_explorer():
    st.header("🏫 University Explorer")
    
    # Filters inside an expander to save space on mobile
    with st.expander("Filter Options", expanded=False):
        budget = st.slider("Max Fees (₹)", 100000, 500000, 300000)
        energy_fit = st.multiselect("Genius Profile", ["Creator (Dynamo)", "Blaze (Influencer)", "Tempo (Catalyst)", "Steel (Analyst)"])
    
    filtered_df = df[df['fees'] <= budget]
    if energy_fit:
        filtered_df = filtered_df[filtered_df['energy'].isin(energy_fit)]
        
    st.write(f"Found {len(filtered_df)} universities.")
    
    # Mobile-friendly Card View
    for index, row in filtered_df.iterrows():
        with st.container(border=True):
            st.subheader(row['name'])
            st.write(f"**{row['program']}** | {row['location']}")
            st.caption(f"Energy Match: {row['energy']}")
            st.metric("Fees", f"₹{row['fees']:,}", f"EMI: ₹{row['emi']}/mo")
            
            c1, c2 = st.columns(2)
            c1.button("Brochure", key=f"b_{index}", use_container_width=True)
            c2.button("Apply", key=f"a_{index}", type="primary", use_container_width=True)

def render_assessment():
    st.header("⚡ Discover Your Spark")
    st.write("Select the option that fits you best.")
    
    with st.form("assessment_form"):
        st.write("**1. When solving a problem, you naturally:**")
        q1 = st.radio("Q1", ["Create new ideas", "Talk to people", "Organize timing", "Analyze details"], label_visibility="collapsed")
        
        st.write("**2. Your ideal work environment:**")
        q2 = st.radio("Q2", ["Freedom & Innovation", "Social & Collaborative", "Busy & Service-oriented", "Quiet & Structured"], label_visibility="collapsed")
        
        st.write("**3. You are most valuable when:**")
        q3 = st.radio("Q3", ["Starting things", "Networking", "Reacting to needs", "Refining systems"], label_visibility="collapsed")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.form_submit_button("Reveal My Profile ➤", type="primary", use_container_width=True):
            st.balloons()
            st.success("Assessment Complete! (Logic placeholder)")

def render_eduveer():
    st.header("🤖 Eduveer AI Chat")
    
    # Chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    if prompt := st.chat_input("Ask about fees, placements..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            response = "I can help you compare universities. Try checking the Explorer tab!"
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

def render_faq():
    st.header("❓ FAQ")
    with st.expander("How do I choose a career?"):
        st.write("We use the 4 Genius framework to match your personality to the right job.")
    with st.expander("Are these degrees valid?"):
        st.write("Yes, all universities listed are UGC-approved.")

# --- 7. MAIN ROUTER ---
if st.session_state.page == 'Home': render_home()
elif st.session_state.page == 'Explorer': render_explorer()
elif st.session_state.page == 'Eduveer': render_eduveer()
elif st.session_state.page == 'Assessment': render_assessment()
elif st.session_state.page == 'FAQ': render_faq()
