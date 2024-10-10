import streamlit as st
import pandas as pd
st.title('CSE17 Attendance')
st.header("Dataframe Example")
data = pd.read_csv("details.xlsx")
st.dataframe(data)