import streamlit as st

st.set_page_config(
    page_title="Alzheimer's Disease Clinical Screening System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ── Header & Overview ──────────────────────────────────────────
st.markdown("""
<div class="clinical-header">
    <div class="clinical-badge">Clinical Screening & Workflow Platform</div>
    <h1 class="header-title">Alzheimer's Disease Detection & Monitoring System</h1>
    <p class="header-desc">
        A clinical screening and patient support platform combining standardized digital 
        cognitive assessments, neuroimaging intake workflows, and longitudinal care tracking.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Key Clinical Metrics / Indicators ─────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-label">Assessment Modalities</div>
        <div class="stat-num">MRI + Cognitive</div>
        <div class="stat-sub">Multimodal evaluation</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-label">Clinical Domains</div>
        <div class="stat-num">5 Domains</div>
        <div class="stat-sub">Standardized testing</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-label">Screening Speed</div>
        <div class="stat-num">&lt; 2 min</div>
        <div class="stat-sub">Rapid intake workflow</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-label">Care Coordination</div>
        <div class="stat-num">Active</div>
        <div class="stat-sub">Caregiver & SOS modules</div>
    </div>
    """, unsafe_allow_html=True)

# ── Platform Capabilities ─────────────────────────────────────
st.markdown("<div style='margin-top: 1.75rem;'></div>", unsafe_allow_html=True)
st.markdown("<h3>Clinical Modules & Capabilities</h3>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="capability-card">
        <div class="cap-icon">🧪</div>
        <h3>Cognitive Screening</h3>
        <p>Standardized 6-stage clinical assessment evaluating orientation, memory encoding, attention, recall, and visuospatial function.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="capability-card">
        <div class="cap-icon">🔬</div>
        <h3>Neuroimaging Intake</h3>
        <p>Intake interface for structural brain scans, diagnostic risk estimation, explainability heatmaps, and downloadable clinical summaries.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="capability-card">
        <div class="cap-icon">📊</div>
        <h3>Patient Monitoring</h3>
        <p>Longitudinal risk progression charts, medication adherence scheduling, caregiver status monitoring, and emergency SOS contacts.</p>
    </div>
    """, unsafe_allow_html=True)

# ── Navigation Notice ─────────────────────────────────────────
st.markdown("""
<div class="clinical-callout">
    💡 <strong>Navigation:</strong> Use the left sidebar to access the <strong>Cognitive Assessment</strong>, <strong>AI Detection</strong>, <strong>Patient Dashboard</strong>, or <strong>Caregiver Panel</strong> modules.
</div>
""", unsafe_allow_html=True)