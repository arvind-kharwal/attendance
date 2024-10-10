import streamlit as st
import pandas as pd
st.title('CSE17 Attendance')
st.header("Dataframe Example")
data = pd.read_excel("sheet.xlsx")
st.dataframe(data)