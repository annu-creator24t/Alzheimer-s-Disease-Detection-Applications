import streamlit as st
from utils import load_css

load_css()

import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Patient Progress Dashboard")

data = pd.DataFrame({
    "Date": pd.date_range(start="2025-01-01", periods=10),
    "Risk": np.random.randint(30,80,10)
})

st.subheader("Risk Trend")
st.line_chart(data.set_index("Date"))

st.subheader("Previous Results")
st.dataframe(data)

st.subheader("Progress Score")
normal_score = int(np.random.randint(50, 95))
st.metric(label="Score", value=normal_score)

st.subheader("Appointment History")
st.write("✔ 12 Feb — Neurologist")
st.write("✔ 28 Feb — MRI Scan")