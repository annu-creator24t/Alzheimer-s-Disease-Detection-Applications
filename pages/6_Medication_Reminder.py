import streamlit as st
from utils import load_css

load_css()

import streamlit as st

st.title("💊 Medication Schedule")

med = st.text_input("Medicine Name")
time = st.time_input("Time")

if st.button("Add Schedule"):
    st.success("Reminder Added")

st.subheader("Today's Status")
st.checkbox("Donepezil - Taken")
st.checkbox("Vitamin B12 - Missed")