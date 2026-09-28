import streamlit as st

st.set_page_config(
    page_title="AI Alzheimer System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ── Hero Section ──────────────────────────────────────────────
st.markdown("""
<div class="hero-container">
    <div class="hero-glow"></div>
    <div class="hero-content">
        <div class="hero-badge">🔬 AI-Powered Diagnostics</div>
        <h1 class="hero-title">🧠 AI Alzheimer<br><span class="hero-accent">Detection System</span></h1>
        <p class="hero-subtitle">
            Early detection powered by machine learning — helping clinicians identify 
            cognitive decline patterns with precision and speed.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Stats Row ─────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-icon">🎯</div>
        <div class="stat-value">94.7%</div>
        <div class="stat-label">Detection Accuracy</div>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-icon">⚡</div>
        <div class="stat-value">&lt; 2 min</div>
        <div class="stat-label">Analysis Time</div>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-icon">🧬</div>
        <div class="stat-value">5 Stages</div>
        <div class="stat-label">Risk Classification</div>
    </div>""", unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-icon">📋</div>
        <div class="stat-value">MRI + EEG</div>
        <div class="stat-label">Supported Inputs</div>
    </div>""", unsafe_allow_html=True)

# ── Feature Cards ─────────────────────────────────────────────
st.markdown("<div style='margin-top: 2.5rem;'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='section-heading'>What You Can Do</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🖼️</div>
        <h3>Upload MRI Scans</h3>
        <p>Submit neuroimaging data for automated segmentation and risk scoring.</p>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3>Track Patient Progress</h3>
        <p>Monitor cognitive trends over time with interactive visual dashboards.</p>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📝</div>
        <h3>Generate Reports</h3>
        <p>Export clinical summaries and AI-generated insights for each patient.</p>
    </div>""", unsafe_allow_html=True)

# ── CTA ───────────────────────────────────────────────────────
st.markdown("""
<div class="cta-bar">
    <span>👈 Use the sidebar to navigate between modules</span>
</div>
""", unsafe_allow_html=True)