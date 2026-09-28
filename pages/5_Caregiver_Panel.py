import streamlit as st
from utils import load_css

load_css()

import streamlit as st

st.title("👨‍👩‍👧 Caregiver Monitoring Panel")

st.metric("Current Risk","72%","+5%")

st.warning("⚠ Risk Increased")

st.subheader("Patient Reports")
st.write("Download latest reports")

st.subheader("Appointment Reminder")
st.info("Next Visit: 25 March")

if st.button("Send Alert"):
    st.success("Alert sent to Doctor")