import streamlit as st
from utils import load_css

load_css()

import streamlit as st

st.title("🚑 Emergency Help")

st.error("Emergency Contacts")

st.write("📞 Doctor: +91-9876543210")
st.write("📞 Caregiver: +91-9999999999")

if st.button("Call Ambulance"):
    st.success("Calling Ambulance (UI Mock)")

st.info("Nearest Hospital: City Care Hospital")