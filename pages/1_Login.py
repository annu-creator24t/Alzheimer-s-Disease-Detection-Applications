import streamlit as st
from utils import load_css

load_css()

import streamlit as st

st.title("🔐 Login Portal")

role = st.selectbox("Login as", ["Patient","Doctor","Caregiver"])

st.text_input("Email")
st.text_input("Password", type="password")

if st.button("Login"):
    st.success(f"Logged in as {role}")