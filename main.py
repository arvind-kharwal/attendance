import streamlit as st
import pandas as pd
st.title('Hello')
st.header("Header")
st.header("Dataframe Example")
data = pd.read_excel("details.xlsx")
st.dataframe(data)