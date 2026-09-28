import streamlit as st
import pandas as pd
import numpy as np
from utils import load_css

load_css()

# ── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="clinical-header">
    <div class="clinical-badge">Longitudinal Monitoring</div>
    <h1 class="header-title">Patient Progress & Trend Dashboard</h1>
    <p class="header-desc">
        Continuous longitudinal tracking of cognitive risk indices, periodic screening scores, 
        and historical clinical consultation timelines.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Generate Dataset ──────────────────────────────────────────
data = pd.DataFrame({
    "Date": pd.date_range(start="2025-01-01", periods=10),
    "Risk": np.random.randint(30, 80, 10)
})

normal_score = int(np.random.randint(50, 95))
latest_risk = int(data["Risk"].iloc[-1])

# ── Top Summary Metrics ───────────────────────────────────────
m1, m2, m3 = st.columns(3)

with m1:
    st.metric(label="Score", value=normal_score)

with m2:
    st.metric(label="Latest Risk Index", value=f"{latest_risk}%")

with m3:
    st.metric(label="Logged Evaluations", value="10 Sessions")

st.markdown("<div style='margin-top: 1.25rem;'></div>", unsafe_allow_html=True)

# ── Charts and Historical Log ─────────────────────────────────
col_chart, col_side = st.columns([3, 2])

with col_chart:
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Risk Trend")
    st.line_chart(data.set_index("Date"))
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Previous Results")
    st.dataframe(data)
    st.markdown("</div>", unsafe_allow_html=True)

with col_side:
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Appointment History")
    st.write("✔ 12 Feb — Neurologist Consultation")
    st.write("✔ 28 Feb — MRI Structural Scan")
    st.write("✔ 25 Mar — Cognitive Follow-up")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="clinical-card">
        <h3>Clinical Guidance</h3>
        <p class="card-hint">
            A sustained increase of &gt;10% across consecutive screening intervals 
            warrants a comprehensive neurocognitive re-evaluation.
        </p>
    </div>
    """, unsafe_allow_html=True)