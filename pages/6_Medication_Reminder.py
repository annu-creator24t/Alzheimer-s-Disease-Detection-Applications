import streamlit as st
from utils import load_css

load_css()

# ── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="clinical-header">
    <div class="clinical-badge">Patient Adherence</div>
    <h1 class="header-title">Prescription Schedule & Adherence Tracker</h1>
    <p class="header-desc">
        Manage daily cognitive support medications, configure dose reminder timings, 
        and log routine administration compliance.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Add Medication Schedule")
    
    med = st.text_input("Medicine Name", placeholder="e.g., Donepezil 10mg")
    time = st.time_input("Time")
    
    st.markdown("<div style='margin-top: 0.75rem;'></div>", unsafe_allow_html=True)
    if st.button("Add Schedule"):
        st.success("Reminder Added")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.subheader("Today's Status")
    st.caption("Review and toggle daily dosage completion:")
    
    st.markdown("<div style='margin: 0.75rem 0;'></div>", unsafe_allow_html=True)
    st.checkbox("Donepezil - Taken")
    st.checkbox("Vitamin B12 - Missed")
    
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    st.info("💡 Consistent administration is vital for sustained therapeutic efficacy.")
    st.markdown("</div>", unsafe_allow_html=True)