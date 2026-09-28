import streamlit as st
from utils import load_css

load_css()

# ── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="clinical-header">
    <div class="clinical-badge">Care Coordination</div>
    <h1 class="header-title">Caregiver Monitoring & Oversight Panel</h1>
    <p class="header-desc">
        Real-time patient oversight, risk variance notifications, clinical summary downloads, 
        and direct clinician alert dispatch.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Patient Risk Status")
    st.metric("Current Risk", "72%", "+5%")
    
    st.markdown("<div style='margin-top: 0.75rem;'></div>", unsafe_allow_html=True)
    st.warning("⚠ Risk Increased: Mild variance detected compared to prior 30-day baseline.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Patient Reports")
    st.write("Download latest reports and clinical summaries below:")
    st.markdown("""
    <ul style="font-size: 0.88rem; color: var(--text-secondary); padding-left: 1.25rem; margin: 0.5rem 0;">
        <li>📄 <em>Neuroimaging Assessment Summary (Feb 2026)</em></li>
        <li>📄 <em>Mini Cognitive Evaluation Log (Jan 2026)</em></li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Appointment Reminder")
    st.info("Next Visit: 25 March — Dr. A. Sharma (Neurology Dept.)")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Physician Alert Dispatch")
    st.write("Notify the primary neurologist regarding observed symptoms or behavioral changes.")
    st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)
    if st.button("Send Alert"):
        st.success("Alert sent to Doctor")
    st.markdown("</div>", unsafe_allow_html=True)