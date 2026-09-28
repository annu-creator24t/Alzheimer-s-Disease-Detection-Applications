import streamlit as st
from utils import load_css, predict_alzheimer, generate_report

load_css()

st.title("🧠 Alzheimer AI Detection")

col1, col2 = st.columns(2)

with col1:
    scan = st.file_uploader("Upload MRI / PET Scan")
    age = st.slider("Patient Age", 40, 95)
    gender = st.selectbox("Gender", ["Male", "Female"])

# ⭐ Prediction only when button clicked
if st.button("Run AI Detection"):

    stage, risk, confidence = predict_alzheimer(age)

    st.subheader("Detection Result")

    st.error(f"Stage: {stage}")
    st.metric("Risk Score", f"{risk}%")
    st.metric("Confidence", f"{confidence}%")

    st.image(
        "https://via.placeholder.com/400x250",
        caption="AI Brain Heatmap"
    )

    report_link = generate_report(stage, risk, confidence)
    st.markdown(report_link, unsafe_allow_html=True)