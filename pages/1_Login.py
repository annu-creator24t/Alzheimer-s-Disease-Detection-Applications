import streamlit as st
from utils import load_css

load_css()

# ── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="clinical-header">
    <div class="clinical-badge">Secure Access</div>
    <h1 class="header-title">Clinical & Patient Portal Login</h1>
    <p class="header-desc">
        Select your role and authenticate to access patient records, diagnostic tools, 
        and cognitive assessment workflows.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Login Form Container ──────────────────────────────────────
st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)

role = st.selectbox("Login as", ["Patient", "Doctor", "Caregiver"], help="Select your portal access level")

email = st.text_input("Email", placeholder="user@hospital.org")
password = st.text_input("Password", type="password", placeholder="••••••••")

st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

if st.button("Login"):
    st.success(f"Logged in as {role}")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="clinical-callout">
    🔒 <strong>Security Note:</strong> All clinical assessments and patient data access comply with standardized hospital privacy protocols.
</div>
""", unsafe_allow_html=True)