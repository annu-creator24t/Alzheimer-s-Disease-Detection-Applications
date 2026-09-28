import streamlit as st
import random
import datetime
import base64

# ---------- LOAD CSS ----------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------- FAKE LOGIN ----------
def login_user(email, password, role):
    if email != "" and password != "":
        return True
    return False


# ---------- MOCK AI PREDICTION ----------
def predict_alzheimer(age):
    risk = random.randint(30, 85)

    if risk < 40:
        stage = "Normal"
    elif risk < 65:
        stage = "Mild"
    else:
        stage = "Severe"

    confidence = random.randint(85, 98)

    return stage, risk, confidence


# ---------- COGNITIVE SCORE ----------
def cognitive_score():
    return random.randint(50, 95)


# ---------- GENERATE REPORT ----------
def generate_report(stage, risk, confidence):
    report = f"""ALZHEIMER'S CLINICAL SCREENING SUMMARY
----------------------------------------
Date: {datetime.date.today()}
Evaluation Type: Neuroimaging Intake & Assessment

DIAGNOSTIC INDICATORS:
- Clinical Stage: {stage}
- Estimated Risk Index: {risk}%
- Assessment Confidence: {confidence}%

NOTICE:
This summary is generated for clinical screening and academic
demonstration purposes and should be reviewed by a certified neurologist.
----------------------------------------
"""

    b64 = base64.b64encode(report.encode()).decode()

    href = f'<a class="download-report-btn" href="data:file/txt;base64,{b64}" download="clinical_assessment_report.txt">📄 Download Clinical Summary Report (.txt)</a>'
    return href


# ---------- EMERGENCY CONTACT ----------
def get_emergency_contacts():
    return {
        "doctor": "+91 9876543210",
        "caregiver": "+91 9123456780",
        "hospital": "City Neuro Hospital"
    }


# ---------- APPOINTMENT MOCK ----------
def get_appointments():
    return [
        "12 Feb — Neurologist Visit",
        "28 Feb — MRI Scan",
        "25 March — Follow-up"
    ]