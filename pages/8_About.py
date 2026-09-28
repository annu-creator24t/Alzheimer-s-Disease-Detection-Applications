import streamlit as st
from utils import load_css

load_css()

# ── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="clinical-header">
    <div class="clinical-badge">Platform Overview</div>
    <h1 class="header-title">About the Alzheimer's Disease Screening System</h1>
    <p class="header-desc">
        An integrated healthcare prototype designed to facilitate multi-modal Alzheimer's 
        screening, digital cognitive evaluations, and longitudinal patient care management.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("System Purpose & Clinical Scope")
    st.write("""
This system helps in early detection of Alzheimer’s using
AI brain scan analysis + cognitive assessment.
    """)
    st.markdown("""
    <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
        By bridging patient-administered cognitive screening tools with clinician-assisted 
        neuroimaging intake workflows, this platform demonstrates an accessible, multi-tiered 
        approach to early cognitive decline identification.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Core Integrated Features")
    st.write("""
Features:
✔ AI Detection  
✔ Caregiver Monitoring  
✔ Risk Dashboard  
✔ Emergency Support  
✔ Medication Reminder  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="clinical-card">
        <h3>Architecture & Design</h3>
        <ul style="font-size: 0.88rem; color: var(--text-secondary); padding-left: 1.25rem; margin: 0; line-height: 1.6;">
            <li><strong>Frontend:</strong> Streamlit Multi-Page Web Architecture</li>
            <li><strong>Styling:</strong> Custom Healthcare Clinical Design System</li>
            <li><strong>Assessment:</strong> Standardized 6-Domain Cognitive Battery</li>
            <li><strong>Intake:</strong> Neuroimaging Scan Diagnostic Workflow</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="clinical-callout">
        ⚖️ <strong>Academic Prototype Notice:</strong> Developed for academic workflow demonstration and screening user-experience exploration.
    </div>
    """, unsafe_allow_html=True)