import streamlit as st
from utils import load_css, predict_alzheimer, generate_report

load_css()

# ── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="clinical-header">
    <div class="clinical-badge">Neuroimaging Diagnostic Intake</div>
    <h1 class="header-title">Neuroimaging Analysis & Risk Stratification</h1>
    <p class="header-desc">
        Upload structural MRI or PET scans alongside demographic parameters for diagnostic 
        risk estimation, visual explainability regions, and downloadable clinical summaries.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Input Section ─────────────────────────────────────────────
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
    st.markdown("<h3>1. Scan & Demographic Intake</h3>", unsafe_allow_html=True)
    
    scan = st.file_uploader("Upload MRI / PET Scan", help="Supported file formats: DICOM, NIfTI, PNG, JPG slice")
    
    c_age, c_gen = st.columns(2)
    with c_age:
        age = st.slider("Patient Age", 40, 95, 65)
    with c_gen:
        gender = st.selectbox("Gender", ["Male", "Female"])

    st.markdown("<div style='margin-top: 0.75rem;'></div>", unsafe_allow_html=True)
    run_btn = st.button("Run AI Detection")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="clinical-card">
        <h3>Standard Protocol Guidelines</h3>
        <p class="card-hint">
            For optimal diagnostic analysis, ensure input scans adhere to standardized 
            T1-weighted structural MRI sequences in axial orientation.
        </p>
        <ul style="font-size: 0.88rem; color: var(--text-secondary); padding-left: 1.25rem; margin: 0; line-height: 1.6;">
            <li><strong>Orientation:</strong> Axial plane view</li>
            <li><strong>Modality:</strong> Structural T1/T2 MRI or FDG-PET</li>
            <li><strong>Matrix:</strong> 224 × 224 standardized resolution</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ── Detection Output ──────────────────────────────────────────
if run_btn:
    stage, risk, confidence = predict_alzheimer(age)

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    st.markdown("<h3>2. Diagnostic Analysis Output</h3>", unsafe_allow_html=True)

    res_col1, res_col2 = st.columns([3, 2])

    with res_col1:
        st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
        
        if stage == "Normal":
            st.success(f"Classified Stage: **{stage}** (No Significant Decline Indicated)")
        elif stage == "Mild":
            st.warning(f"Classified Stage: **{stage}** (Mild Cognitive Impairment Pattern)")
        else:
            st.error(f"Classified Stage: **{stage}** (Elevated Neurological Risk Pattern)")

        m1, m2 = st.columns(2)
        with m1:
            st.metric("Risk Score", f"{risk}%")
        with m2:
            st.metric("Confidence", f"{confidence}%")

        st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)
        report_link = generate_report(stage, risk, confidence)
        st.markdown(report_link, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with res_col2:
        st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
        st.markdown("<h3>Explainability Activation</h3>", unsafe_allow_html=True)
        st.image(
            "https://via.placeholder.com/400x250",
            caption="AI Brain Heatmap"
        )
        st.caption("Visual attention overlay highlighting cortical and hippocampal region activations.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="clinical-callout">
        ℹ️ <strong>Prototype Notice:</strong> Inference results displayed above represent simulated diagnostic workflow output for platform demonstration.
    </div>
    """, unsafe_allow_html=True)