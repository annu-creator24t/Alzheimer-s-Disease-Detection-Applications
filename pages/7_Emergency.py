import streamlit as st
from utils import load_css

load_css()

# ── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="clinical-header">
    <div class="clinical-badge badge-danger">Critical Support</div>
    <h1 class="header-title">Emergency Assistance & Rapid Response</h1>
    <p class="header-desc">
        Immediate access to primary care clinicians, designated family caregivers, 
        and emergency neuro-hospital dispatch services.
    </p>
</div>
""", unsafe_allow_html=True)

st.error("Emergency Contacts Directory")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Verified Contact Channels")
    
    st.markdown("""
    <div class="contact-row">
        <span class="contact-name">Primary Neurologist</span>
        <span class="contact-val">+91-9876543210</span>
    </div>
    <div class="contact-row">
        <span class="contact-name">Designated Caregiver</span>
        <span class="contact-val">+91-9999999999</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("📞 Doctor: +91-9876543210")
    st.write("📞 Caregiver: +91-9999999999")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Immediate Action Dispatch")
    st.write("Trigger automated emergency dispatch and alert designated responders:")
    
    st.markdown("<div style='margin-top: 0.75rem;'></div>", unsafe_allow_html=True)
    if st.button("Call Ambulance"):
        st.success("Calling Ambulance (UI Mock)")
    
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    st.info("Nearest Hospital: City Care Hospital (Emergency Neuro Dept.)")
    st.markdown("</div>", unsafe_allow_html=True)